from data import *

global_init('db/bot.db')
session = create_session()

l1 = Locations(location='Парки')
l2 = Locations(location='Исторические места')
l3 = Locations(location='Интересная архитектура')
for i in range(1, 4):
    session.add(eval(f'l{i}'))

c1 = Categories(category='Развлечение')
c2 = Categories(category='Для детей')
c3 = Categories(category='Историческое наследие')
for i in range(1, 4):
    session.add(eval(f'c{i}'))

ap1 = AdviceParams(param='Путешествует всей семьёй')
ap2 = AdviceParams(param='Хочет вкусно покушать')
ap3 = AdviceParams(param='Ищет интересные развлечения')
for i in range(1, 4):
    session.add(eval(f'ap{i}'))

a1 = Answers(category=1, question='aaaaaaaaaaa', answer='bbbbbbbbbbb')
a2 = Answers(category=1, question='eeeeeeeeeee', answer='rrrrrrrrrrr')
a3 = Answers(category=2, question='fffffffffff', answer='ggggggggggg')
a4 = Answers(category=2, question='vvvvvvvvvvvv', answer='nnnnnnnnnnnnn')
a5 = Answers(category=3, question='ssssssssssss', answer='kkkkkkkkkkkkkkkkk')
a6 = Answers(category=3, question='wwwwwwwwwwwww', answer='mmmmmmmmmmmmmmm')
for i in range(1, 7):
    session.add(eval(f'a{i}'))
session.commit()
