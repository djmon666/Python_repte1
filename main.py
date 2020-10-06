DNA="ATTGTGCTATCCCTCGACCTTATCAAAGCTTGCTA"
def comDNA(DNA):
  D=""
  p=len(DNA)-1
  while p >=0:
    if DNA[p] == "A":
      D=D+"T"
    else:
      D=D+DNA[p] 
    p-=1 
  return D
print comDNA(DNA)