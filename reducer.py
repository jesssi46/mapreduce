#!/usr/bin/env python
#Exercise 6: calculating the average sales per category
import sys

sum_of_values = 0
count_of_values = 0

previous_key = None

for line in sys.stdin:
    data = line.strip().split("\t")
    key, value = data

    if previous_key != None and previous_key != key:
        average = sum_of_values / count_of_values
        sys.stdout.write("{0}\t{1}\n".format(previous_key, average))
        sum_of_values = 0
        count_of_values = 0
    sum_of_values += float(value)
    count_of_values += 1
    previous_key = key

if previous_key != None:
    average = sum_of_values / count_of_values
    sys.stdout.write("{0}\t{1}\n".format(previous_key, average))
