"""
#import lesson_package.utils
#この下の書き方が一番いい
#from lesson_package import utils
#as で違う文字に変えることが可能
#from lesson_package import utils as u
from lesson_package.tools.utils import say_twice
#from lesson_package.talk import human
#from lesson_package.talk import animal
from lesson_package.talk import *

print(animal.sing())
print(animal.cry)

#r = lesson_package.utils.say_twice("hello")
#r = utils.say_twice("hello")
#r = say_twice("hello")
#print(r)

#print(human.sing())
#print(human.cry)


try:
    from lesson_package.tools import utils
except ImportError:
    from lesson_package.tools import utils

utils.say_twice("word")
"""

#組み込み関数について
#もともと入っている関数
import builtins 

builtins.print("https://jkliop")
#print(globals())

ranking = {
    "A" : 100,
    "B" : 85,
    "C" :95
} 

#ソートされている小さいから順に
print(sorted(ranking, key = ranking.get))
print(sorted(ranking, key = ranking.get,reverse=True))