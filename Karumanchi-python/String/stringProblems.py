# give an algorithm for reversing a string

def reverseString(S):
    return S[::-1]



# give an algorithm for finding the length of the longest palindromic substring

def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    max_length = 0
    start = 0
    for i in range(n):
        dp[i][i] = True
        max_length = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        start = i
    return s[start:start + max_length]

    # give an algorithm for reversing words in a sentence


def reverse_sentence(sentence):
    """
    Reverse the words in the given sentence.

    Parameters:
        sentence (str): The sentence to reverse.

    Returns:
        str: The reversed sentence.
    """
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

print (reverse_sentence("hello world this is a wild fire"))