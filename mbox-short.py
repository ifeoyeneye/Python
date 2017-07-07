# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:
  fh = open(fname)
except:
  print("Invalid file name")
  quit()

count = 0
tot = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        spos = line.find('0')
        fval = float(line[spos:])
        count = count + 1
        tot = tot + fval
    else:
        continue

print("Average spam confidence:", tot/count)
