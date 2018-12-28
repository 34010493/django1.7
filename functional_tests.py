from selenium import webdriver

browser = webdriver.Firefox('/Users/Harry/Work/django/test/')

browser.get('http://localhost:8000')

assert 'Django' in browser.title