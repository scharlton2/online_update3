"""
Script to normalize Update.xml
"""

from xml.dom import minidom

def normalize_xml(filename):
    dom = minidom.parse(filename)
    dom.writexml(open(filename, 'w'))

normalize_xml('dev/Updates.xml')
normalize_xml('prod/Updates.xml')
normalize_xml('yasu/Updates.xml')
