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
    result_map = nav.getJpegMap()

    print result_map



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
