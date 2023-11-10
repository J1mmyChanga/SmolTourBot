from data import *

global_init('db/bot.db')
session = create_session()

l1 = Locations(location='Парки')
l2 = Locations(location='Исторические места')
l3 = Locations(location='Интересная архитектура')
for i in range(1, 4):
    session.add(eval(f'l{i}'))

session.commit()
