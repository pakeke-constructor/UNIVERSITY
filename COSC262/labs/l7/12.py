"""An incomplete Huffman Coding module, for use in COSC262.
   Richard Lobb, April 2021.
"""
import re

HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)

    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__repr__(level + 1) + ',\n' +
            self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False

    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count)) # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')


class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label) # Add this leaf to the graph


def traverse(node, dicc=None, path=''):
    if dicc is None:
        dicc = dict( )
    
    if isinstance(node, Leaf):
        # then leaf node, push path onto stack
        dicc[node.char] = path
        return dicc
    else:
        traverse(node.left, dicc, path + '0')
        traverse(node.right, dicc, path + '1')
        return dicc


class HuffmanTree:
    """Operations on an entire Huffman coding tree.
    """
    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root

    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.
        """
        dicc = traverse(self.root)
        binary = []
        for char in text:
            binary.append(dicc[char])
        return ''.join(binary)

    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        cur = self.root
        shove = []
        for c in binary:
            if isinstance(cur, Leaf):
                shove.append(cur.char)
                cur = self.root
                if c == "0":
                    cur = cur.left
                elif c == "1":
                    cur = cur.right
            elif c == "0":
                cur = cur.left
            elif c == "1":
                cur = cur.right
        if isinstance(cur, Leaf):
            shove.append(cur.char)
        return ''.join(shove)

    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)

    def build_from_freqs(self, freqs):
        """Define self to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        pairs = [] # Leaf (freq, char)
        for key, val in freqs.items():
            pairs.append(Leaf(val, key))
        pairs.sort(key=lambda node: -node.count)
        while len(pairs) > 1:
            pairs.sort(key=lambda node: -node.count - ord())
            a,b = pairs.pop(), pairs.pop()
            if a.count == b.count:
                # sort alphabet, nodes go on the right if can
                if isinstance(b, Leaf) and isinstance(a, Leaf):
                    if a.char < b.char:
                        b,a = a,b
            pairs.append(Node(a,b))
        
        assert len(pairs) > 0, "hmmm"
        self.root = pairs.pop()

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)









# The example from the notes
freqs = {'a': 9,
         'b': 8,
         'c': 15,
         'd': 3,
         'e': 5,
         'f': 2}
tree = HuffmanTree()
tree.build_from_freqs(freqs)
print(tree)

print("\n\n")


freqs = {
   'p': 27,
   'q': 11,
   'r': 27,
   'u': 8,
   't': 5,
   's': 3}
tree = HuffmanTree()
tree.build_from_freqs(freqs)
print(tree)







