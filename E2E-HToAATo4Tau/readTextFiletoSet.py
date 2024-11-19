import os

lines = []
with open('TTBar.txt','r') as file:
    lines = [line.strip() for line in file]   

print(len(lines))
linesSet = set(lines)
print(len(linesSet))
