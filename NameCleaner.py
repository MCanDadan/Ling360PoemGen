def TurkishNameCleaner():
  """Cleans the names file and creates a new one"""

f = open("clean_names.txt", "x")

with open("name_tally.txt", "r", encoding='utf8') as f:
  names = f.read()
for i in names:
  if i.isnumeric():
    names=names.replace(i,"")
    names=names.title()
    f = open("clean_names.txt", "w")
    f.write(names)
