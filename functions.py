from difflib import SequenceMatcher
import os


def get_dictionary(file_name):
    
    try:
        file = open(file_name)
    except FileNotFoundError:
        return False
    
    dictionary = file.read().split()
    
    file.close()
    
    return dictionary


def search_item(alist, item):

    if not alist or len(alist) == 0:
        raise Exception("List is empty!")
    
    if item.isdigit():
        return 0
    
    start = 0
    end = len(alist) - 1
    
    while start <= end:
        
        mid = (start + end) // 2
        
        if item > alist[mid]:
            start = mid + 1
        elif item < alist[mid]:
            end = mid - 1
        else:
            return mid
            
    return -1
    

def search_items(alist, items):

    missed_items = []
    
    for item in items:
        if search_item(alist, item) == -1:
            missed_items.append(item)
            
    return missed_items
    

def bubble_sort(alist):
    
    n = len(alist)

    for i in range(3):
        for j in range(n - 1):
            if alist[j][0] > alist[j + 1][0]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                
    return alist[-3:]
    
    
def get_suggestions(words, dictionary):
    
    suggestions = {}
    s = SequenceMatcher()
    
    for word in words:
        
        suggestions[word] = []
        s.set_seq2(word)
        
        for x in dictionary:
            
            s.set_seq1(x)
            if s.real_quick_ratio() >= 0.65 and \
               s.quick_ratio() >= 0.65 and \
               s.ratio() >= 0.65:
                suggestions[word].append((s.ratio(), x))
        suggestions[word] = bubble_sort(suggestions[word])[::-1]
    
    return suggestions
    
    
def print_suggestions(wrong_words, suggestions):

    print("\033[1;32m######### Wrong words & Suggestions #########\033[0m\n")
    
    for word in wrong_words:
        if suggestions[word] == []:
            print(f"\033[1m{word}:\033[0m No suggestions!")
        else:
            print(f"\033[1m{word}:\033[0m ", end='')
            for w in range(2):
                print(f"\033[38;5;45m{suggestions[word][w][1]}, ", end='')
                
            print(f"{suggestions[word][2][1]}.\033[0;0m")


def print_underlined(words, wrong_words):
    
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    print("\033[38;5;231mEnter a sentence to check spelling: \033[0m")
    
    for word in words:
        if word in wrong_words:
            print(f"\033[4;31m{word}\033[0m", end=' ')
        else:
            print(word, end=' ')
    print("\n")