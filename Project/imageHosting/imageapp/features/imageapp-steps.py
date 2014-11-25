from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from imageapp.models import User

@before.all
def set_browser():
    world.browser = Client()

#1	
@step(r'that I hit log in')
def hit_login(step,url):
	response = world.browser.get(url)
        world.dom = html.fromstring(response.content)
	
@step(r'I should see "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')
    for h in header:
		if h.text == text:	
			assert header.text == text

#2			
@step(r'that I enter my email')
def enter_email(test):
	user = create_test_user()
	user.email = "nikifajardo@yahoo.com"
	response = world.browser.get(url)
        world.dom = html.fromstring(response.content)

@step(r'I should see "(.*)"')
def error_header(step, text):
	header = world.dom.cssselect('h1')
	for h in header:
		    if h.text == text:	
			    assert header.text == text

#3
@step(r'that I enter my password')
def enter_password(test):
	user = create_test_user()
	user.password = "1234567890"
	response = world.browser.get(url)
        world.dom = html.fromstring(response.content)

#@step(r'I should see "(.*)"')

#4
@step(r'that I enter the wrong password')
def wrong_pass(test):
	user = create_test_user()
	user.email = "nikifajardo@yahoo.com"
	user.password = "hgajghlkhdf"
	response = world.browser.get(url)
        world.dom = html.fromstring(response.content)

#@step(r'I should see "(.*)"')


#5
@step(r'that I enter a valid email/password')
def valid_info(step):
        url = "http://localhost:8000"
	user = create_test_user()
	user.email = "nikifajardo@yahoo.com"
	user.password = "1234567890"
	response = world.browser.get(url)
        world.dom = html.fromstring(response.content)

#@step(r'I should see "(.*)"')


def create_test_user():
	first_name = ""
	second_name = ""
	email = ""
	password = ""
	return  User(first_name=first_name, second_name=second_name, email=email, password=password)
