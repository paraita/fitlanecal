import os, sys, string, urllib2
from lxml import html
import urllib2
from datetime import datetime
from datetime import timedelta
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gaenv'))


# To add third-party libraries go to
# https://cloud.google.com/appengine/docs/python/tools/libraries27?hl=en#vendoring

classes = {
	'2' : 'Body Balance',
	'3' : 'Yoga',
	'4' : 'Pilates',
	'5' : 'Stretching',
	'6' : 'Aquagym',
	'7' : 'Oxygene',
	'8' : 'Hatha Yoga',
	'9' : 'Astanga Yoga',
	'10' : 'RPM',
	'11' : 'Body Combat',
	'12' : 'Body Attack',
	'13' : 'Spinning',
	'14' : 'Step',
	'15' : 'Zumba',
	'16' : 'Body Jam',
	'17' : 'Zumba Toning',
	'18' : 'Zumba Kids',
	'19' : 'Ragga Dance Hall',
	'20' : 'Athletic Jazz',
	'21' : 'House Dance',
	'22' : 'Acro Dance',
	'23' : 'Body Pump',
	'24' : 'Cx Worx',
	'25' : 'Abdos Fessiers',
	'26' : 'Body Sculpt',
	'27' : 'NRJ Sculpt',
	'28' : 'Athletic Force',
	'29' : 'LIA',
	'30' : 'Cross Training',
	'31' : 'HIIT',
	'32' : 'Salsa',
	'33' : 'Hitbox',
	'34' : 'Fitlane Cinema',
	'35' : 'Hatha Yoga',
	'36' : 'Astanga Yoga',
	'37' : 'Bachata',
	'38' : 'Special Buste',
	'39' : 'Jazz Training',
	'40' : 'Dos/Abdos',
	'41' : 'Hip Hop',
	'42' : 'Cardio Sculpt',
	'43' : 'Body Balance Video',
	'44' : 'Zumba Video',
	'45' : 'Body Pump Video',
	'46' : 'Yoga Video',
	'47' : 'Body Combat Video',
	'48' : 'CX Worx Video',
	'49' : 'Stretching Video',
	'50' : 'Pilates Video',
	'51' : 'Body Sculpt Video',
	'52' : 'Shbam Video',
	'53' : 'Spinning Video',
	'54' : 'Body Boxe Video',
	'55' : 'NRJ Sculpt Video',
	'56' : 'Power Step Video',
	'57' : 'Body Swiss Ball Video',
	'58' : 'Dynamique Yoga Video',
	'59' : 'Body Barre Video',
	'60' : 'HIIT Video',
	'61' : 'Abdos Video',
	'62' : 'Lady Dance',
	'63' : 'Lady Dance',
	'64' : 'Zumba Step',
	'65' : 'Special Abdos',
	'66' : 'Special Fessiers',
	'67' : 'Dance Clubbing',
	'68' : 'R\'Lace',
	'69' : 'LIA Video',
	'70' : 'Cardio Sculpt Video',
	'71' : 'Aquactive',
	'72' : 'Aqua Dynamic',
	'73' : 'Aqua Cycling',
	'74' : 'Urban Camp',
	'75' : 'Forme et Tonus',
	'76' : 'Abdos',
	'77' : 'Flexibilite',
	'78' : 'Urban Yoga',
	'79' : 'Cuisses Abdos Fessiers',
	'80' : 'Boot Camp Video',
	'81' : 'Kids Academy',
	'82' : 'Fit Jazz' }

clubs = {
    'cannes-carnot' : 'Cannes Carnot',
    'cannes-gare' : 'Cannes Gare',
    'cannes-la-bocca' : 'Cannes La Bocca',
    'juan-les-pins' : 'Juan Les Pins',
    'mandelieu' : 'Mandelieu',
    'nice-centre' : 'Nice Centre',
    'nice-st-isidore' : 'Nice St Isidore',
    'sophia-antipolis' : 'Sophia Antipolis',
    'villeneuve-loubet' : 'Villeneuve Loubet',
    'villeneuve-A8' : 'Villeneuve A8' }


    
CAL_FR_LABELS = { 'Lundi' : 'MO',
                  'Mardi' : 'TU',
                  'Mercredi' : 'WE',
                  'Jeudi' : 'TH',
                  'Vendredi' : 'FR',
                  'Samedi' : 'SA',
                  'Dimanche' : 'SU' }
    
