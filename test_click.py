import unittest

import click
from click import Click


class ClickTesCase(unittest.TestCase):

    def test_click_get_value(self):
        click = Click()
        click.set_value("a", 5)
        assert click.get_value("a") == 5, "get_value is broken"
        click.set_value("a", 0)
        assert click.get_value("a") == 0, "get_value is broken"

    def test_click_set_value(self):
        click = Click()
        click.set_value("a", 5)

    def test_click_delete_value(self):
        click = Click()
        click.set_value("a", 5)
        click.delete_value("a")
        try:
            click.delete_value("b")
        except KeyError:
            print("key not found. error")

    def test_exec_decorators(self):
        @click.command
        @click.option('--count', default=1, help='Number of greetings.')
        @click.option('--name', prompt='Your name',
                      help='The person to greet.')
        def hello(count, name):
            """Simple program that greets NAME for a total of COUNT times."""
            for x in range(count):
                click.echo('Hello %s!' % name)





if __name__ == '__main__':
    unittest.main()
