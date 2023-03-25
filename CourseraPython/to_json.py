from json import dumps
import functools
from solution import FileReader

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return dumps(func(*args, **kwargs))
    return wrapped


@to_json
def get_data():
    return {
        'data': 42
    }


#get_data()  # вернёт '{"data": 42}'

reader = FileReader('not_exist_file.txt')
text = reader.read()
print(text)

with open('some_file.txt', 'w') as file:
    file.write('some text')

reader = FileReader('some_file.txt')
text = reader.read()
print(text)
print(type(reader))
