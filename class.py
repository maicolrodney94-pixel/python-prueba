

carreras: tuple[str, ...] = ("Ingeniería de Software", "Contabilidad", "Derecho")

personas: list[tuple[str, str, int, int]] = []

estudiantes: list[dict[str, str | int]] = []

for _ in range(5):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Ingrese la edad como un número entero.")

    while True:
        try:
            carrera = int(input("Carrera (0: Ingeniería de Software, 1: Contabilidad, 2: Derecho): "))
            while not 0 <= carrera < len(carreras):
                print("Ingrese 0, 1 o 2.")
                carrera = int(input("Carrera (0: Ingeniería de Software, 1: Contabilidad, 2: Derecho): "))
            break
        except ValueError:
            print("Ingrese la carrera como un número entero.")

    personas.append((nombre, apellido, edad, carrera))
    print("")

for nombre, apellido, edad, indice_carrera in personas:
    estudiantes.append(
        {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "carrera": carreras[indice_carrera],
        }
    )

for estudiante in estudiantes:
    print(
        f"{estudiante['nombre']} {estudiante['apellido']} tiene "
        f"{estudiante['edad']} años y estudia {estudiante['carrera']}"
    )

carreras: tuple[str, ...] = ("Ingeniería de Software", "Contabilidad", "Derecho")


git init
git add .
git commit -m "Agrega ejercicio de Python"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/python-prueba.git
git push -u origin main