# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def uniqueString(s):
    for i in range(len(s) - 1):
        if s[i] in s[i + 1 :]:
            return False
    return True


# print(uniqueString("abcd"))

# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.


def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the
# "true" length of the string. (Note: If implementing in Java, please use a character array so that you
# can perform this operation in place.)


def urlify(s):
    if s is None:
        raise ValueError("Input string is None")
    return s.rstrip().replace(" ", "%20")


print(urlify("Mr John Smith    "))


# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
#  A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.


def palindromePermutation(s):
    """

    The basic idea here is to count the number of times each character appears.
    If the string is a permutation of a palindrome,
    then exactly one character should appear an odd number of times.
    If more than one character appears an odd number of times,
    then the string is not a permutation of a palindrome.

    :param s: The string to check if it is a palindrome permutation.
    :return: True if the string is a permutation of a palindrome, False otherwise.
    """
    if s is None:
        return False

    # Remove spaces and convert to lower case
    s = s.replace(" ", "").lower()
    char_count = {}

    # Count the number of times each character appears
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Count the number of odd counts
    odd_count = 0
    for count in char_count.values():
        if count % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                # If there are more than one odd counts, then the string is not a permutation of a palindrome
                return False

    # If there is exactly one odd count, then the string is a permutation of a palindrome
    return True


# print(palindromePermutation("Tact Coa"))


# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.


def oneAway(s: str, t: str) -> bool:
    # Check if the length of the first string is smaller than the second string
    # If true, recursively call the function with the arguments swapped to ensure the second string is shorter
    if len(s) < len(t):
        return oneAway(t, s)

    m, n = len(s), len(t)  # Get the lengths of the two strings

    # Check if the difference in lengths is greater than 1
    # If true, return False as more than one edit is required
    if m - n > 1:
        return False

    # Iterate through the characters of the shorter string
    for i, c in enumerate(t):
        # Check if the characters at the current index are different
        # If true, check for replacement or insertion/removal to make the strings match
        if c != s[i]:
            return s[i + 1 :] == t[i + 1 :] if m == n else s[i + 1 :] == t[i:]

    # If no differences found, check for the case where one character is inserted at the end of the longer string
    return m == n + 1


print(oneAway("pale", "ple"))
