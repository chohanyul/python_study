import datetime

year = int(input("태어난 해는 언제인가요?"))
month = int(input("태어난 달는 언제인가요?"))
day = int(input("태어난 날는 언제인가요?"))

bday = datetime.datetime(year, month, day)

if bday.weekday() == 6:
  dow = "일"
if bday.weekday() == 0:
  dow = "월"
if bday.weekday() == 1:
  dow = "화"
if bday.weekday() == 2:
  dow = "수"
if bday.weekday() == 3:
  dow = "목"
if bday.weekday() == 4:
  dow = "금"
if bday.weekday() == 5:
  dow = "토"

print("태어난 날은", dow, "요일이군요")