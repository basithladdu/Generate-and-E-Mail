import qrcode

def generate_qr_code(unique_code):
    # Construct the verification URL.
    url = f"https://yourdomain.com/verify?code={unique_code}"
    
    # Generate the QR Code.
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR Code image.
    qr_filename = f"qr_{unique_code}.png"
    img.save(qr_filename)
    return qr_filename

# Example usage:
if __name__ == "__main__":
    code = "TESTCODE1"
    filename = generate_qr_code(code)
    print(f"QR code saved as {filename}")