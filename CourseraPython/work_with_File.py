import tempfile
import os.path


class File:

    def __init__(self, name_file):
        self.__name_file = name_file
        self.__file = os.path.join(tempfile.gettempdir(), name_file + '.txt')

    def read(self):
        with open(self.__file, 'r') as file:
            return file.read()

    def write(self, text):
        with open(self.__file, 'w') as file:
            file.write(text)
            return len(text)

    def __add__(self, other):
        self.write(self.read() + '\n' + other.read())
        return File(self.__name_file)

    def __str__(self):
        return self.__file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.__file, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    raise StopIteration
                return line


obj_1 = File('44')
print(obj_1)
obj_2 = File('444')
print(obj_2)
print(obj_1.write('qwe'))
print(obj_2.read())
print(obj_2.write('asd'))
print(obj_2.read())
new_obj = obj_1 + obj_2
print(isinstance(new_obj, File))
print(new_obj)
#for line in new_obj:
    #print(ascii(line))

new_path_to_file = str(new_obj)
os.path.exists(new_path_to_file)
file_obj_3 = File(new_path_to_file)
print(file_obj_3)
