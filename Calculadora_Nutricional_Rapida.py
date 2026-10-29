def calculadora_macros (proteina,carbohidratos,grasa):
    calorias_proteina = proteina*4
    calorias_carbohidratos = carbohidratos*4
    calorias_grasa = grasa*9
    total_calorias = calorias_proteina+calorias_carbohidratos+calorias_grasa
    return total_calorias


print("\n             --- BIENVENIDO A LA CALCULADORA NUTRICIONAL---"                           )
print("\nA continuacion diligencia la siguiente informacion para calcular la cantidad de macros")
print("----------------------------------------------------------------------------------------")

gramos_proteina = float(input("\nIngrese los gramos de proteina: "))
gramos_carbohidratos = float(input("Ingrese los gramos de carbohidratos: "))
gramos_grasa = float(input("Ingrese los gramos de grasa: "))

calorias_comida = calculadora_macros(gramos_proteina,gramos_carbohidratos,gramos_grasa)

print("\nEl total de calorias de la receta es:", calorias_comida)
print("---------------------------------------------------------------------------------------\n")

