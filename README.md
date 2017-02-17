# rorodata-assignment
A repo with solutions for assignment given by rorodata

## Problems
### Problem 1

The Google Maps provides a Distance Matrix API that provides travel distance and time for given source and destination. More information about it can be found from: https://developers.google.com/maps/documentation/distance-matrix/start

Write a program howlong.py that takes two arguments, the source and destination and prints the travel distance and time. The distance should be in km or meters. The output should just contain 2 lines with distance on the first line and time in the second line.
```sh
$ python howlong.py Hyderabad Chennai
627 km
10 hours 10 mins
```
For example, visit: https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=Hyderabad&destinations=Chennai The API says that you need an API key, but it works without that as well.

### Problem 2

Write a program split.py that splits a large file into multiple smaller files. The program should take a filename and the number of lines as arguments and write multiple small files each containing the specified number of lines (The last one may have smaller number of lines).
```sh
$ python split.py files/100.txt 30
writing files/100-part1.txt
writing files/100-part2.txt
writing files/100-part3.txt
writing files/100-part4.txt
```

## Usage

### Installation
```sh
$ pip install -r requirements.txt
```
### Execute
Howlong
```sh
$ python howlong.py Hyderabad Lucknow
```
Split
```sh
$ python split files/sample.txt 8
```

May the force be with you
