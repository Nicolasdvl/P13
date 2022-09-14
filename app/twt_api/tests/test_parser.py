from django.test import TestCase
from ..parser import Parser


class ParserTestCase(TestCase):
    def setUp(self) -> None:
        self.parser = Parser()

    def test_parser(self) -> None:
        pass
