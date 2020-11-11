## JetLend Test Task

Тестовое задание для JetLend.  
API для работы с личным кабинетом инвестора.

###### Важные моменты:
1. Безопасность - я старался, сделать запросы к API максимально приватными.
2. Автоматизация - id пользователя во все запросы передается автоматически, квалификация создается автоматически
3. Docker - быстрая развертка, легкое использование


#### QuickStart:

- `docker-compose build`
- `docker-compose up -d`
- Создать пользователя `POST` `http://localhost:8000/api-auth/users/`,  
обязательные параметры:  `username`, `email`, `password` 
    > Автоматически будет создана квалификация
- Получить токен `POST` `http://localhost:8000/api-auth/token/login/`  
обязательные параметры: `username`, `password`  
вернется: `Token`
- Добавляем паспортные данные и сканы паспорта `POST` `http://localhost:8000/api/v1/add_passport/`
    > в headers передать Authorization | Token `ваш токен`
                                                                                                     
обязательноые параметры:  
    - `name` - Имя  
    - `surname` - Фамилия  
    - `patronymic_name` - Отчество  
    - `serial_number` - Серия и номер  
    - `birth_date` - Дата рождения  
    - `birth_place` - Место рождения  
    - `date_of_issue` - Дата выдачи  
    - `issued_by` - Кем выдан  
    - `code_unit` - Код подразделения  
    - `place_residence` - Регистрация  
    - `photo_main_page` - Фото главной страницы паспорта  
    - `photo_reg_page` - Фото страницы с регистрацией  
> формат даты YYYY-MM-DD

> При успешном добавлении паспорта, квалификация автоматически изменит свое состояние с `NEW` на `Level 1`

- Далее необходимо принять правила платформы `PUT` `http://localhost:8000/api/v1/qualification/rules/`
    > в headers передать Authorization | Token `ваш токен`

обязательные параметры: `rule` : `True | False`

> При согласии с правилами, квалификация автоматически изменит свое состояние на `Level 2`

- Загружаем документы для прохождения квалификации `POST` `http://localhost:8000/api/v1/add_document/`
    > в headers передать Authorization | Token `ваш токен`

обязательные параметры: `title`, `file`

- Осталось подтвердить или отказаться от квалификации `PUT` `http://localhost:8000/api/v1/qualification/accept/`
    > в headers передать Authorization | Token `ваш токен`

обязательные параметры: `accept` : `True | False`
    > При подтверждении состояние станет `Confirm`, при продолжении без квалификации состояние станет `Failure`
    
#### Остальные методы:

- Получить данные о квалификации `GET` `http://localhost:8000/api/v1/qualification/`
- Получить паспортные данные `GET` `http://localhost:8000/api/v1/passport/`
- Получить данные о документе `GET` `http://localhost:8000/api/v1/document/`
> Все эти методы работают только с авторизованными пользователями поэтому в headers передать Authorization | Token `ваш токен`