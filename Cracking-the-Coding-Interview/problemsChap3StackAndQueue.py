# Three in One: Implement k stacks in one array
# https://www.geeksforgeeks.org/three-in-one-data-structure/


def ThreeInOne(arr, n, k):
    """
    Implement k stacks in one array

    Parameters:
        arr (list): The array to store the k stacks
        n (int): The size of the array
        k (int): The number of stacks

    Returns:
        None
    """
    if arr is None or n < k:
        raise ValueError(
            "Array size must be greater than or equal to the number of stacks"
        )
    if k == 0:
        return

    # Initialize the top of each stack
    top = [-1] * k

    # Push an element onto the top of a stack
    def push(stackNum, item):
        if top[stackNum] == len(arr) - 1:
            raise IndexError("Stack is full")
        top[stackNum] += 1
        arr[top[stackNum]] = item

    # Pop an element off the top of a stack
    def pop(stackNum):
        if top[stackNum] == -1:
            raise IndexError("Stack is empty")
        item = arr[top[stackNum]]
        top[stackNum] -= 1
        return item

    # Peek an element off the top of a stack
    def peek(stackNum):
        if top[stackNum] == -1:
            raise IndexError("Stack is empty")
        return arr[top[stackNum]]

    # Check if a stack is empty
    def isEmpty(stackNum):
        return top[stackNum] == -1

    return push, pop, peek, isEmpty


# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.


class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store the elements
        self.min_stack = []  # Auxiliary stack to store the minimum values

    def push(self, val):
        # Push the value onto the main stack
        self.stack.append(val)
        # Push the value onto the min stack if it's the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            # Pop the value from the main stack
            popped = self.stack.pop()
            # If the popped value is the same as the top of the min stack, pop the min stack as well
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def min(self):
        # Return the minimum element, which is at the top of the min stack
        if self.min_stack:
            return self.min_stack[-1]
        else:
            raise IndexError("Min operation cannot be performed on an empty stack")

    def top(self):
        # Return the top element of the main stack without removing it
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("Top operation cannot be performed on an empty stack")


# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).


def setOfStacks():
    """
    A SetOfStacks is a data structure that mimics a single stack but uses multiple stacks to
    store its elements. It creates a new stack when the previous one exceeds a certain capacity.
    """
    stacks = []  # List of stacks
    capacity = 3  # The number of elements each stack can hold


def push(item):
    """
    Push an element onto the SetOfStacks.

    If the last stack is full, a new stack is created. Otherwise, the element is added to the
    last stack.
    """
    if len(stacks) == 0 or len(stacks[-1]) == capacity:
        # Create a new stack
        stacks.append([item])
    else:
        # Add to the last stack
        stacks[-1].append(item)


def pop():
    """
    Pop an element off the SetOfStacks.

    If the SetOfStacks is empty, return None. Otherwise, pop off the last element of the last
    stack. If the last stack is empty after popping, remove it from the list of stacks.
    """
    if len(stacks) == 0:
        return None
    item = stacks[-1].pop()
    if len(stacks[-1]) == 0:
        stacks.pop()
    return item


if __name__ == "__main__":
    # Example usage
    stack_set = setOfStacks()
    for i in range(10):
        stack_set.push(i)
    print(stack_set.pop())  # 9
    print(stack_set.pop())  # 8
    print(stack_set.pop())  # 7
    print(stack_set.pop())  # 6
    print(stack_set.pop())  # 5
    print(stack_set.pop())  # 4
    print(stack_set.pop())  # 3
    print(stack_set.pop())  # 2
    print(stack_set.pop())  # 1
    print(stack_set.pop())  # 0
    print(stack_set.pop())  # None


# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2


# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.


def sort_stack(stack):
    """
    Sort a stack such that the smallest items are on the top.

    This function takes a stack as an argument, and returns a new stack with the same elements, but sorted in ascending order.

    The algorithm works as follows: we pop each element from the stack and push it onto a temporary stack. While pushing the element onto the temporary stack, we pop any elements from the temporary stack that are greater than the current element, and push them back onto the original stack. This effectively "inserts" the current element into its correct position in the sorted stack.

    Finally, we pop all the elements from the temporary stack and push them back onto the original stack, at which point the stack is sorted.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not stack:
        return
    temp_stack = []  # A temporary stack to store the elements
    while stack:
        temp = stack.pop()  # Pop the next element from the stack
        while (
            temp_stack and temp_stack[-1] > temp
        ):  # While the top element of the temporary stack is greater than the current element
            stack.append(
                temp_stack.pop()
            )  # Pop the top element from the temporary stack and push it back onto the original stack
        temp_stack.append(temp)  # Push the current element onto the temporary stack
    stack.extend(
        temp_stack
    )  # Pop all the elements from the temporary stack and push them back onto the original stack
    return stack


# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked list data structure.


class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.time = 0

    def enqueue(self, animal):
        self.time += 1
        if animal == "dog":
            self.dogs.append(self.time)
        else:
            self.cats.append(self.time)
        return self.time

    def dequeueAny(self):
        if len(self.dogs) == 0:
            return self.cats.pop(0)
        if len(self.cats) == 0:
            return self.dogs.pop(0)
        if self.dogs[0] < self.cats[0]:
            return self.dogs.pop(0)
        else:
            return self.cats.pop(0)

    def dequeueDog(self):
        return self.dogs.pop(0)

    def dequeueCat(self):
        return self.cats.pop(0)
