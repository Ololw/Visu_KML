#!/usr/bin/python3
import random
latitude=random.randrange(-90,90)
longitude=random.randrange(-180,180)


kml=(
'<?xmlversion ="1.0"encoding="UTF-8"?>\n'
'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
'<Document>\n'
'')

#Lecture du fichier cities.txt
with open("cities.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

nb_ville = content.__len__()
i=0

coordinates_Line = '\n'

for line in content:
    words = line.split()

    coordinates = str(words[1] + ',' + words[2])
    coordinates_Line = coordinates_Line + coordinates + '\n'
    kml +=(
    '<Placemark>\n'
        '<name>'+words[0]+': '+words[3]+' millions</name>\n'
        '<TimeSpan>\n'
        '<begin>'+str(2018-nb_ville+i)+'</begin>\n'
        '</TimeSpan>\n'
        '<Point>\n'
        '<coordinates>\n' +
        coordinates
        +
        '</coordinates>\n'
        '</Point>\n'
    '</Placemark>\n'
    )
    i = i + 1


kml+=(

'</Document>\n'
'</kml>')
#affichage sur la sortie standard
print(kml)

