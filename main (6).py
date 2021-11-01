def mini(L):
  mini= L[0]
  for x in L:
    if(x<mini):
      mini =x
  return mini

def sort(L):
  if(L==[] or len(L)==1):
    return L
  m = mini(L)
  L.remove(m)
  return [m]+sort(L)

L=[34,54,35,15,67,98,89]
print(sort(L))