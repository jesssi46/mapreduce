#!/usr/bin/env python
#Exercise 3: Adding error message when the number of elements is not 6

import sys

for line in sys.stdin:

    data = line.strip().split("\t")
    if len(data) != 6:
        raise ValueError("Expected 6 elements")
    date, time, item, category, sales, payment = data
#changed from payment to category
    sys.stdout.write("{0}\t{1}\n".format(category, sales))
