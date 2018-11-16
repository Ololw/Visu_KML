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

for line in content:
    words = line.split()
    kml +=(
    '<Placemark>\n'
        '<name>'+words[0]+': '+words[3]+' millions</name>\n'
        '<Point>\n'
        '<coordinates>\n' +
        words[1] + ',' + words[2]
        +
        '</coordinates>\n'
        '</Point>\n'
    '</Placemark>\n'
    )


#ajout des coordonnees aleatoires
#kml+=str(longitude)+","+str(latitude)
kml+=(

'</Document>\n'
'</kml>')
#affichage sur la sortie standard
print(kml)

