#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use explore method."""

import qi
import argparse
import sys
import os


def main(session):
    """
    This example uses the explore method.
    """
    # Get the services ALNavigation and ALMotion.
    nav = session.service("DecosNavigationFiles")

    #Show all maps
    maps = nav.showMaps()
    print maps

    #download map 1
    map = nav.getMap( maps[0] )
    print map


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
