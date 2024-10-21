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
    parser.add_argument('-c', '--bytes', action='store_true', help='Count bytes')
    parser.add_argument('-l', '--lines', action='store_true', help='Count lines')
    parser.add_argument('-w', '--words', action='store_true', help='Count words')
    parser.add_argument('-m', '--chars', action='store_true', help='Count characters')
    parser.add_argument('file', nargs='?', help='File to process')

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as file:
            content = file.read()
    else:
        content = sys.stdin.read()

    results = []
    if args.lines or (not args.bytes and not args.words and not args.chars):
        results.append(str(count_lines(content)))
    if args.words or (not args.bytes and not args.lines and not args.chars):
        results.append(str(count_words(content)))
    if args.chars or (not args.bytes and not args.lines and not args.words):
        results.append(str(count_characters(content)))
    if args.bytes:
        results.append(str(count_bytes(content)))

    if args.file:
        results.append(args.file)

    print(" ".join(results))

if __name__ == '__main__':
    main()
