from functions import *
from time import time

print("Enter a sentence to check spelling: ")
words = input().lower().split()

start0 = time()

dictionary = get_dictionary("Dictionary.txt")

start1 = time()
wrong_words = search_items(dictionary, words)
end1 = time()

print_underlined(words, wrong_words)

start2 = time()
suggestions = get_suggestions(wrong_words, dictionary)
end2 = time()

print_suggestions(wrong_words, suggestions)

end0 = time()
print(f"\n\033[38;5;231mExecution time of getting missed words: {(end1 - start1) * 1000} ms")
print(f"Execution time of getting suggestions: {(end2 - start2)} sec")
print(f"Execution time of the whole program: {(end0 - start0)} sec\033[0m")