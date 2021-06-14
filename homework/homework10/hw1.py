import asyncio
import json
from concurrent.futures import ProcessPoolExecutor

import aiohttp
import requests
from bs4 import BeautifulSoup

ORIGIN_URLS = [
    f"https://markets.businessinsider.com/index/components/s&p_500?p={page}"
    for page in range(1, 11)
]
companies_url = []


async def fetch_response(url):
    """Function for making responses"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_page_http(urls):
    """Parallelization of getting requests"""
    http = []
    tasks = [asyncio.create_task(fetch_response(url)) for url in urls]
    await asyncio.gather(*tasks)
    for task in tasks:
        http.append(task.result())
    return http


def get_dollar_rate():
    """Getting Dollar-Rub rate"""
    request = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    soup = BeautifulSoup(request.text, "lxml")
    rate = soup.find("valute", id="R01235")
    return float((rate.find("value").text.replace(",", ".")))


def get_main_page_info(main_http):
    """Parsing information from main page"""
    result = []
    dollar_rate = get_dollar_rate()
    for http in main_http:
        soup = BeautifulSoup(http, "lxml")
        digits_info_all_companies = soup.find_all("td", class_="table__td")
        companies = soup.find_all("td", class_="table__td table__td--big")
        for company, company_cost_pure, year_profit in zip(
            companies, digits_info_all_companies[1::8], digits_info_all_companies[7::8]
        ):
            company_name = company.find("a")["title"]
            company_code = company.find("a")["href"].replace("/stocks/", "")
            company_url = company.find("a")["href"]
            company_year_profit = float(
                year_profit.text.strip()[year_profit.text.strip().find("\n") + 1 : -1]
            )
            company_cost = (
                float(
                    (
                        (
                            company_cost_pure.text.strip()[
                                : company_cost_pure.text.strip().find("\n")
                            ]
                        ).strip()
                    ).replace(",", "")
                )
                * dollar_rate
            )
            companies_url.append(f"https://markets.businessinsider.com{company_url}")
            result.append(
                [company_name, company_code, company_cost, company_year_profit]
            )
    return result


def get_company_page_info(company_http):
    """Parsing information from companies pages"""
    soup = BeautifulSoup(company_http, "lxml")
    # Some companies doesnt have 52 week analytics
    try:
        low_info = (
            soup.find_all(
                "div", class_="snapshot__data-item snapshot__data-item--small"
            )[1]
            .text.strip()
            .replace(",", "")
        )
        high_info = (
            soup.find_all(
                "div",
                class_="snapshot__data-item snapshot__data-item--small snapshot__data-item--right",
            )[1]
            .text.strip()
            .replace(",", "")
        )
        company_sell_profit = (
            (
                float(high_info[: high_info.find("\n")])
                - float(low_info[: low_info.find("\n")])
            )
            / float(low_info[: low_info.find("\n")])
            * 100
        )
        pe_info = (
            soup.find_all("div", class_="snapshot__data-item")[8]
            .text.strip()
            .replace(",", "")
        )
    except IndexError:
        company_sell_profit = 0
        pe_info = (
            soup.find_all("div", class_="snapshot__data-item")[6]
            .text.strip()
            .replace(",", "")
        )
    company_pe = float(pe_info[: pe_info.find("\n")])
    return [company_pe, company_sell_profit]


def get_information_about_companies():
    """Putting all information together and make statistics"""
    result = []
    company_main_info = get_main_page_info(asyncio.run(get_page_http(ORIGIN_URLS)))
    with ProcessPoolExecutor() as pool:
        company_deep_info = pool.map(
            get_company_page_info, asyncio.run(get_page_http(companies_url))
        )
    for first_elem, second_elem in zip(company_main_info, company_deep_info):
        result.append(first_elem + second_elem)
    with open("most_expensive.json", "w") as f:
        json.dump(sorted(result, reverse=True, key=lambda x: x[2])[:10], f)
    with open("lowest_pe.json", "w") as f:
        json.dump(sorted(result, key=lambda x: x[4])[:10], f)
    with open("most_year_profit.json", "w") as f:
        json.dump(sorted(result, reverse=True, key=lambda x: x[3])[:10], f)
    with open("most_52week_profit.json", "w") as f:
        json.dump(sorted(result, reverse=True, key=lambda x: x[5])[:10], f)
