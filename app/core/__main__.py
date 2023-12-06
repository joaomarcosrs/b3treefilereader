import os
from views import file_reader

basedir = os.path.abspath(os.path.dirname(__file__))

def main():
    file_reader()

if __name__ == '__main__':
    main()