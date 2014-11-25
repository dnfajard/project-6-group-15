from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from imageapp.models import User



@step(r'that I need to contact the owner of imageSpace')
def hit_contact(step):
	response = world.browser.get('/contact/')
	world.dom == html.fromstring(response.content)
	
@step(r'I should see "(.*)"')
def see_page(step, url):
        response = world.browser.get(url)
        world.dom == html.fromstring(response.content)
	

@step(r'that I want to go to the home page')
def click_home(step):
	response = world.browser.get('/home/')
	world.dom = html.fromstring(response.content)


@step(r'that I want to upload a new photo')
def upload(step):
	response = world.browser.get('/upload/')
	world.dom = html.fromstring(response.content)

@step(r'that I want to change my profile pictures')
def change_profile_picture(step):
	response = world.browser.get('/settings/')
	world.dom = html.fromstring(response.content)

@step(r'that I am done using imageSpace')
def logout(step,url):
	response = world.browser.get(url)
	world.dom = html.fromstring(response.content)

@step(r'I should see header "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')
    for h in header:
		if h.text == text:	
			assert header.text == text
	
