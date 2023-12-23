import sys
from reader_txt import file_reader_txt


def main():
    # if sys.argv != 2:
    #     sys.exit(1)
    
    # path = sys.argv[1]
    
    try:
        df = file_reader_txt('/home/joaomarcos/quotes/COTAHIST_A2022.TXT')
        
        return df
    except FileNotFoundError:
        # print(f'File {path} not found.')
        return None
    except Exception as error:
        print('An error occurred while reading file {error}')
        return None

if __name__ == '__main__':
    df = main()
    print(df)