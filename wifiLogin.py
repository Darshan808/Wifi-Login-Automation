'''THIS PYTHON PROGRAM AUTOMATES THE BORING AND REPETITIVE TASK OF LOGGING IN EVERY TIME WE CONNECT TO CAMPUS WIFI'''

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def main():
    # <<<---------Enter Your Username Here------------------>>>
    my_username = '079bct036'
    # <<<----------Enter Your Password Here------------------>>>
    my_password = '2022-'  # fill this
    if (len(my_password) != 9):
        print("Fill your password!!!")
        return
    login_page_link = 'https://10.100.1.1:8090/httpclient.html'
    scripts = [f"document.querySelector('#username').value = '{my_username}'",
               f"document.querySelector('#password').value = '{my_password}'",
               "submitRequest()"]
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(options)
    browser.get(login_page_link)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    while (soup.find('div', class_='button') == None):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        sleep(.1)
    for i in range(len(scripts)):
        browser.execute_script(scripts[i])

    while (soup.find('h1', class_='entry-title') == None):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        sleep(.1)


if (__name__ == "__main__"):
    main()
