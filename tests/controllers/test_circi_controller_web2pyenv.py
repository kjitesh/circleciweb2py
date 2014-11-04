#!/usr/bin/env python

'''py.test test cases to test people application.

These tests run simulating web2py shell environment and don't use webclient
module.

So, they run faster and don't need web2py server running.

If you want to see webclient approach, see test_people_controller_webclient.py
in this same directory.
'''

def test_default_index_exists(web2py):
    '''Page index exists?
    '''
    # run the controller, without view
    result = web2py.run('default', 'index', web2py)

    # now, render the view with context received from controller
    html = web2py.response.render('circi/index.html', result)
    assert "Hello World" in html

def test_all_tweets_page(web2py):
    """Check if all tweets page is displaying"""
    # run the controller, without view
    result = web2py.run('tweets', 'all', web2py)

    # now, render the view with context received from controller
    html = web2py.response.render('circi/all.html', result)
    assert "All Tweets" in html





