# A python file to send sms using Arkesel to users
# Importing libraries
import requests
import dotenv
import os

# Loading environment variables from .env file
dotenv.load_dotenv()

# Getting the API key from environment variable
api_key = os.getenv("ARKESEL_API")

# Function to send sms using an Array of phone numbers and a message
def send_sms(phone_numbers, message,  api_key):
    url = "https://sms.arkesel.com/api/v2/sms/send"
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json',
    }
    data = {
        "sender": "AI/ML Club",
        "recipients": phone_numbers,
        "message": message
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


# Array of numbers
phone_numbers = [
    "+233257581661",
    "+233240174827",
    "+233537789667",
    "0539795981",
    "+233 597637459",
    "0542775114",
    "+233209044665",
    "+233530238585",
    "0555295797",
    "0257139920",
    "+233531801880",
    "+233502803531",
    "+233534672221",
    "0594742792",
    "0549873371",
    "0500728657",
    "+233548419365",
    "+233546860241",
    "0546053893",
    "233531864204",
    "+233202824663",
    "+233531994414",
    "0591342621",
    "+233595974661",
    "+233248606683",
    "0545218364",
    "+233593660818",
    "+233535777279",
    "+233545214318",
    "0540743033",
    "+233596190247",
    "+233546763600",
    "+233533892842",
    "0547885060",
    "0245599539",
    "+233544792872",
    "+233241469846",
    "+233598268182",
    "+233201746502",
    "+233249487225",
    "+233597940209",
    "+233555129239",
    "0595326921",
    "0597758597",
    "+233559534678",
    "+233551062643",
    "+233536485099",
    "+233536523611",
    "+233243084819",
    "+233554563511",
    "+233592514482",
    "0549211089",
    "0248850090",
    "233248744464",
    "+233549420344",
    "+233551662314"
]

# Message to send
message = "Thanks for joining our AI/ML Club! Join our WhatsApp group for updates: https://bit.ly/4cFwhIK"

# Formatting the individual phone numbers to use +233 instead of 0 or 233
for i in range(len(phone_numbers)):
    if phone_numbers[i].startswith("0"):
        phone_numbers[i] = "+233" + phone_numbers[i][1:]
    elif phone_numbers[i].startswith("233"):
        phone_numbers[i] = "+" + phone_numbers[i]

# Sending the sms
response = send_sms(phone_numbers, message, api_key)
print(response)