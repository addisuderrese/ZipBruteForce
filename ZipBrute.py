from zipfile import ZipFile
import argparse

parser = argparse.ArgumentParser(description="\n Usage: python ZipBrute.py -z <zipfile.azip> -p <passwordfile.txt>")

parser.add_argument("-z", dest="ziparchive", help="Zip Archive File")
parser.add_argument("-p", dest="passfile", help="Password Files")

parsed_args = parser.parse_args()

def banner():
    font = """ 
  ___ ____   __   ___ _  _ ____ ____  
 / __|  _ \ /__\ / __| )/ | ___|  _ \ 
( (__ )   //(__)( (__ )  ( )__) )(_) )
 \___|_)\_|__)(__)___|_)\_|____|____/ """
    print(font)


try:
    ziparchive = ZipFile(parsed_args.ziparchive)
    passfile = parsed_args.passfile
    foundpass = ""

except:
    print(parser.description)
    exit(0)

with open(passfile, "r") as f:
    for line in f:
        password = line.strip("\n")
        password = password.encode("utf-8")

        try:
            foundpass = ziparchive.extractall(pwd=password)
            if foundpass == None:
                banner()
                print("\nFound Password :", password.decode())
        except RuntimeError:
            pass

    if foundpass == "":
        print("Password Not Found")

