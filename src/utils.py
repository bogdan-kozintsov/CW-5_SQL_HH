employer_ids = []


def get_employee_data():
    """
    функция для получения данных о компаниях с сайта HH.ru
    :return: список компаний
    """
    pass


def get_vacancies_data():
    """
    функция для получения данных о вакансиях с сайта HH.ru
    :return: список вакансий
    """
    pass


def create_database(database_name: str, params: dict) -> None:
    """
    функция для создания Базы Данных и создания таблиц в БД
    """
    pass


def save_data_to_database_emp(data_emp: list[dict[str, Any]], database_name: str, params: dict) -> None:
    """
    Функция для заполнения таблицы компаний в БД
    """
    pass


def save_data_to_database_vac(data_vac: list[dict[str, Any]], database_name: str, params: dict) -> None:
    """
    Функция для заполнения таблицы вакансий в БД
    """
    pass
