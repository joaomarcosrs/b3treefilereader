from views import file_reader_txt


def main():
    file = file_reader_txt('/home/joaomarcos/projects/historical_quotes/COTAHIST_A2010.TXT')
    df = file[0]
    
    print(df)

if __name__ == '__main__':
    main()