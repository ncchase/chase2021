import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

gc = gspread.service_account(filename='client_secret.json')

sh = gc.open_by_key("18-Zpykkx5VGWbcIkjQw0sJEKmLFKE_7Rcj-Ri00_xsk")
mut = sh.worksheet("MUT")

dataframe = pd.DataFrame(mut.get_all_records())
