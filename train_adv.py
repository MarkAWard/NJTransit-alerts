import feedparser
from datetime import datetime

feed = feedparser.parse("https://www.njtransit.com/rss/RailAdvisories_feed.xml")
terms = ["Main","Bergen", "Glen Rock", "Boro Hall"]


def isNew(item_time):
    months = { 'Jan': '01',
               'Feb': '02',
               'Mar': '03',
               'Apr': '04',
               'May': '05',
               'Jun': '06',
               'Jul': '07',
               'Aug': '08',
               'Sep': '09',
               'Oct': '10',
               'Nov': '11',
               'Dec': '12'
               }
    # current date time
    date, time = str(datetime.now()).split()
    c_year, c_mon, c_day = date.split('-')
    c_hr, c_min, c_sec = time.split(':')

    # alert date time
    a_mon, a_day, a_year, tme, ampm = str(item_time).replace(',', '').split()
    a_hr, a_min, a_sec = tme.split(':')
    if ampm == 'PM' and a_hr != '12':
        a_hr = str(int(a_hr) + 12)
    if ampm == 'AM' and a_hr == '12':
        a_hr = str(int(a_hr) - 12)
    a_mon = months[a_mon]

    if c_year == a_year and c_mon == a_mon and c_day == a_day:
        hdif = (int(c_hr) - int(a_hr)) * 60
        mdif = int(c_min) - int(a_min)
        tdif = hdif + mdif

        # set threshold for how recent the alert has to be
        if tdif < 90:
            result = True
        else:
            result = False
    else:
        result = False
    return result

def isRelevant(desc, terms):
    for term in terms:
        if str(desc).find(term) >= 0:
            return True
    return False
    


def func():
    for item in feed.entries:
        if isNew(item.title) and isRelevant(item.description, terms):
            yield str(item.title) +'\t'+ str(item.description)  

