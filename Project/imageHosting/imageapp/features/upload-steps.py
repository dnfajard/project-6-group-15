from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from imageapp.models import User

@before.all
def set_browser():
    world.browser = Client()

@step(r'that I want a new photo')
def want_new_photo(step):
	pass 

@step(r'And I select a photo')
def select_photo(step):
	pass 

@step(r'I should see the file name')
def filename(step):
	pass 

@step(r'when I click "(.*)" I should see "(.*)"')
def check(step, button, url):
	pass 

@step(r'that I click "(.*)"')
def click(step, button):
	pass 

@step(r'I should see header "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')
    for h in header:
		if h.text == text:	
			assert header.text == text

@step(r'that I need to contact the owner of imageSpace')
def contact(step):
	response = world.browser.get('/contact/')
	world.dom = html.fromstring(response.content)

@step(r'that I want to go to the home page')
def home(step):
	response = world.browser.get('/home/')
	world.dom = html.fromstring(response.content)
	
@step(r'that I want to upload a new photo')
def upload(step):
	response = world.browser.get('/upload/')
	world.dom = html.fromstring(response.content)

@step(r'that I want to change my profile pictures')
def settings(step):
	response = world.browser.get('/settings/')
	world.dom = html.fromstring(response.content)
