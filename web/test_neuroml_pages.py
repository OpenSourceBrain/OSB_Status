import random
import unittest
import sys
from bs4 import BeautifulSoup
import generalfunctions
from generalfunctions import CONTENT_PAGE_ERROR, getPageContent
import re

USERNAME = None
PASSWORD = None

url_base = "http://www.neuroml.org/"
# url_base = "http://spike.la.asu.edu"
# url_base = "http://127.0.0.1:3000/"

url_path = {}
#Home Page
url_path["test_home"] = ""

#old urls (should be working) 
url_path["test_old_meetings"] = "meetings.php" #Redirect to workshops
url_path["test_old_neuroml2coretypes_cells"] = "NeuroML2CoreTypes/Cells.html" 
url_path["test_old_neuromlvalidator_string"] = "NeuroMLValidator/Validation.jsp?pastedFile=%3Cb%3Ell%3C/b%3E"
url_path["test_old_neuromlvalidator_file"] = "NeuroMLValidator/Transform.jsp?localFile=NeuroMLFiles/Schemata/v1.8.1/Level1/MorphML_v1.8.1.xsd&xslFile=NeuroMLFiles/Schemata/XSD_Readable.xsl"
url_path["test_old_view"] = "view.php"
url_path["test_old_lems"] = "lems/"

#General Pages
url_path["test_specifications"] = "specifications"
url_path["test_examples"] = "examples"
url_path["test_relevant_publications"] = "relevant_publications"
url_path["test_tool_support"] = "tool_support"
url_path["test_browse_models"] = "browse_models"
url_path["test_history"] = "history"
url_path["test_projects"] = "projects"

#NeuromlValidator Pages
url_path["test_neuromlvalidator_samples"] = "NeuroMLValidator/Samples.jsp"
url_path["test_neuromlvalidator_neuroml_level2"] = "NeuroMLValidator/NeuroMLFiles/Schemata/v1.8.1/Level2/NeuroML_Level2_v1.8.1.xsd"

#Neuroml2core
url_path["test_neuroml2coretypes_pynn"] = "NeuroML2CoreTypes/PyNN.html#IF_curr_alpha"

#Temporal Webs
#CRCNS2014 Web
url_path["test_CRCNS2014"] = "CRCNS2014/"


