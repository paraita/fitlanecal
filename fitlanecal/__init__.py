import os, sys, string, urllib2
from lxml import html
import urllib2
from datetime import datetime
from datetime import timedelta


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
    '82' : 'Fit Jazz',
    '113' : 'Sprint'}

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

TYPE_PLANNING = {
    'COLLECTIF': 'cours-collectifs',
    'VELO': 'cours-velo' }
    
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

class FitlaneCalException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


    
def course_name(key):
    """Returns the associated name string from an image id"""
    if key in classes:
        return classes[key]
    else :
        return '???'
    
def club_name(key):
    if key in clubs:
        return clubs[key]
    else:
        return clubs['nice-centre']

def planning_url(type_planning, club):
    """Returns a fitlane URL
       The URL is based on the type of planning and the club name
    """
    if type_planning in TYPE_PLANNING:
        return ("http://www.fitlane.com/fr/clubs/"
                "{0}/planning/{1}".format(club, TYPE_PLANNING[type_planning]))
    else:
        raise FitlaneCalException("Unknown type of planning: " + type_planning)

def fetch_html_from_club(type_planning, club):
    """Returns the dom tree of a given planning type in a  given club."""
    url = planning_url(type_planning, club)
    print url
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
    print "{0} -> {1}".format(img_src, img_id)
    return course_name(img_id)

def fetch_courses_on(tree, dayName):
    """Returns all courses for a given day as a list."""
    today_slots_raw = tree.xpath('//div[@data-jour="{0}"]/@data-horaire'
                                 .format(dayName))
    today_slots = {}
    for slot_hour in today_slots_raw:
        divs = tree.xpath('//div[@data-jour="{0}" and @data-horaire="{1}"]'
                          .format(dayName,slot_hour))
        for p in divs:
            slot = {}
            img = p.xpath('string(p/a/img/@src)')
            print img
            prof_name = p.xpath('string(p/a/@data-prof)')
            print prof_name
            duration = p.xpath('string(p/a/@data-duree)')
            slot['name'] = sanitize_course_name(img)
            slot['duration'] = duration
            today_slots[slot_hour] = slot
    print "JOUR: {0}".format(dayName)
    print today_slots
    return today_slots

def fetch_all_courses_at_club(type_planning, club_name):
    """Returns all raw courses of a given planning type and given clubName.

       If the planning type or the clubName is invalid
       an exception in raised
    """
    club_tree = fetch_html_from_club(type_planning, club_name)
    club_courses = {}
    for day in CAL_FR_LABELS:
        club_courses[day] = fetch_courses_on(club_tree, day)
    return club_courses

# BEWARE THE FOLLOWING FUNCTION IS RATED PG-13
# KEEP THE FAINTED OUT OF THIS REGION
def delta_time_duration(duration):
    """Returns the tuple (hour,minute)
    That tuple represents the amount of time to add to
    the starting datetime of a course to obtain the exact
    datetime of the end of the course.
    """
    res_hour = 1
    res_min = 0
    res_tmp = duration
    if duration is None:
        return res_hour,res_min # default case if no duration
    # case where duration is wrong e.g "Stretching / 1h"
    if "/" in duration:
        res_tmp = duration.split("/")
        res_tmp = res_tmp[1]
    if "min" in res_tmp and "h" in res_tmp:
        print "1h30min case detected, returning default value (1,0)"
        return res_hour,res_min
    elif "min" in res_tmp:
        res_tmp = res_tmp.split("min")
        if " " in res_tmp[0]:
            # "leve 1 45min" and " 45 min" cases
            if len(res_tmp[0]) > 3:
                res_tmp = res_tmp[0].split(" ")
                if len(res_tmp) > 2:
                    if res_tmp[-1] == "":
                        res_tmp = res_tmp[-2]
                    else:
                        res_tmp = res_tmp[-1]
                else:
                    res_tmp = res_tmp[1]
            else:
                res_tmp = string.replace(res_tmp[0]," ","")
            return 0,int(res_tmp)
        else:
            return 0,int(res_tmp[0])
    elif "h" in res_tmp:
        res_tmp = res_tmp.split("h")
        if res_tmp[0] != "":
            if " " in res_tmp[0]:
                # remove any string preceding the hour number
                #filtered_hour = (res_tmp[0]).split(" ")
                filtered_hour = string.replace((res_tmp[0]), " ", "")
                res_hour = int(filtered_hour[-1])
            else:
                res_hour = int(res_tmp[0])
        if res_tmp[1] != "" and res_tmp[1] != " ":
            res_min = int(res_tmp[1])
    return res_hour,res_min

def get_ical_for_the_week(week, datetime):
    """Returns the ics representation of the week"""
    ical_content = ""
    for day in week:
        all_day_slots = week[day]
        for slot in all_day_slots:
            slot_content = all_day_slots[slot]
            print slot_content
            day_value = ICAL_BYDAY[CAL_FR_LABELS[day]]
            slot_date = slot.split(":")
            dtstart_obj = datetime.replace(day=day_value,
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
            ical_content += "RRULE:FREQ=WEEKLY;BYDAY="
            ical_content += CAL_FR_LABELS[day] + "\n"
            ical_content += "SUMMARY:" + slot_content['name'] + "\n"
            ical_content += "END:VEVENT\n"
    return ical_content

def get_calendar_at_club(club_name):
    """Returns the courses in a ics format calendar."""
    current_datetime = datetime.today()
    week_collectif = fetch_all_courses_at_club('COLLECTIF', club_name)
    week_velo = fetch_all_courses_at_club('VELO', club_name)
    ical_content = "BEGIN:VCALENDAR\n"
    ical_content += get_ical_for_the_week(week_collectif, current_datetime)
    ical_content += get_ical_for_the_week(week_velo, current_datetime)
    ical_content += "END:VCALENDAR\n"
    return ical_content

if __name__ == "__main__":
    pass
