n1 = input("Ingrese el primer número: ")
n2 = input("Ingrese el segundo número: ")

u1 = n1[2]
u2 = n2[2]

d1 = n1[1] 
d2 = n2[1]

c1 = n1[0] 
c2 = n2[0]

n1_invertido = n1[-1:-4:-1]
n2_invertido = n2[-1:-4:-1]

suma = int(n1_invertido) + int(n2_invertido) + int(n1) + int(n2)

cifras6 = n1 + n2_invertido

print(f'primer número: u1={u1}, d1={d1}, c1={c1}')
print(f'segundo número: u2={u2}, d2={d2}, c2={c2}')
print(f'suma: {suma}')
print(f'cifras6: {cifras6}')
