#!/usr/bin/python3

file = open("constellationship.fab", "r")
for line in file:
  strings = line.split()
  if len(strings) < 2:
    continue
  if len(strings) != 2+2*int(strings[1]):
    print("Mismatch at",strings[0],expected)
    continue
  outf = open(strings[0]+".txt","w")
  for i in range(int(strings[1])):
    outf.write(("%s,%s\n") % (strings[2*i+2], strings[2*i+3]))
  outf.close()
