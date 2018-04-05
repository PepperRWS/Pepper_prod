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
    map_to_load = "meeting_room_A33"

    # Get the services ALNavigation and ALMotion.
    nav = session.service("DecosNavigation")

    file = open(map_to_load + ".explo", "r")
    nav.uploadMap( file.read() , map_to_load + ".explo" )

    nav.loadMap( map_to_load + ".explo")

    result_map = nav.getMetricalMap()

    #print origin
    origin = [ result_map[3][0]/result_map[0] , result_map[3][1]/result_map[0] ]
    print "Origin is at " + str(origin)

    map_width = result_map[1]
    map_height = result_map[2]
    img = numpy.array(result_map[4]).reshape(map_width, map_height).T
    img = (100 - img) * 2.55 # from 0..100 to 255..0
    img = numpy.array(img, numpy.uint8)
    #
    with open(map_to_load + ".txt", "w") as text_file:
        text_file.write( str(result_map) )
    #
    Image.fromarray(img).save(map_to_load + ".jpeg")
    Image.fromarray(img).show()


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
