#!/usr/local/bin/python3

import os
import argparse

def checkpath(path):
    if os.path.exists(path):
        return path
    else:
        return False

def explore(dir, depth):
    """explore a directory, we need to track the depth in order to indent"""
    #print("exploring " + str(dir) + str(depth))
    files = os.listdir(dir)
    for f in files:
        path = os.path.join(dir, f)
        if not args.full:
            print(depth*2*" " + f)
        else:
            print(path)
        if os.path.isdir(path):
            if depth+1 < args.depth:
                explore(path,depth+1)

parser = argparse.ArgumentParser(description="explore the file system and print a tree representing it.")
parser.add_argument("--full", action="store_true", dest="full")
parser.add_argument("--depth", type=int, default=2**63)
parser.add_argument("path", help="path to start from", default=".", type=checkpath)
#, type=os.path.exists)
args = parser.parse_args()
explore(args.path, 0)
