from bs4 import BeautifulSoup

html ='''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тестовая страница для веб-парсинга</title>
</head>
<body>
    <p id="435456" class="123984">Веб-парсинг – это мощный инструмент для анализа данных в интернете.</p>
    <p id="284359" class="493572">Python предоставляет отличные библиотеки для парсинга веб-страниц.</p>
    <p id="789234" class="293487">Для начинающих веб-парсеров важно изучить основы HTML и CSS.</p>
    <p id="239048" class="392874">Библиотека BeautifulSoup позволяет легко извлекать данные с веб-страниц.</p>
    <p id="923874" class="120948">Scrapy – другой популярный фреймворк для веб-парсинга на Python.</p>
    <p id="982374" class="302984">Веб-парсинг может помочь аналитикам и маркетологам собирать ценную информацию.</p>
    <p id="238940" class="238492">Соблюдение законов и правил при парсинге веб-сайтов – это ключевой момент.</p>
    <p id="923485" class="283947">Ограничения robots.txt могут влиять на возможность парсинга некоторых сайтов.</p>
    <p id="293847" class="394872">Динамические веб-сайты могут требовать использование Selenium для парсинга.</p>
    <p id="239487" class="238492">Регулярные выражения могут быть полезными при извлечении специфических данных.</p>
    <p id="203984" class="394872">При веб-парсинге важно учитывать нагрузку на целевой веб-сайт.</p>
    <p id="394872" class="203984">Кэширование данных может ускорить процесс парсинга и снизить нагрузку на сервер.</p>
    <p id="238492" class="394872">Прокси-сервера могут помочь обойти ограничения, связанные с IP-адресом.</p>
    <p id="239847" class="238947">Парсинг может быть автоматизирован с помощью планировщика задач.</p>
    <p id="394872" class="238492">Обработка ошибок – важный этап в разработке парсера.</p>
    <p id="238492" class="394872">Сохранение данных в базу данных позволяет легко анализировать и обрабатывать информацию.</p>
    <p id="293847" class="203984">Многопоточность может значительно ускорить процесс парсинга веб-сайтов.</p>
    <p id="394872" class="203984">Веб-парсинг – это не только технический процесс, но и аналитический навык.</p>
    <p id="293847" class="394872">Изучение веб-парсинга открывает новые возможности для исследования интернета.</p>
    <p id="238947" class="238492">Качественный парсер требует тщательной проработки и тестирования.</p>
    <p id="384756" class="293487">Парсинг веб-страниц – это процесс извлечения данных с онлайн-ресурсов.</p>
    <p id="238947" class="293487">Python стал популярным языком для веб-парсинга благодаря своей простоте и богатой экосистеме.</p>
    <p id="384756" class="238492">Знание структуры HTML и CSS сделает вас более эффективным веб-парсером.</p>
    <p id="238947" class="238492">BeautifulSoup предоставляет удобные методы для поиска и извлечения данных из HTML-документов.</p>
    <p id="384756" class="293487">Scrapy облегчает парсинг множества страниц и управление запросами.</p>
    <p id="238947" class="293487">Веб-парсинг помогает в анализе конкурентов и рынка для бизнеса.</p>
    <p id="384756" class="238492">Соблюдение этичных и юридических норм важно при веб-парсинге.</p>
    <p id="238947" class="238492">Файл robots.txt указывает правила доступа для веб-краулеров и парсеров.</p>
    <p id="384756" class="293487">Selenium полезен для парсинга динамических веб-сайтов с JavaScript.</p>
    <p id="238947" class="293487">Регулярные выражения могут быть мощным инструментом для извлечения данных из текста.</p>
    <p id="384756" class="238492">Оптимизация запросов и паузы важны для избежания блокировки при парсинге.</p>
    <p id="238947" class="238492">Кэширование данных улучшает производительность парсера и снижает нагрузку.</p>
    <p id="384756" class="293487">Использование прокси-серверов помогает в обходе ограничений по IP-адресу.</p>
    <p id="238947" class="293487">Автоматизация парсинга с помощью планировщика может сэкономить время.</p>
    <p id="384756" class="238492">Обработка и логирование ошибок важны для стабильной работы парсера.</p>
    <p id="238947" class="238492">Сохранение данных в базу данных обеспечивает их долгосрочное хранение и анализ.</p>
    <p id="384756" class="293487">Многопоточность увеличивает скорость парсинга и снижает время выполнения задач.</p>
    <p id="238947" class="293487">Веб-парсинг требует аналитического мышления и понимания данных.</p>
    <p id="384756" class="238492">Изучение веб-парсинга расширяет возможности для исследования интернета и данных.</p>
    <p id="238947" class="238492">Разработка качественного парсера – это процесс, требующий тщательной проработки и тестирования.</p>
    <p id="384756" class="293487">Извлечение данных из веб-страницы – ключевой этап в анализе интернет-контента.</p>
    <p id="238947" class="293487">Python предоставляет множество возможностей для работы с текстом и данными.</p>
    <p id="384756" class="238492">Оптимизация запросов и управление скоростью парсинга – залог успешного сбора данных.</p>
    <p id="238947" class="238492">Использование кэширования может значительно снизить нагрузку на серверы и ускорить работу парсера.</p>
    <p id="384756" class="293487">Прокси-сервера – надежный способ обойти ограничения по IP и повысить анонимность.</p>
    <p id="238947" class="293487">Автоматизация задач с помощью планировщика обеспечивает регулярное обновление данных.</p>
    <p id="384756" class="238492">Обработка ошибок и их логирование помогают выявить проблемы и улучшить стабильность парсера.</p>
    <p id="238947" class="238492">Сохранение данных в базе обеспечивает их сохранность и возможность дальнейшего анализа.</p>
    <p id="384756" class="293487">Использование многопоточности позволяет параллельно обрабатывать множество страниц.</p>
    <p id="238947" class="293487">Веб-парсинг – это искусство анализа и извлечения информации из виртуального мира.</p>
    <p id="384756" class="238492">Изучение веб-парсинга даёт возможность исследовать интернет в поисках ценных данных.</p>
    <p id="238947" class="238492">Разработка парсера – это непрерывный процесс улучшения и оптимизации.</p>
    <p id="384756" class="293487">API предоставляют более удобный способ доступа к данным, чем парсинг страниц.</p>
    <p id="238947" class="293487">XPath – мощный инструмент для навигации и извлечения данных из XML и HTML.</p>
    <p id="384756" class="238492">Парсинг данных из JSON позволяет эффективно работать с данными в этом формате.</p>
    <p id="238947" class="238492">Анализ времени выполнения запросов помогает оптимизировать парсинг и снизить нагрузку.</p>
    <p id="384756" class="293487">Эффективный веб-парсинг требует понимания принципов работы HTTP-протокола.</p>
    <p id="238947" class="293487">Системы управления версиями помогают отслеживать изменения в коде парсера.</p>
    <p id="384756" class="238492">Интеграция с облачными хранилищами данных облегчает анализ собранных данных.</p>
    <p id="238947" class="238492">Аналитика и визуализация данных помогают получить ценные инсайты из собранных информационных ресурсов.</p>
    <p id="384756" class="293487">Понимание DOM-структуры помогает эффективно навигировать по веб-страницам.</p>
    <p id="238947" class="293487">Python имеет богатую экосистему для анализа данных, что делает его отличным выбором для парсинга.</p>
    <p id="384756" class="238492">Контроль частоты запросов позволяет избегать блокировок со стороны серверов.</p>
    <p id="238947" class="238492">Использование регулярных выражений требует навыков и практики, но может быть мощным инструментом.</p>
    <p id="384756" class="293487">Прокси-сервера могут быть необходимы для работы с сайтами, блокирующими IP-адреса.</p>
    <p id="238947" class="293487">Планировщики задач помогают автоматизировать процесс парсинга по расписанию.</p>
    <p id="384756" class="238492">Обработка ошибок включает в себя исключения и стратегии восстановления парсера.</p>
    <p id="238947" class="238492">Сохранение данных в базе обеспечивает надежное хранение и возможность долгосрочного анализа.</p>
    <p id="384756" class="293487">Использование многопоточности может значительно ускорить процесс сбора данных.</p>
    <p id="238947" class="293487">Веб-парсинг помогает исследователям извлекать информацию из различных источников.</p>
    <p id="384756" class="238492">Разработка парсера требует тщательного планирования и тестирования функциональности.</p>
    <p id="238947" class="238492">Интеграция с RESTful API облегчает получение данных с веб-серверов.</p>
    <p id="384756" class="293487">XPath позволяет точно находить и извлекать элементы на веб-странице.</p>
    <p id="238947" class="293487">JSON является удобным форматом для передачи и хранения данных при парсинге.</p>
    <p id="384756" class="238492">Мониторинг и управление ресурсами помогают избежать перегрузки серверов.</p>
    <p id="238947" class="293487">Знание структуры URL важно для формирования правильных запросов.</p>
    <p id="384756" class="293487">Веб-парсинг может использоваться для сравнения цен на товары и услуги.</p>
    <p id="238947" class="238492">Эффективный парсер должен быть адаптирован к особенностям целевых веб-сайтов.</p>
    <p id="384756" class="293487">Интеграция с базами данных позволяет хранить и анализировать большие объемы данных.</p>
    <p id="238947" class="238492">Аналитика данных позволяет выявить тенденции и паттерны в собранных информационных ресурсах.</p>
</body>
</html>
'''


def sum_even_length_ids(html):
    soup = BeautifulSoup(html, 'html.parser')
    even_paragraphs = soup.select('p')
    total_id_sum = sum(int(data['id']) for data in even_paragraphs if len(data.text.replace(' ', '')) % 2 == 0)
    total_class_sum = sum(int(data['class'][0]) for data in even_paragraphs if len(data.text.replace(' ', '')) % 2 == 0)
    return total_id_sum + total_class_sum


print(sum_even_length_ids(html))