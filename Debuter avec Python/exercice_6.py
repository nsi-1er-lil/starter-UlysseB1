def surface_cylindre(r):
    from math import pi 
    return 2*pi*r**2
r = 8
def volume_cylindre(h):
    from math import pi
    return pi*r**2*h
h = 6
print("La surface du cylindre de rayon : ",
      r,"est de :", surface_cylindre(r))
print("Le volume du cylindre de rayon: ",
      r,"et de hauteur : ",h,"est de :", volume_cylindre(h))

