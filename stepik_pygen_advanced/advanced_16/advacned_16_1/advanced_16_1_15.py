def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    return f'To: {mail}\n' \
           f'Приветствую, {name}!\n' \
           f'Вам назначен экзамен, который пройдет {date}, в {time}.\n' \
           f'По адресу: {place}.\n' \
           f'Экзамен будет проводить {teacher} в кабинете {number}.\n' \
           f'Желаем удачи на экзамене!'