ICAL_BYDAY = { 'MO' : 1,
               'TU' : 2,
               'WE' : 3,
               'TH' : 4,
               'FR' : 5,
               'SA' : 6,
               'SU' : 7 }

    
def course_name(key):
    """Returns the associated name string from an image id"""
    if key in classes:
        return classes[key]
    else :
        return '???'

    
def club_url(key):
    if key in clubs:
        return clubs[key]
    else:
        return clubs['Nice Centre']

    
def fetch_html_from_club(club):
    """Returns the dom tree of a given club."""
    url = "http://www.fitlane.com//fr/clubs/{0}/planning/".format(club)
    try:
        result = urllib2.urlopen(url)
        return html.fromstring(result.read())
    except urllib2.URLError, e:
        print 'Connection error for ',club
        

def sanitize_course_name(img_src):
    """Returns the name of the course from its image source url"""
    img_id = string.replace(string.replace(img_src,'.jpg',''),
                            '/site/uploaded/cours/cours_logo_',
                            '')
    return course_name(img_id)


def fetch_courses_on(tree, dayName):
    """Returns all courses for a given day as a list."""
    today_slots_raw = tree.xpath('//div[@data-jour="{0}"]/@data-horaire'.format(dayName))
    today_slots = {}
    for slot_hour in today_slots_raw:
        divs = tree.xpath('//div[@data-jour="{0}" and @data-horaire="{1}"]'.format(dayName,slot_hour))
        for p in divs:
            slot = {}
            imgs = map(sanitize_course_name, p.xpath('p/a/img/@src'))
            durations = p.xpath('p[@class="resume"]/text()')
            for img, duration in map(None, imgs, durations):
                slot['name'] = img
                slot['duration'] = duration
            today_slots[slot_hour] = slot
    return today_slots


def fetch_all_courses_at_club(clubName):
    """Returns all raw courses for a given clubName.

    Or null if the clubName is not found.
    result is a list containing lists representing days.
    Each day is a list of courses.
    """
    club_tree = fetch_html_from_club(clubName)
    club_courses = {}
    for day in CAL_FR_LABELS:
        club_courses[day] = fetch_courses_on(club_tree, day)
    return club_courses


def delta_time_duration(duration):
    """Returns the tuple (hour,minute)
    That tuple represents the amount of time to add to
    the starting datetime of a course to obtain the exact
    datetime of the end of the course.
    """
    res_hour = 1
    res_min = 0
    res_tmp = duration
    if "/" in duration:
        res_tmp = duration.split("/")
        res_tmp = res_tmp[1] # case where duration is wrong e.g "Stretching / 1h"
    if "min" in res_tmp:
        res_tmp = res_tmp.split("min")
        return 0,int(res_tmp[0])
    if "h" in res_tmp:
        res_tmp = res_tmp.split("h")
        res_hour = int(res_tmp[0])
        if res_tmp[1] != "":
            res_min = int(res_tmp[1])
    return res_hour,res_min


def get_calendar_at_club(clubName):
    """Returns the courses in a ics format calendar."""
    current_datetime = datetime.today()
    week = fetch_all_courses_at_club(clubName)
    ical_content = "BEGIN:VCALENDAR\n"
    for day in week:
        all_day_slots = week[day]
        for slot in all_day_slots:
            slot_content = all_day_slots[slot]
            day_value = ICAL_BYDAY[CAL_FR_LABELS[day]]
            slot_date = slot.split(":")
            dtstart_obj = current_datetime.replace(day=day_value,
                                                   hour=int(slot_date[0]),
                                                   minute=int(slot_date[1]),
                                                   second=0)
            dtstart = dtstart_obj.strftime("%Y%m%dT%H%M%S")
            h,m = delta_time_duration(slot_content['duration'])
            dtend_obj = dtstart_obj + timedelta(hours=h, minutes=m)
            dtend = dtend_obj.strftime("%Y%m%dT%H%M%S")
            ical_content += "BEGIN:VEVENT\n"
            ical_content += "DTSTART;TZID=Europe/Paris:" + dtstart + "\n"
            ical_content += "DTEND;TZID=Europe/Paris:" + dtend + "\n"
            ical_content += "RRULE:FREQ=WEEKLY;BYDAY=" + CAL_FR_LABELS[day] + "\n"
            ical_content += "SUMMARY:" + slot_content['name'] + "\n"
            ical_content += "END:VEVENT\n"
    return ical_content + "END:VCALENDAR\n"


if __name__ == "__main__":
    pass
