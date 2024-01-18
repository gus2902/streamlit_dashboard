import gspread

gc = gspread.service_account("product_manage.json")
sh = gc.open("product_list")

print(sh.sheet1.get('A1'))