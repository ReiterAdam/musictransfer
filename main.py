import logging
from spotify import Spotify
from deezer import Deezer

def main():

    print('hello there')
    print('General Kenobi')

    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filemode='w',
                        level=logging.DEBUG,
                        format=LOG_FORMAT,
                        filename=".\\logs\\log1.log")

    logger = logging.getLogger()

    logger.info('Start')

    d1 = Deezer()
    d1.get_saved_songs()
    
    
if __name__ == '__main__':
    main()
