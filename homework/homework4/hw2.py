import urllib.error
import urllib.request


class Count:
    def __init__(self):
        pass

    def _get_html(self, url: str):
        try:
            data = urllib.request.urlopen(url)
        except urllib.error.URLError:
            raise ValueError(f"Unreachable {url}")
        html_text = data.read().decode("utf-8")
        return html_text

    def count_dots_on_i(self, url: str) -> int:
        html_text = self._get_html(url)
        count = 0
        for symbol in html_text:
            if symbol == "i":
                count += 1
        return count
