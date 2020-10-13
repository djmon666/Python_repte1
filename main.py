DNA="ATTGTGCTATCCCTCGACCTTATCAAAGCTTGCTA"
def comDNA(DNA):
  D=""
  p=len(DNA)-1
  while p >=0:
    if DNA[p] == "A":
      D=D+"T"
    elif DNA[p] == "T":
      D=D+"A"
    elif DNA[p] == "C":
      D=D+"G" 
    elif DNA[p] == "G":
      D=D+"C"    
    p-=1 
  return D
print comDNA(DNA)