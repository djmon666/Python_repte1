def reverse(phrase):
  i=""
  i = i.join(list(map(lambda x: x[::-1], phrase.split())))
  k=""
  for si in i:
    if si=="A":
      k=k+"T"
    elif si=="C":
      k=k+"G"
    elif si=="G":
      k=k+"C"
    else:
      k=k+"A"
  return k
