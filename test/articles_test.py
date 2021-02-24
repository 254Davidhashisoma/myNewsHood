import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):
    '''
    Class to test the behaviour of the articles class
    '''
    def setUp(self):
        self.new_article = Articles('Koinange', 'No human is limited', 'Kipchoge runs a marathon in less than 2 hours', 'https://bing.com', 'https://bing.com/images', '2019-10-12T11:31:03Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_article.author, 'Koinange')
        self.assertEquals(self.new_article.title, 'No human is limited')
        self.assertEquals(self.new_article.description, 'Kipchoge runs a marathon in less than 2 hours')
        self.assertEquals(self.new_article.url, 'https://bing.com')
        self.assertEquals(self.new_article.urlToImage,'https://bing.com/images')
        self.assertEquals(self.new_article.publishedAt, '2019-10-12T11:31:03Z')