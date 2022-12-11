tabla1 = 1 
tabla2 = 10 
comienzo = 1 
final = 10 

for numero in range(tabla1, tabla2 + 1):
	print(f'Tabla de multiplicar del {numero}:') 
	for numeromultiplicado in range(comienzo, final + 1):
		print(f'{numero} x {numeromultiplicado} = {numero * numeromultiplicado}')
	print()