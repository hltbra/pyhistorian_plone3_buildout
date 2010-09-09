import unittest
from pyhistorian import *
from base import TestCase, FunctionalTestCase


class PyhistorianFirstStory(Story):
    """
    As a smart plone guy
    I want to use pyhistorian
    So that I can try some BDD
    """
    scenarios = ['PassingScenario']


class PassingScenario(Scenario, TestCase):
    @Given('I am logged as portal owner')
    def given2_pass(self):
        self.setUp()
        self.loginAsPortalOwner()

    @When('I create a folder, titled "My First Folder"')
    def when2_pass(self):
        self.portal.invokeFactory(type_name='Folder', id='folder1', title='My First Folder')

    @Then('I should see the title "My First Folder" in the root folder')
    def pass2_ok(self):
        self.assertEquals('My First Folder', self.portal.folder1.title)


def test_suite():
    return unittest.TestSuite([suite.PyhistorianSuite(PyhistorianFirstStory())])
