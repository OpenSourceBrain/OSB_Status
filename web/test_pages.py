import random
import unittest
import sys
from bs4 import BeautifulSoup
import generalfunctions
import re

USERNAME = None
PASSWORD = None

# url_base = "http://opensourcebrain.org/"
#url_base = "http://comodl.org/"
url_base = "http://127.0.0.1:3000/"

url_path = {}
#Home Page
url_path["test_home"] = ""
#OSB Explore
url_path["test_projects"] = "projects"
url_path["test_projectsGraph"] = "projects/cells_graph"
url_path["test_projectsList"] = "projects/cells_list"
url_path["test_projectsCarousel"] = "projects/cells_gallery"
url_path["test_projectsCloud"] = "projects/cells_tags"
url_path["test_technology"] = "projects/technology"
url_path["test_projectsGroups"] = "projects/groups"
url_path["test_people"] = "projects/people"
url_path["test_informationOSB"] = "projects/informationOSB"
#Register / Login
url_path["test_register"] = "account/register"
url_path["test_login"] = "login"
#Search
url_path["test_search"] = "search?q=purkinje"
#User
url_path["test_user"] = "users/4"
#Group
url_path["test_groups"] = "groups/7"
#Project OSB
url_path["test_projectIndex"] = "projects/osb"
url_path["test_projectActivity"] = "projects/osb/activity"
url_path["test_projectWiki"] = "projects/osb/wiki"
url_path["test_projectFiles"] = "projects/osb/files"
url_path["test_projectSettings"] = "projects/osb/settings"
url_path["test_projectIssues"] = "projects/osb/issues"
url_path["test_projectNews"] = "projects/osb/news"

#Project nc_superdeep
url_path["test_projectIndex_nc_superdeep"] = "projects/nc_superdeep"


#ERRORS
CONTENT_PAGE_ERROR = "Content Page Error"

