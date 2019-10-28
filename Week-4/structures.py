'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists
the_list=['a','b','c','d','e']
# write a function that returns a list containing the first and the last element
# of "the_list". 
def first_and_last(the_list):
    return [the_list[0], the_list[-1]]
print(first_and_last(the_list)) #test

# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    return (the_list[beginning : end+1])[::-1]
print(part_reverse(the_list, 1, 3)) #test

# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    the_list.insert(index+1, the_list[index])
    the_list.insert(index+1, the_list[index])
    return the_list
print(repeat_at_index(the_list, 2)) #test



# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    reverse = ''
    for i in word:
        reverse = i+reverse
    if word == reverse :
        return 'Yes'
    else :
        return 'No'
print(palindrome_word('malayalam')) #test

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' #define punctuations

def palindrome_sentence(sentence):
    noPunct = ''
    for char in sentence :
        if char not in punctuations:
            noPunct = noPunct + char
    noMaj = noPunct.lower() #removes upper cases
    noSpaceMaj = noMaj.replace(' ', '')
    reverse = ''
    for i in noSpaceMaj :
        reverse = i+reverse
    if noSpaceMaj == reverse :
        return 'Yes'
    else :
        return 'No'
print(palindrome_sentence('Ma ya &&&lay aM!!!')) #test

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and there must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):
    sentenceOne = list(sentence1)
    sentenceTwo = list(sentence2)

    # First let's remove the potential start/end whitespaces
    
    while sentenceOne[0] == ' ':
        del sentenceOne[0]
    while sentenceOne[-1] == ' ':
        del sentenceOne[-1]

    while sentenceTwo[0] == ' ':
        del sentenceTwo[0]
    while sentenceTwo[-1] == ' ':
        del sentenceTwo[-1]

    # Now let's check the uppercase and punctuation

    conditionOneA = sentenceOne[0].isupper()
    conditionTwoA = sentenceTwo[0].isupper()
    punct = ['.','?','!']
    if sentenceOne[-1] == '.' :
        conditionOneB = True
    elif sentenceOne[-1] == '!' :
        conditionOneB = True
    elif sentenceOne[-1] == '?' :
        conditionOneB = True
    else :
        conditionOneB = False
    
    #if sentenceTwo[-1] in punct :
    #    conditionTwoB = True
    #else :
    #    conditionTwoB = False

    if sentenceTwo[-1] == '.' :
        conditionTwoB = True
    elif sentenceTwo[-1] == '!' :
        conditionTwoB = True
    elif sentenceTwo[-1] == '?' :
        conditionTwoB = True
    else :
        conditionTwoB = False

    if conditionOneA and conditionOneB != True :
        raise ValueError
    if conditionTwoA and conditionTwoB != True :
        raise ValueError
    
    final1 = ''.join(map(str, sentenceOne)) 
    final2 = ''.join(map(str, sentenceTwo))

    return final1 + ' ' + final2
print(concatenate_sentences('    This is a beautiful day.   ', '   Yeah I know right !   ')) #Test


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary.keys() :
        return True
    if key not in dictionary.keys() :
        return False
print(index_exists({'cat': 'Romeo', 'dog': 'Barg'}, 'mom')) #test

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values() :
        return True
    if value not in dictionary.values() :
        return False

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    dictionary1.update(dictionary2)
    return dictionary1
print(merge_dictionaries({'dog':'Barg'},{'cat':'Mina' , 'chicken':'Coco'}))