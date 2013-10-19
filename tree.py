#!/usr/local/bin/python

import os
import argparse

def explore(dir, depth):
    """explore a directory, we need to track the depth in order to indent"""
    #print("exploring " + str(dir) + str(depth))
    files = os.listdir(dir)
    for f in files:
        path = os.path.join(dir, f)
        if args.sparse:
            print(depth*2*" " + f)
        else:
            print(path)
        if os.path.isdir(path):
            explore(path,depth+1)

path = "."

parser = argparse.ArgumentParser(description="explore the file system and print a tree representing it.")
parser.add_argument("--sparse", action="store_true", dest="sparse")
parser.add_argument("path", help="path to start from")
args = parser.parse_args()
explore(args.path, 0)
