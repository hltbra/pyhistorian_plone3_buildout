import unittest
from pyhistorian import suite, Story, Scenario, Given, When, Then
from base import TestCase


class PyhistorianFirstStory(Story):
    """
    As a smart plone guy
    I want to use pyhistorian
    So that I can try some BDD
    """
    scenarios = ['PassingScenario']


class PassingScenario(Scenario, TestCase):
    @Given('I am logged as portal owner')
    def login_as_portal_owner(self):
        self.setUp()
        self.loginAsPortalOwner()

    @When('I create a folder, titled "My First Folder"')
    def create_folder1(self):
        self.portal.invokeFactory(type_name='Folder', id='folder1', title='My First Folder')

    @Then('I should see the title "My First Folder" in the root folder')
    def check_title(self):
        self.assertEquals('My First Folder', self.portal.folder1.title)


def test_suite():
    return suite.PyhistorianSuite(PyhistorianFirstStory())
