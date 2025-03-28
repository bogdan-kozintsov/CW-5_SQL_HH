import requests
import psycopg2
from typing import Any


employer_ids = [9694561, 4219, 5919632, 5667343, 9301808, 774144, 10571093, 198614, 6062708, 4306]


def get_employee_data():
    """
    функция для получения данных о компаниях с сайта HH.ru
    :return: список компаний
    """
    employers = []
    for employer_id in employer_ids:
        url_emp = f"https://api.hh.ru/employers/{employer_id}"
        employer_info = requests.get(url_emp, ).json()
        employers.append(employer_info)

    return employers


def get_vacancies_data():
    """
    функция для получения данных о вакансиях с сайта HH.ru
    :return: список вакансий
    """
    vacancy = []
    for vacacies_id in employer_ids:
        url_vac = f"https://api.hh.ru/vacancies?employer_id={vacacies_id}"
        vacancy_info = requests.get(url_vac, params={'page': 0, 'per_page': 100}).json()
        vacancy.extend(vacancy_info['items'])

    return vacancy


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
