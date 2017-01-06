import random
import unittest
import sys
from bs4 import BeautifulSoup
import generalfunctions
from generalfunctions import get_page, CONTENT_PAGE_ERROR
import re

USERNAME = None
PASSWORD = None

url_base = "http://opensourcebrain.org/"
# url_base = "http://comodl.org/"
#url_base = "http://0.0.0.0:3000/"

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
#Doc
url_path["test_doc"] = "docs"

url_path["test_projectWiki"] = "projects/osb/wiki"
url_path["test_projectFiles"] = "projects/osb/files"
url_path["test_projectSettings"] = "projects/osb/settings"
url_path["test_projectIssues"] = "projects/osb/issues"
url_path["test_projectNews"] = "projects/osb/news"

class TestWebPages(unittest.TestCase):
    longMessage = True

    @classmethod
    def setUpClass(cls):
        generalfunctions.USERNAME = USERNAME
        generalfunctions.PASSWORD = PASSWORD 
        generalfunctions.url_base = url_base
        generalfunctions.url_path = url_path

    def getPageContent(self, url=None):
        if not url:
            url = url_base + url_path[self._testMethodName]
        page, e = get_page(url)
        if e is not None:
            exceptionMessage = "URL: %s produced error %d (%s)" % (url,e.code,e.msg)
            self.fail(exceptionMessage)
        self.assertIsNotNone(page, CONTENT_PAGE_ERROR + " / Page is blank")
        return page

    def getPageContentURL(self, url):
        page, e = get_page(url)
        if e is not None:
            exceptionMessage = "URL: %s produced error %d (%s)" % (url,e.code,e.msg)
            self.fail(exceptionMessage)
        self.assertIsNotNone(page, CONTENT_PAGE_ERROR + " / Page is blank")
        return page
        
    def test_home(self):
        self.check_general_aspects()

    def test_projects(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="cells"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="technology"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="groups"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="people"), CONTENT_PAGE_ERROR)
        
    def test_projectsGraph(self):
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        #GRAPH TAB
        self.assertIsNotNone(soup.find(id="jsontree"), CONTENT_PAGE_ERROR)
        
    def test_projectsList(self):     
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        #LIST TAB
        self.assertIsNotNone(soup.find(id="cellslist"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(href="#cell9"), CONTENT_PAGE_ERROR)
        
    def test_projectsCarousel(self):     
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        #CAROUSEL TAB
        self.assertIsNotNone(soup.find(id="carouselMainPage"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(href="/projects/purkinjecell"), CONTENT_PAGE_ERROR)
        
        #self.assertIsNotNone(soup.find_all("svg"), CONTENT_PAGE_ERROR)
        
    def test_projectsCloud(self):     
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        #TAGS CLOUD TAB
        self.assertIsNotNone(soup.find(id="tagCanvas"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href=re.compile("neuroConstruct")), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href=re.compile("Detailed cell model")), CONTENT_PAGE_ERROR)
        
    def test_technology(self):
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find_all(href="#cell81"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="cell81"), CONTENT_PAGE_ERROR)
        
    def test_projectsGroups(self):
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="group7"), CONTENT_PAGE_ERROR)
        
    def test_people(self):
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="user4"), CONTENT_PAGE_ERROR)
        #print soup.prettify()
        
    def test_informationOSB(self):
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
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
        
    def test_doc(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        #NAV BAR
        self.assertIsNotNone(soup.find_all(id="project_overview_list"), CONTENT_PAGE_ERROR)
        #CONTENT
        self.assertIsNotNone(soup.find_all(id="helpTitle"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(class_="page-header"), CONTENT_PAGE_ERROR)

    def get_soup(self, url):
        page = self.getPageContentURL(url)
        return BeautifulSoup(page, "lxml")

    def check_general_aspects(self, url=None, page_title='Open Source Brain', check_title=True, check_header_footer=True):
        if not url:
            page = self.getPageContent()
        else:
            page = self.getPageContent(url)
        soup = BeautifulSoup(page, "lxml")
        
        if check_title:
            self.assertEqual(soup.title.string, page_title, CONTENT_PAGE_ERROR + " / Title does not match")
        if check_header_footer:
            self.assertIsNotNone(soup.find(id="osblogo"), CONTENT_PAGE_ERROR + " / OSB logo can not be found")
            self.assertIsNotNone(soup.find(id="wellcomelogolink"), CONTENT_PAGE_ERROR + " / Wellcome logo in footer can not be found")
            self.assertIsNotNone(soup.find_all(class_="footer-links"), CONTENT_PAGE_ERROR + " / Footer links can not be found")
        
        return soup

# Projects
# these belong to different categories (OSB, Project, Theme)
projects = {"osb": {"title": "The Open Source Brain repository"},
            "nc_superdeep": {"title": "CA1 Pyramidal Sublayer Microcircuit - Lee et al 2014 "},
            "corticalmodelling": {"title": "Neocortical modelling"}}

class TestProjectPagesMeta(type):
    def __new__(mcs, name, bases, dict):
        def gen_index_test(project):
            def test(self):
                url = "{}projects/{}".format(url_base, project)
                soup = self.get_soup(url)
                self.check_general_aspects(url, 'Overview - {} - Open Source Brain'.format(projects[project]["title"]))
                #CHECKING SPECIFIC ASPECTS
                #NAV BAR
                self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)
                #CHECK TABS
                self.assertIsNotNone(soup.find_all(href="#description"), CONTENT_PAGE_ERROR)
                self.assertIsNotNone(soup.find(id="description"), CONTENT_PAGE_ERROR)
                #self.assertIsNotNone(soup.find_all(href="#subprojects"), CONTENT_PAGE_ERROR)
                #self.assertIsNotNone(soup.find(id="subprojects"), CONTENT_PAGE_ERROR)
                self.assertIsNotNone(soup.find_all(href="#members"), CONTENT_PAGE_ERROR)
                self.assertIsNotNone(soup.find(id="members"), CONTENT_PAGE_ERROR)
            return test

        def gen_activity_test(project):
            def test(self):
                url = "{}projects/{}/activity".format(url_base, project)
                soup = self.get_soup(url)
                self.check_general_aspects(url, page_title = 'Activity - {} - Open Source Brain'.format(projects[project]["title"]))
                #NAV BAR
                self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)
                #CHECK ACTIVITIES
                self.assertIsNotNone(soup.find_all(class_="activity-item"), CONTENT_PAGE_ERROR)
            return test

        def gen_wiki_test(project):
            def test(self):
                url = "{}projects/{}/wiki".format(url_base, project)
                soup = self.get_soup(url)
                self.check_general_aspects(url, page_title = 'Wiki - {} - Open Source Brain').format(projects[project]["title"])
                #CHECKING SPECIFIC ASPECTS
                #NAV BAR
                self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)
                #CONTRIBUTORS
                self.assertIsNotNone(soup.find_all(href="/users/4"), CONTENT_PAGE_ERROR)
                #WIKI CONTENT
                self.assertIsNotNone(soup.find_all(href="Open-Source-Brain-Wiki"), CONTENT_PAGE_ERROR)
                self.assertIsNotNone(soup.find_all(href="Questions"), CONTENT_PAGE_ERROR)
            return test

        def gen_files_test(project):
            def test(self):
                url = "{}projects/{}/files".format(url_base, project)
                soup = self.get_soup(url)
                self.check_general_aspects(url, page_title = 'Files - {} - Open Source Brain'.format(projects[project]["title"]))
                #CHECKING SPECIFIC ASPECTS 
                #NAV BAR
                self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)
                #FILES
                self.assertIsNotNone(soup.find_all(class_="list"), CONTENT_PAGE_ERROR)
            return test

        def gen_settings_test(project):
            def test(self):
                url = "{}projects/{}/settings".format(url_base, project)
                soup = self.get_soup(url)
                self.check_general_aspects(url)
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
            return test
                                           
        def gen_issues_test(project):
            def test(self):
                url = "{}projects/{}/issues".format(url_base, project)
                soup = self.get_soup(url)
                self.check_general_aspects(url, page_title = 'Issues - {} - Open Source Brain'.format(projects[project]["title"]))
                #CHECKING SPECIFIC ASPECTS
                #NAV BAR
                self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)  
                #CONTENT
                self.assertIsNotNone(soup.find_all(id="issues_list"), CONTENT_PAGE_ERROR)
                self.assertIsNotNone(soup.find_all(class_="odd"), CONTENT_PAGE_ERROR)
            return test
                                                  
        def gen_news_test(project):
            def test(self):
                url = "{}projects/{}/news".format(url_base, project)
                soup = self.get_soup(url)
                self.check_general_aspects(url, page_title = 'News - {} - Open Source Brain'.format(projects[project]["title"]))
                #CHECKING SPECIFIC ASPECTS
                #NAV BAR
                self.assertIsNotNone(soup.find_all(id="menucontainer"), CONTENT_PAGE_ERROR)      
                #CONTENT
                self.assertIsNotNone(soup.find_all(class_="author"), CONTENT_PAGE_ERROR)
                self.assertIsNotNone(soup.find_all(class_="wiki"), CONTENT_PAGE_ERROR)
            return test
                                           
        for project in projects:
            dict["test_{}_index".format(project)] = gen_index_test(project)
            dict["test_{}_activity".format(project)] = gen_activity_test(project)
            dict["test_{}_wiki".format(project)] = gen_wiki_test(project)
            dict["test_{}_files".format(project)] = gen_files_test(project)
            dict["test_{}_settings".format(project)] = gen_settings_test(project)
            dict["test_{}_issues".format(project)] = gen_issues_test(project)
            dict["test_{}_news".format(project)] = gen_news_test(project)
                                           
        return type.__new__(mcs, name, bases, dict)

    
class TestProjectPages(TestWebPages, unittest.TestCase):
    __metaclass__ = TestProjectPagesMeta

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
    
    unittest.main(verbosity=2)
    
    #if testResult.wasSuccessful() is False:
        #mailText = "Errors\n" + str(testResult.errors) + "Failures\n" + str(testResult.failures)  
        #generalfunctions.sendmail('adrianquintana@gmail.com', 'adrianquintana@gmail.com', mailText)
