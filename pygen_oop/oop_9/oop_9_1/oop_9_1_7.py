class Pagination:
    def __init__(self, data: list[str], size: int):
        self.__pages = self.__make_book(data[:], size)
        self.total_pages = len(self.__pages)
        self.current_page = 1 if self.__pages else None

    @staticmethod
    def __make_book(iterable: list[str], count: int) -> list[list[str]]:
        total = len(iterable) // count if len(iterable) % count == 0 else len(iterable) // count + 1
        result = []
        while total > 0:
            result.append(iterable[:count])
            iterable = iterable[count:]
            total -= 1
        return result

    def get_visible_items(self) -> list:
        return self.__pages[self.current_page - 1]

    def prev_page(self):
        self.current_page -= 1 if self.current_page > 1 else 0
        return self

    def next_page(self):
        self.current_page += 1 if self.current_page < self.total_pages else 0
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page: int):
        if page <= 0:
            self.first_page()
        elif page >= self.total_pages:
            self.last_page()
        else:
            self.current_page = page
        return self
