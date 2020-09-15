import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
  
  def setUp(self):
    self.new_article = Articles('bbc','brad','what to do','an article on what to do','cnn.com/articles','image.article',)