#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use explore method."""

import qi
import argparse
import sys

import time

import numpy
from PIL import Image

def main(session):
    """
    This example uses the explore method.
    """

    use_map="meeting_room_A33"

    # Get the services ALNavigation and ALMotion.
    nav = session.service("DecosNavigation")

    nav.stop()

    file = open(use_map + ".explo", "r")
    nav.uploadMap( file.read() , use_map + ".explo" )

    nav.loadMap(use_map + ".explo")

    result_map = nav.getMetricalMap()
    origin = [ result_map[3][0]/result_map[0] , result_map[3][1]/result_map[0] ]

    print "Origin is at "+str(origin)

    nav.start()
    while (1):
        time.sleep(1)
    print nav.getPosition()
    print "In pixels:"
    print nav.getPositionInPixels()

    #coords_to_pepper = [ goal[0]*result_map[0] + result_map[3][0] , - goal[1]*result_map[0] + result_map[3][1] ]
    print nav.goToPixel( 99 , 92 )
    print nav.getPosition()
    print "In pixels:"
    print nav.getPositionInPixels()

    print nav.goToPixel( 119 , 92 )
    print nav.getPosition()
    print "In pixels:"
    print nav.getPositionInPixels()

    print nav.goToPixel( 153 , 91 )
    print nav.getPosition()
    print "In pixels:"
    print nav.getPositionInPixels()

    print nav.goToPixel( 157 , 101 )
    print nav.getPosition()
    print "In pixels:"
    print nav.getPositionInPixels()

    print nav.goTo(0,0)
    print nav.getPosition()

    nav.stop()


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
