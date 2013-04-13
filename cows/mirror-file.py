#!/usr/bin/python
# author: Mikael Vik
# mirror the contents of an ascii art file
# add mirrors if need be

import sys


replacements = [
  ('$thoughts', 'T'), 
  ('$tongue', 'UU'), 
  ('$eyes', 'EE')
]
mirrors = {
  "/": "\\", 
  "\\": "/",
  "(": ")",
  ")": "(", 
  "<": ">", 
  ">": "\<", 
  "{": "}",
  "}": "{"
}

def do_replace(line, set=True):
  for r in replacements: 
    if set:
      line = line.replace(*r)
    else:
      line = line.replace(*r[::-1])
  return line

infile = open(sys.argv[1], 'r')
stripped = [line.rstrip("\n") for line in infile.readlines()]
infile.close()

numchars = len(sys.argv) > 2 and int(sys.argv[2]) or 100

reverted = []
for line in stripped:
  if line.startswith(("#", "$", "EOC")):
    reverted.append(line)
    continue

  line = do_replace(line)
  if len(sys.argv) <= 3: print line
  line = line.ljust(numchars)[:numchars]

  reverted.append(''.join(
    [mirrors.has_key(c) and mirrors[c] or c for c in line[::-1]]
  ))

for line in reverted:
  if len(sys.argv) > 3: 
    line = do_replace(line, False)
  print line


