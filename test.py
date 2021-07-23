
import os
import urllib2
import sys
print("\033[92m")
os.system("figlet site Knowledge ")
print("\033[94m")
print("Coded by: MD.NAZIM")
print("From Bangladesh")
print("\033[96m")
print("Tools name is 'Site Knowledge'")
print("\033[98m")
url =raw_input("Enter your full website link with https : ")
url.rstrip ( )
header = urllib2.urlopen (url) .info( )
print(str(header))



