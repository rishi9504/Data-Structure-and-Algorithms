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

# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def stringCompression(s):
    # Check if the input string is None and raise a ValueError if it is
    if s is None:
        raise ValueError("Input string is None")

    # Initialize an empty string to store the compressed version
    compressed = ""

    # Initialize a counter to count occurrences of the current character
    count = 1

    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        # If the current character is the same as the previous one, increment the count
        if s[i] == s[i - 1]:
            count += 1
        else:
            # If the current character is different, append the previous character and its count to the compressed string
            compressed += s[i - 1] + str(count)
            # Reset the count for the new character
            count = 1

    # Append the last character and its count to the compressed string
    compressed += s[-1] + str(count)

    # Return the compressed string if it's shorter than the original, otherwise return the original string
    return compressed if len(compressed) < len(s) else s


print(stringCompression("aabcccccaaa"))

# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


def rotateMatrix(matrix):
    if matrix is None:
        raise ValueError("Input matrix is None")

    # Transpose the matrix
    # The transpose of a matrix is obtained by swapping rows with columns
    # For an element at position (i, j), we swap it with the element at (j, i)
    for i in range(len(matrix)):
        for j in range(i):
            # Swap elements at (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    # Reversing each row gives the effect of rotating the matrix 90 degrees
    # clockwise after transposing
    for i in range(len(matrix)):
        # Reverse the ith row
        matrix[i].reverse()

    return matrix


print(rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0


def zeroMatrix(matrix):
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column are set to 0
    """
    if matrix is None:
        raise ValueError("Input matrix is None")

    # Create sets to hold the rows and columns that contain 0s
    rows_with_zero = set()
    cols_with_zero = set()

    # Iterate through the matrix and keep track of the rows and columns that contain 0s
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == 0:
                rows_with_zero.add(row_index)
                cols_with_zero.add(col_index)

    # Iterate through the matrix again and set the elements of the rows and columns that
    # contain 0s to 0
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if row_index in rows_with_zero or col_index in cols_with_zero:
                matrix[row_index][col_index] = 0
    return matrix


# String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").


def stringRotation(s1, s2):
    """
    Checks if s2 is a rotation of s1 by calling isSubstring once.

    Given two strings, sl and s2, this function checks if s2 is a rotation of sl using only one
    call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

    Parameters
    ----------
    s1 : str
        The first string.
    s2 : str
        The second string.

    Returns
    -------
    bool
        True if s2 is a rotation of s1, False otherwise.
    """
    if s1 is None or s2 is None:
        raise ValueError("Input string is None")

    # Check if s2 is a substring of s1 concatenated with itself
    # If s2 is a rotation of s1, then it is a substring of s1 concatenated with itself
    return s1 in s2 + s2


print(stringRotation("waterbottle", "erbottlewat"))
