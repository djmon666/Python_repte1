def caca (s):
  cacabuya=""
  i=len(s)-1
  while i>=0:
    cacabuya+=s[i]
    i-=1
  return cacabuya
def uwu (b):
  owo=""
  for letter in b:
    if letter=="A":
      owo+="T"
    elif letter=="C":
      owo+="G"
    elif letter=="G":
      owo+="C"
    elif letter=="T":
      owo+="A"
  return owo
def result (Gerard):
  return uwu (caca (Gerard))
print result ("ATTGTGCTATCCCTCGACCTTATCAAAGCTTGCTA")