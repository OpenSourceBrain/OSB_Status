import random
import unittest
import sys
from bs4 import BeautifulSoup
import generalfunctions

USERNAME = None
PASSWORD = None

url_base = "http://opensourcebrain.org/"

url_path = {}
#OSB Explore
url_path["test_projects"] = "projects.json"


#ERRORS
CONTENT_PAGE_ERROR = "Content Page Error"

class TestAPI(unittest.TestCase):

    longMessage = True

    @classmethod
    def setUpClass(cls):
        generalfunctions.USERNAME = USERNAME
        generalfunctions.PASSWORD = PASSWORD  
        generalfunctions.url_base = url_base
        generalfunctions.url_path = url_path

    def test_projects(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        #self.assertIsNotNone(soup.find(id="osbcircle"), CONTENT_PAGE_ERROR)
     
        
    def check_general_aspects(self, page_title='Open Source Brain'):
        page = generalfunctions.getPageContent(self)
        soup = BeautifulSoup(page)
        return soup

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        try:
            key,value = arg.split(":")
            if key == "username":            
                USERNAME = value
            if key == "password":
                PASSWORD = value
        except ValueError,e:
            ignored_arg = arg
            #print "Command line argument %s had error %s" % (arg,e.strerror)
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAPI)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)  
    
    #if testResult.wasSuccessful() is False:
        #mailText = "Errors\n" + str(testResult.errors) + "Failures\n" + str(testResult.failures)  
        #generalfunctions.sendmail('adrianquintana@gmail.com', 'adrianquintana@gmail.com', mailText)
