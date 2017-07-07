# code to calculate gross pay
def computepay(hours, rate):
  if hours <= 40:
    pay = hours * rate
    return pay
  else:
    diff = hours - 40
    pay = (40 * rate) + (diff * rate * 1.5)
    return pay

i_hours = input("Enter the number of hours worked: ")

try:
  hours = float(i_hours)
except:
  print("Enter the number of hours worked in number format")
  quit()

i_rate = input("Enter the hourly rate: ")

try:
  rate = float(i_rate)
except:
  print("Enter the hourly rate in number format")
  quit()

print("Pay: ", computepay(hours, rate))
