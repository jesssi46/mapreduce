#!/usr/bin/env python
#Exercise 4: Creating a subset of categorynthat should contain: "Computers", "Cameras", "Video Games"

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        raise ValueError("Expected 6 elements")
    date, time, item, category, sales, payment = data
    if category in ["Computers", "Cameras", "Video Games"]:
#changed from payment to category
        sys.stdout.write("{0}\t{1}\n".format(category, sales))