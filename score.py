# code to compute score grade

i_score = input("Enter your score: ")

try:
  score = float(i_score)
except:
  print("The is not a number")
  quit()

if score > 1.0:
    print("The number you entered is out of range")
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')
