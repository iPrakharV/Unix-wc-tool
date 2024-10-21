import argparse

def count_bytes(file):
    return len(file.encode('utf-8'))

def main():
    parser = argparse.ArgumentParser(description='Unix WC Tool')
    parser.add_argument('-c', action='store_true', help='Count Bytes')
    parser.add_argument('file', help='File to process')