import random

cChoice = random.choice("SPR")

name = input("이름이 무엇인가요?: ")
print("반갑습니다 ",name, "님. 그럼 저와 가위바위보 게임을 할까요? ")

print("가위 바위 보?")
uChoice = input("S(가위) R(바위) P(보) 중 하나를 고르세요: ").upper().strip()

print("여러분: ", uChoice)
print("컴퓨터: ", cChoice)

if name == "Ben":
  if uChoice == "R":
    cChoice = "S"
  if uChoice == "P":
    cChoice = "R"
  if uChoice == "S":
    cChoice = "P"

if cChoice == uChoice:
  print("무승부입니다!")
  
elif uChoice == "R" and cChoice == "P":
  print("여러분이 고른 것은 바위(R), 컴퓨터가 고른 것은 보(P)."
        "여러분이 졌네요")
  
elif uChoice == "P" and cChoice == "R":
  print("여러분이 고른 것은 보(P), 컴퓨터가 고른 것은 바위(R)."
        "여러분이 이겼네요")

elif uChoice == "R" and cChoice == "S":
  print("여러분이 고른 것은 바위(R), 컴퓨터가 고른 것은 가위(S)."
        "여러분이 이겼네요")
  
elif uChoice == "S" and cChoice == "R":
  print("여러분이 고른 것은 가위(S), 컴퓨터가 고른 것은 바위(R)."
        "여러분이 졌네요")

elif uChoice == "S" and cChoice == "P":
  print("여러분이 고른 것은 가위(S), 컴퓨터가 고른 것은보(P)."
        "여러분이 이겼네요")

elif uChoice == "P" and cChoice == "S":
  print("여러분이 고른 것은 보(P), 컴퓨터가 고른 것은 가위(S)."
        "여러분이 졌네요")
  
else:
  print("게임 설명을 또 듣는 일은 지겨울 겁니다. 그렇죠?")