# fitlanecal

[![Build Status](https://travis-ci.org/paraita/fitlanecal.png)](https://travis-ci.org/paraita/fitlanecal)

A Fitlane calendar web service that parses Fitlane agenda and outputs an ical

The source can be deployed as is in Google App Engine.

## Usage
Once deployed, simply add the url + club name to your calendar app
configuration, for example:
```
https://fitlanecal.appspot.com/nice-centre
```
The following club names are available:
* cannes-carnot
* cannes-gare
* cannes-la-bocca
* juan-les-pins
* mandelieu
* nice-centre
* nice-st-isidore
* sophia-antipolis
* villeneuve-loubet
* villeneuve-A8


## Tests
Tests can be run locally by first installing requirements:
```
pip install -r requirements.txt
```
Then, just run:
```
nosetests
```

## Credits
This project is not affiliated with [Fitlane](http://www.fitlane.com/fr/)
