import nltk
from scipy import stats
import random
nltk.download('punkt')

with open("poems.txt", "r", encoding='utf8') as f:
  corpus = f.read()
  
  
def token_maker(corpus):
  '''tokenizes poems'''

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

  for i in final_corpus:
    if i not in ss_list:
      all_words.append(i)
    
    else:
      continue
        
  return final_corpus, all_words
  
def ryhme_finder(last_word_of_the_line):
  '''finds ryhming words'''
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

  if len(rhyming_words) == 0:

    for words in all_words:
      for chars in range(len(words)):
        if words[-2:] in temp_temp_word:
          rhyming_words.append(words)
        break
    
  if len(rhyming_words) == 0:
    
    for words in all_words:
      for chars in range(len(words)):
        if words[-1:] in temp_temp_word:
          rhyming_words.append(words)
        break
  
  final_rhyming_words = []

  #if len(rhyming_words) == 0:
    #final_rhyming_words.append(last_word_of_the_line)
    
  for i in rhyming_words:
    if len(i) > 2:
      if i not in final_rhyming_words:
        final_rhyming_words.append(i)

  return(final_rhyming_words)

def normal_line_maker():
  ''' generater normal lines'''
  corner = random.choice(all_words) # need fixing
  no_initial = ["da", "de", "misin", "mısın", "müsün", "musun", "mi", "mu", "mı", "mü", "ve", "ile"] #expand the list

  if corner in no_initial:
    corner = random.choice(all_words)
  else:
    corner = corner

  current_word = ("<s>", corner)

  poem_trigrams = [((final_corpus[i], final_corpus[i+1]), final_corpus[i+2]) for i in range(len(final_corpus) - 2) ]
  poem_trigram_freq = nltk.FreqDist(poem_trigrams)
  poem_trigram_cfd = nltk.ConditionalFreqDist(poem_trigrams)
  poem_trigram_pbs = nltk.ConditionalProbDist(poem_trigram_cfd, nltk.MLEProbDist)

  line = []

  a = 10

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
  
 
 
def reverse_token_maker(corpus):
  '''tokenizes poems and reverses the list'''

  poem_lines = corpus.split("\n")
  poem_lines_updated = []

  for i in range(len(poem_lines)):
    if len(poem_lines[i]) > 0:
      poem_lines_updated.append(poem_lines[i])

  poem_lines_tokenized = [nltk.word_tokenize(s) for s in poem_lines_updated]

  cleaned_poem_lines_tokenized = []

  for i in poem_lines_tokenized: ###fix this for English
    for char in i:
      if len(char) > 1:
        cleaned_poem_lines_tokenized.append(i)
      break
  final_corpus = []
  for sentence in cleaned_poem_lines_tokenized:
    final_corpus += ["<s>"]+sentence+["</s>"]

  final_corpus = [i.lower() for i in final_corpus]
  final_corpus_dict = []



  ss_list = ["<s>", "</s>"]

  for i in final_corpus:
    if i not in ss_list:
      final_corpus_dict.append(i)
    
    else:
      continue
  
  reverse_final_corpus = []

  for i in reversed(final_corpus):
    reverse_final_corpus.append(i)

  return reverse_final_corpus
  
  
def reverse_line_maker(reverse_corner):
  ''' generates rhyming lines using the previous line'''

  rhyme_2_find = reverse_corner[-1]

  rhyming_list = ryhme_finder(rhyme_2_find)

  reverse_corner = random.choice(rhyming_list)


  reverse_current_word = ("</s>", reverse_corner)
  
  reverse_poem_trigrams = [( (reverse_final_corpus[i], reverse_final_corpus[i+1]), reverse_final_corpus[i+2]) for i in range(len(reverse_final_corpus) - 2) ]
  reverse_poem_trigram_freq = nltk.FreqDist(reverse_poem_trigrams)
  reverse_poem_trigram_cfd = nltk.ConditionalFreqDist(reverse_poem_trigrams)
  reverse_poem_trigram_pbs = nltk.ConditionalProbDist(reverse_poem_trigram_cfd, nltk.MLEProbDist)

  reverse_line = []
  reverse_line_final = []

  a = 10 ###input here

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
  
final_corpus = (token_maker(corpus))[0]
all_words = (token_maker(corpus))[1]
reverse_final_corpus = reverse_token_maker(corpus)



def UPPPoem():
  ''' creates poems based on the input'''
  
  final_poem = []
  first_stanza_list = []
  print("Enter a rhyming schema and stanza number. Avaible options: 'random','ABAB', 'AAAA', 'AABB' ")


  while True:
    try:
      rhyme, stanza_number = input().split()
    except:
      print("Wrong schema Boo!")
      continue
    break

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
  

  elif rhyme == "ABAB":

    for i in range(int(stanza_number)):

      for line in range(1):
        while True:
          try:
            final_poem.append(normal_line_maker())
          except IndexError:
            continue
          break
      
        temp_rhyme_one = final_poem[-1]

      for line in range(1):
        while True:
          try:
            final_poem.append(normal_line_maker())
          except IndexError:
            continue
          break  

        temp_rhyme_two = final_poem[-1]
      
      for line in range(1):
        while True:
          try:
            final_poem.append(reverse_line_maker(temp_rhyme_one))
          except IndexError:
            continue
          break   
      

        while True:
          try:
            final_poem.append(reverse_line_maker(temp_rhyme_two))
          except IndexError:
            continue
          break
      final_poem.append("\n")            
  
    stanza1  = ""
    temp_line = ""

    for line in final_poem:
      for word in line:
        temp_line += word + " "
      temp_line += "\n "
    poem = temp_line
  

  elif rhyme == "AAAA":

    for i in range(int(stanza_number)):

      for line in range(1):
        while True:
          try:
            final_poem.append(normal_line_maker())
          except IndexError:
            continue
          break

        temp_rhyme = final_poem[-1]

      for line in range(3):
        while True:
          try:
            final_poem.append(reverse_line_maker(temp_rhyme))
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
  

  elif rhyme == "AABB":

    for i in range(int(stanza_number)):
      for line in range(1):
        while True:
          try:
            final_poem.append(normal_line_maker())
          except IndexError:
            continue
          break

        temp_rhyme = final_poem[-1]

      for line in range(1):
        while True:
          try:
            final_poem.append(reverse_line_maker(temp_rhyme))
          except IndexError:
            continue
          break

      for line in range(1):
        while True:
          try:
            final_poem.append(normal_line_maker())
          except IndexError:
            continue
          break

        temp_rhyme = final_poem[-1]

      for line in range(1):
        while True:
          try:
            final_poem.append(reverse_line_maker(temp_rhyme))
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

  return poem
