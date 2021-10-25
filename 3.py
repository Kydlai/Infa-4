# -*- coding: utf-8 -*-
import time
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

open("timetable.json", "w").write(output_txt)
print(time.perf_counter() - start_time)

import json
import xmltodict

start_time = time.perf_counter()
with open("timetable.xml", 'r', encoding="utf-8") as file:
    my_xml = file.read()

table = xmltodict.parse(my_xml)

open("timetable.json", "w").write(json.dumps(table, indent=4, ensure_ascii=False))
print(time.perf_counter() - start_time)
