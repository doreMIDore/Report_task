import urllib.error
import time
import requests
import sys

URLTODOS = 'https://json.medrocket.ru/todos'
URLUSERS = 'https://json.medrocket.ru/users'


def getData(url, strError="Не удалось получить данные"):
    try:
        for _ in range(5):
            responseUsers = requests.get(url)
            if responseUsers.status_code == 404:
                time.sleep(1)
                continue
            else:
                return responseUsers.json()
        raise urllib.error.URLError(strError)
    except urllib.error.URLError as ex:
        print(ex.reason)
        sys.exit()


def getUsers():  # getData(url, strError)
    try:
        for _ in range(5):
            responseUsers = requests.get(URLUSERS)
            if responseUsers.status_code == 404:
                time.sleep(1)
                continue
            else:
                a = responseUsers.json()
                return a
        raise urllib.error.URLError("Не удалось получить список пользователей")
    except urllib.error.URLError as ex:
        print(ex.reason)
        sys.exit()


def getTodos():
    try:
        for _ in range(5):
            responseTodos = requests.get(URLTODOS)
            if responseTodos.status_code == 404:
                time.sleep(1)
                continue
            else:
                return responseTodos.json()
        raise urllib.error.URLError("Не удалось получить список задач")
    except urllib.error.URLError as ex:
        print(ex.reason)
        sys.exit()
