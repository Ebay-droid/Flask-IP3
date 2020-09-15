import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
  
  def setUp(self):
    self.new_article = Articles('bbc','brad','what to do','an article on what to do','cnn.com/articles','image.article','2nd march')
    
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Articles))  
    
    
if __name__ == "__main__":
      unittest.main()   