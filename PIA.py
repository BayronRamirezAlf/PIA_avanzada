class Tres_programas:
    def descuento_clientes(self, monto):
        descuento = 0
        if monto < 500:
            descuento = 0
        elif 500 <= monto <= 1000:
            descuento = monto * 0.05
        elif 1000 < monto <= 7000:
            descuento = monto * 0.11
        elif 7000 < monto <= 15000:
            descuento = monto * 0.18
        else:
            descuento = monto * 0.25
        return descuento

    def imprimir_descuento(self, monto):
        descuento = self.descuento_clientes(monto)
        print(f"Para una compra de ${monto}, el descuento aplicado es de ${descuento}")

    def imprimir_info_dinosaurio(self, nombre, peso, longitud):
        class Dinosaurio:
            def __init__(self, nombre, peso, longitud):
                self.nombre = nombre
                self.peso = peso
                self.longitud = longitud
                self.peso_en_kg = self.convertir_a_kg()
                self.longitud_en_metros = self.convertir_a_metros()

            def convertir_a_kg(self):
                return self.peso / 2.20462

            def convertir_a_metros(self):
                return self.longitud * 0.3048

            def imprimir(self):
                print("Información del Dinosaurio:")
                print(f"Nombre: {self.nombre}")
                print(f"Peso: {self.peso} libras - {self.peso_en_kg:.2f} kg")
                print(f"Longitud: {self.longitud} pies - {self.longitud_en_metros:.2f} metros")

        dino = Dinosaurio(nombre, peso, longitud)
        dino.imprimir()

    def calcular_total_gasolina(self, galones):
        class Gasolina:
            def __init__(self, galones):
                self.galones = galones
                self.total = self.calcular_total()

            def calcular_total(self):
                litros_por_galon = 3.785
                precio_por_litro = 8.20
                total_pagar = self.galones * litros_por_galon * precio_por_litro
                return total_pagar

            def imprimir_informacion(self):
                print(f"Galones comprados: {self.galones}")
                print(f"Total a pagar: ${self.total:.2f}")

        venta_gasolina = Gasolina(galones)
        venta_gasolina.imprimir_informacion()


# bloque principal
tres_programas = Tres_programas()

# Calcular descuento de clientes
monto_compra = 8000
tres_programas.imprimir_descuento(monto_compra)

# Imprimir información de un dinosaurio
nombre_dinosaurio = "Tyrannosaurus Rex"
peso_dinosaurio = 9000  # en libras
longitud_dinosaurio = 40  # en pies
tres_programas.imprimir_info_dinosaurio(nombre_dinosaurio, peso_dinosaurio, longitud_dinosaurio)

# Calcular el total de gasolina
galones_comprados = 10
tres_programas.calcular_total_gasolina(galones_comprados)

class Tres_programas:
    def archivos_txt(self, nombre_archivo, contenido=None):
        if contenido is None:
            # Leer
            try:
                with open(nombre_archivo, 'r') as archivo:
                    contenido = archivo.read()
                    print(f"Contenido de '{nombre_archivo}':\n{contenido}")
            except FileNotFoundError:
                print(f"El archivo '{nombre_archivo}' no existe.")
        else:
            # Escribir
            with open(nombre_archivo, 'w') as archivo:
                archivo.write(contenido)
                print(f"Se ha escrito en '{nombre_archivo}':\n{contenido}")

    def descuento_compra(self, compra):
        descuento = 0.1
        total_descuento = compra * descuento
        total_pagar = compra - total_descuento
        return total_descuento, total_pagar

    def libras_a_kilogramos(self, peso_libras):
        return peso_libras * 0.453592

    def pies_a_metros(self, longitud_pies):
        return longitud_pies * 0.3048

    def total_pagar_gasolina(self, galones_comprados, precio_por_litro):
        litros_comprados = galones_comprados * 3.785
        total_pagar = litros_comprados * precio_por_litro
        return total_pagar


# bloque principal
programas = Tres_programas()


programas.archivos_txt('compra.txt', '4000')
programas.archivos_txt('dinosaurio.txt', '8000')
programas.archivos_txt('longitud.txt', '40')
programas.archivos_txt('gasolina.txt', '10')

# Leer
programas.archivos_txt('compra.txt')
programas.archivos_txt('dinosaurio.txt')
programas.archivos_txt('longitud.txt')
programas.archivos_txt('gasolina.txt')


total_descuento, total_pagar_con_descuento = programas.descuento_compra(4000)
print(f"Descuento: ${total_descuento}, Total a pagar con descuento: ${total_pagar_con_descuento}")

peso_kg = programas.libras_a_kilogramos(8000)
print(f"Peso del dinosaurio en kilogramos: {peso_kg} kg")

longitud_metros = programas.pies_a_metros(40)
print(f"Longitud en metros: {longitud_metros} m")

total_pagar_gasolina = programas.total_pagar_gasolina(10, 8.20)
print(f"Total a pagar por la gasolina: ${total_pagar_gasolina}")



#Constructor
class Tres_programas:
    def __init__(self):
        pass

    def descuento_clientes(self, monto):
        def descuento_clientes(self, monto):
         descuento = 0
        if monto < 500:
            descuento = 0
        elif 500 <= monto <= 1000:
            descuento = monto * 0.05
        elif 1000 < monto <= 7000:
            descuento = monto * 0.11
        elif 7000 < monto <= 15000:
            descuento = monto * 0.18
        else:
            descuento = monto * 0.25
        return descuento

    def imprimir_descuento(self, monto):
        descuento = self.descuento_clientes(monto)
        print(f"Para una compra de ${monto}, el descuento aplicado es de ${descuento}")

    def imprimir_info_dinosaurio(self, nombre, peso, longitud):
            class Dinosaurio:
             def __init__(self, nombre, peso, longitud):
                self.nombre = nombre
                self.peso = peso
                self.longitud = longitud
                self.peso_en_kg = self.convertir_a_kg()
                self.longitud_en_metros = self.convertir_a_metros()

            def convertir_a_kg(self):
                return self.peso / 2.20462

            def convertir_a_metros(self):
                return self.longitud * 0.3048

    def calcular_total_gasolina(self, galones):
        class Gasolina:
            def __init__(self, galones):
                self.galones = galones
                self.total = self.calcular_total()

    # constructor
    def __init__(self):
        self.opcion = 0

    def opcion_menu(self):
        print("Selecciona una opción:")
        print("1. Calcular descuento")
        print("2. Imprimir información de dinosaurio")
        print("3. Calcular total de gasolina")
        self.opcion = int(input("Ingrese el número de la opción: "))

    def ejecutar_opcion(self):
        if self.opcion == 1:
            monto_compra = 8000
            self.imprimir_descuento(monto_compra)
        elif self.opcion == 2:
            nombre_dino = "Tyrannosaurus Rex"
            peso_dino = 9000
            longitud_dino = 40
            self.imprimir_info_dinosaurio(nombre_dino, peso_dino, longitud_dino)
        elif self.opcion == 3:
            galones_comprados = 10
            self.calcular_total_gasolina(galones_comprados)
        else:
            print("Opción no válida.")

# bloque principal
tres_programas = Tres_programas()
tres_programas.opcion_menu()
tres_programas.ejecutar_opcion()