class TestWebPages(unittest.TestCase):

    longMessage = True

    @classmethod
    def setUpClass(cls):
        generalfunctions.USERNAME = USERNAME
        generalfunctions.PASSWORD = PASSWORD  
        generalfunctions.url_base = url_base
        generalfunctions.url_path = url_path

    ###############
    ## Home Page ##
    ###############
    def test_home(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(id="slider"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="content"), CONTENT_PAGE_ERROR)

    ##############
    ## OLD URLS ##
    ##############
    def test_old_meetings(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text=re.compile("Workshops")), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="workshops_table"), CONTENT_PAGE_ERROR)

    def test_old_neuroml2coretypes_cells(self):
        soup = self.check_general_aspects_component_types()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text=re.compile("baseCell")), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text=re.compile("baseChannelDensityCond")), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text=re.compile("biophysicalProperties")), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(href="Cells.html#baseCell"), CONTENT_PAGE_ERROR)
        
        
    def test_old_neuromlvalidator_string(self):    
        soup = self.check_general_aspects(page_title= "Validate NeuroML file", check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find("h1"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find("textarea"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.findAll('input', {'type':'submit'}), CONTENT_PAGE_ERROR)
        
    def test_old_neuromlvalidator_file(self):
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find("h3"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Converting the file: MorphML_v1.8.1.xsd"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="SpineShape"), CONTENT_PAGE_ERROR)
        

    def test_old_view(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Specifications for NeuroML v1.8.1"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find("h3"), CONTENT_PAGE_ERROR)

    def test_old_lems(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find("li"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="NeuroML Version 2.0"), CONTENT_PAGE_ERROR)
        
    ################### 
    ## General Pages ##
    ###################
    def test_specifications(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Specifications for NeuroML v1.8.1"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find("h3"), CONTENT_PAGE_ERROR)

    def test_examples(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Examples"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all("table"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 1: "), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 2: "), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 3: "), CONTENT_PAGE_ERROR)
        
    def test_relevant_publications(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Publications"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Book Chapters"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Abstracts"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="http://www.ncbi.nlm.nih.gov/pubmed/24795618"), CONTENT_PAGE_ERROR)
        
    def test_tool_support(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Current Application Support For NeuroML"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="longlist"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="http://www.neurodynamics.nl/netmorph.html"), CONTENT_PAGE_ERROR)
        
    def test_browse_models(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Models"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="highlighted"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="/NeuroMLValidator/Samples.jsp"), CONTENT_PAGE_ERROR)
        
    def test_history(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="A Brief History of NeuroML"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1088511/"), CONTENT_PAGE_ERROR)
                                  
    def test_projects(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS 
        self.assertIsNotNone(soup.find(text="Get NeuroML"), CONTENT_PAGE_ERROR)   
        self.assertIsNotNone(soup.find(id="longlist"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Specifications & examples"), CONTENT_PAGE_ERROR)                             

    ############################ 
    ## NeuromlValidator Pages ##
    ############################
    def test_neuromlvalidator_samples(self):
        soup = self.check_general_aspects(page_title='Samples of NeuroML files', check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Examples of NeuroML files"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all("table"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 1: "), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 2: "), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 3: "), CONTENT_PAGE_ERROR)
        
    def test_neuromlvalidator_neuroml_level2(self):
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        
    ######################### 
    ## Neuroml2 Core Pages ##
    #########################    
    def test_neuroml2coretypes_pynn(self):
        soup = self.check_general_aspects_component_types(page_title='PyNN')
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="PyNN"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all("table"), CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(class_="sidebar-nav"), CONTENT_PAGE_ERROR)
    
    ######################### 
    ## CRCNS2014 Pages ##
    #########################
    def test_CRCNS2014(self):
        soup = self.check_general_aspects(page_title='CRCNS 2014', check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS 
        self.assertIsNotNone(soup.find(text="Local Organizers: Brian Smith and Sharon Crook"), CONTENT_PAGE_ERROR)

    ########### 
    ## Utils ##
    ###########
    def check_general_aspects(self, page_title='NeuroML - A Model Description Language for Computational Neuroscience', check_title=True, check_header_footer=True):
        page, e = getPageContent(url_base + url_path[self._testMethodName])
        if e is not None:
            exceptionMessage = "URL: %s produced error %d (%s)" % (url,e.code,e.msg)
            self.fail(exceptionMessage)
        self.assertIsNotNone(page, CONTENT_PAGE_ERROR + " / Page is blank")
        soup = BeautifulSoup(page, "lxml")
        
        if check_title:
            self.assertEqual(soup.title.string, page_title, CONTENT_PAGE_ERROR + " / Title does not match")
        if check_header_footer:
            self.assertIsNotNone(soup.find(id="logo"), CONTENT_PAGE_ERROR + " / NeuroML logo can not be found")
            self.assertIsNotNone(soup.find(id="nav"), CONTENT_PAGE_ERROR + " / Navigation bar can not be found")
            self.assertIsNotNone(soup.find_all(class_="page_item"), CONTENT_PAGE_ERROR + " / Footer links can not be found")
        
        return soup
    
    def check_general_aspects_component_types(self, page_title='Cells', check_title=True, check_header_footer=True):
        page, e = getPageContent(url_base + url_path[self._testMethodName])
        soup = BeautifulSoup(page, "lxml")
        
        if check_title:
            self.assertEqual(soup.title.string, page_title, CONTENT_PAGE_ERROR + " / Title does not match")
        if check_header_footer:
            self.assertIsNotNone(soup.find_all(class_="brand"), CONTENT_PAGE_ERROR + " / NeuroML Component Types logo can not be found")
            self.assertIsNotNone(soup.find(class_="container").find_all("li"), CONTENT_PAGE_ERROR + " / Navigation bar can not be found")
        
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
