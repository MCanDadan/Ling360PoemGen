def TurkishSurnameCleaner():
  """Cleans the surnames file and creates a new one"""

f = open("clean_surnames.txt", "x")

with open("surname_tally.txt", "r", encoding='utf8') as f:
  surnames = f.read()
for i in surnames:
  if i.isnumeric():
    surnames=surnames.replace(i,"")
    surnames=surnames.title()
    f = open("clean_surnames.txt", "w")
    f.write(surnames)
