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

    coordinates = words[1] + ',' + words[2]

    diff = float(words[3])*0.0974

    hauteur = 10000

    coordinates_bg = [float(words[1])-diff, float(words[2]) - diff]
    coordinates_hg = [float(words[1])-diff, float(words[2]) + diff]
    coordinates_hd = [float(words[1])+ diff, float(words[2]) + diff]
    coordinates_bd = [float(words[1]) + diff, float(words[2]) - diff]


    kml +=(
    '\n\n<Placemark>\n'
        '<name>'+words[0]+': '+words[3]+' millions</name>\n'
        
        '<Point>\n'
        '<coordinates>\n' +
        words[1] + ',' + words[2]
        +
        '</coordinates>\n'
        '</Point>\n'
        '</Placemark>'
        
        '<Placemark>'
        '<Polygon>\n'
        '<extrude>1</extrude>\n'
        '<altitudeMode>relativeToGround</altitudeMode>\n'
        '<outerBoundaryIs>\n'
        '<LinearRing>\n'
        '<coordinates>\n' +
        str(coordinates_bg[0]) + ',' + str(coordinates_bg[1]) + ','+  str(hauteur)+ '\n' +
        str(coordinates_hg[0]) + ',' + str(coordinates_hg[1]) + ','+  str(hauteur)+ '\n' +
        str(coordinates_hd[0]) + ',' + str(coordinates_hd[1]) + ','+  str(hauteur)+ '\n' +
        str(coordinates_bd[0]) + ',' + str(coordinates_bd[1]) + ','+  str(hauteur)+ '\n' +
        str(coordinates_bg[0]) + ',' + str(coordinates_bg[1]) + ','+  str(hauteur)+ '\n' +

    '</coordinates>\n'
        '</LinearRing>\n'
        '</outerBoundaryIs>\n'
            '</Polygon>\n'

        '</Placemark>\n'

    )

    i = i + 1




kml+=(

'</Document>\n'
'</kml>')
#affichage sur la sortie standard
print(kml)

#print("\n\n\n" + coordinates_Line)