#!/usr/bin/env python
#Exercise 2: adjusted to count the values instead of doing sum
import sys

count_of_values = 0

previous_key = None

for line in sys.stdin:
    data = line.strip().split("\t")
    key, value = data

    if previous_key != None and previous_key != key:
        sys.stdout.write("{0}\t{1}\n".format(previous_key, count_of_values))
        count_of_values = 0
    # Increment the count instead of summing the values
    count_of_values += 1
    previous_key = key

if previous_key != None:
    sys.stdout.write("{0}\t{1}\n".format(previous_key, count_of_values))