import unittest
from pyhistorian import *
from base import TestCase


####
# todo:
# make a story with a couple of scenarios
# and try using plone stuff on that
# like creating content type
####
class PyhistorianFirstStory(Story):
    """
    As a smart plone guy
    I want to use pyhistorian
    So that I can try some BDD
    """


class PassingScenario(Scenario):
    @Then('it should pass')
    def pass_ok(self):
        pass



def test_suite():
    return unittest.TestSuite([suite.PyhistorianSuite(PyhistorianFirstStory())])
