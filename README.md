UPP - Untitled Poetry Project
A Turkish/English poem generator 

A poem generator that uses N-gram language model to generate lines. 
The generator also has a built-in rhyme function for Turkish poems.

An input of rhyme structure (AAAA, ABAB...) and a number input for the number
of stanzas wished to generate is given by the user then, using a trigram model, 
a poem of given rhyme structure and stanza length is generated by the code.
Initally cornerstone word to decide the theme of the poem was also planned to be 
included but the idea was later ditched.



Packages used: NLTK, SciPy, Python Random Module, re, string

Data:
A collection of Turkish poems and English epic books cleaned by hand and RegEx.
Corpora of names, surnames, city names etc. used as data for our generating tasks.
