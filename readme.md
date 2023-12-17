## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/ARGEN03/TASK15
    cd yourapp
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    .\venv\Scripts\activate  # Для Windows
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции:

    ```bash
    python manage.py migrate
    ```

5. Запустите сервер:

    ```bash
    python manage.py runserver

# Модели Django для Многие ко Многим (Many-to-Many) Отношений

## Модель Продукта (Product)

Модель `Product` представляет собой продукт в магазине с следующими полями:

- **title:** Название продукта (CharField, максимальная длина 60 символов).
- **price:** Цена продукта (IntegerField).

Кроме того, в модели определен метод `__str__`, который возвращает строковое представление продукта, используемое, например, при выводе в административном интерфейсе Django.

## Модель Категории (Category)

Модель `Category` представляет собой категорию, к которой может принадлежать один или несколько продуктов. Она включает следующие элементы:

- **title:** Название категории (CharField, максимальная длина 70 символов) с выбором из фиксированных значений, определенных в кортеже `CATEGORIES`.
- **products:** Связь "многие ко многим" с моделью `Product`. Каждая категория может содержать несколько продуктов, и каждый продукт может принадлежать нескольким категориям. В коде используются `related_name` и `related_query_name` для определения обратных связей и именованных обратных отношений.

# Django One-to-One Example


## Использование

### Пример взаимодействия с консолью

1. Откройте командную оболочку Django:

    ```bash
    python manage.py shell
    ```

2. Внутри оболочки Django импортируйте модели:

    ```python
    from ваше_приложение.models import Product, Category
    ```

3. Создайте экземпляр продукта:

    ```python
    product1 = Product.objects.create(title='Лаптоп', price=800)
    ```

4. Создайте экземпляры категорий:

    ```python
    category1 = Category.objects.create(title='электроника')
    category2 = Category.objects.create(title='компьютеры')
    ```

5. Добавьте продукт в обе категории:

    ```python
    category1.products.add(product1)
    category2.products.add(product1)
    ```

6. Получите все продукты, связанные с конкретной категорией:

    ```python
    products_in_category1 = category1.products.all()
    ```

    Выведите результат:

    ```python
    for product in products_in_category1:
        print(product.title, product.price)
    ```

    Этот код выведет название и цену всех продуктов, связанных с категорией 'электроника'.

## Зависимости

### Данный проект использует следующие зависимости:
Django - веб-фреймворк для разработки веб-приложений на языке Python.

psycopg2-binary - драйвер для взаимодействия Django с базой данных PostgreSQL.
Данный драйвер используется для работы с PostgreSQL базой данных.

# Django One-to-One Example

## Использование

1. Создайте сотрудника:

  ```bash
    python manage.py shell
    ```

    ```python
    from OneToOne.models import Employee, PersonalData

    # Создание сотрудника
    employee1 = Employee.objects.create(name='John Doe', position_at_work='Developer')

    # Создание личных данных для сотрудника
    personal1 = PersonalData.objects.create(phone='+996704234223', Email='niki03@gmail.com', address='ул.Пушкина14', employee=employee1)
    ```

2. Получите личные данные для сотрудника:

    ```bash
    python manage.py shell
    ```

    ```python
    from OneToOne.models import Employee

    # Получение личных данных для сотрудника
    personal_data_for_employee1 = Employee.objects.get(name='John Doe').human.all()
    ```

Не стесняйтесь адаптировать и расширять эти модели в соответствии с вашими конкретными требованиями.

