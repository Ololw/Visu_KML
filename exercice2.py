#!/usr/bin/python3
import random
kml = (
  '<?xml version ="1.0" encoding="UTF-8"?>\n'
  '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
  )
kml += (
  '\t<GroundOverlay>\n'
  '\t\t<name>Exemple d\'Overlay</name>\n'
  '\t\t<Icon>\n'
  '\t\t<href>data-tp2/PlanCampus.jpg</href>\n'
  '\t\t</Icon>\n'
  '\t\t<LatLonBox>\n'
  '\t\t\t<north>45.2021</north>\n'
  '\t\t\t<south>45.18377</south>\n'
  '\t\t\t<east>5.78775</east>\n'
  '\t\t\t<west >5.7450</west>\n'
  '\t\t\t<rotation>-0.1556640799496235</rotation>\n'
  '\t\t</LatLonBox>\n'
  '\t\t<color>a0ffffff</color>\n'
  '\t</GroundOverlay>\n'
  '</kml>'
  )
# affichage sur la sortie standard
print(kml)
