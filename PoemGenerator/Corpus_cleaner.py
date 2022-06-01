import re
#upload a file and enter the name of the text file you want cleaned below
f = open("epics_all.txt", encoding="utf-8")
text=f.read()

f=open("numbers_cleaned.txt", "x", encoding="utf-8")

def NumClean(text):
  """Clear numbers"""  
  text_cleaned=re.sub("\d", "", text)
  return text_cleaned

def BraClean(text):
  """Clean Brackets"""
  text_cleaned=re.sub(r"\([^)]*\)|\[[^]]*\]|\{[^}]*\}", "", text)
  return text_cleaned

def LowerText(text):
  """Lowers the characters"""  
  for i in text:
    return text.lower()

f=open("numbers_cleaned.txt", "w", encoding="utf-8")
f.write(NumClean(text))

f=open("brackets_cleaned.txt", "x", encoding="utf-8")

f=open("brackets_cleaned.txt", "w", encoding="utf-8")
f.write(BraClean(NumClean(text)))

#name the final file below
f=open("epics_cleaned.txt", "x", encoding="utf-8")

f=open("epics_cleaned.txt", "w", encoding="utf-8")
f.write(LowerText(BraClean(NumClean(text))))
#now you can download the final file

f=open("epics_cleaned.txt")
f.read()
