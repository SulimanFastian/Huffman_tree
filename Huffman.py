import heapq
import os

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

class HuffmanEncoding:
    def __init__(self, filename):
        self.filename = filename
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}

    def frequency_counter(self, text):
        frequency = {}
        for char in text:
            frequency[char] = frequency.get(char, 0) + 1
        return frequency

    def build_heap(self, frequency):
        for char, freq in frequency.items():
            node = Node(char, freq)
            heapq.heappush(self.heap, (freq, node))

    def build_tree(self):
        while len(self.heap) > 1:
            freq1, node1 = heapq.heappop(self.heap)
            freq2, node2 = heapq.heappop(self.heap)

            merged_node = Node(None, freq1 + freq2)
            merged_node.left = node1
            merged_node.right = node2

            heapq.heappush(self.heap, (freq1 + freq2, merged_node))

    def build_codes_helper(self, node, current_code):
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_codes[current_code] = node.char
            return

        self.build_codes_helper(node.left, current_code + '0')
        self.build_codes_helper(node.right, current_code + '1')

    def build_codes(self):
        root = heapq.heappop(self.heap)[1]
        self.build_codes_helper(root, '')

    def compress(self):
        with open(self.filename, 'r') as file:
            text = file.read()

        frequency = self.frequency_counter(text)
        self.build_heap(frequency)
        self.build_tree()
        self.build_codes()

        compressed_text = ''.join(self.codes[char] for char in text)

        # Write compressed data to binary file
        output_filename = os.path.splitext(self.filename)[0] + "_compressed.bin"
        with open(output_filename, 'wb') as output_file:
            output_file.write(bytearray(int(compressed_text[i:i+8], 2) for i in range(0, len(compressed_text), 8)))

# Usage
file_names = ["dataset/1000.txt", "dataset/10000.txt", "dataset/100000.txt"]

for file_name in file_names:
    huffman = HuffmanEncoding(file_name)
    huffman.compress()


for file_name in file_names:
    huffman = HuffmanEncoding(file_name)
    huffman.compress()
