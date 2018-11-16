#!/usr/bin/python3
import random
latitude=random.randrange(-90,90)
longitude=random.randrange(-180,180)
kml=(
'<?xmlversion ="1.0"encoding="UTF-8"?>\n'
'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
#'<Placemark>\n'
#'<name>Random Placemark</name>\n'
#'<Point>\n'
#'<coordinates>\n'
'')
#ajout des coordonnees aleatoires
#kml+=str(longitude)+","+str(latitude)
kml+=(
#'</coordinates>\n'
#'</Point>\n'
#'</Placemark>\n'

'<GroundOverlay>\n'
'<name>Exemple d\' Overlay</name>\n'
'<Icon>\n' 
'<href>PlanCampus.jpg</href>\n'
'</Icon>\n'
'<LatLonBox>\n'
'<north>45.1988667</north>\n'
'<south>45.1848</south>\n'
'<east>5.78475</east>\n'
'<west>5.745333333333333</west>\n'
'</LatLonBox>\n'
'<color>ffffffff</color>\n'
'</GroundOverlay>\n'

'</kml>')
#affichage sur la sortie standard
print(kml)

