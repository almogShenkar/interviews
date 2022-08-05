def ClickException(Exception):
    pass


class Click:
    data = dict()

    @staticmethod
    def set_value(k, v):
        Click.data[k] = v

    @staticmethod
    def get_value(k):
        return Click.data[k]

    @staticmethod
    def delete_value(k):
        del Click.data[k]

    @staticmethod
    def help():
        print("Options:")
        for k, v in Click.data.items():
            print(f"--{k} {k['help']}")


def command(func):
    def inner(*args, **kwargs):
        for arg in args:
            Click().data[arg] = kwargs
        return func(args, kwargs)

    return inner


def option():
    def add(func):
        def add_option(*args, **kwargs):
            return func(*args, **kwargs)

        return add_option
    return add


def echo(cmd_with_keys):
    next_word_is_key = False
    result = ""

    for w in enumerate(cmd_with_keys.split(' ')):

        if w == '%':
            next_word_is_key = True

        if next_word_is_key:
            result += Click().get_value(w)

        else:
            result += w
