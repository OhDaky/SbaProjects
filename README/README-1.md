Python object

Object = 기능 (function) + 속성(property, attribute, feature) => 파라미터 (ai 파트)

하나의 { … } 에 같이 있음
() 라운드 {} 컬 [] 스퀘어 브레이스 는 총 3가지 (전 프로그래밍 공통)

() 컨디션, 파라미터존, 튜플
{} 블락, JSON, Dict
[] array
[[]] matrix

===> notation 이라 한다
===> 언어기호학

기본적으로 컴공 0, 1 만이 존재한다. 이진수 binary code

George Bool
T, F 판단  —> 전선(모스부호) —> 컴퓨터

선택지는 항상 두가지 중 하나를 선택하는 구조 -> 컴공해법


On, off 의 개념
요소가 존재, 비존재로 종류가 나뉜다 ==> Decision Tree (origin ai 알고리즘)

Q 객체지향 vs 함수형 프로그래밍을 구분하는 기준
무엇이 있고 없고?
속성의 유무


클래스 내부에서 메소드의 종류는 ? dynamic 동적, static 정적
해석:
기준: self 
self exist dynamic -> 데이터를 메모리에서 메소드가 유효한 시간동안만 존재. 그 메소드가 소멸된 후 값은 self에 저장 
self !exist static -> 


def print_info(self):
        print(f'이름:{self.name}, 전화번호:{self.phone}')