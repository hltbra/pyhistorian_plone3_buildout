import unittest
from pyhistorian import Story, Scenario, Given, When, Then
from pyhistorian import plone
from base import TestCase

class PyhistorianFirstStory(Story):
    """
    As a smart plone guy
    I want to use pyhistorian
    So that I can try some BDD
    """
    scenarios = ['PassingScenario', 'AnotherPassingScenario']


class PassingScenario(Scenario, TestCase):

    @Given('I am logged as portal owner')
    def login_as_portal_owner(self):
        self.setUp()
        self.loginAsPortalOwner()

    @When('I create a folder, titled "My First Folder"')
    def create_folder(self):
        self.portal.invokeFactory(type_name='Folder', id='folder1', title='My First Folder')

    @Then('I should see the title "My First Folder" in the root folder')
    def check_title(self):
        self.assertEquals('My First Folder', self.portal.folder1.title)

    Given('I am logged as portal owner')

class AnotherPassingScenario(Scenario, TestCase):

    Given('I am logged as portal owner')
    When('I create a folder, titled "My First Folder"')
    @Then('i should see stuff')
    def see_stuff(self):
        self.assertEqual(1,1)

def test_suite():
    return plone.PyhistorianPloneSuite(PyhistorianFirstStory())
