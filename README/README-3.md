머신러닝 = 기계학습 = ML (== Deep Learning)

ML : 지도, 비지도, 강화
ML Process 4 : 
    preprocessing
    modeling
    learning, evaluation
    완성되면 submit (파일로 저장)


ML Algorithm

1. 퍼셉트론 (perceptron) -> 뉴런 (neuron)
2. 회귀
3. 분류
4. SVM
5. 결정 트리 D-tree
6. k mean
7. PCA
8. R-forest -> RF
9. NLP
10. Deep Learning -> DL

여기까지가 chap 13
외워두기
지도 외우듯이
Tensorflow

_____________
비지니스 로직 - service
processing 하는 방법


페이로드 (컴퓨팅): 전송되는 데이터

this.fname = payload -> setter 할당 연산자 = 있으면 setter
this.fname = payload -> getter             없으면 getter


"""
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked => 메타데이터 = 스키마 = features = variables = property
1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
"""


차원 (dim)

variable    x = 3 스칼라, 0 차원
array       [] = {1, 2, 3} 벡터, 1차원이 되고, variable 은 element 가 된다
matrix      [[]] = {{1, 2, 3}, {4, 5, 6}} 매트릭스, 2차원 data frame


==========================

지도학습에서 반드시 해야 할 일은 dataset을 생성하는 것입니다
그때 dataset 은 반드시 train, test 두 가지 형태로 작성합니다. p.149