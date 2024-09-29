def brute_force_string_matching(text, pattern):
    """
    Return the index of the first occurrence of the given pattern in the given text,
    using the brute force string matching algorithm.

    Time Complexity: O(n*m)
    Space Complexity: O(1)

    Parameters:
        text (str): The string in which to search for the pattern.
        pattern (str): The pattern to search for in the text.

    Returns:
        int: The index of the first occurrence of the pattern in the text, or -1 if
            the pattern is not found.
    """
    for i in range(len(text) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1

text = "xyzabc123"
pattern = "abc"
index = brute_force_string_matching(text, pattern)
if index != -1:
    print(f"Pattern found at position {index}")
else:
    print("Pattern not found")


def robin_karp_string_matching(text, pattern):
    """
    Return the index of the first occurrence of the given pattern in the given text,
    using the Rabin-Karp string matching algorithm.

    Time Complexity: O(n+m)
    Space Complexity: O(1)

    Parameters:
        text (str): The string in which to search for the pattern.
        pattern (str): The pattern to search for in the text.

    Returns:
        int: The index of the first occurrence of the pattern in the text, or -1 if
            the pattern is not found.
    """
    d = 256  # base of the hash function
    q = 101  # modulus of the hash function
    n = len(text)
    m = len(pattern)
    pattern_hash = 0
    text_hash = 0
    h = 1

    # calculate h value, h = d^(m-1) % q
    for _ in range(m - 1):
        h = (h * d) % q

    # calculate the initial hash values for pattern and text
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # check for the characters one by one
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                return i

        # calculate the hash value for the next window
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if text_hash < 0:
                text_hash += q

    return -1

text = "xyzabc123"
pattern = "abc"
index = robin_karp_string_matching(text, pattern)
if index != -1:
    print(f"Pattern found at position {index}")
else:
    print("Pattern not found")

def string_matching_by_finite_automata(text, pattern):

    # The time complexity of the string matching by finite automata algorithm is O(n + m), where n is the length of the text and m is the length of the pattern. This is because the algorithm uses a finite automaton to recognize the pattern, which can be constructed in O(m) time.
    
    
    n = len(text)
    m = len(pattern)
    states = m + 1
    transitions = [[0] * 256 for _ in range(states)]

    # construct the transitions table
    for i in range(m):
        transitions[i][ord(pattern[i])] = i + 1

    # initialize the FA
    current_state = 0

    # read the characters of the text
    for i in range(n):
        current_state = transitions[current_state][ord(text[i])]
        if current_state == m:
            return i - m + 1

    return -1

text = "xyzabc123"
pattern = "bc"
index = string_matching_by_finite_automata(text, pattern)
if index != -1:
    print(f"Pattern found at position {index}")
else:
    print("Pattern not found")    



def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j
    return lps

def kmp_string_matching(text, pattern):
    """
    Return the index of the first occurrence of the given pattern in the given text,
    using the KMP string matching algorithm.

    Time Complexity: O(n + m)
    Space Complexity: O(m)

    Parameters:
        text (str): The string in which to search for the pattern.
        pattern (str): The pattern to search for in the text.

    Returns:
        int: The index of the first occurrence of the pattern in the text, or -1 if
            the pattern is not found.
    """
    
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

text = "xyzabc123"
pattern = "abc"
index = kmp_string_matching(text, pattern)
if index != -1:
    print(f"Pattern found at position {index}")
else:
    print("Pattern not found")