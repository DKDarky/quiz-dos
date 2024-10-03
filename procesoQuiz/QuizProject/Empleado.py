#Proceso para ingresar los datos por teclado
Nombre = input("Nombre del empleado: ")
Dias = int (input("Dias contratados: "))
Salario = int (input("Ingrese salario: "))

#Invocar y imprimir los datos ingresados
print(f" Nombre del empleado: {Nombre}, Salario es: {Salario}, Dias que lleva el empleado: {Dias}")
#Proceso de liquidacion
print(f"Salario del empleado: {Salario}")
#Proceso de prima
Prima = Salario * Dias / 360
print(f"Su prima seria: {Prima}")
#Cesantias
Cesantias = Salario * Dias / 360
print((f"Su Cesantias: {Cesantias}"))
#Intereses de cesantias
Valor = float(0.12)
IntereseCesantias = Cesantias* Valor / Dias
print(f"Sus intereses Cesantias serian: {IntereseCesantias}")
#Vacaciones
Vacaciones = Salario * Dias / 720
print(f"Sus vacaciones son: {Vacaciones}")
#Liquidacion
Liquidacion = Prima + Cesantias + IntereseCesantias + Vacaciones
print(f"Su liquidacion es: {Liquidacion}")


