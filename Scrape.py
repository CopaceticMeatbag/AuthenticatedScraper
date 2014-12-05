import requests
from bs4 import BeautifulSoup as bs

###------STATIC VARIABLES-----###
Username="USERNAME"
Password="PASSWORD"
loginURL="https://myaccount.website.com/login.aspx"
secureURL = 'https://myaccount.website.com/ProtectedPage.aspx'
headers={"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"}
s=requests.Session()
###----------------------------###

###-------MAIN FUNCTION--------###
def main():
    s.headers.update(headers)
    SessionData();
    SecretData = ProtectedData();
    print(SecretData)
###----------------------------###

###---------FUNCTIONS----------###
def SessionData():
    r=s.get(loginURL)
    soup=bs(r.content)
    dataFields = {'ctl00$MemberToolsContent$txtUsername':Username,
                  'ctl00$MemberToolsContent$txtPassword':Password,
                  'ctl00$MemberToolsContent$btnLogin':"Login",
                  'MemberToolsContent_HiddenField_Redirect':"",
                  'ctl00_TopMenu_RadMenu_TopNav_ClientState':"",
                  'RadMasterScriptManager_TSM':"",
                  '__EVENTTARGET':(soup.find(id="__EVENTTARGET")['value']),
                  '__EVENTARGUMENT':(soup.find(id="__EVENTARGUMENT")['value']),
                  '__VIEWSTATE':(soup.find(id="__VIEWSTATE")['value']),
                  '__VIEWSTATEGENERATOR':(soup.find(id="__VIEWSTATEGENERATOR")['value'])}
    s.post(loginURL,data=dataFields)

def ProtectedData():
    retVals = {};
    r2 = s.get(secureURL)
    soup = bs(r2.content)
    for string in soup.find(id="YourFieldIDHere"):
        retVals['RetreivedField'] = string
    return retVals;

###----------------------------###
if __name__ == "__main__":
    main()
