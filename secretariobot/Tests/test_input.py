#-*- coding: utf-8 -*-
import os
import unittest

from secretariobot.Input import Input


class InputTest(unittest.TestCase):

    def test_clean(self):
        my_string = u'y el @uterope ya aparece en la lista de usuarios de Scrapy http://t.co/qZlUr7yRRO (ver final de página)'
        expected_string = u'y el uterope ya aparece en la lista de usuarios de Scrapy ver final de página'
        obj = Input(my_string.encode("utf-8"))
        result = obj.clean_string

        self.assertEqual(result, expected_string.encode("utf-8"))


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)
