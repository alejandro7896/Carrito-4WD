"""
Carrito WiFi Controlado por Web – MicroPython

Autor: Alex de El Taller de Alex
Proyecto educativo/hobby para controlar un carrito robótico usando ESP32/ESP8266.
Incluye:
    - Servidor web integrado
    - Botones táctiles (pointer events)
    - Control de motores mediante GPIO

Si te gusta este proyecto, considera suscribirte al canal de YouTube

Este código es open-source bajo licencia MIT. ¡Diviértete y experimenta!
"""

import network
import socket
from machine import Pin
import time

# Motores del lado izquierdo
in1 = Pin(2, Pin.OUT)
in2 = Pin(3, Pin.OUT)

# Motores del lado derecho
in3 = Pin(4, Pin.OUT)
in4 = Pin(6, Pin.OUT)


# Funciones de movimiento
def avanzar():
    print("AVANZAR ►")
    in1.high(); in2.low()
    in3.high(); in4.low()

def retroceder():
    print("◄ RETROCEDER ")
    in1.low(); in2.high()
    in3.low(); in4.high()

def izquierda():
    print("◄ -- IZQUIERDA ")
    in1.low(); in2.high()
    in3.high(); in4.low()


def derecha():
    print("DERECHA -- ► ")
    in1.high(); in2.low()
    in3.low(); in4.high()


def parar():
    print(" ---- STOP ----")
    in1.low(); in2.low()
    in3.low(); in4.low()

# Crear red WiFi como Access Point
ap = network.WLAN(network.AP_IF)
ap.config(essid="CarritoAlex", password="12345678")
ap.active(True)

while not ap.active():
    pass

print("AP activado, IP:", ap.ifconfig()[0])

# Interfaz HTML con eventos táctiles
html = """<!DOCTYPE html>
<html>
<head>
    <title>Control del Carrito</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 30px; }
        button {
            width: 120px; height: 60px; margin: 10px;
            font-size: 20px; border-radius: 10px;
            background-color: #226e93; color: white; border: none;
        }
        body, button {
    user-select: none;
    -webkit-user-select: none;
    -ms-user-select: none;
    -moz-user-select: none;
}
    </style>
</head>
<body>
    <h2>🚗 Control del Carrito WiFi</h2>
    <div>
        <button onpointerdown="enviar('/avanzar')" onpointerup="enviar('/parar')">Avanzar</button><br>
        <button onpointerdown="enviar('/izquierda')" onpointerup="enviar('/parar')">Izquierda</button>
        <button onpointerdown="enviar('/parar')">Parar</button>
        <button onpointerdown="enviar('/derecha')" onpointerup="enviar('/parar')">Derecha</button><br>
        <button onpointerdown="enviar('/retroceder')" onpointerup="enviar('/parar')">Retroceder</button>
    </div>
    <script>
        function enviar(cmd) {
            fetch(cmd).catch(err => console.log("Error:", err));
        }
    </script>
</body>
</html>
"""

# Servidor web simple
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Servidor listo, esperando conexiones...")

while True:
    cl, addr = s.accept()
    print("Cliente conectado desde", addr)
    request = cl.recv(1024).decode()
    print("Solicitud:", request)

    # Comandos simples vía URL
    if "/avanzar" in request:
        avanzar()
    elif "/retroceder" in request:
        retroceder()
    elif "/izquierda" in request:
        izquierda()
    elif "/derecha" in request:
        derecha()
    elif "/parar" in request:
        parar()

    # Respuesta HTML
    cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
    cl.sendall(html)
    cl.close()