class TestWebPages(unittest.TestCase):

    longMessage = True

    @classmethod
    def setUpClass(cls):
        generalfunctions.USERNAME = USERNAME
        generalfunctions.PASSWORD = PASSWORD  

    def test_home(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="myCarouselMainPage"), CONTENT_PAGE_ERROR)

    def test_projects(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="cells"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="technology"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="groups"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="people"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="informationOSB"), CONTENT_PAGE_ERROR)
        
    def test_projectsGraph(self):
        soup = self.check_general_aspects(check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        #GRAPH TAB
        self.assertIsNotNone(soup.find(id="jsontree"), CONTENT_PAGE_ERROR)
        
    def test_projectsList(self):     
        soup = self.check_general_aspects(check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        #LIST TAB
        self.assertIsNotNone(soup.find(id="cellslist"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(href="#cell9"), CONTENT_PAGE_ERROR)
        
    def test_projectsCarousel(self):     
        soup = self.check_general_aspects(check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        #CAROUSEL TAB
        self.assertIsNotNone(soup.find(id="myCarousel"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(href="/projects/purkinjecell"), CONTENT_PAGE_ERROR)
        
        #self.assertIsNotNone(soup.find_all("svg"), CONTENT_PAGE_ERROR)
        
    def test_projectsCloud(self):     
        soup = self.check_general_aspects(check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        #TAGS CLOUD TAB
        self.assertIsNotNone(soup.find(id="tagCanvas"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href=re.compile("neuroConstruct")), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href=re.compile("Detailed cell model")), CONTENT_PAGE_ERROR)
        
    def test_technology(self):
        soup = self.check_general_aspects(check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find_all(href="#cell81"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="cell81"), CONTENT_PAGE_ERROR)
        
    def test_projectsGroups(self):
        soup = self.check_general_aspects(check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="group7"), CONTENT_PAGE_ERROR)
        
    def test_people(self):
        soup = self.check_general_aspects(check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="user4"), CONTENT_PAGE_ERROR)
        #print soup.prettify()
        
    def test_informationOSB(self):
        soup = self.check_general_aspects(check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find_all(href="about"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="projects/osb/wiki/Faq"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="projects/osb/wiki/Meetings"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="guides"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="themes"), CONTENT_PAGE_ERROR)
        
    def test_register(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="user_login"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="user_password"), CONTENT_PAGE_ERROR)
        
        
    def test_login(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="username"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="password"), CONTENT_PAGE_ERROR)
        
    def test_search(self):
        soup = self.check_general_aspects(page_title='Search - Open Source Brain')
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="search-input"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all("dt"), CONTENT_PAGE_ERROR)
        
    def test_user(self):
        soup = self.check_general_aspects(page_title='Padraig Gleeson - Open Source Brain')
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find_all(href="/projects/osb"), CONTENT_PAGE_ERROR)
        
    def test_groups(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS    
        self.assertIsNotNone(soup.find_all(href="/users/4"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="/projects/gitintro"), CONTENT_PAGE_ERROR)
        
        
    def test_projectIndex(self):
        soup = self.check_general_aspects(page_title = 'Overview - The Open Source Brain repository - Open Source Brain')
        #CHECKING SPECIFIC ASPECTS
        #NAV BAR
        self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR) 
        #CHECK TABS
        self.assertIsNotNone(soup.find_all(href="#description"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="description"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="#subprojects"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="subprojects"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="#members"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="members"), CONTENT_PAGE_ERROR)
        
    def test_projectActivity(self):
        soup = self.check_general_aspects(page_title = 'Activity - The Open Source Brain repository - Open Source Brain')
        #CHECKING SPECIFIC ASPECTS
        #NAV BAR
        self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)
        #CHECK ACTIVITIES
        self.assertIsNotNone(soup.find_all(class_="activity-item"), CONTENT_PAGE_ERROR) 
        
    def test_projectWiki(self):
        soup = self.check_general_aspects(page_title = 'Wiki - The Open Source Brain repository - Open Source Brain')
        #CHECKING SPECIFIC ASPECTS
        #NAV BAR
        self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)
        #CONTRIBUTORS
        self.assertIsNotNone(soup.find_all(href="/users/4"), CONTENT_PAGE_ERROR)
        #WIKI CONTENT
        self.assertIsNotNone(soup.find_all(href="Open-Source-Brain-Wiki"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="Questions"), CONTENT_PAGE_ERROR)
        
        
    def test_projectFiles(self):
        soup = self.check_general_aspects(page_title = 'Files - The Open Source Brain repository - Open Source Brain')
        #CHECKING SPECIFIC ASPECTS 
        #NAV BAR
        self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)
        #FILES
        self.assertIsNotNone(soup.find_all(class_="list"), CONTENT_PAGE_ERROR)
        
    def test_projectSettings(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        #NAV BAR
        self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)
        #SETTINGS BAR
        self.assertIsNotNone(soup.find_all(id="tab_info"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(id="tab_modules"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(id="tab_members"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(id="tab_versions"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(id="tab_categories"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(id="tab_wiki"), CONTENT_PAGE_ERROR)
        #CONTENT TAB
        self.assertIsNotNone(soup.find_all(id="project_name"), CONTENT_PAGE_ERROR)
        
    def test_projectIssues(self):
        soup = self.check_general_aspects(page_title = 'Issues - The Open Source Brain repository - Open Source Brain')
        #CHECKING SPECIFIC ASPECTS
        #NAV BAR
        self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)  
        #CONTENT
        self.assertIsNotNone(soup.find_all(id="issues_list"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(class_="odd"), CONTENT_PAGE_ERROR)
        
    def test_projectNews(self):
        soup = self.check_general_aspects(page_title = 'News - The Open Source Brain repository - Open Source Brain')
        #CHECKING SPECIFIC ASPECTS
        #NAV BAR
        self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)      
        #CONTENT
        self.assertIsNotNone(soup.find_all(class_="author"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(class_="wiki"), CONTENT_PAGE_ERROR)
        
    def test_projectIndex_nc_superdeep(self):
        soup = self.check_general_aspects(page_title = 'Overview - CA1 Pyramidal Sublayer Microcircuit - Lee et al 2014  - Open Source Brain')
        #CHECKING SPECIFIC ASPECTS
        #NAV BAR
        self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR) 
        #CHECK TABS
        self.assertIsNotNone(soup.find_all(href="#description"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="description"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="#members"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="members"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="#references"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="references"), CONTENT_PAGE_ERROR)
        
    def check_general_aspects(self, page_title='Open Source Brain', check_header_footer=True):
        url = url_base + url_path[self._testMethodName]
        page, e = generalfunctions.get_page(url)
        if e is not None:
            exceptionMessage = "URL: %s produced error %d (%s)" % (url,e.code,e.msg)
            self.fail(exceptionMessage)
            
        self.assertIsNotNone(page, CONTENT_PAGE_ERROR + " / Page is blank")
        
        soup = BeautifulSoup(page)
        
        if check_header_footer:
            self.assertEqual(soup.title.string, page_title, CONTENT_PAGE_ERROR + " / Title does not match")
            self.assertIsNotNone(soup.find(id="osblogo"), CONTENT_PAGE_ERROR + " / OSB logo can not be found")
            self.assertIsNotNone(soup.find(id="wellcomelogolink"), CONTENT_PAGE_ERROR + " / Wellcome logo in footer can not be found")
            self.assertIsNotNone(soup.find_all(class_="footer-links"), CONTENT_PAGE_ERROR + " / Footer links can not be found")
        
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
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWebPages)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)  
    
    #if testResult.wasSuccessful() is False:
        #mailText = "Errors\n" + str(testResult.errors) + "Failures\n" + str(testResult.failures)  
        #generalfunctions.sendmail('adrianquintana@gmail.com', 'adrianquintana@gmail.com', mailText)
