import csv
import os

ARCHIVO_CLIENTES = "clientes.csv"
ARCHIVO_TICKETS = "tickets.csv"

EMPRESA = "TeleConecta"

OPCIONES_SOPORTE = {
    "1": {
        "descripcion": "No tengo conexión a internet / se corta seguido",
        "solucion": (
            "Probá lo siguiente:\n"
            "  1. Reiniciá el módem (desenchufalo 30 segundos y volvé a enchufarlo).\n"
            "  2. Verificá que los cables estén bien conectados al módem.\n"
            "  3. Probá conectarte desde otro dispositivo para descartar un problema local."
        )
    },
    "2": {
        "descripcion": "Quiero cambiar la contraseña del WiFi",
        "solucion": (
            "Probá lo siguiente:\n"
            "  1. Ingresá a la app o Sucursal Virtual con tu número de cliente.\n"
            "  2. Buscá la sección 'Internet' y luego 'Configuración del WiFi'.\n"
            "  3. Ahí podés cambiar el nombre de red y la contraseña."
        )
    },
    "3": {
        "descripcion": "Consulta o reclamo sobre mi factura",
        "solucion": (
            "Probá lo siguiente:\n"
            "  1. Revisá el detalle de tu factura en la Sucursal Virtual.\n"
            "  2. Verificá la fecha de vencimiento y los medios de pago habilitados.\n"
            "  3. Si ves un cargo que no reconocés, anotá el concepto exacto para el reclamo."
        )
    },
    "4": {
        "descripcion": "Quiero cambiar de plan",
        "solucion": (
            "Probá lo siguiente:\n"
            "  1. Ingresá a la Sucursal Virtual con tu número de cliente.\n"
            "  2. Buscá la sección 'Mi Plan' para ver las opciones disponibles.\n"
            "  3. Tené en cuenta que el cambio puede tardar hasta 48hs en aplicarse."
        )
    }
}


def cargar_clientes():
#Lee el archivo clientes.csv y devuelve la lista de clientes registrados.
    clientes = []

    if not os.path.exists(ARCHIVO_CLIENTES):
        return clientes

    try:
        with open(ARCHIVO_CLIENTES, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                clientes.append(fila)
    except Exception as e:
        print("Error al leer clientes.csv:", e)

    return clientes


def buscar_cliente(numero_cliente, clientes):
#Busca un cliente por número de cliente. Devuelve el diccionario del cliente o None.
    for cliente in clientes:
        if cliente["numero_cliente"] == numero_cliente:
            return cliente
    return None


def pedir_numero_cliente(clientes):
#Solicita el número de cliente en un bucle hasta recibir uno válido.
    while True:
        numero = input("Ingresá tu número de cliente: ").strip()

        if numero == "":
            print("El número de cliente no puede estar vacío.")
            continue

        if not numero.isdigit():
            print("El número de cliente solo puede contener dígitos.")
            continue

        cliente = buscar_cliente(numero, clientes)

        if cliente is None:
            print("No encontramos ese número de cliente. Verificalo e intentá de nuevo.")
            continue

        return cliente


def cargar_tickets():
#Lee el archivo CSV y devuelve la lista de tickets existentes.
    tickets = []

    if not os.path.exists(ARCHIVO_TICKETS):
        return tickets

    try:
        with open(ARCHIVO_TICKETS, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                tickets.append(fila)
    except Exception as e:
        print("Error al leer el CSV:", e)

    return tickets


def guardar_ticket(ticket):
#Agrega un nuevo ticket al archivo CSV, creando el encabezado si no existe.
    existe = os.path.exists(ARCHIVO_TICKETS)

    with open(ARCHIVO_TICKETS, "a", newline="", encoding="utf-8") as archivo:
        campos = ["id", "numero_cliente", "nombre", "categoria", "descripcion", "nivel"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        if not existe:
            escritor.writeheader()

        escritor.writerow(ticket)


def generar_id_ticket(tickets):
#Genera el siguiente ID de ticket con formato TCK-001.
    numero = len(tickets) + 1
    return f"TCK-{numero:03d}"


def mostrar_menu():
#Muestra las opciones de soporte disponibles.
    print("\n¿En qué te podemos ayudar?")
    for clave, opcion in OPCIONES_SOPORTE.items():
        print(f"  {clave}. {opcion['descripcion']}")
    print("  5. Ninguna de las anteriores / no se resolvió mi problema")


def pedir_confirmacion(mensaje):
#Pide una respuesta sí/no al usuario.
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Por favor respondé 's' o 'n'.")


#Programa principal
def chatbot():
    print("=" * 60)
    print(f"  BIENVENIDO AL SOPORTE DE {EMPRESA}")
    print("=" * 60)

    clientes = cargar_clientes()
    cliente = pedir_numero_cliente(clientes)

    print(f"\n¡Hola {cliente['nombre']}! Vimos que tenés el plan '{cliente['plan']}'.")

    tickets = cargar_tickets()

    while True:
        mostrar_menu()
        opcion = input("\nElegí una opción: ").strip()

        if opcion in OPCIONES_SOPORTE:
            categoria = OPCIONES_SOPORTE[opcion]["descripcion"]
            print(f"\n{OPCIONES_SOPORTE[opcion]['solucion']}")

            resuelto = pedir_confirmacion("\n¿Esto resolvió tu consulta?")

            if resuelto:
                ticket = {
                    "id": generar_id_ticket(tickets),
                    "numero_cliente": cliente["numero_cliente"],
                    "nombre": cliente["nombre"],
                    "categoria": categoria,
                    "descripcion": "Resuelto con la solución sugerida por el bot.",
                    "nivel": "Nivel 1 (autoservicio)"
                }
                tickets.append(ticket)
                guardar_ticket(ticket)

                print(f"\n✔ Se generó el ticket {ticket['id']} (resuelto).")
                print(f"Gracias por contactarte con {EMPRESA}. ¡Hasta luego!")
                break
            else:
                detalle = input("\nContanos brevemente qué pasó para escalarlo: ").strip()

                ticket = {
                    "id": generar_id_ticket(tickets),
                    "numero_cliente": cliente["numero_cliente"],
                    "nombre": cliente["nombre"],
                    "categoria": categoria,
                    "descripcion": detalle if detalle != "" else "Sin detalle adicional.",
                    "nivel": "Nivel 2"
                }
                tickets.append(ticket)
                guardar_ticket(ticket)

                print(f"\n✔ Se generó el ticket {ticket['id']} y fue escalado a soporte Nivel 2.")
                print("Un especialista se va a poner en contacto a la brevedad. ¡Hasta luego!")
                break

        elif opcion == "5":
            detalle = input("\nContanos brevemente cuál es tu consulta o problema: ").strip()

            ticket = {
                "id": generar_id_ticket(tickets),
                "numero_cliente": cliente["numero_cliente"],
                "nombre": cliente["nombre"],
                "categoria": "Otro / no especificado",
                "descripcion": detalle if detalle != "" else "Sin detalle adicional.",
                "nivel": "Nivel 2"
            }
            tickets.append(ticket)
            guardar_ticket(ticket)

            print(f"\n✔ Se generó el ticket {ticket['id']} y fue escalado a soporte Nivel 2.")
            print("Un especialista se va a poner en contacto a la brevedad. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Por favor elegí una opción del menú.")


chatbot()
