from xml.etree import ElementTree

tree = ElementTree.parse("timetable.xml")
print(str(tree))
root = tree.getroot()
output_txt = "lang;group;day;time;room;lesson;teacher;format\n"

                
                
for tt in root.iter('timetable'):
    for lessons in tt.iter("lessons"):
        for information in lessons.iter('lesson'):
            output_txt += ';'.join([tt.attrib['lang'], tt.attrib['group'], tt.attrib['day'], information.attrib['time'], information.attrib['room'], information.attrib['lesson'], information.attrib['teacher'], information.attrib['format']]) + '\n'
open("timetable.csv", 'w', encoding="utf-8").write(output_txt)                
            