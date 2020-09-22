# property 는 url, parser, path, api, apikey 전부 str 타입
import sys
sys.path.insert(0, '/Users/odakyeong/SbaProjects')

from dataclasses import dataclass

class Entity:
    url: str =''
    parser: str = ''
    path: str = ''
    api: str = ''
    apikey: str = ''