# code to calculate gross pay
i_hours = input("Enter the number of hours worked: ")
i_rate = input("Enter the hourly rate: ")

hours = float(i_hours)
rate = float(i_rate)
pay = 0

if hours <= 40:
  pay = hours * rate
else:
    diff = hours - 40
    pay = (40 * rate) + (diff * rate * 1.5)

print(pay)
