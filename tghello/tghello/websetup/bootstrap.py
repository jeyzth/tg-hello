# -*- coding: utf-8 -*-
"""Setup the tghello application"""
from __future__ import print_function
from tghello import model


def bootstrap(command, conf, vars):
    """Place any commands to setup jeyzth42 here"""
    # <websetup.bootstrap.before.auth
    
    t1 = model.TaskOne()
    t1.name = 'Evgen'
    t1.lastname = 'Anonimov'
    t1.dateofbird='01.01.1973'
    t1.bio="""I like cats, but don't like dogs. """
    
    t1.email='jeyzth@gmail.com'
    t1.jabber='jeyzth@khavr.com'
    t1.skype='jeyzth'
    t1.othr="Phones 717123456 Mobile +77011234567"
    
    model.DBSession.flush()
    model.DBSession.clear()

    # <websetup.bootstrap.after.auth>
