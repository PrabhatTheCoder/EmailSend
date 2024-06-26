import os
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError

class Util:
    
    @staticmethod
    def send_email(data):
        subject = data["subject"]
        body = data['body']
        from_email = os.environ.get("EMAIL_USER")  # Use environment variable for from_email
        to_email = data.get("to_email")  # Use the provided to_email from data

        if not from_email:
            raise ValueError("EMAIL_USER environment variable is not set")

        if not to_email:
            raise ValueError("to_email is missing from data")

        try:
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=from_email,
                to=[to_email],  # Pass to_email as a list
            )
            email.send()  # Send the email
            print("Email Sent")

        except ValidationError as e:
            print(f"Email validation error: {e}")

        except Exception as e:
            print(f"Failed to send email: {e}")