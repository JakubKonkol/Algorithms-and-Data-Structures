# Jakub Konkol S24406
import os
# tekst do zakodowania
with open("tekst.txt", "r") as file:
    text = file.read()
# text = "kocham asd"


# zliczanie wystapien znakow
def getUniqueCharacters(txt):
    chars = {}
    for char in txt:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


znakiZ = getUniqueCharacters(text)
# wypisanie znakow
print("\nZnaki:")
for i in znakiZ:
    print(i + ":", znakiZ[i])
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
def heapSort(array):
    n = len(array)
    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array

def heapify(array, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1
    if left < n and array[i] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)
# stworzenie drzewa
def createTree(znaki):
    nodes = []
    for key, value in znaki.items():
        nodes.append(Node(key, value))
    while len(nodes) > 1:
        nodes = heapSort(nodes)
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

tree = createTree(znakiZ)
codes = createCode(tree, "", {})
for i in codes:
    print(i + ":", codes[i])
print("\nWprowadzony tekst:", text)

zakodowany_text = encode(text, codes)

print("\nZakodowany tekst: "+zakodowany_text)
# zapis zakodowanego tekstu do pliku jako kod binarny
with open("zakodowany", "wb") as f:
    f.write(int(zakodowany_text, 2).to_bytes(len(zakodowany_text) // 8, byteorder='big'))

# porownanie wielkosci plikow przed i po zakodowaniu
print("\nRozmiar originalnego pliku tekstowego: ", os.path.getsize("tekst.txt"), "B")
print("Rozmiar pliku zakodowanego: ", os.path.getsize("zakodowany"), "B")
