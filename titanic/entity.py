class Entity:

    context: str = '/Users/odakyeong/SbaProjects/titanic/data/'
    fname: str = ''
    train: object = None # 데이터 프레임으로 뽑아서 전환할 것 -> object
    test: object = None
    id: str = ''
    label : str = ''