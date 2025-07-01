import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail:
    sender_email = "ShashwatRajPhotosAcc@gmail.com"
    sender_password = "xyqu dacm rslg kswd"

    def __init__(self,email):
        self.email = email

    def send_email(self):
    # Email configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create message
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = self.email
        message["Subject"] = "Test Email"

        # Email body
        body = "This is a test email sent from Python!"
        message.attach(MIMEText(body, "plain"))

        # Send email
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Enable encryption
            server.login(self.sender_email, self.sender_password)
            server.send_message(message)
            server.quit()
            print("Email sent successfully!")

        except Exception as e:
            print(f"Error: {e}")
