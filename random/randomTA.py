import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('random-matching-fe28e183d850.json', scope)
gs = gspread.authorize(credentials)
bs=gs.open("random allocation")
a = bs.get_worksheet(0)
b = bs.get_worksheet(1)
def randomize(j):
 while 1>0:
  y=0
  z=(a.cell(j,random.randint(2,len(a.row_values(j))))).value
  for k in range(2,j):
   if z==(b.cell(k,2)).value:
    y=1
  if y==0:
   return z
for i in range(2,len(a.col_values(1))+1):
 b.update_cell(i, 1, (a.cell(i,1)).value)
 b.update_cell(i, 2, randomize(i))
