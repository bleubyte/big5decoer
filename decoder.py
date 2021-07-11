## python script for Big5 cookie decoder from https://secureideas.com/blog/2013/02/decoding-f5-cookie.html
import struct
import sys

def decode(cookie_value):

     (host, port, end) = cookie_value.split('.')

     (a, b, c, d) = [ord(i) for i in struct.pack("<I", int(host))]

     p = [ord(i) for i in struct.pack("<I", int(port))]
     portOut = p[0]*256 + p[1]

     print "%s.%s.%s.%s:%s" % (a,b,c,d,portOut)

if len(sys.argv) != 3:
     print "Usage: %s input_type encoded_string" % sys.argv[0]
     print "-c Individual cookie value"
     print "-f File Name containing cookie values on each linen"
     print "ex. %s -c 839518730.47873.0000" % sys.argv[0]
     print "ex. %s -f inputfile.txt" % sys.argv[0]
     exit(1)

if sys.argv[1] == "-c":
     cookie_text = sys.argv[2]
     decode(cookie_text)
if sys.argv[1] == "-f":
     file_name = sys.argv[2]
     with open(file_name,'r') as f:
          for x in f:
               x = x.rstrip()
               if not x: continue
               decode(x)
