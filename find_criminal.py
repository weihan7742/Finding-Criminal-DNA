"""
Author: Ng Wei Han
"""

#%%
class Node:
    """
    A class representing a node which stores some payloads.
    """
    def __init__(self,data=None,size=5):
        """
        Initialization of a Node object.

        :param data: Data to be stored in the node as payload.
        :param size: Size of the array to be initialized

        Best/Worst Time Complexity: O(size)
        Total Space Complexity: O(size)
        Auxiliary Space Complexity: O(size)
        """
        self.link = [None]*size
        self.frequency = 0
        self.data = data
        self.child_char = None
class SequenceDatabase:

    """
    A class representing a database to store and query various different resistant
    gene sequences.
    """ 
    def __init__(self) -> None:
        """
        Initialization of a SequenceDatabase object.
        
        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        self.root = Node()

    def addSequence(self,s): 
        """
        Store a character into the database represented by the instance of SequenceDatabase.

        :param s: Single nonempty string of uppercase letters in uppercase [A-D]

        Best/Worst Time Complexity: O(len(s))
        s - The length of string
        Total Space Complexity: O(len(s))
        Auxiliary Space Complexity: O(len(s))
        """
        current = self.root
        word = self.insert_recur_aux(current,s,s)
        
        # Assign best child if not yet assigned
        if current.child_char is None:
            current.data = word.data
            current.child_char = s[0]
            current.frequency = word.frequency
        else:
            if s[0] <= current.child_char and word.frequency >= current.frequency: 
                current.frequency = word.frequency
                current.data = word.data
                current.child_char = s[0]
            elif word.frequency > current.frequency: 
                current.frequency = word.frequency
                current.data = word.data
                current.child_char = s[0]
        
    def insert_recur_aux(self,current,s,data):
        """
        Inserting a word into a Trie data structure.

        :param current: The current Node to be linked with
        :param s: Single nonempty string of uppercase letters in uppercase [A-D]
        :param data: Data to be used as a payload
        :return: Data of current Node

        Best/Worst Time Complexity: O(len(s))
        s - The length of the string
        Total Space Complexity: O(len(s))
        Auxiliary Space Complexity: O(len(s))

        """
        if len(s) == 0:
            # if no existing word
            if current.link[0] is None:
                current.link[0] = Node()
            current = current.link[0]
            current.data = data
            current.frequency += 1
            return current

        else: 
            index = ord(s[0]) - 65 + 1
            # if path exist
            if current.link[index] is not None: 
                current = current.link[index]
            # If path does not exist
            else: 
                current.link[index] = Node()
                current = current.link[index]

            new_word = self.insert_recur_aux(current,s[1:],data)

            # if first time assigned
            if current.child_char is None:
                current.data = new_word
                if len(s) <= 1: 
                    current.child_char = "$"
                else:
                    current.child_char = s[1]
            else: 
                if current.data.frequency < new_word.frequency:
                    current.data = new_word
                if current.data.frequency == new_word.frequency:
                    # Check lexicographically order
                    if len(s) > 1:
                        child = s[1]
                        if current.child_char >= child:
                            current.child_char = child
                            current.data = new_word
                    else:
                        current.child_char = "$"
                        current.data = new_word

            return current.data


    def query(self,q):
        """
        Find a string with a particular prefix with highest frequency and in least lexicographically ordering.
        
        :param q: Single string of uppercase letters in uppercase [A-D].
        :return: A string with q as a prefix, higher frequency and in least lexicographically ordering; None if doesn't exist.

        Best Time Complexity: O(1) - when string is found in the first node
        Worst Time Complexity: O(len(q))
        q - The length of string
        Total Space Complexity: O(len(q))
        Auxiliary Space Complexity: O(1)
        """
        # begin from root
        current = self.root

        if q == "":
            try:
                return current.data
            except AttributeError:
                return None

        # Go through the key 1 by 1
        for char in q: 
            index = ord(char) - 65 + 1
            # If path exist
            if current.link[index] is not None: 
                current = current.link[index]
            else: 
                return None

        # Reached desired node
        return current.data.data