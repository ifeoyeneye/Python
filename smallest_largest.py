smallest = None
largest = None

while True :
  sval = input("Enter a number: ")

  if sval == 'done' :
    break

  try :
    ival = int(sval)
  except :
    print("Invalid Input")
    continue

  if smallest is None :
      smallest = ival
  elif ival < smallest :
      smallest = ival

  if largest is None :
      largest = ival
  elif ival > largest :
      largest = ival

print("Maximum is", largest)
print("Minimim is", smallest)
