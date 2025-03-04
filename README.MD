# API de Generación de Códigos QR

Esta es una API desarrollada con **FastAPI** que permite generar códigos QR personalizados con opciones como tamaño, colores y logos.

## 🚀 Características
- Generación de códigos QR a partir de texto o URL.
- Personalización del tamaño del QR.
- Soporte para cambiar los colores de fondo y primer plano.
- Posibilidad de incluir un logo en el centro del QR.
- Caché para evitar regeneraciones innecesarias.
- Formatos soportados: `png`, `jpg`, `svg`.

---

## 📌 Instalación y Ejecución
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/qr-api.git
cd qr-api
```

### 2️⃣ Crear un entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la API
```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`

---

## 📄 Uso de la API
### **🔹 Endpoint: Generar un código QR**
**URL:** `POST /generate_qr/`

**Ejemplo de solicitud:**
```json
{
  "text": "https://mi-sitio.com",
  "size": 10,
  "fg_color": "#000000",
  "bg_color": "#ffffff",
  "format": "png",
  "logo_url": "https://mi-sitio.com/logo.png"
}
```

**Ejemplo de respuesta:**
```json
{
  "message": "Código QR generado",
  "qr_url": "/static/qr_codes/mi-sitio-com.png"
}
```

Si el QR ya existía en caché:
```json
{
  "message": "Código QR recuperado desde caché",
  "qr_url": "/static/qr_codes/mi-sitio-com.png"
}
```

---

## 🛠 Tecnologías Usadas
- **FastAPI**: Framework web para Python.
- **Uvicorn**: Servidor ASGI para FastAPI.
- **qrcode**: Librería para generar códigos QR.
- **Pillow**: Manipulación de imágenes.

---

## 📌 Estructura del Proyecto
```
qr-api/
│-- main.py  # Archivo principal con la API
|-- models.py # Modelo de la API
|-- services.py # Servicio de la API
│-- requirements.txt  # Dependencias del proyecto
│-- static/
│   └── qr_codes/  # Carpeta donde se guardan los QR
│-- README.md  # Documentación del proyecto
```

---

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**. Puedes usarlo, modificarlo y distribuirlo libremente.

---

## ✨ Autor
Desarrollado por [Tu Nombre](https://github.com/tu-usuario).

