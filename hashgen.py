import hashlib
import sys


if (len(sys.argv) < 2):
  print("[+] Usage python3 "+ sys.argv[0] +" file hash-format")
else:
  filename = sys.argv[1]
  file = open(filename,encoding='utf-8',errors='ignore')
  Lines = file.readlines()
  for line in Lines:
    hashtype = sys.argv[2]
    sline = line.encode('utf-8')
    m = hashlib.new(hashtype,sline)
    print(m.hexdigest())
