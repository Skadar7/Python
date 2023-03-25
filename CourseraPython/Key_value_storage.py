import os
import argparse
from json import loads, dumps

storage_path = os.path.join(r"E:\coursera_round#2", 'storage.txt')

def is_empty_file():
    if os.path.exists(storage_path) and os.path.getsize(storage_path) > 0:
        with open(storage_path, 'r') as f:
            return loads(f.read())
    else:
        return {}


def write(key, value):
    file = is_empty_file()
    if key in file:
        file[key] += value
    else:
        file.setdefault(key, []).append(value)

    with open(storage_path, 'w') as f:
        f.write(dumps(file))


def read(key):
    with open(storage_path, 'r') as f:
        d = loads(f.read())
        if d:
            return ", ".join(d[key])
        else:
            return ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--val")
    args = parser.parse_args()

    if args.val and args.key:
        write(args.key, args.val)
    elif args.key:
        print(read(args.key))
    else:
        print("Error")
