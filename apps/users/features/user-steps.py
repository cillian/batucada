from lettuce import step, world
from lettuce.django import django_url
from nose.tools import assert_equals
from lxml import html
from users.models import UserProfile
from django.core import mail

@step(u'I go to the "(.*)" URL')
def i_go_to_the_url(step, url):
    world.response = world.browser.visit(django_url(url))

@step(u'a user exists with username "(.*)"')
def a_user_exists_with_username(step, p_username):
    user = UserProfile(username=p_username, email='example@example.com')
    user.set_password('secret007')
    user.save()

@step(u'Given a user exists with username: "(.*)", password: "(.*)"')
def given_a_user_exists_with_email_and_password(step, p_username, p_password):
    # ToDo: remove duplication with above step.
    user = UserProfile(username=p_username, email='example@example.com')
    user.set_password(p_password)
    user.save()

@step(u'I fill in "(.*)" with "(.*)"')
def i_fill_in(step, field, value):
    world.browser.fill(field, value)

@step(u'I check "(.*)"')
def i_check(step, field):
    world.browser.check(field)

@step(u'I press "(.*)"')
def i_press(step, button_label):
    # ToDo: .click() doesn't work with zope.testbrowser on buttons
    button = world.browser.find_by_xpath('//button[text()="%s"]' % button_label).first
    button.click()

@step(u'I move focus away from the username field')
def and_i_move_focus_away_from_the_username_field(step):
    world.browser.fill("password", "value")
    world.browser.wait_for_xpath('//*[@id="availability" and text()="not available"]')

@step(u'I should see "(.*)"')
def i_should_see(step, text):
    assert text in world.browser.html

@step(u'I should receive an email at "(.*)" with the subject "(.*)"')
def i_should_receive_email_with_subject(step, address, subject):
    assert_equals(len(mail.outbox), 1)
    assert_equals(mail.outbox[0].to, [address,])
    assert_equals(mail.outbox[0].subject, subject)

@step(u'the page title should be "(.*)"')
def the_page_title_should_be(step, page_title):
    assert_equals(world.browser.title, page_title)

