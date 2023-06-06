filen = input("file:")
handle = open(filen)
for line in handle:
    line = line.rstrip
    numb = re.findall("[0-9]+")
    inumb = int(nunb)
    total += inumb
print(total)