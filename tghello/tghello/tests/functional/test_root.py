# -*- coding: utf-8 -*-
"""
Functional test suite for the root controller.

This is an example of how functional tests can be written for controllers.

As opposed to a unit-test, which test a small unit of functionality,
functional tests exercise the whole application and its WSGI stack.

Please read http://pythonpaste.org/webtest/ for more information.

"""

from nose.tools import ok_

from tghello.tests import TestController


class TestRootController(TestController):
    """Tests for the method in the root controller."""

    def test_index(self):
        """The front page is working properly"""
        response = self.app.get('/')
        msg = '42 Coffee Cups Test Assignment '
        email = '@gmail.com'
        jabber = '@khavr.com'
        # You can look for specific strings:
        ok_(msg in response and email in response and jabber in response, "Evgen!\nThere are no control frase here!" )

        # You can also access a BeautifulSoup'ed response in your tests
        # (First run $ easy_install BeautifulSoup
        # and then uncomment the next two lines)

        # links = response.html.findAll('a')
        # print(links)
        # ok_(links, "Mummy, there are no links here!")

