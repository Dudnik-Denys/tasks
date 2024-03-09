class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width, self.__height = None, None
        self.width = width
        self.height = height

    def show(self):
        return f'{self.__title}: {self.__width}, {self.__height}'

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) == int and 0 <= width <= 10_000:
            self.__width = width
            if self.__width:
                self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) == int and 0 <= height <= 10_000:
            self.__height = height
            if self.__height:
                self.show()
