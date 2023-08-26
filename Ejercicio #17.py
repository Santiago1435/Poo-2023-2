import math

p=math.pi

R = int(input("cual es el radio de el circulo? "))

area= round(R*(p**2),2)
longitud= round((2*p)*R,2)

print(f"Dado el radio:{R}, su Area será:{area} y su longitud será:{longitud}")