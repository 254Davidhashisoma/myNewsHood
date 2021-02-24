import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test case to test the behaviour of the Sources class
    '''
    def setUp(self):
        '''
        Function that will run before every test
        '''
        self.new_source = Sources('allnews', 'Latest News', 'We have the latest updates', 'https://bing.com', 'general', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_check_instance_variables(self):
        '''
        Test case to check if the objects are instansiated correctly
        '''
        self.assertEquals(self.new_source.id, 'allnews')
        self.assertEquals(self.new_source.name, 'Latest News')
        self.assertEquals(self.new_source.description, 'We have the latest updates')
        self.assertEquals(self.new_source.url, 'https://bing.com')
        self.assertEquals(self.new_source.category, 'general')
        self.assertEquals(self.new_source.country, 'us')