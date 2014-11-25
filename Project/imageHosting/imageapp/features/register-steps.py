from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from imageapp.models import User

@before.all
def set_browser():
    world.browser = Client()

@step(r'that I hit register now with one or more fields not filled')
def register(step):
	response = world.browser.get('/register/')
	world.dom = html.fromstring(response.content)

@step(r'I should see "(.*)" at the empty field')
def see_empty_headers(step, text):
    header = world.dom.cssselect('h1')
    for h in header:
		if h.text == text:	
			assert h.text == text



@step(r'that I hit register now without all fields filled')
def some_fields(step):
	pass 
	
@step(r'I should see "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')
    for h in header:
		if h.text == text:	
			assert header.text == text


@step(r'that I enter an existing email only')
def existing_email(step):
	pass 

@step(r'I should see "(.*)" and "(.*)"')
def see_headers(step, text, text2):
    header = world.dom.cssselect('h1')
    for h in header:
		if h.text == text:	
			for c in header:
				if c.text == text2:
					assert header.text == text

@step(r'that I hit register now with a non-existing email and all fields are filled')
def register_new_user(step):
	pass 

