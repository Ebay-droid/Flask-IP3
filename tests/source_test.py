import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
  
  def setUp(self):
    '''
    Tests behaviour of source class
    '''
    
    self.new_source = Sources('cnn','cnn_news','For the best news in town','cnn.com','general','english','us')
    
  def test_instance(self):
    self.assertTrue(isinstance(self.new_source,Sources))  