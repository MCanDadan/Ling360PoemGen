import nltk
from scipy import stats
import random
import re
nltk.download('punkt')

with open("epics_cleaned.txt", "r", encoding='utf8') as f:
  corpus = f.read()
  
def token_maker(corpus):
  '''takes a corpus as an inputs, returns tokenized, and reverse tokenized forms, with addition of a list of unique words in the said corpus'''

  poem_lines = corpus.split("\n")
  poem_lines_updated = []

  for i in range(len(poem_lines)):
    if len(poem_lines[i]) > 0:
      poem_lines_updated.append(poem_lines[i])

  poem_lines_tokenized = [nltk.word_tokenize(s) for s in poem_lines_updated]

  cleaned_poem_lines_tokenized = []

  for i in poem_lines_tokenized:
    for char in i:
      if len(char) > 1:
        cleaned_poem_lines_tokenized.append(i)
      break
  final_corpus = []
  for sentence in cleaned_poem_lines_tokenized:
    final_corpus += ["<s>"]+sentence+["</s>"]

  final_corpus = [i.lower() for i in final_corpus]
  all_words = []



  ss_list = ["<s>", "</s>"]

  for i in final_corpus:   #this part removes the "<s>" and "</s>" from the list.
    if i not in ss_list:
        all_words.append(i)
    else:
      continue
    
  all_words_set = set(all_words)    # we convert to a set to get unique values.
  all_words_final = list(all_words_set) # and convert back to a list.

  reverse_final_corpus = final_corpus[::-1] # reverses the corpus.


  return final_corpus, all_words_final, reverse_final_corpus


def ryhme_finder(last_word_of_the_line):
  '''finds ryhming words based on the last word of the previous line'''

  last_three_chars = []
  for i in last_word_of_the_line:
    last_three_chars.append(i)

  temp_word = last_three_chars[-3:]
  temp_temp_word = ("".join(temp_word))

  rhyming_words = []

  for words in all_words:
    for chars in range(len(words)):
      if words[-3:] in temp_temp_word:
        rhyming_words.append(words)
      break

  
  final_rhyming_words = []

  
  for i in rhyming_words:
    if len(i) > 2:
      if i not in final_rhyming_words:
        final_rhyming_words.append(i)
  
  if len(final_rhyming_words) == 0:   # if it cannot find a rhyming word, it uses the same word.
    final_rhyming_words.append(last_word_of_the_line)

  return(final_rhyming_words)


#this part assigns values to variables
temp = token_maker(corpus)
final_corpus = temp[0]
all_words = temp[1]
reverse_final_corpus = temp[2]

def normal_poem_trigrams():
  '''calculates the conditional probability distribution using the normal tokenized corpus '''
   
  poem_trigrams = [((final_corpus[i], final_corpus[i+1]), final_corpus[i+2]) for i in range(len(final_corpus) - 2) ]
  poem_trigram_cfd = nltk.ConditionalFreqDist(poem_trigrams)
  poem_trigram_pbs = nltk.ConditionalProbDist(poem_trigram_cfd, nltk.MLEProbDist)

  return poem_trigram_pbs


def reverse_poem_trigrams():
  '''calculates the conditional probability distribution using the reversed tokenized corpus '''
  reverse_poem_trigrams = [((reverse_final_corpus[i], reverse_final_corpus[i+1]), reverse_final_corpus[i+2]) for i in range(len(reverse_final_corpus) - 2) ]
  reverse_poem_trigram_cfd = nltk.ConditionalFreqDist(reverse_poem_trigrams)
  reverse_poem_trigram_pbs = nltk.ConditionalProbDist(reverse_poem_trigram_cfd, nltk.MLEProbDist)

  return reverse_poem_trigram_pbs


#this part assigns values to variables
poem_trigram_pbs = normal_poem_trigrams()
reverse_poem_trigram_pbs = reverse_poem_trigrams()


def normal_line_maker():
  ''' generater normal lines'''
  
  corner = random.choice(all_words)

  current_word = ("<s>", corner)

  line = []

  a = 15

  for i in range(a):
    probable_words = list(poem_trigram_pbs[current_word].samples())
    word_probabilities = [poem_trigram_pbs[current_word].prob(word) for word in probable_words]
    result = stats.multinomial.rvs(1,word_probabilities)
    index_of_probable_word = list(result).index(1)
    current_word = (current_word[1], probable_words[index_of_probable_word])
    line.append(current_word[1])

  ultimate_output = []
  ss_list = ["<s>", "</s>"]

  for i in line:
    if i not in ss_list:
      ultimate_output.append(i)
    
    else:
      continue
  return ultimate_output


def reverse_line_maker(reverse_corner):
  ''' generates rhyming lines using the previous line'''

  rhyme_2_find = reverse_corner[-1]

  rhyming_list = ryhme_finder(rhyme_2_find)

  reverse_corner = random.choice(rhyming_list)


  reverse_current_word = ("</s>", reverse_corner)
  


  reverse_line = []
  reverse_line_final = []

  a = 15

  for i in range(a):
    reverse_probable_words = list(reverse_poem_trigram_pbs[reverse_current_word].samples())
    reverse_word_probabilities = [reverse_poem_trigram_pbs[reverse_current_word].prob(word) for word in reverse_probable_words]
    reverse_result = stats.multinomial.rvs(1,reverse_word_probabilities)
    reverse_index_of_probable_word = list(reverse_result).index(1)
    reverse_current_word = (reverse_current_word[1], reverse_probable_words[reverse_index_of_probable_word])
    reverse_line.append(reverse_current_word[0])

  reverse_ultimate_output = []
  ss_list = ["<s>", "</s>"]

  for i in reverse_line:
    if i not in ss_list:
      reverse_ultimate_output.append(i)
    
    else:
      continue
      
  reverse_ultimate_output.reverse()
  return reverse_ultimate_output



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


def UPPEpic():
  ''' creates poems based on the input'''
  
  final_poem = [" ",]
  first_stanza_list = []
  print("Enter a rhyming schema and stanza number. Avaible options: 'random'")


  while True:
    try:
      rhyme, stanza_number = input().split()
    except:
      print("Wrong schema Boo!")
      continue
    break
 
  poet_name = EpicPoetSays()
  poet_name_str = str(poet_name)
  poet_name_str += " \n"

  if rhyme == "random":

    for i in range(int(stanza_number)):
    
      for line in range(4):
        while True:
          try:
            final_poem.append(normal_line_maker())
          except IndexError:
            continue
          break
      final_poem.append("\n")

    stanza1 = ""
    temp_line = ""

    for line in final_poem:
      for word in line:
        temp_line += word + " "
      temp_line += "\n "
    poem = temp_line
  
  
  poem = poet_name_str + poem 
  return poem

print(UPPEpic())
