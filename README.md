Для работы тестов нужно:
1. Склонировать репозиторий
2. Создать виртуальное окружение
3. Установить все зависимости 
```
pip install -r requirements.txt
```
4. Возможно потребуется установить браузеры для Playwright
```
playwright install 
```
5. Запуск тестов 
```
pytest tests/test_user.py  
```
```
pytest tests/test_auth.py
```
______________________________________
*Описание структуры проекта (шаблон)*
```
│
├── config 
│   └── config.py ---------------- Валидация и передача данных
│
├── core
│   ├── db (опционально. + динамически меняется под проект)
│   │   ├── db.py ---------------- Подкючения к БД
│   │   └── models
│   │       └── public.py -------- Модели БД 
│   │
│   └── utils
│       ├── api_client.py -------- Запросы к API(не реализовано)
│       ├── data_generators.py --- Методы генерации тестовых данных
│       └── file_helpers.py ------ Хранение статичных тестовых данных
│
├── page_objects
│   ├── base_page.py ------------- Класс основных методов
│   ├── locators
│   │   └── base_locators.py ----- Общие локаторы страниц (если указана в проекте)
│   │
│   └── page
│       └── auth.py -------------- Класс с методами(из общих) и локаторами для страницы авторизации
│
└── tests
    └── test_auth_page.py ------- Тесты для страницы авторизации
```
