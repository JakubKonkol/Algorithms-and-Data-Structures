# Jakub Konkol S24406

# tekst do zakodowania
text = "kocham asd"


# zliczanie wystapien znakow
def getUniqueCharacters(txt):
    chars = {}
    for char in txt:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


znaki = getUniqueCharacters(text)
# wypisanie znakow
print("\nZnaki:")
for i in znaki:
    print(i + ":", znaki[i])
print("\n Kody znaków:")

# struktura drzewa
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return str(self.value)

# stworzenie drzewa
def createTree(znaki):
    nodes = []
    for key, value in znaki.items():
        nodes.append(Node(key, value))
    while len(nodes) > 1:
        nodes = sorted(nodes)
        node1 = nodes[0]
        node2 = nodes[1]
        node3 = Node(None, node1.value + node2.value)
        node3.left = node1
        node3.right = node2
        nodes.remove(node1)
        nodes.remove(node2)
        nodes.append(node3)
    return nodes[0]

# stworzenie kodu dla kazdego znaku
def createCode(node, code, codes):
    if node is None:
        return
    if node.key is not None:
        codes[node.key] = code
        return
    createCode(node.left, code + "0", codes)
    createCode(node.right, code + "1", codes)
    return codes


# zakodowanie
def encode(txt, code):
    encoded = ""
    for char in txt:
        encoded += code[char]
    return encoded

tree = createTree(znaki)
codes = createCode(tree, "", {})
for i in codes:
    print(i + ":", codes[i])
print("\nWprowadzony tekst:", text)
zakodowany_text = encode(text, codes)
print("\nZakodowany tekst: "+zakodowany_text)

