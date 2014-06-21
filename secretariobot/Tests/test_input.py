#-*- coding: utf-8 -*-
import os
import unittest

from secretariobot.Input import Input


class InputTest(unittest.TestCase):

    def test_clean(self):
        tweet_id = "480428719463337985"
        obj = Input(tweet_id)

        expected_string = u'y el uterope ya aparece en la lista de usuarios de Scrapy ver final de página'
        result = obj.clean_string

        self.assertEqual(result, expected_string.encode("utf-8"))

    def test_is_reply(self):
        tweet_id = "479726791259860992"


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)
