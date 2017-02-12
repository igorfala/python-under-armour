from UnderArmour import UAOauth2Client
from unittest.mock import Mock, patch
import unittest
import UnderArmour

class UAOauth2ClientTest(unittest.TestCase):
    """
    Test Case for OAuth Connection
    """
    test_client = { 'client_id':     'test_client',
                    'client_secret': 'test_secret',
                    }
    test_call_callback_url = 'http://127.0.0.1:8000'

    def test_authorize_token_url(self):
        """
        Tests to make sure the returned URL is generated correctly
        """
        test_OauthObject = UAOauth2Client(**self.test_client)
        test_url, test_state = test_OauthObject.authorize_token_url(self.test_call_callback_url)
        expected_url = 'https://www.mapmyfitness.com/v7.1/oauth2/uacf/authorize/?redirect_uri=http%3A%2F%2F127.0.0.1%3A8000&response_type=code&client_id=test_client&state='
        self.assertEqual(test_url, '{}{}'.format(expected_url,test_state))

    #@patch(UnderArmour.json)
    @patch('UnderArmour.requests', create=True)
    def test_fetch_access_token(self, mock_requests):
        pass

if __name__ == '__main__':
        unittest.main()
