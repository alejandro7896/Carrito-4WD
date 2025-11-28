# 🚗 Carrito WiFi Controlado por Web – ESP32 / ESP8266

Proyecto sencillo pero poderoso: un carrito robótico controlado **desde cualquier dispositivo** vía WiFi, usando un servidor web integrado en un **ESP32/ESP8266**.  
Incluye interfaz táctil optimizada para móvil y control de motores mediante GPIO.

Ideal para hobby, enseñanza, makers, o simplemente para presumirle a tu primo que tu carrito sí obedece.

---

## ⭐ Características
- El ESP/Raspberry crea su **propio Access Point** (no necesitas internet).
- Control del carrito desde el navegador.
- Interfaz táctil (usa **pointerdown / pointerup**).
- Respuesta inmediata: mientras mantienes presionado, se mueve; sueltas → se detiene.
- Código simple, 100% MicroPython.

---

## 📡 Hardware Necesario
- ESP32 o ESP8266 con MicroPython.
- Driver de motores (L298N, L293D o equivalente).
- Carrito con motores DC.
- Una pizca de paciencia (opcional, pero recomendado).

---

## 🔌 Pines usados (puedes ajustarlos)
| Función | Pin |
|--------|-----|
| Motor Izquierdo IN1 | GPIO 2 |
| Motor Izquierdo IN2 | GPIO 3 |
| Motor Derecho IN3 | GPIO 4 |
| Motor Derecho IN4 | GPIO 6 |

---

## 🚀 Cómo usar
1. Carga MicroPython en tu ESP.
2. Copia el archivo `main.py` a la memoria del ESP.
3. Reinicia.
4. Conéctate a la WiFi que crea el carro:
```
SSID: CarritoAlex
Password: 12345678
```
5. Abre en tu navegador:
```
http://192.168.4.1
```

6. Juega como si fuera un Need For Speed versión “yo lo armé”.

---

## 📁 Código
El proyecto incluye:
- `main.py` → Control del servidor web + control de motores.

---

## 🎥 Video de YouTube
[![Mira el video en YouTube](https://i.ytimg.com/vi/LMMG2ajQQfk/hqdefault.jpg)]((https://www.youtube.com/watch?v=LMMG2ajQQfk))


---

## 🧠 Notas
- Recuerda ajustar los pines a tu placa si usas un modelo diferente.
- Si el carro no se mueve en línea recta… bienvenido al club. Ajusta el cableado, o acepta que tu robot tiene libre albedrío.

---

## 📜 Licencia
MIT – úsalo, modifícalo, rómpelo, arréglalo; solo deja la atribución.
