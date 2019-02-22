import csv
#import os
from pathlib import Path

with open('lijst2018.txt') as txtfile:
    temp = txtfile.read().splitlines()
    line_count = 0
    for line in temp[800:1000]:
        line_count += 1
        fn = open(line,"w")
        fn.write(" ")
        fn.close()
        #print(line)
    print(f"Totaal: {line_count}")

