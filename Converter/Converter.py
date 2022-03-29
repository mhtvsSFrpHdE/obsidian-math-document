import sys

if len(sys.argv) == 1:
	print("No file to open")
	sys.exit()

filePath = sys.argv[1]

# https://stackoverflow.com/questions/13089234/replacing-text-in-a-file-with-python

replacements = {'openFont':'<font', 'closeFont':'>', 'endFont':'</font>'}

lines = []

with open(filePath, encoding="utf-8") as infile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        lines.append(line)
with open(filePath, 'w', encoding="utf-8") as outfile:
    for line in lines:
        outfile.write(line)