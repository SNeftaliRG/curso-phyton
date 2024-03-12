#UNIR DOS CADENAS 
a="Sa"
b="muel"
suma=a+b
print(suma)

#MULTIPLICAR CADENAS
a="Sa"
b="muel"
suma=a+b
print(a*5)
print(b*5)
print(suma*5)

#RELACIONALES
a="Sa"
b="muel"
#igual que
print("a ES IGUAL QUE b:",a == b)
print("a ES IGUAL QUE a:",a == a)#tiene que ser igual en todas sus letras 

#distinto que
print("a ES DISTINTO QUE b:",a != b)
print("b ES DISTINTO QUE b:",b != b)

#mayor que 
print("a ES MAYOR QUE b:",a > b)

#menor que 
print("a ES MENOR QUE b:",a < b)

#mayor igual que
print("a ES MAYOR-IGUAL QUE b:",a >= b)

#menor igual que 
print("a ES MENOR-IGUAL QUE b:",a <= b)

#EXPRESION ANIDADA
c=10
d=5
print("RESPUESTA 1: ",c*d-2**d>=20 and not (c%d)!=0)
print("RESPUESTA 2: ",c*d-2**d>=20 or not (c%d)!=0)
