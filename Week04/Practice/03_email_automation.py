import smtplib
from email.message import EmailMessage

sender_email = "milind36036@gmail.com"
app_password = "qwdy jkog uwno xfos"
receiver_email = "vivek36036@gmail.com"

message = EmailMessage()
message["Subject"] = "Test Email from Python"
message["From"] = sender_email
message["To"] = receiver_email

message.set_content(
    "Hello,\n\n"
    "This is a test email sent using Python.\n\n"
    "Regards,\n"
    "Milind"
)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(message)

    print("Email sent successfully!")

except Exception as error:
    print("Error:", error)