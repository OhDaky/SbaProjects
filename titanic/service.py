import sys
sys.path.insert(0, '/Users/odakyeong/SbaProjects')

from titanic.entity import Entity
import numpy as np
import pandas as pd

"""
PassengerId  고객ID,
Survived 생존여부, --> 맞춰야할 답
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
"""

# 외부에 있는 파이썬 파일(.py)을 import 해야 속성, 기능을 사용할 수 있다.
# 내부에서는 이것을 인스턴스화 해야한다
# entity = Entity()
# 이떄 소문자 entity는 인스턴스라고 하고 이를 객체로 정의한다
# 대문자 Entity는 클래스
# 라운드 브레이스가 있는 Entity()는 생성자라고 한다
# 결론: 객체지향 oop에서는 속성과 기능을 호출하는 구조로
# 두 가지 방식이 있는데
# calc = Calculator() 있다고 하면
# calc 는 인스턴스 객체가 되고
# Calculator 는 클래스객체 (스태틱)라고 한다
# calc.sum()하면 인스턴스 호출방식=다이나믹
# Calculator.sum() 하면 클래스호출방식 = 스태틱 이라 한다
# p.137  df = tensor
        

class Service:
    def __init__(self):
        self.entity = Entity()
        
    def new_model(self, payload) -> object:
        this = self.entity
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1) # train은 답이 제거된 데이터셋이다

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived'] # label 은 곧 답이 된다
        
    @staticmethod
    def drop_feature(this, feature):
        this.train = this.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1) # p.149에 보면 훈련, 테스트 세트로 나눈다
