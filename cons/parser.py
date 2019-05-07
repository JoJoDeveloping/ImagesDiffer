#!/usr/bin/python3

index = open("hygdata_v3.csv", "r")
a = {}
k=True
for line in index:
  if k:
    k = False
    continue
  ls = line.split(",")
  if len(ls) < 3: continue
  if ls[2] == "" or ls[1] == "": continue
  a[int(ls[1])]=int(ls[2])

es=[]
for line in open("stars.txt"):
  spl = line.split()
  if len(spl) < 4: continue
  es = es + [int(spl[3])]

file = open("constellationship.fab", "r")
for line in file:
  strings = line.split()
  if len(strings) < 2:
    continue
  if len(strings) != 2+2*int(strings[1]):
    print("Mismatch at",strings[0],expected)
    continue
  outf = open("result/"+strings[0]+".txt","w")
  for i in range(int(strings[1])):
    lo1 = a[int(strings[2*i+2])]
    lo2 = a[int(strings[2*i+3])]
    if lo1 not in es or lo2 not in es: 
      print("Ignoring",lo1,"and",lo2)
      continue
    outf.write(("%d,%d\n") % (lo1, lo2))
  outf.close()
