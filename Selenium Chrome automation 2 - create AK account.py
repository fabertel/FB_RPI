
"""
Created on Mon Jun  3 11:18:17 2019
Chrome automation - aprire chrome e fare una ricerca 


"""
#installare https://chromedriver.storage.googleapis.com/index.html?path=74.0.3729.6/


import os 
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print(os.getcwd())
sys.path.append("c:\\users\\105028218\\box sync\\fb pc sync\\python\\venv\\lib\\site-packages")

browser = webdriver.Chrome(r"C:\Users\105028218\Box Sync\FB PC SYNC\PYTHON\venv\Lib\site-packages\chromedriver.exe")

# TEST AK 
browser.get('https://ak.na02.ibhge.com/index.html#/usercreation')
time.sleep(5)

SSOL = browser.find_element_by_name("username")
SSOL.send_keys("105028218")
SSOL = browser.find_element_by_name("password")
SSOL.send_keys("S23dS23dS23d")
SSOL.send_keys(Keys.RETURN)

time.sleep(3)
browser.get("https://ak.na02.ibhge.com/index.html#/usercreation");
time.sleep(7)
            
#bottone = browser.find_element_by_xpath("//body/div/div/div/div/span/input")

checkbox = browser.find_element_by_xpath("//input[@value='Add New User']")
checkbox.click() 

time.sleep(3)

SSOI = browser.find_element_by_xpath("//*[@id=\"ngdialog1\"]/div[2]/div[1]/div[2]/form/table/tbody/tr[1]/td[2]/input")
SSOI.send_keys("105028218")

#selezionare da menu a tendina 

#Questo va correggere su SUBMIT !! 
#SSOI = browser.find_element_by_xpath("//*[@id=\"ngdialog1\"]/div[2]/div[1]/div[3]/button[1]")
#SSOI .click() 



# ---BACKUP -------

#bottone = browser.find_element_by_class_name("btn btn-success btn-flat")
#bottone = browser.find_element_by_tag_name("input")
#print(bottone)
#bottone.click()

##browser.execute_script("javascript:addNewEntity();")
#for x in range(2):
#    browser.send_keys(Keys.TAB)
##    
##browser.send_keys(Keys.RETURN)

#<input type="button" class="btn btn-success btn-flat" value="Add New User" ng-click="functions.addNewEntity()">
       
#CAMPO LOGIN SSO 
#<input name="username" type="text" id="username" placeholder="SSO ID" autocomplete="off">
#CAMPO PASSW SSO
#<input name="password" placeholder="Password" type="password" id="password" autocomplete="off" onkeypress="javascript:eventHandler(event)">

#-------------------
# TEST FUNZIONANTE SU PAGINA SELENIUM 
#browser.get('https://www.seleniumhq.org')
#assert "Python" in browser.title
#elem = browser.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in browser.page_source
#browser.close()
#-------------------

#<input type="button" class="btn btn-success btn-flat" value="Add New User" ng-click="functions.addNewEntity()">
