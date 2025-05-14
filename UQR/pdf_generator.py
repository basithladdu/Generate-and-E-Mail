from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def generate_offer_letter_pdf(name, date, unique_code, qr_filename):
    # Create a filename for the PDF.
    safe_name = name.replace(" ", "_")
    pdf_filename = f"{safe_name}_Offer_Letter.pdf"
    
    # Create a PDF canvas with A4 size.
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4

    # Set a font and add dynamic text.
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 50, f"Dear {name},")
    c.drawString(50, height - 70, f"We are pleased to offer you an internship starting on {date}.")
    c.drawString(50, height - 90, "To verify this offer letter, please scan the QR code below.")
    c.drawString(50, height - 110, f"Unique Code: {unique_code}")
    
    # Embed QR code image into the PDF.
    # Adjust the coordinates (50, height - 330) and image size (150x150) as needed.
    c.drawImage(qr_filename, 50, height - 330, width=150, height=150)
    
    # Optionally, include instructions on what to do if verification is needed.
    c.drawString(50, height - 350, "Visit our verification portal by scanning the QR or entering your code at:")
    c.drawString(50, height - 370, "https://yourdomain.com/verify")

    c.save()
    return pdf_filename

# Example usage:
if __name__ == "__main__":
    pdf = generate_offer_letter_pdf("John Doe", "06 April 2025", "TESTCODE1", "qr_TESTCODE1.png")
    print(f"Offer letter PDF generated: {pdf}")