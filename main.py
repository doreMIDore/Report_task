# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os.path
import datetime
import sys
import traceback

from model import getData, URLTODOS, URLUSERS


def createReport():
    try:
        os.mkdir("tasks")
    except OSError:
        print("Создать директорию %s не удалось" % "tasks")
    else:
        print("Успешно создана директория %s " % "tasks")

    users = getData(URLUSERS, "Не удалось получить список пользователей")
    todos = getData(URLTODOS, "Не удалось получить список задач")

    formattedTimeForTitle = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M')
    formattedTimeForReport = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')

    # TODO CreateListOfTodosInUsers
    # TODO for in users to create empty 2 list
    # TODO for in todos to fill list completed\ornot


    for user in users:
        newFileName = renameFiles(fr"{os.getcwd()}\tasks\{user['username']}.txt",
                                  fr"{os.getcwd()}\tasks\old_{user['username']}",
                                  addingFormattedTimeToOld=False
                                  )
        completedTaskDict = dict()
        actualTaskDict = dict()
        countOfTask = {"count": 0}
        idUser = user['id']
        print(user['username'])
        for number, task in enumerate(todos):
            fillDict(completedTaskDict, actualTaskDict, countOfTask, idUser, task, number)

        try:
            with open(fr"{os.getcwd()}\tasks\{user['username']}.txt", "w+") as newFile:
                try:
                    # if user['username'] == "Antonette":
                    #    raise OSError("Генерация ошибки OSError")
                    writeFile(newFile, user, formattedTimeForReport, countOfTask, completedTaskDict,
                              actualTaskDict)

                except OSError:
                    newFile.close()
                    os.remove(fr"{os.getcwd()}\tasks\{user['username']}.txt")
                    raise OSError("Не удалось записать информацию в файл")

        except OSError as ex:
            if len(ex.args) == 1:
                print(ex.args[0])
            else:
                print("Не удалось создать файл")
            if newFileName is not None:
                renameFiles(newFileName,
                            fr"{os.getcwd()}\tasks\{user['username']}",
                            None
                            )


def fillDict(completedTaskDict, actualTaskDict, countOfTask, idUser, task, number):
    try:
        if idUser == task['userId']:
            countOfTask['count'] += 1
            if task['completed']:
                completedTaskDict[number] = task['title']
            else:
                actualTaskDict[number] = task['title']
    except KeyError:
        print(f"Задача {task['id']} не закреплена")


def renameFiles(oldFileName, newFileName, addingFormattedTimeToOld, formatFile=".txt"):
    try:
        with open(oldFileName) as f:  # checking for files
            usefulStr = f.readlines()[1]
            startStr = usefulStr.find('>')
            endStr = len(usefulStr)
            reportTime = usefulStr[startStr + 2:endStr - 1]
            formatTimeForTitle = datetime.datetime.strptime(reportTime, '%d.%m.%Y %H:%M').strftime('%Y-%m-%dT%H-%M')
            if addingFormattedTimeToOld:
                oldFileName += '_' + formatTimeForTitle + formatFile
            if addingFormattedTimeToOld is None:
                newFileName += formatFile
            if addingFormattedTimeToOld == False:
                newFileName += '_' + formatTimeForTitle + formatFile
        os.renames(oldFileName, newFileName)
        print("Файлы успешно переименованы")
        return newFileName
    except OSError:
        print("Переименовать файлы не удалось")


def writeFile(newFile, user, formatTimeForReport, countOfTask, actualTaskDict, completedTaskDict):
    header = headerText(user, formatTimeForReport, countOfTask, actualTaskDict)
    todos = todosText(actualTaskDict)
    textOfReport = header + todos + f"\n## Завершённые задачи ({len(completedTaskDict)}):\n"
    todos = todosText(completedTaskDict)
    textOfReport += todos
    newFile.write(textOfReport)


def headerText(user, formatTimeForReport, countOfTask, actualTaskDict):
    header = (f"# Отчёт для {user['company']['name']}.\n"  # Отчёт для Deckow-Crist. 
              f"{user['name']} <{user['email']}> {formatTimeForReport}\n"  # Ervin Howell <Shanna@melissa.tv>  23.09.2020 15:25      
              f"Всего задач: {countOfTask['count']}\n\n"  # Всего задач: 4
              f"## Актуальные задачи ({len(actualTaskDict)}):\n")
    return header


def todosText(todosDict):
    textOfTodos = ""
    for task in todosDict.values():
        if len(task) > 46:
            task = (task[:46] + '...')
        textOfTodos += (f"- {task}\n")
    return textOfTodos


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createReport()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
