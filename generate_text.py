import random
import random

class DataGenerator:
    def generate_data(self, length):
        characters = ['a', 'b', 'c', 'd', 'e']
        return ''.join(random.choice(characters) for _ in range(length))

    def create_file(self, filename, length):
        data = self.generate_data(length)
        with open(filename, 'w') as file:
            file.write(data)

# Generate files of lengths 1000, 10000, and 100000 characters
generator = DataGenerator()
generator.create_file("1000.txt", 1000)
generator.create_file("10000.txt", 10000)
generator.create_file("100000.txt", 100000)
