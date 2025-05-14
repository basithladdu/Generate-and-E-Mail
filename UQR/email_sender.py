import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, pdf_filename):
    # Create the root message.
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Internship Offer Letter"
    
    # Add an email body.
    body = ("Dear Intern,\n\nPlease find your internship offer letter attached. "
            "The letter contains a QR code for certificate authenticity verification.\n\nRegards,\nHR Team")
    msg.attach(MIMEText(body, "plain"))
    
    # Attach the PDF.
    with open(pdf_filename, "rb") as f:
        part = MIMEApplication(f.read(), Name=pdf_filename)
    part['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
    msg.attach(part)
    
    # Send the email using SMTP (update the details as needed).
    try:
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server and port.
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)

# Example usage (ensure you update the credentials and SMTP server details):
if __name__ == "__main__":
    send_email("hr@example.com", "your_password", "john.doe@example.com", "John_Doe_Offer_Letter.pdf")