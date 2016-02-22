# fitlanecal

[![Build Status](https://travis-ci.org/paraita/fitlanecal.png)](https://travis-ci.org/paraita/fitlanecal)

A Fitlane calendar web service that parses Fitlane agenda and outputs an ical

The source can be deployed as is in Google App Engine.

## Usage
Once deployed, simply add the url + club name to your calendar app
configuration, for example:
```
https://fitlanecal.appspot.com/nice-centre.ics
```
The following club names are available:
* cannes-carnot.ics
* cannes-gare.ics
* cannes-la-bocca.ics
* juan-les-pins.ics
* mandelieu.ics
* nice-centre.ics
* nice-st-isidore.ics
* sophia-antipolis.ics
* villeneuve-loubet.ics
* villeneuve-A8.ics


## Tests
Tests can be run locally by first installing requirements:
```
pip install -r requirements.txt
```
Then, just run:
```
nosetests fitlanecal
```

## Deployment
It is necessary to bundle all third-party dependencies using [the vendor feature](https://cloud.google.com/appengine/docs/python/tools/libraries27).

## Credits
This project is not affiliated with [Fitlane](http://www.fitlane.com/fr/)
