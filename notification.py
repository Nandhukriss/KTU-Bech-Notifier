import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


def send_message(message_body):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    # Use your Twilio number from the environment variable
    twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
    to_number = os.getenv('TO_PHONE_NUMBER')

    try:
        message = client.messages.create(
            from_=twilio_number,
            to=to_number,
            body=message_body
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'Failed to send message: {str(e)}')