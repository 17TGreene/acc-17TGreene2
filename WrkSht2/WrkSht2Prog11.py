daysOfWeek = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
date = input("Please enter your date in format day/month/year.")
#dd/mm/yyyy
#0123456789
dd = int(date[0:2])
mm = int(date[3:5])
if mm < 3:
    mm += 12

if mm > 12:
    y = int(date[8:10]) - 1
else:
    y = int(date[8:10])
    
c = int(date[6:8])

print(dd,mm,y,c)

w = (dd + ((13*(mm+1))//5) + y + (y//4) + (c//4) -(2*c)) % 7
print("This date was/is/will be a "+daysOfWeek[w]+".")