def cacabuya(l):
  o=""
  i=len(l)-1
  while i>=0:
    o+=l[i]
    i-=1
  u=""
  for c in o:
    if c=="A":
      u+="T"
    elif c=="C":
      u+="G"
    elif c=="G":
      u+="C"
    elif c=="T":
      u+="A"
  return u

print cacabuya("ATTGTGCTATCCCTCGACCTTATCAAAGCTTGCTA")