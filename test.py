import unittest

from utils import replace_url, extract_tweet_id, send_post_request


class TestUtils(unittest.TestCase):
    def test_twitter_url(self):
        """
        Test that it works correctly
        """
        test_data = "1667184877270073344"
        result = replace_url(test_data)
        self.assertEqual(result, "https://twitter-thread.com/t/1667184877270073344")

    def test_extract_tweet_id(self):
        """
        Test that tweet id is correctly extracted
        """
        test_data = "https://twitter.com/defi_mochi/status/1667184877270073344"
        result = extract_tweet_id(test_data)
        self.assertEqual(result, "1667184877270073344")
        
        test_data = "https://x.com/zerokn0wledge_/status/1742897423754932297?t=deFYPUSwvQGG7paCTH00Cw&s=09"
        result = extract_tweet_id(test_data)
        self.assertEqual(result, "1742897423754932297")
    
    def test_send_post(self):
        """
        Test that it works correctly
        """
        test_data = "1667184877270073344"
        result = send_post_request(test_data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()