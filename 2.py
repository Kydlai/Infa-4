import json
import xmltodict

with open("timetable.xml", 'r', encoding="utf-8") as file:
    my_xml = file.read()

table = xmltodict.parse(my_xml)

open("timetable.json", "w").write(json.dumps(table, indent=4, ensure_ascii=False))
