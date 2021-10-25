# -*- coding: utf-8 -*-
import re

def fnd(txt, key):
    for i in range(len(txt)):
        if txt[i:i+len(key)] == key:
            for j in range(i+len(key)+2, len(txt)):
                if txt[j] == "\"":
                    return txt[i + len(key) + 1:j+1]
    return -1
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
            output_txt += ","
            output_txt += "\n"
        output_txt = output_txt[:-2] + "\n"
                
        output_txt += tabs * 4 * ' ' + "},\n"
        tabs -= 1
    if fnd(i, "timetable") != -1:
        s = re.split("=\"*\"", i) 
        for j in range(len(s) - 1):
            sign = last_word(s[j])
            timetable_txt += 4 * ' ' + "\"" + sign + "\": " + fnd(i, sign)
            timetable_txt += ","
            timetable_txt += "\n"   
        
output_txt = output_txt[:-2] + "\n"
output_txt += tabs * 4 * ' ' + "]\n"
tabs -= 1
output_txt += tabs * 4 * ' ' + "},\n"

output_txt += timetable_txt[:-2] + "\n}"

open("timetable.json", "w").write(output_txt)
print(output_txt)