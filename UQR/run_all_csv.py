import pandas as pd
from datetime import datetime
import uuid
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# ----- Function Definitions -----

def generate_unique_code() -> str:
    """Generate a short unique code using uuid."""
    return str(uuid.uuid4())[:8]

def generate_qr_code(unique_code: str) -> str:
    """Generate a QR code embedding a verification URL."""
    verification_url = f"https://yourdomain.com/verify?code={unique_code}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(verification_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    qr_filename = f"qr_{unique_code}.png"
    img.save(qr_filename)
    return qr_filename

def generate_offer_letter_pdf(name: str, date: str, unique_code: str, qr_filename: str) -> str:
    """Generate an internship offer letter PDF."""
    pdf_filename = f"{name.replace(' ', '_')}_Offer_Letter.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4

    # Add text content
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 50, f"Dear {name},")
    c.drawString(50, height - 70, f"We are pleased to offer you an internship starting on {date}.")
    c.drawString(50, height - 90, "Scan the QR code below to verify the authenticity of your offer letter:")
    c.drawString(50, height - 110, f"Unique Code: {unique_code}")
    
    # Add QR code image to PDF
    c.drawImage(qr_filename, 50, height - 330, width=150, height=150)
    c.drawString(50, height - 350, "Or visit: https://yourdomain.com/verify")
    c.save()
    return pdf_filename

def send_email(sender_email: str, smtp_server: str, smtp_port: int, receiver_email: str, pdf_filename: str):
    """Send the PDF offer letter via email."""
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Internship Offer Letter"
    
    # Email body
    body = (
        "Dear Intern,\n\n"
        "Please find attached your internship offer letter.\n"
        "This letter includes a QR code for verification of authenticity.\n\n"
        "Regards,\nHR Team"
    )
    msg.attach(MIMEText(body, "plain"))
    
    # Attach the PDF
    with open(pdf_filename, "rb") as pdf_file:
        part = MIMEApplication(pdf_file.read(), Name=pdf_filename)
    part['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
    msg.attach(part)
    
    # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.send_message(msg)
    server.quit()

# ----- Main Workflow -----

if __name__ == "__main__":
    # Load intern data from CSV
    df = pd.read_csv("interns.csv")
    today_date = datetime.now().strftime("%d %B %Y")

    # Email sender details
    sender_email = "hr@example.com"
    smtp_server = "localhost"  # Change for production
    smtp_port = 1025           # Change for production

    # Process each intern
    for _, row in df.iterrows():
        full_name = row['FullName'].title()  # Convert name to CamelCase
        email = row['Email']
        unique_code = generate_unique_code()

        # Generate QR code and PDF
        qr_file = generate_qr_code(unique_code)
        pdf_file = generate_offer_letter_pdf(full_name, today_date, unique_code, qr_file)
        
        # Send email with the PDF attached
        send_email(sender_email, smtp_server, smtp_port, email, pdf_file)
        print(f"Processed {full_name}: Email sent to {email}.")