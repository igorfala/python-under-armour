from UnderArmour import UAOauth2Client
import unittest

class UAOauth2ClientTest(unittest.TestCase):
    """
    Test Case for OAuth Connection
    """
    test_client = { 'client_id':     'test_client',
                    'client_secret': 'test_secret',
                    }
    test_call_callback_url = 'http://127.0.0.1:800'

    def test_authorize_token_url(self):
        """
        Tests to make sure the returned URL is generated correctly
        """
        test_OauthObject = UAOauth2Client(**self.test_client)
        test_url, test_state = test_OauthObject.authorize_token_url(self.test_call_callback_url)
        print(test_url)
        print(test_state)
        expected_url = 'https://www.mapmyfitness.com/v7.1/oauth2/uacf/authorize/?redirect_uri=http%3A%2F%2F127.0.0.1%3A800&response_type=code&client_id=test_client&state='
        self.assertEqual(test_url, '{}{}'.format(expected_url,test_state))

    def test_fetch_access_token(self):
        pass
        
if __name__ == '__main__':
    print('https://www.mapmyfitness.com/v7.1/oauth2/uacf/authorize/?redirect_uri=http%3A%2F%2F127.0.0.1%3A800&response_type=code&client_id=test_client&state=C18UP3sSt2uMdIjkr2TNyvVDgsU75c'=='https://www.mapmyfitness.com/v7.1/oauth2/uacf/authorize/?redirect_uri=http%3A%2F%2F127.0.0.1%3A800&response_type=code&client_id=test_client&state=dmwuQaDKIWRVu8hvC50bTQcXyhHQqB')
    unittest.main()
