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

f=open("clean_names.txt", 'r', encoding="utf-8")
print(f.read())
# Used this function only once to put the names in the desired format.

f=open("clean_surnames.txt", 'r', encoding="utf-8")
print(f.read())

import random
import re
def TurkishPoetGenerator():
  """Generates a Turkish poet name"""

  f=open("clean_names.txt", "r", encoding="utf-8")
  names=f.read()
  names=names.split(" \n")

  f=open("clean_surnames.txt", "r", encoding='utf8')
  surnames = f.read()
  surnames=surnames.split(" \n")

  poet=f"""{random.choice(names)} {random.choice(surnames)} siz degerli siirseverlere son eserini sunmaktan mutluluk duyar..."""
  return poet

TurkishPoetGenerator()

def EpicPoetSays():
  """Generates an epic poet name"""
  f=open("epic_poet_names.txt", "r", encoding="utf-8")
  names=f.read()
  names=names.split("\n")

  f=open("epic_cities.txt", "r", encoding="utf-8")
  cities=f.read()
  cities=cities.split("\n")

  f=open("verbsing.txt", "r", encoding="utf-8")
  verbs=f.read()
  verbs=verbs.title()
  verbs=re.findall("[\w]+ing", verbs)

  poet=f"""Behold! I, {random.choice(names)} {random.choice(names)} of {random.choice(cities)}, presenteth thee this most wondrous piece of poetry: 'The {random.choice(verbs)} of {random.choice(names)}' """
  return poet

EpicPoetSays()
