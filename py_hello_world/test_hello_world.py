import unittest
import sys
from cStringIO import StringIO

#from py_hello_world import hello_world
import hello_world

class TestHelloWorld(unittest.TestCase):
    sentence = "Test this sentence"

    def setUp(self):
        self.bckp = sys.stdout
        sys.stdout = StringIO()
    
    def tearDown(self):
        sys.stdout = self.bckp

    def test_sentence(self):
        hello_world.say_hello(self.__class__.sentence)
        out = sys.stdout.getvalue() 
        self.assertEqual(self.__class__.sentence+'\n',out)


if __name__ == '__main__':
    unittest.main()


