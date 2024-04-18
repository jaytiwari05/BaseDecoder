#!/usr/bin/python3

import argparse
import base64
import sys

parser = argparse.ArgumentParser(description="Python script to decode base64 and base 32", 
                                usage='%(prog)s --b64/--b32 cipher', 
                                epilog="Example ./%(prog)s --b64 SGVsbG8gd29ybGQ=")

#help= Help Menu
#metvar= The text which the user will give will be stored in this varibale
# nargs= ?, *, +, 1,2,3.. ? -> optional :: * -> 1 or multiply :: + -> atlest 1 argument
parser.add_argument("--b64", 
                    help="decode base64 encoding", 
                    metavar="base64", 
                    dest="b64", 
                    nargs="+")

parser.add_argument("--b32",
                    help="base32",
                    dest="b32",
                    nargs="+")

parser.add_argument("-v",
                    help="version",
                    action="version",
                    version="%(prog)s 1.0")

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

b64 = args.b64
b32 = args.b32

if b64:
    for i in b64:
        print((base64.b64decode(i)).decode())

if b32:
    for i in b32:
        print((base64.b32decode(i)).decode())