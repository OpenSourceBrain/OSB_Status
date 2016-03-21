import random
import unittest
import sys
from bs4 import BeautifulSoup
import generalfunctions
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


#ERRORS
generalfunctions.CONTENT_PAGE_ERROR = "Content Page Error"

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
        self.assertIsNotNone(soup.find(id="slider"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="content"), generalfunctions.CONTENT_PAGE_ERROR)

    ##############
    ## OLD URLS ##
    ##############
    def test_old_meetings(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text=re.compile("Workshops")), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="workshops_table"), generalfunctions.CONTENT_PAGE_ERROR)

    def test_old_neuroml2coretypes_cells(self):
        soup = self.check_general_aspects_component_types()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text=re.compile("baseCell")), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text=re.compile("baseChannelDensityCond")), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text=re.compile("biophysicalProperties")), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(href="Cells.html#baseCell"), generalfunctions.CONTENT_PAGE_ERROR)
        
        
    def test_old_neuromlvalidator_string(self):    
        soup = self.check_general_aspects(page_title= "Validate NeuroML file", check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find("h1"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find("textarea"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.findAll('input', {'type':'submit'}), generalfunctions.CONTENT_PAGE_ERROR)
        
    def test_old_neuromlvalidator_file(self):
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find("h3"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Converting the file: MorphML_v1.8.1.xsd"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="SpineShape"), generalfunctions.CONTENT_PAGE_ERROR)
        

    def test_old_view(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Specifications for NeuroML v1.8.1"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find("h3"), generalfunctions.CONTENT_PAGE_ERROR)

    def test_old_lems(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find("li"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="NeuroML Version 2.0"), generalfunctions.CONTENT_PAGE_ERROR)
        
    ################### 
    ## General Pages ##
    ###################
    def test_specifications(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Specifications for NeuroML v1.8.1"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find("h3"), generalfunctions.CONTENT_PAGE_ERROR)

    def test_examples(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Examples"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all("table"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 1: "), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 2: "), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 3: "), generalfunctions.CONTENT_PAGE_ERROR)
        
    def test_relevant_publications(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Publications"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Book Chapters"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Abstracts"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="http://www.ncbi.nlm.nih.gov/pubmed/24795618"), generalfunctions.CONTENT_PAGE_ERROR)
        
    def test_tool_support(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Current Application Support For NeuroML"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="longlist"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="http://www.neurodynamics.nl/netmorph.html"), generalfunctions.CONTENT_PAGE_ERROR)
        
    def test_browse_models(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Models"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(id="highlighted"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="/NeuroMLValidator/Samples.jsp"), generalfunctions.CONTENT_PAGE_ERROR)
        
    def test_history(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="A Brief History of NeuroML"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(href="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1088511/"), generalfunctions.CONTENT_PAGE_ERROR)
                                  
    def test_projects(self):
        soup = self.check_general_aspects()
        #CHECKING SPECIFIC ASPECTS 
        self.assertIsNotNone(soup.find(text="Get NeuroML"), generalfunctions.CONTENT_PAGE_ERROR)   
        self.assertIsNotNone(soup.find(id="longlist"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Specifications & examples"), generalfunctions.CONTENT_PAGE_ERROR)                             

    ############################ 
    ## NeuromlValidator Pages ##
    ############################
    def test_neuromlvalidator_samples(self):
        soup = self.check_general_aspects(page_title='Samples of NeuroML files', check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="Examples of NeuroML files"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all("table"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 1: "), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 2: "), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find(text="Level 3: "), generalfunctions.CONTENT_PAGE_ERROR)
        
    def test_neuromlvalidator_neuroml_level2(self):
        soup = self.check_general_aspects(check_title=False, check_header_footer=False)
        
    ######################### 
    ## Neuroml2 Core Pages ##
    #########################    
    def test_neuroml2coretypes_pynn(self):
        soup = self.check_general_aspects_component_types(page_title='PyNN')
        #CHECKING SPECIFIC ASPECTS
        self.assertIsNotNone(soup.find(text="PyNN"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all("table"), generalfunctions.CONTENT_PAGE_ERROR)
        self.assertIsNotNone(soup.find_all(class_="sidebar-nav"), generalfunctions.CONTENT_PAGE_ERROR)
    
    ######################### 
    ## CRCNS2014 Pages ##
    #########################
    def test_CRCNS2014(self):
        soup = self.check_general_aspects(page_title='CRCNS 2014', check_header_footer=False)
        #CHECKING SPECIFIC ASPECTS 
        self.assertIsNotNone(soup.find(text="Local Organizers: Brian Smith and Sharon Crook"), generalfunctions.CONTENT_PAGE_ERROR)

    ########### 
    ## Utils ##
    ###########
    def check_general_aspects(self, page_title='NeuroML - A Model Description Language for Computational Neuroscience', check_title=True, check_header_footer=True):
        page = generalfunctions.getPageContent(self)
        soup = BeautifulSoup(page)
        
        if check_title:
            self.assertEqual(soup.title.string, page_title, generalfunctions.CONTENT_PAGE_ERROR + " / Title does not match")
        if check_header_footer:
            self.assertIsNotNone(soup.find(id="logo"), generalfunctions.CONTENT_PAGE_ERROR + " / NeuroML logo can not be found")
            self.assertIsNotNone(soup.find(id="nav"), generalfunctions.CONTENT_PAGE_ERROR + " / Navigation bar can not be found")
            self.assertIsNotNone(soup.find_all(class_="page_item"), generalfunctions.CONTENT_PAGE_ERROR + " / Footer links can not be found")
        
        return soup
    
    def check_general_aspects_component_types(self, page_title='Cells', check_title=True, check_header_footer=True):
        page = generalfunctions.getPageContent(self)
        soup = BeautifulSoup(page)
        
        if check_title:
            self.assertEqual(soup.title.string, page_title, generalfunctions.CONTENT_PAGE_ERROR + " / Title does not match")
        if check_header_footer:
            self.assertIsNotNone(soup.find_all(class_="brand"), generalfunctions.CONTENT_PAGE_ERROR + " / NeuroML Component Types logo can not be found")
            self.assertIsNotNone(soup.find(class_="container").find_all("li"), generalfunctions.CONTENT_PAGE_ERROR + " / Navigation bar can not be found")
        
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
