#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use explore method."""

import qi
import argparse
import sys

import numpy
from PIL import Image

def main(session):
    """
    This example uses the explore method.
    """
    # Get the services ALNavigation and ALMotion.
    nav = session.service("DecosNavigation")

    map_name = nav.createMap(5.0)

    print "Map saved as: "+map_name

    result_map = nav.getMap( map_name )

    #print nav.getPosition()

    #map_width = result_map[1]
    #map_height = result_map[2]
    #img = numpy.array(result_map[4]).reshape(map_width, map_height)
    #img = (100 - img) * 2.55 # from 0..100 to 255..0
    #img = numpy.array(img, numpy.uint8)

    #with open("your_map.txt", "w") as text_file:
    #    text_file.write( str(result_map) )

    #Image.fromarray(img).save("your_map.jpeg")
    #Image.fromarray(img).show()

    #file = open("hallway-upload.explo", "r")
    #nav.uploadMap( file.read() , "uploaded_via_tiago.explo" )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
