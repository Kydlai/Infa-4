# -*- coding: utf-8 -*-
import time
import re
start_time = time.perf_counter()

def fnd(txt, key):
    for i in range(len(txt)):
        if txt[i:i+len(key)] == key:
            for j in range(i+len(key)+2, len(txt)):
                if txt[j] == "\"":
                    return txt[i + len(key) + 1:j+1]
    return -1

input_txt = open("timetable.xml", "r", encoding="utf-8").readlines()
signs = ["time", "room", "place", "lesson", "teacher", "format"]
main_signs = ["lang", "group", "day"]
tabs = 1
output_txt = "{\n" + tabs * 4 * " " + "\"" + "lessions" + "\"" + ": [\n"
tabs += 1
for i in input_txt:
    if fnd(i, "lesson") != -1:
        output_txt += tabs * 4 * ' ' + "\"lession\": {\n"
        tabs += 1
        for j in range(len(signs)):
            sign = signs[j]
            output_txt += tabs * 4 * ' ' + "\"" + sign + "\": " + fnd(i[14:], sign)
            if j != len(signs) - 1:
                output_txt += ","
            output_txt += "\n"
                
        output_txt += tabs * 4 * ' ' + "},\n"
        tabs -= 1
output_txt = output_txt[:-2] + "\n"
output_txt += tabs * 4 * ' ' + "]\n"
tabs -= 1
output_txt += tabs * 4 * ' ' + "},\n"

for i in input_txt:
    if i[:3] == "<ti":
        for j in range(len(main_signs)):
            sign = main_signs[j]
            output_txt += tabs * 4 * ' ' + "\"" + sign + "\": " + fnd(i, sign)
            if j != len(signs) - 1:
                output_txt += ","
            output_txt += "\n" 
        output_txt = output_txt[:-2] + "\n"
        tabs -= 1
        output_txt += tabs * 4 * ' ' + "}\n"       
        break

print(time.perf_counter() - start_time)

########################################################################################################

import json
import xmltodict

start_time = time.perf_counter()
with open("timetable.xml", 'r', encoding="utf-8") as file:
    my_xml = file.read()

table = xmltodict.parse(my_xml)

print(time.perf_counter() - start_time)

########################################################################################################

start_time = time.perf_counter()
def last_word(txt):
    for i in range(len(txt)-1, -1, -1):
        if txt[i] == " ":
            return txt[i+1:]
    return -1

input_txt = open("timetable.xml", "r", encoding="utf-8").readlines()
tabs = 1
output_txt = "{\n" + tabs * 4 * " " + "\"" + "lessions" + "\"" + ": [\n"
timetable_txt = ""
tabs += 1
for i in input_txt:
    if fnd(i, "lesson") != -1:
        output_txt += tabs * 4 * ' ' + "\"lession\": {\n"
        tabs += 1
        s = re.split("=\"*\"", i) 
        for j in range(len(s) - 1):
            sign = last_word(s[j])
            output_txt += tabs * 4 * ' ' + "\"" + sign + "\": " + fnd(i[14:], sign)
            if j != len(signs) - 1:
                output_txt += ","
            output_txt += "\n"
                
        output_txt += tabs * 4 * ' ' + "},\n"
        tabs -= 1
    if fnd(i, "timetable") != -1:
        s = re.split("=\"*\"", i) 
        for j in range(len(s) - 1):
            sign = last_word(s[j])
            timetable_txt += 4 * ' ' + "\"" + sign + "\": " + fnd(i, sign)
            if j != len(signs) - 1:
                timetable_txt += ","
            timetable_txt += "\n"        
output_txt = output_txt[:-2] + "\n"
output_txt += tabs * 4 * ' ' + "]\n"
tabs -= 1
output_txt += tabs * 4 * ' ' + "},\n"

output_txt += timetable_txt[:-2] + "\n}"
print(time.perf_counter() - start_time)
