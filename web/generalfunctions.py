import urllib
import urllib2
import base64
from bs4 import BeautifulSoup
import smtplib

USERNAME = None
PASSWORD = None
#ERRORS
CONTENT_PAGE_ERROR = "Content Page Error"

def get_page(url,username=None,password=None):
    request = urllib2.Request(url)
    if username is None:
        username = USERNAME
    if password is None:
        password = PASSWORD
    
    result = None
    req = urllib2.Request(url)
    if username and password:
        auth = base64.urlsafe_b64encode("%s:%s" % (username, password))
        req.add_header("Authorization", "Basic %s" % auth)
        #req.add_header("Content-Type", "application/json")
        #req.add_header("Accept", "application/json")
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        return None, e
    else:
        result = response.read()
    return result, None

    
def sendmail(from_who, to, msg):
    s = smtplib.SMTP('localhost')
    s.sendmail(from_who, [to], msg)
    s.quit()
    
