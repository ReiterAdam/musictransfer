
from spotify import Spotify

def main():

    print('hello there')

    sp1 = Spotify()
    print(sp1.get_saved_songs())

if __name__ == '__main__':
    main()