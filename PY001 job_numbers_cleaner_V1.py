# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:32:33 2015

@author: 105053093
"""

import csv
import re

job_number_pattern = re.compile("^[0-9]+([-][0-9])?[&]?[0-9]+([-][0-9])?$")
item_pattern = re.compile("^RR-[0-9]{7}$")
output_list = []

with open('job_numbers_giuliano.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if len(row) != 2:
            print "*** Warning! More values found in", row
        
        raw_item = row[1]
        if item_pattern.match(raw_item):
            item = raw_item.replace("-", "O")
        else:
            print "*** Warning! Item string not matching pattern:", raw_item
            item = raw_item.replace("-", "O")
            
        raw_job_number = row[0]
        
        if job_number_pattern.match(raw_job_number):
            
            strings = raw_job_number.split("&")
            first = strings[0]
            
            if "-" in first:
                job_start = first.split("-")[0]
                end = first.split("-")[1]
                if len(job_start) <> 7:
                    print "*** Warning! Strange value in job number string:", raw_job_number
                else:
                    job_end = job_start[:(7-len(end))] + end
                    #print raw_job_number, job_start, job_end
                    for job_number in range(int(job_start), int(job_end)):
                        output_list.append([str(job_number), item])
                    output_list.append([job_end, item])
            else:
                output_list.append([first, item])
            
            if len(strings)>1:
                second = strings[1]
                if "-" in second:
                    if first == "1705723":
                        for job_number in ["1705725", "1705726"]:
                            output_list.append([job_number, item])
                    else:
                         print "*** Warning! Non-standard job number string not handled:", raw_job_number
                else:
                    job_start = first[:7-len(second)]
                    job_number = job_start + second
                    output_list.append([job_number, item])
        else:
            print "*** Warning! Job number string not matching pattern:", raw_job_number

with open('job_numbers_giuliano_clean.txt', 'wb') as f:
    writer = csv.writer(f)
    for elem in output_list:
        #elem = [elem]
        writer.writerow(elem)

with open('job_numbers_giuliano_clean_SQL.txt', 'wb') as f:
    writer = csv.writer(f, csv.QUOTE_NONE)
    for elem in output_list:
        elem = "'" + str(elem) + "',"
        elem = [elem]
        writer.writerow(elem)