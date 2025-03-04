import qrcode
from io import BytesIO

def generate_qr(text: str, size: int = 10):
    qr = qrcode.QRCode(
        version=1,
        box_size=size,
        border=5
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="PNG")
    return img_byte_arr.getvalue()
