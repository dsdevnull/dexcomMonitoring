from pydexcom import Dexcom
from dotenv import load_dotenv
import os

load_dotenv()
account_id = os.getenv("ACCOUNT_ID")
password = os.getenv("PASSWORD")

dexcom = Dexcom(account_id=account_id, password=password)

glucose_reading = dexcom.get_current_glucose_reading()

print(glucose_reading.json)
