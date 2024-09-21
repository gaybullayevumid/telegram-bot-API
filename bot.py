import requests

BOT_TOKEN = '7714575462:AAE88sVMe9_NsfZ1fBSEeOjqCSy1iOe2Lwo'
URL = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'

# Function to send a message requesting phone number
def request_phone_number(chat_id):
    phone_request_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {
        "chat_id": chat_id,
        "text": "Please share your phone number:",
        "reply_markup": {
            "keyboard": [
                [
                    {
                        "text": "Share phone number",
                        "request_contact": True
                    }
                ]
            ],
            "one_time_keyboard": True,
            "resize_keyboard": True
        }
    }
    response = requests.post(phone_request_url, json=data)
    print(f"Phone number request sent: {response.json()}")

# Function to send a greeting message when the /start command is received
def send_welcome_message(chat_id):
    welcome_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {
        "chat_id": chat_id,
        "text": "Welcome to the bot! I'm here to help you. You can share your phone number by pressing the button below."
    }
    response = requests.post(welcome_url, json=data)
    print(f"Welcome message sent: {response.json()}")

# Fetch the latest updates (messages or contacts shared)
response = requests.get(URL)
updates = response.json()

if updates['ok']:
    for update in updates['result']:
        # Get message info
        message = update.get('message')
        if message:
            user = message.get('from')
            chat_id = message['chat']['id']
            text = message.get('text', '')

            # Handle /start command
            if text == '/start':
                send_welcome_message(chat_id)
                continue  # Skip to the next update, as we don't want to process further info on /start

            # Get User ID and Username
            user_id = user['id']
            username = user.get('username', 'No username')

            print(f"User ID: {user_id}")
            print(f"Username: {username}")

            # Check for profile photo
            profile_photo_url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUserProfilePhotos?user_id={user_id}'
            photo_response = requests.get(profile_photo_url).json()

            if photo_response['result']['total_count'] > 0:
                photo_file_id = photo_response['result']['photos'][0][0]['file_id']
                file_info_url = f'https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={photo_file_id}'
                file_info_response = requests.get(file_info_url).json()
                file_path = file_info_response['result']['file_path']
                download_url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}'
                print(f"Profile photo URL: {download_url}")
            else:
                print("No profile photo available")

            # Check if the user has shared contact info (phone number)
            if 'contact' in message:
                phone_number = message['contact']['phone_number']
                print(f"Phone Number: {phone_number}")
            else:
                # If no phone number is shared yet, request it
                request_phone_number(chat_id)
        else:
            print("No message found.")
else:
    print("No updates found.")