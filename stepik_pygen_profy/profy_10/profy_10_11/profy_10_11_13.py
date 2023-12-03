from itertools import groupby
from collections import namedtuple

tasks = [('Отдых', 'поспать днем', 3),
        ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
        ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
        ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
        ('Отдых', 'погулять вечером', 4),
        ('Курс по ооп', 'обсудить темы', 1),
        ('Урок по groupby', 'добавить задачи на программирование', 3),
        ('Урок по groupby', 'написать конспект', 1),
        ('Отдых', 'погулять днем', 2),
        ('Урок по groupby', 'добавить тестовые задачи', 2),
        ('Уборка', 'убраться в ванной', 2),
        ('Уборка', 'убраться в комнате', 1),
        ('Уборка', 'убраться на кухне', 3),
        ('Отдых', 'погулять утром', 1),
        ('Курс по ооп', 'обсудить задачи', 2)]


Task = namedtuple('Task', ['business', 'action', 'rank'])

for i in range(len(tasks)):
    tasks[i] = Task(*tasks[i])

group_iter = groupby(sorted(tasks, key=lambda x: x.business), key=lambda x: x.business)

for group in group_iter:
    name, data = group
    print(name + ':')
    for task in sorted(data, key=lambda x: x.rank):
        print(f'    {task.rank}. {task.action}')
    print()
