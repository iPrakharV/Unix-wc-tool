import argparse

def count_bytes(file_content):
    return len(file_content.encode('utf-8'))

def count_lines(file_content):
    return len(file_content.splitlines())

def count_words(file_content):
    return len(file_content.split())

def count_characters(file_content):
    return len(file_content)

def main():
    parser = argparse.ArgumentParser(description='Custom wc tool in Python')
    parser.add_argument('-c', action='store_true', help='Count bytes')
    parser.add_argument('-l', action='store_true', help='Count lines')
    parser.add_argument('-w', action='store_true', help='Count words')
    parser.add_argument('-m', action='store_true', help='Count characters')
    parser.add_argument('file', help='File to process')

    args = parser.parse_args()

    with open(args.file, 'r') as file:
        content = file.read()

    if args.c:
        print(f'Bytes: {count_bytes(content)}')
    if args.l:
        print(f'Lines: {count_lines(content)}')
    if args.w:
        print(f'Words: {count_words(content)}')
    if args.m:
        print(f'Characters: {count_characters(content)}')

if __name__ == '__main__':
    main()