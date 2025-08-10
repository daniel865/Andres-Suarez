def calcular_nota():
    """
    Programa que lee 5 notas del teclado y determina el estado del estudiante
    basado en el promedio de las notas.
    """
    print("Ingrese 5 notas (valores entre 0 y 100):")
    
    notas = []
    
    for i in range(5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i+1}: "))
                if 0 <= nota <= 100:
                    notas.append(nota)
                    break
                else:
                    print("Error: La nota debe estar entre 0 y 100. Intente de nuevo.")
            except ValueError:
                print("Error: Por favor ingrese un número válido.")
    
    promedio = sum(notas) / len(notas)
    
    print(f"\nNotas ingresadas: {notas}")
    print(f"Promedio: {promedio:.2f}")
    
    if promedio >= 60:
        print("Aprobado")
    elif 40 <= promedio <= 59:
        print("En recuperacion")
    else:
        print("Reprobado")

if __name__ == "__main__":
    calcular_nota() 