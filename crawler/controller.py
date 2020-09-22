import sys
sys.path.insert(0, '/Users/odakyeong/SbaProjects')

from crawler.entity import Entity
from crawler.service import Service

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

if __name__ == '__main__':
    ctrl = Controller()
    service = ctrl.service
    service.save_webtoon_csv('https://comic.naver.com/webtoon/weekday.nhn')
    service.save_movie_csv('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')