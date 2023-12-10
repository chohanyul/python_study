import datetime

year = int(input("태어난 해는 언제인가요?"))
month = int(input("태어난 달는 언제인가요?"))
day = int(input("태어난 날는 언제인가요?"))

bday = datetime.datetime(year, month, day)

if bday.weekday() == 6:
  print("태어난 날은 일요일이군요")
if bday.weekday() == 0:
  print("태어난 날은 월요일이군요")
if bday.weekday() == 1:
  print("태어난 날은 화요일이군요")
if bday.weekday() == 2:
  print("태어난 날은 수요일이군요")
if bday.weekday() == 3:
  print("태어난 날은 목요일이군요")
if bday.weekday() == 4:
  print("태어난 날은 금요일이군요")
if bday.weekday() == 5:
  print("태어난 날은 토요일이군요")
