'''
############
Do Now 5.02
############

1. In your Console
------------------
Type the following:

my_dictionary = {
'kittens': 'cute animals'
}
my_dictionary['kittens'] = 'p. cute'
print(my_dictionary)

In your Notebook
----------------
Respond to the following:

Write down what the 2nd line does.


2. In your Console
------------------
my_dictionary = {}
my_dictionary['puppies'] = 'baby dogs'
print(my_dictionary)

Continue in your Notebook
-------------------------
Respond to the following prompt
Write down what the 2nd line does.

3. In your Console
my_dictionary = {
'kittens': 'cute animals',
'puppies': 'baby dogs'
}
​
my_dictionary.pop('kittens')
print(my_dictionary)
my_dictionary.pop('bunnies')
my_dictionary.pop('bunnies', None)
Continue In your Notebook
Write down what the second line does.

What is different between my_dictionary.pop('bunnies') and my_dictionary.pop('bunnies', None)?
'''
# my_dictionary = {
# 'kittens': 'cute animals'
# }
# my_dictionary['kittens'] = 'p. cute'
# print(my_dictionary)

# my_dictionary = {}
# my_dictionary['puppies'] = 'baby dogs'
# print(my_dictionary)

my_dictionary = {
'kittens': 'cute animals',
'puppies': 'baby dogs'
}

my_dictionary.pop('kittens')
print(my_dictionary)
my_dictionary.pop('bunnies')
my_dictionary.pop('bunnies', None)

