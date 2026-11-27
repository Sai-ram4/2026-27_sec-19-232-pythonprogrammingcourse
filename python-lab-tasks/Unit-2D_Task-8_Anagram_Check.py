# Unit 2D Task 8 - anagram check
# two strings are anagrams if they have the same letters, so sorting both gives the same list

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")
