from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from urllib.parse import quote
import qrcode
import os
from PIL import Image

app = FastAPI(title="API de Códigos QR")

# Montamos la carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Caché en memoria para evitar regenerar QR
qr_cache = {}

# Ruta donde se guardarán los QR
QR_FOLDER = "qr_api/static/qr_codes"
os.makedirs(QR_FOLDER, exist_ok=True)

@app.post("/generate_qr/")
async def generate_qr_code(
    text: str,
    size: int = Query(10, ge=1, le=50),
    fg_color: str = "black",
    bg_color: str = "white",
    format: str = "png"
):
    safe_filename = f"{quote(text, safe='')}.{format}"
    file_path = os.path.join(QR_FOLDER, safe_filename)

    if not os.path.exists(file_path):
        qr = qrcode.QRCode(box_size=size, border=2)
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fg_color, back_color=bg_color)
        img.save(file_path, format=format.upper())

    qr_url = f"/static/qr_codes/{safe_filename}"
    qr_cache[text] = qr_url

    return JSONResponse(content={"message": "Código QR generado", "qr_url": qr_url})

@app.post("/generate_qr_with_logo/")
async def generate_qr_with_logo(text: str, logo_url: str = "static/logo.png"):
    safe_filename = f"{quote(text, safe='')}_logo.png"
    file_path = os.path.join(QR_FOLDER, safe_filename)

    if not os.path.exists(file_path):
        qr = qrcode.QRCode(box_size=10, border=2)
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white").convert("RGB")

        try:
            logo = Image.open(logo_url)
            logo = logo.resize((50, 50))
            img_w, img_h = img.size
            logo_w, logo_h = logo.size
            pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
            img.paste(logo, pos, logo)
        except Exception as e:
            return JSONResponse(content={"error": f"Error al cargar el logo: {str(e)}"}, status_code=400)

        img.save(file_path)

    qr_url = f"/static/qr_codes/{safe_filename}"
    return JSONResponse(content={"message": "Código QR con logo generado", "qr_url": qr_url})
