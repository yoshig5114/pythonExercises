import re
total = 0
filen = input("file:")
handle = open(filen)
for line in handle:
    numbs = re.findall("[0-9]+",line)
    if len(numbs) < 1:
        continue
    for numb in numbs:
        inumb = int(numb)
        total += inumb
print(total)