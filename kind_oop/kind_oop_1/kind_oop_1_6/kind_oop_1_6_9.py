TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, arg):
        obj = object.__new__(DialogWindows if TYPE_OS == 1 else DialogLinux)
        setattr(obj, 'name', arg)
        return obj
