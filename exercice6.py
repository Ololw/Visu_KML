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

    #Boucle pour les points intermédiaires
    if i!=0:
        xvector = float(words[1]) - xSave
        yvector = float(words[2]) - ySave
        for j in range(10):
            xInter = xSave + (xvector * (j+1) / 10.0)
            yInter = ySave + (yvector * (j+1) / 10.0)
            coordinates_Line = coordinates_Line + str(xInter) + ',' + str(yInter) + ',67850\n'


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
    xSave = float(words[1])
    ySave = float(words[2])

kml +=(
'<Placemark>\n'
        '<name>Make Europe Great Again</name>\n'
        '<Description>\n'
        'Un mur pour les gouverner tous'
        '</Description>\n'
        '<styleUrl>#yellowLineGreenPoly</styleUrl>\n'
        '<LineString>\n'
        '<extrude>1</extrude>\n'
        '<tessellate>1</tessellate>\n'
        '<altitudeMode>absolute</altitudeMode>\n'
        '<coordinates>\n' +
        coordinates_Line +
        '</coordinates>\n'
        '</LineString>\n'
    '</Placemark>\n'
)



kml+=(

'</Document>\n'
'</kml>')
#affichage sur la sortie standard
print(kml)

#print("\n\n\n" + coordinates_Line)