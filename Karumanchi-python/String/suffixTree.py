# **Suffix Tree**

# A suffix tree is a data structure that represents all the suffixes of a given string. It is a compact representation of all possible suffixes of a string, and it can be used to efficiently search for all occurrences of a substring within a string.

# **Definition**

# A suffix tree is a tree-like data structure that represents all the suffixes of a given string. Each node in the tree corresponds to a substring of the string, and the edges of the tree represent the prefix-suffix relationship between the substrings. The root of the tree represents the empty string, and the leaves of the tree represent the suffixes of the string.

# **Example**

# Suppose we have the string "banana". The suffix tree for this string is shown below:

# ```
#         a
#        / \
#       /   \
#      /     \
#     b       n
#    / \     / \
#   /   \   /   \
#  /     \ /     \
# b      a  n      a
# ```

# In this example, the root of the tree represents the empty string, and the leaves of the tree represent the suffixes of the string. The edges of the tree represent the prefix-suffix relationship between the substrings. For example, the edge from the root to the node labeled "b" represents the prefix-suffix relationship between the empty string and the substring "banana". The edge from the node labeled "b" to the node labeled "a" represents the prefix-suffix relationship between the substring "banana" and the substring "anana".

# **Construction**

# There are several algorithms for constructing a suffix tree, including the Ukkonen algorithm and the Manber-Myers algorithm. The Ukkonen algorithm constructs the suffix tree in linear time, while the Manber-Myers algorithm constructs the suffix tree in linear time with a constant factor.

# **Properties**

# A suffix tree has several useful properties:

# 1. **Efficient substring search**: A suffix tree can be used to efficiently search for all occurrences of a substring within a string. This is because the tree represents all the suffixes of the string, and the edges of the tree represent the prefix-suffix relationship between the substrings.

# 2. **Efficient string matching**: A suffix tree can be used to efficiently match a pattern within a string. This is because the tree represents all the suffixes of the string, and the edges of the tree represent the prefix-suffix relationship between the substrings.

# 3. **Efficient longest common substring search**: A suffix tree can be used to efficiently find the longest common substring between two strings. This is because the tree represents all the suffixes of the strings, and the edges of the tree represent the prefix-suffix relationship between the substrings.

# 4. **Efficient pattern matching**: A suffix tree can be used to efficiently match a pattern within a string. This is because the tree represents all the suffixes of the string, and the edges of the tree represent the prefix-suffix relationship between the substrings.

# 5. **Efficient string compression**: A suffix tree can be used to efficiently compress a string by representing repeated substrings using a smaller representation. This is because the tree represents all the suffixes of the string, and the edges of the tree represent the prefix-suffix relationship between the substrings.

# 6. **Efficient string matching with wildcards**: A suffix tree can be used to efficiently match a pattern with wildcards within a string. This is because the tree represents all the suffixes of the string, and the edges of the tree represent the prefix-suffix relationship between the substrings.

# 7. **Efficient string matching with regular expressions**: A suffix tree can be used to efficiently match a regular expression within a string. This is because the tree represents all the suffixes of the string, and the edges of the tree represent the prefix-suffix relationship between the substrings.


class Node:
    def __init__(self, label):
        self.label = label
        self.children = {}
        self.suffix_link = None

def ukkonen(string):
    
    
    root = Node("")
    current_node = root
    for i in range(len(string)):
        current_char = string[i]
        if current_char not in current_node.children:
            new_node = Node(current_char)
            current_node.children[current_char] = new_node
            current_node = new_node
        else:
            current_node = current_node.children[current_char]
        if i > 0:
            update_suffix_link(current_node, current_char)
    return root

def update_suffix_link(node, char):
    if node.suffix_link is None:
        node.suffix_link = node.children[char]
    else:
        node.suffix_link = node.suffix_link.children[char]

string = "banana"
root = ukkonen(string)