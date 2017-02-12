import unittest
from .test_oauth import UAOauth2ClientTest

def suite():
    tests = ['UAOauth2ClientTest']

    return unittest.TestSuite(map(WidgetTestCase, tests))

if __name__ == '__main__':
    suite()
