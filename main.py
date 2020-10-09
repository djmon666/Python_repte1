def down(s):
  x=""
  result=""
  y=len(s)
  while y>0:
    y-=1
    x=x+s[y]
  for i in x:
    if i=="A":
      result+="T"
    if i=="C":
      result+="G"
    if i=="G":
      result+="C"
    if i=="T":
      result+="A"
  return result