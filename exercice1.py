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
'<href>carte.jpg</href>\n'
'</Icon>\n'
'<LatLonBox>\n'
'<north>51.14582064171803</north>\n'
'<south>42.22993231551517</south>\n'
'<east>10.79288010970161</east>\n'
'<west>-6.151180487455577</west>\n'
'</LatLonBox>\n'
'<color>a0ffffff</color>\n'
'</GroundOverlay>\n'

'</kml>')
#affichage sur la sortie standard
print(kml)

