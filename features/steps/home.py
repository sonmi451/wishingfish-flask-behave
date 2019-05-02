''' all behave tests '''

################################################################################
# IMPORT

import time
import requests
from bs4 import BeautifulSoup as bs

################################################################################
# TEAMPLATES

@given('')
def the_thing(context):
    return context

@when('')
def a_thing_is_done(context):
    return context

@then('')
def the_thing_is_this(context):
    return context

################################################################################
# CONSTANTS

FLASK = "http://localhost:5000/"
PAGE_TITLE = "wishing fish cards"


IMAGES = {
        "Semyorka": "/static/Semyorka.jpg",
        "Molniya": "/static/Molniya.jpg"
        }

OK = "<Response [200]>"

################################################################################
# FUNCTIONS

def get_page(url):
    server_response = requests.get(url)
    page_text = server_response.text
    page_html = bs(page_text)
    print(server_response, page_text)
    return server_response, page_text, page_html

def find_img_src(page_html):
    image_elem = page_html.find('img')
    image_name = '{}'.format(image_elem['src'])
    return image_name

def find_a_href(page_html):
    a_elem = page_html.find('a')
    a_href = a_elem['href']
    return a_href

################################################################################
# GIVEN

@given('you are on the {homepage}')
def get_homepage(context, homepage):
    homepage = FLASK
    context.page_response, context.page_text, context.page_html = get_page(homepage)

################################################################################
# WHEN

@when('you click the shop link')
def get_shop_url(context):
    shop_url = find_a_href(context.page_html)
    context.shop_page_response, context.shop_page_text, context.shop_page_html \
    = get_page(shop_url)
    assert "etsy" in shop_url
    return context

################################################################################
# THEN

@then('you wait for {seconds} seconds')
def wait_for_refresh(seconds):
    wait_time = int(seconds)
    time.sleep(wait_time)

@then('you refresh the page')
def refresh_page(context):
    context.refresh_page_response, context.refresh_page_text, context.refresh_page_html \
    = get_page(FLASK)

@then('the page title is displayed')
def title_check(context):
    assert PAGE_TITLE in context.page_text

@then('the navigation panel is displayed')
def navigtion_check(context):
    assert "shop" in context.page_text

@then('the main content is displayed')
def main_content_check(context):
    context.image_name = find_img_src(context.page_html)
    assert context.image_name in IMAGES.values()

@then('you are taken to the etsy shop')
def etsy_check(context):
    assert OK == '{}'.format(context.shop_page_response)

@then('the main content shows a new image')
def new_image(context):
    context.new_image_name = find_img_src(context.refresh_page_html)
    assert context.new_image_name != context.image_name
