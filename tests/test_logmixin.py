from unittest import TestCase

from logmixin.logmixin import LogMixin


class TestLogMixin(TestCase):
    def test_get_logger(self):

        class TestClass(LogMixin):
            def test(self):
                return self.get_logger()

        tc = TestClass()
        logger = tc.test()
        self.assertEqual(logger.name, "test_logmixin.TestClass.test")
