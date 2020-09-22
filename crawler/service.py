import sys
sys.path.insert(0, '/Users/odakyeong/SbaProjects')

import os, shutil
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame
import pandas as pd
from crawler.entity import Entity

class Service:
    def __init__(self):
        self.entity = Entity()
        
    def bugs_music(self):
        pass

    # url 을 받아서 soup 초기화
    def get_url(self, url):
        myparser = 'html.parser'
        response = urlopen(url)
        self.soup = BeautifulSoup(response, myparser)
        return self.soup

    # 각 이미지를 요일별 폴더에
    def save_webtoon_img(self, mysrc, myweekday, mytitle):
        weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일', 'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}
        myfolder = '/Users/odakyeong/SbaProjects/crawler/img'
        image_file = urlopen(mysrc)
        filename = myfolder + weekday_dict[myweekday] + '/' + mytitle + '.jpg'
        myfile = open(filename, mode='wb')
        myfile.write(image_file.read()) # 바이트 형태로 저장
        myfile.close()

        try :
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    # rmtree : remove tree
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err :
            print(err)


    def save_webtoon_csv(self, url):
        mytarget = Service.get_url.find_all('div', attrs={'class':'thumb'})
        mylist = [] # 데이터를 저장할 리스트
        
        for abcd in mytarget:
            myhref = abcd.find('a').attrs['href']
            myhref = myhref.replace('/webtoon/list.nhn?', '')
            result = myhref.split('&')

            mytitleid = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]

            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?', '').replace(':', '')
    
            mysrc = imgtag.attrs['src']

            Service.save_webtoon_img(mysrc, myweekday, mytitle)

            sublist = []
            sublist.append(mytitleid)
            sublist.append(myweekday)
            sublist.append(mytitle)
            sublist.append(mysrc)
            mylist.append(sublist)

        mycolumns = ['타이틀번호', '요일', '제목', '링크']
        myframe = DataFrame(mylist, columns=mycolumns)
        filename = 'cartoon.csv'

        myframe.to_csv(filename, encoding='utf-8', index=False)
        print(filename + ' 파일로 저장됨')
    
    def get_movie_url(self, url):
        url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn"
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def get_movie_tags(self, url, url_header):
        tags = Service.get_movie_url(url).findAll('div', attrs={'class':'tit3'})
    
        for tag in tags :
            print(tag.a.string)

        print('<a> 태그의 href 전체 태그')
        for tag in tags :
            print(url_header + tag.a['href'])

    def save_movie_csv(self, url):
        mytrs = Service.get_movie_url(url).find_all('tr')
        no = 0 # 순서를 의미하는 번호
        totallist = [] # 전체를 저장할 리스트

        for one_tr in mytrs :
            title = ''
            up_down = '' # '상승/하강/불변'을 위한 설명 문구

        mytd = one_tr.find('td', attrs={'class':'title'})
        if(mytd != None):
            no += 1
            newno = str(no).zfill(2)

            mytag = mytd.find('div', attrs={'class':'tit3'})

            # string 속성 : 해당 태그가 가지고 있는 문자열을 출력
            title = mytag.a.string

            # td 태그 중에서 3번째 요소를 찾기
            mytd = one_tr.select_one('td:nth-of-type(3)')
            myimg = mytd.find('img')
            if myimg.attrs['alt'] == 'up' :
                up_down = '상승'
            elif myimg.attrs['alt'] == 'down' :
                up_down = '하락'
            else :
                up_down = '불변'

            change = one_tr.find('td', attrs={'class':'range ac'})
            change = change.string

            # print(newno + '/' + title + '/' + up_down + '/' + change)
            totallist.append((newno, title, up_down, change))

        mycolumn = ['순위', '제목', '변동', '변동값']
        myframe = DataFrame(totallist, columns=mycolumn)

        filename = 'naverMovie.csv'

        myframe.to_csv(filename)

        print(filename + ' 파일 저장됨')
    