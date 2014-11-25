from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from imageapp.models import User

@before.all
def set_browser():
    world.browser = Client()

@step(r'that I am a new user')
def new_user(step):
	pass #needs work
@step(r'I see "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')
    for h in header:
		if h.text == text:	
			assert header.text == text

@step(r'I click "Upload photo"')
def upload_photo(step):
	pass #needs work


@step(r'I should see "(.*)"')
def see_page(step, url):
    response = world.browser.get(url)
    world.dom == html.fromstring(response.content)

@step(r'that I am an existing user')
def check_existing(step):
	pass #needs work

@step(r'I should see all of my uploaded pictures')
def check_photos(step):
	pass #needs work

@step(r'that I want to edit a photo')
def want_to_edit(step):
	pass #needs work

@step(r'I click edit')
def click_edit(step):
	pass #needs work

@step(r'I should see an adjustment bar that enhances the brightness')
def see_edit_tool(step):
	pass #needs work

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


@step(r'that I am done using imageSpace')
def logout(step):
	response = world.browser.get('/logout/')
	world.dom = html.fromstring(response.content)
	

