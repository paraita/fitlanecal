import os.path
import sys
from mock import patch
from fitlanecal import *

def course_name_test():
    assert course_name('11') == 'Body Combat'
    assert course_name('tamure') == '???'

@patch('fitlanecal.course_name')    
def sanitize_course_name_test_mocked(mocked):
    mocked.return_value = "dumb"
    str_test1 = "/site/uploaded/cours/cours_logo_11.jpg"
    str_test2 = "/site/uploaded/cours/cours_logo_11"
    str_test3 = "11.jpg"
    str_test4 = "11"
    str_test5 = ""
    str_test6 = "/site/uploaded/cours/cours_logo_.jpg"
    assert sanitize_course_name(str_test1) == "dumb"
    assert sanitize_course_name(str_test2) == "dumb"
    assert sanitize_course_name(str_test3) == "dumb"
    assert sanitize_course_name(str_test4) == "dumb"
    assert sanitize_course_name(str_test5) == "dumb"        
    assert sanitize_course_name(str_test6) == "dumb"  

def sanitize_course_name_test():
    str_test1 = "/site/uploaded/cours/cours_logo_11.jpg"
    str_test2 = "/site/uploaded/cours/cours_logo_11"
    str_test3 = "11.jpg"
    str_test4 = "11"
    str_test5 = ""
    str_test6 = "/site/uploaded/cours/cours_logo_.jpg"
    assert sanitize_course_name(str_test1) == "Body Combat"
    assert sanitize_course_name(str_test2) == "Body Combat"
    assert sanitize_course_name(str_test3) == "Body Combat"
    assert sanitize_course_name(str_test4) == "Body Combat"
    assert sanitize_course_name(str_test5) == "???"        
    assert sanitize_course_name(str_test6) == "???"
        
def fetch_courses_on_test():
    basepath = os.path.dirname(__file__)
    orig_path = os.path.abspath(os.path.join(basepath,"resources","fitlane-planning-test.html"))
    expected_path = os.path.abspath(os.path.join(basepath,"resources","expected_fetch_courses_on_test.txt"))
    fd_fitlane = open(orig_path,"r")
    fd_expected = open(expected_path,"r")
    content_fitlane = fd_fitlane.read()
    content_expected = fd_expected.read()
    tree = html.fromstring(content_fitlane)
    res = fetch_courses_on(tree, 'Lundi')
    assert str(res) == content_expected[:-1]

@patch('fitlanecal.fetch_html_from_club')
def fetch_all_courses_at_club_test(mocked):
    basepath = os.path.dirname(__file__)
    orig_path = os.path.abspath(os.path.join(basepath,"resources","fitlane-planning-test.html"))
    expected_path = os.path.abspath(os.path.join(basepath,"resources","expected_fetch_all_courses_test.txt"))
    fd_fitlane = open(orig_path,"r")
    fd_expected = open(expected_path, "r")
    content_expected = fd_expected.read()
    mocked.return_value = html.fromstring(fd_fitlane.read())
    res = str(fetch_all_courses_at_club("Nice Centre"))
    assert res == content_expected[:-1]

def delta_time_duration_test():
    #delta_time_duration(duration)
    assert delta_time_duration("1h") == (1,0)
    assert delta_time_duration("1h30") == (1,30)
    assert delta_time_duration("45min") == (0,45)
    assert delta_time_duration("Stretching / 1h") == (1,0)
    assert delta_time_duration("") == (1,0)

@patch('fitlanecal.fetch_html_from_club')
def get_calendar_at_club_test(mocked):
    basepath = os.path.dirname(__file__)
    orig_path = os.path.abspath(os.path.join(basepath,"resources","fitlane-planning-test.html"))
    expected_path = os.path.abspath(os.path.join(basepath,"resources","expected_calendar_test.txt"))
    fd_fitlane = open(orig_path,"r")
    fd_expected = open(expected_path, "r")
    content_expected = fd_expected.read()
    mocked.return_value = html.fromstring(fd_fitlane.read())
    assert get_calendar_at_club("Nice Centre") == content_expected


