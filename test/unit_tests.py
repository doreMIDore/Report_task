import os
import unittest
import traceback
import collections.abc
from model import getUsers, getTodos


class MyTestCase(unittest.TestCase):
    def testCompanyNames(self):
        templates = getUsers()
        for user in templates:
            print(user['company']['name'])

    def testCountOfTask(self):
        todos = getTodos()
        users = getUsers()

        for user in users:
            countOfSuccessTask = dict()
            countOfNotSuccessTask = dict()  # L:\\Programming\\Python\\MedRocket'bbb.txt
            countOfTask = 0
            idUser = user['id']
            print(idUser)
        for number, task in enumerate(todos):
            try:
                if idUser == task['userId']:
                    countOfTask += 1
                if idUser == task['userId'] and task['completed']:
                    countOfSuccessTask[number] = task['title']
                if idUser == task['userId'] and not task['completed']:
                    countOfNotSuccessTask[number] = task['title']
            except KeyError:
                pass

            print(f"{user['name']} Количество задач: {countOfTask}")
            print(f"{user['name']} Завершенные задачи {len(countOfSuccessTask)}: {countOfSuccessTask}")
            print(f"{user['name']} Активные задачи {len(countOfNotSuccessTask)}: {countOfNotSuccessTask}")

            print(countOfSuccessTask)

    def testDelete(self):
        users = getUsers()
        user = users[3]
        os.remove(fr"E:\Programming\Python\MedRocket\tasks\{user['username']}.txt")

    def testModel(self):
        getTodos()
        getUsers()

    def testdict(self):
        users = getUsers()
        todos = getTodos()

        for user in users:
            idUser = user['id']
            for number, task in enumerate(todos):
                try:
                    taskDict = []
                    completedTaskDict = dict()
                    actualTaskDict = dict()
                    countOfTask = 0
                    if idUser == task['userId']:
                        countOfTask += 1
                        if task['completed']:
                            completedTaskDict[number] = task['title']
                        else:
                            actualTaskDict[number] = task['title']
                    taskDict.append(actualTaskDict)
                    taskDict.append(completedTaskDict)
                    print(taskDict)
                    return taskDict
                except KeyError:
                    print(f"Задача {task['id']} не закреплена")

    def testDict(self, idUser, task, number):
        try:
            taskDict = []
            completedTaskDict = dict()
            actualTaskDict = dict()
            countOfTask = 0
            if idUser == task['userId']:
                countOfTask += 1
                if task['completed']:
                    completedTaskDict[number] = task['title']
                else:
                    actualTaskDict[number] = task['title']
            taskDict.append(actualTaskDict)
            taskDict.append(completedTaskDict)
            return taskDict
        except KeyError:
            print(f"Задача {task['id']} не закреплена")

    def testList(self):
        users = getUsers()  # getData()
        todos = getTodos()
        for user in users:
            user['completedTask'] = {}
            user['actualTask'] = {}
        try:
            for task in todos:
                userid = task['userId'] - 1
                if task['completed']:
                    users[userid]['completedTask'].update({task['id']: task['title']})
                if not task['completed']:
                    users[userid]['actualTask'].update({task['id']: task['title']})
        except KeyError:
            print(traceback.format_exc())

        for user in users:
            print(user)

    def testaddingToDict(self):
        a = {'a': {'a': 'some value'}}
        b = {'a': {'b': 'some_value'}}
        a['a'].update(b['a'])
        print(a)



if __name__ == '__main__':
    unittest.main()
