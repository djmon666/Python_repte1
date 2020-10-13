def caca(c):
    i=''
    r=0
    p=len(c)-1
    while r<=p:
        if c[p]=="A":
          i=i+"T"
        elif  c[p]=="T":
          i=i+"A"
        elif  c[p]=="C":
          i=i+"G"
        elif  c[p]=="G":
          i=i+"C"
        p=p-1
    return i
print caca("ATTGTGCTATCCCTCGACCTTATCAAAGCTTGCTA")
