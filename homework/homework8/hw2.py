import sqlite3


class TableData:
    """Take a SQLite file, that we can use it like iter object.
    Can return number of items with 'len' function.
    Allow to use first column values like keys and return all data for that values."""

    def __init__(self, database_name, table_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.table_name = table_name
        self._index = 0
        cursor = self.conn.execute(f"select * from {table_name}")
        self.names = list(map(lambda x: x[0], cursor.description))

    def __getitem__(self, key):
        self.cursor.execute(f"SELECT * from {self.table_name} WHERE name='{key}'")
        return self.cursor.fetchall()

    def __len__(self):
        self.cursor.execute(f"SELECT * from {self.table_name}")
        return len(self.cursor.fetchall())

    def __contains__(self, item):
        self.cursor.execute(f"SELECT * from {self.table_name} WHERE name='{item}'")
        return self.cursor.fetchall()

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self):
            self.cursor.execute(f"SELECT * from {self.table_name}")
            current_data = dict(zip(self.names, self.cursor.fetchall()[self._index]))
            self._index += 1
            return current_data
        else:
            raise StopIteration
