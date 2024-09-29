# given an array of charecters give an algorithm for removing the duplicates using hashing

def removeDuplicates(arr):
    unique = []
    hs = set()
    for i in arr:
        if i not in hs:
            unique.append(i)
            hs.add(i)
    return unique

print(removeDuplicates([1,3,2,4,5,1,8,9,2]))

# given a string, give an algorithm for finding the first repeating letter in string.

def firstRepeatingLetter(string):
    hs = set()
    for i in string:
        if i in hs:
            return i
        else:
            hs.add(i)
    return -1

print(firstRepeatingLetter("abba"))