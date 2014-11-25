from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from imageapp.models import User


@step(r'that I want a new photo')
def new_photo(step):
	pass #needs work

@step(r'I select a photo')
def select_photo(step):
	pass #needs work

@step(r'I should see the file name')
def filename(step):
	pass #needs work

@step(r'when I click "(.*)" I should see the new photo in an icon')
def click_submit(step, button):
	pass #needs work


@step(r'that I click "(.*)"')
def click(step, button):
	pass #needs work

@step(r'I should see header "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')
    for h in header:
		if h.text == text:	
			assert header.text == text

@step(r'that I am done using imageSpace')
def logout(step):
	response = world.browser.get('/logout/')
	world.dom = html.fromstring(response.content)

@step(r'that I need to contact the owner of imageSpace')
def contact(step):
	response = world.browser.get('/contact/')
	world.dom = html.fromstring(response.content)

@step(r'I should see "(.*)"')
def see_page(step, url):
        response = world.browser.get(url)
        world.dom == html.fromstring(response.content)

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
