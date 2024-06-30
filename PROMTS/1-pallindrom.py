
# function pallindrom

def pallindrom(n):
    if n == n[::-1]:
        return True
    else:
        return False
    
    
    
def pallindrom(n):
    return n == n[::-1]

# create docstring for the function


def pallindrom(n):
    """
    Check if a number is a pallindrom
    """
    return n == n[::-1]


# create annotation for the function

def pallindrom(n: str) -> bool:
    """
    Check if a number is a pallindrom
    """
    return n == n[::-1]       


# function pallindrom by for

# test function pallindom by asserting the result
assert pallindrom("racecar") == True
assert pallindrom("hello") == False
assert pallindrom(121) == True
assert pallindrom(123) == False
assert pallindrom("nursesrun") == True

# test function pallindrom by using the doctest module
import doctest
doctest.testmod()

# test function pallindrom by using the unittest module
import unittest
class TestPallindrom(unittest.TestCase):
    def test_pallindrom(self):
        self.assertTrue(pallindrom("racecar"))
        self.assertFalse(pallindrom("hello"))
        self.assertTrue(pallindrom(121))
        self.assertFalse(pallindrom(123))
        self.assertTrue(pallindrom("nursesrun"))
        


def get_anagram(word):
    """
    Get all anagrams of a word
    """
    if len(word) == 1:
        return [word]
    else:
        anagrams = []
        for i in range(len(word)):
            for anagram in get_anagram(word[:i] + word[i+1:]):
                anagrams.append(word[i] + anagram)
        return anagrams
    
    
# anagram
def anagram(word1, word2):
    """
    Check if two words are anagrams
    """
    return sorted(word1) == sorted(word2)

'''

'''
# test function anagram by asserting the result
assert anagram("race", "care") == True 
assert anagram("hello", "world") == False
assert anagram("listen", "silent") == True
assert anagram("hello", "world") == False
assert anagram("listen", "silent") == True
assert anagram("elephant", "tiger") == False
assert anagram("dog", "god") == True
assert anagram("dog", "cat") == False
assert anagram("dog", "god") == True

# anagram by set
def anagram(word1, word2):
    """
    Check if two words are anagrams
    """
    return set(word1) == set(word2)

'''

'''
# test function anagram by using the doctest module
import doctest  
doctest.testmod()
'''
'''
# test function anagram by using the unittest module
import unittest
class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(anagram("race", "care"))
        self.assertFalse(anagram("hello", "world"))
        self.assertTrue(anagram("listen", "silent"))
        self.assertFalse(anagram("hello", "world"))
        self.assertTrue(anagram("listen", "silent"))
        self.assertFalse(anagram("elephant", "tiger"))
        self.assertTrue(anagram("dog", "god"))
        self.assertFalse(anagram("dog", "cat"))
        self.assertTrue(anagram("dog", "god"))
        self.assertFalse(anagram("dog", "cat"))
        


