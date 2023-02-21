import logging
from unittest import TestCase

from logmixin.logmixin import LogMixin


class TestLogMixin(TestCase):
    def test_get_logger(self):

        class TestClass(LogMixin):
            def test(self):
                logger = self.get_logger()
                logger.info("Hello, world!")
                return logger

        logging.basicConfig(level=logging.DEBUG)
        tc = TestClass()
        _logger = tc.test()
        self.assertEqual(_logger.name, "test_logmixin.TestClass.test")