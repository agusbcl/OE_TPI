# Chatbot de Soporte Técnico — TeleConecta

Aplicación de consola desarrollada en Python que simula un chatbot de soporte técnico para una empresa proveedora de servicios de internet. El bot valida al cliente, ofrece un menú de consultas frecuentes con soluciones sugeridas, y genera un ticket de soporte que se deriva a Nivel 2 si el problema no se resuelve.

Trabajo Práctico Integrador — POrganización empresarial
Tecnicatura Universitaria en Programación — UTN

---

## Integrantes

| Nombre | Participación |
|--------|--------------|
| Agustina Balcarcel | Desarrollo, documentación |

---

## Requisitos

- Python 3.x

---

## Instrucciones de uso

1. Clonar o descargar el repositorio.
2. Asegurarse de que el archivo `clientes.csv` esté en la misma carpeta que `chatbot_soporte.py`.
3. Ejecutar el programa:

```
python chatbot_soporte.py
```

4. Ingresar el número de cliente cuando se solicite (el sistema lo valida contra `clientes.csv`).
5. Elegir una opción del menú de soporte.
6. Indicar si la solución sugerida resolvió el problema.
7. Al finalizar, se genera automáticamente un ticket en `tickets.csv`.

---

## Funcionalidades

- **Validación de cliente:** solicita el número de cliente en un bucle hasta recibir uno que exista en la base de datos.
- **Menú de soporte:** ofrece opciones sobre conexión a internet, contraseña de WiFi, factura y cambio de plan.
- **Solución sugerida:** muestra pasos a seguir según la categoría elegida.
- **Generación de ticket:** crea un registro con un ID único (`TCK-XXX`) por cada consulta.
- **Escalado a Nivel 2:** si el problema no se resuelve, o si el cliente elige "ninguna de las anteriores", el ticket se deriva automáticamente a soporte Nivel 2.

---

## Ejemplos de entradas y salidas

### Validación de cliente

```
Ingresá tu número de cliente: 999999
No encontramos ese número de cliente. Verificalo e intentá de nuevo.
Ingresá tu número de cliente: 100001

¡Hola Juan Perez! Vimos que tenés el plan 'Internet 300 Megas'.
```

### Consulta resuelta (Nivel 1)

```
¿En qué te podemos ayudar?
  1. No tengo conexión a internet / se corta seguido
  2. Quiero cambiar la contraseña del WiFi
  3. Consulta o reclamo sobre mi factura
  4. Quiero cambiar de plan
  5. Ninguna de las anteriores / no se resolvió mi problema

Elegí una opción: 1

Probá lo siguiente:
  1. Reiniciá el módem (desenchufalo 30 segundos y volvé a enchufarlo).
  2. Verificá que los cables estén bien conectados al módem.
  3. Probá conectarte desde otro dispositivo para descartar un problema local.

¿Esto resolvió tu consulta? (s/n): s

✔ Se generó el ticket TCK-001 (resuelto).
Gracias por contactarte con TeleConecta. ¡Hasta luego!
```

### Consulta escalada a Nivel 2

```
¿Esto resolvió tu consulta? (s/n): n
Contanos brevemente qué pasó para escalarlo: se corta cada 10 minutos

✔ Se generó el ticket TCK-002 y fue escalado a soporte Nivel 2.
Un especialista se va a poner en contacto a la brevedad. ¡Hasta luego!
```

---

## Estructura del proyecto

```
/
├── chatbot_soporte.py          # Código fuente principal
├── clientes.csv                 # Base de datos simulada de clientes
├── tickets.csv                  # Registro de tickets generados (se crea automáticamente)
├── diccionario_de_datos.md     # Diccionario de datos del proyecto
└── README.md                    # Este archivo
```

---

## Enlaces

- Diagramas: https://drive.google.com/file/d/1OZQ6zwd2pG6jTFDp5VyXAbv0h1qhUsJi/view?usp=drive_link