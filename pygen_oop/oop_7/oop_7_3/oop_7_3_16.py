class TitledText(str):
    def __new__(cls, content, text_title, *args, **kwargs):
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        return instance

    def title(self) -> str:
        return self.text_title
