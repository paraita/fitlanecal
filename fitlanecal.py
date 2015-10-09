import os, sys, string
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gaenv'))
from lxml import html


classes = {
	'2' : '',
	'3' : '',
	'4' : '',
	'5' : '',
	'6' : '',
	'7' : '',
	'8' : '',
	'9' : '',
	'10' : '',
	'11' : '',
	'12' : '',
	'13' : '',
	'14' : '',
	'15' : '',
	'16' : '',
	'17' : '',
	'18' : '',
	'19' : '',
	'20' : '',
	'21' : '',
	'22' : '',
	'23' : '',
	'24' : '',
	'25' : '',
	'26' : '',
	'27' : '',
	'28' : '',
	'29' : '',
	'30' : '',
	'31' : '',
	'32' : '',
	'33' : '',
	'34' : '',
	'35' : '',
	'36' : '',
	'37' : '',
	'38' : '',
	'39' : '',
	'40' : '',
	'41' : '',
	'42' : '',
	'43' : '',
	'44' : '',
	'45' : '',
	'46' : '',
	'47' : '',
	'48' : '',
	'49' : '',
	'50' : '',
	'51' : '',
	'52' : '',
	'53' : '',
	'54' : '',
	'55' : '',
	'56' : '',
	'57' : '',
	'58' : '',
	'59' : '',
	'60' : '',
	'61' : '',
	'62' : '',
	'63' : '',
	'64' : '',
	'65' : '',
	'66' : '',
	'67' : '',
	'68' : '',
	'69' : '',
	'70' : '',
	'71' : '',
	'72' : '',
	'73' : '',
	'74' : '',
	'75' : '',
	'76' : '',
	'77' : '',
	'78' : '',
	'79' : '',
	'80' : '',
	'81' : '',
	'82' : '' }

clubs = {
    '' : '',
    '' : '' }

def className(key):
    """Returns the right course name for a given key.

    Or null if the key maps to nothing
    """
    pass

# TODO
def fetch_html_from_club(club):
    """Returns the dom tree for a given club."""
    f = open("fitlane-planning.html","r")
    content = f.read()
    return html.fromstring(content)

def fetch_courses_on(tree, dayName):
    """Returns all courses for a given day as a list.
    
    hours = [h for h in day_courses if '.jpg' not in h]
    courses = map(lambda x : string.replace(x, '/site/uploaded/cours/cours_logo_', ''),
                  map(lambda x : string.replace(x, '.jpg', ''),
                     [c for c in day_courses if '.jpg' in c]))
    """
    
    day_hours = tree.xpath('//div[@data-jour="{0}"]/@data-horaire'
                           .format(dayName))
    courses = {}
    for hour in day_hours:
        courses[hour] = map(lambda x : string.replace(x,'/site/uploaded/cours/cours_logo_',
                                                      ''),
                            map(lambda x : string.replace(x,'.jpg',
                                                          ''),
                                tree.xpath('//div[@data-jour="{0}" and @data-horaire="{1}"]/p/a/img/@src'
                                           .format(dayName, hour))))
    return courses

def fetch_all_courses_at_club(clubName):
    """Returns all raw courses for a given clubName.

    Or null if the clubName is not found.
    result is a list containing lists representing days.
    Each day is a list of courses.
    """
    club_tree = fetch_html_from_club(clubName)
    club_courses = {}
    for day in ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]:
        club_courses[day] = fetch_courses_on(club_tree, day)
    return club_courses

def toCalendar(courses):
    """Returns the courses in a ics format calendar."""
    pass
