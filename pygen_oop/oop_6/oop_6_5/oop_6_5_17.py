class HtmlTag:
    LEVEL = 0

    def __init__(self, tag: str, inline: bool = False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        print('  ' * HtmlTag.LEVEL, end='')
        print(f'<{self.tag}>', end='\n' if not self.inline else '')
        HtmlTag.LEVEL += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        HtmlTag.LEVEL -= 1
        if not self.inline:
            print('  ' * HtmlTag.LEVEL + f'</{self.tag}>')

    def print(self, text: str):
        if not self.inline:
            print('  ' * (not self.inline) * HtmlTag.LEVEL + text, end='\n' if not self.inline else '')
        else:
            print(f'{text}</{self.tag}>')
