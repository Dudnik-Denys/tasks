class Viber:
    MESSAGES = []

    @classmethod
    def add_message(cls, msg):
        cls.MESSAGES.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.MESSAGES.remove(msg)

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, num):
        print(cls.MESSAGES[-num:])

    @classmethod
    def total_messages(cls):
        return len(cls.MESSAGES)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like
