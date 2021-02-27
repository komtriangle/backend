import sqlite3
from collections import Counter


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def send_category(self, category_name):
        """
        добавляет категорию
        """
        self.cursor.execute(
            f"INSERT INTO traning_category (name) VALUES('{category_name}')")
        self.connection.commit()

    def send_progres(self, user_id, date, completed):
        """
        Добавляет прошресс юзера
        """
        self.cursor.execute(
            f"INSERT INTO progress (user_id, date, completed) VALUES('{user_id}', '{date}', '{completed}')")
        self.connection.commit()

    def send_sber_id(self, sber_id):
        """
        Вставка в БД нового пользователя
        :param int: id пользователя
        """
        self.cursor.execute(
            f"INSERT INTO devise (sber_id) VALUES('{sber_id}')")
        self.connection.commit()

    def send_user(self, sber_id, username, age, gender, active):
        """
        Вставка в БД нового пользователя
        """
        self.cursor.execute(
            f"INSERT INTO users (sber_id, name, age, gender, active) VALUES('{sber_id}', '{username}', '{age}', '{gender}', '{active}')")
        self.connection.commit()

    def get_users_by_sberid(self, sber_id):
        """
        достает юзера по сберайди
        """
        users = self.cursor.execute(
            f"SELECT * FROM users WHERE sber_id = '{sber_id}'").fetchall()
        result = dict()
        for i in range(len(users)):
            res = dict()
            res["id"] = users[i][0]
            res["sber_id"] = users[i][1]
            res["name"] = users[i][2]
            res["age"] = users[i][3]
            res["gender"] = users[i][4]
            res["active"] = users[i][5]
            result[str(users[i][0])] = res

        return result

    def get_all_category(self):
        """
        Достает все категории
        """
        category = self.cursor.execute(
            f"SELECT * FROM traning_category").fetchall()
        result = dict()
        for i in range(len(category)):
            res = dict()
            res["name"] = category[i][1]
            result[str(category[i][0])] = res
        return result

    def get_progres_by_user(self, user_id):
        """
        Достает прогрес юзера
        """
        progres = self.cursor.execute(
            f"SELECT * FROM progress WHERE user_id = '{user_id}'").fetchall()
        result = dict()
        for progres_day in progres:
            res = dict()
            res["id"] = progres_day[0]
            res["user_id"] = progres_day[1]
            res["date"] = progres_day[2]
            res["completed"] = progres_day[3]
            result[str(progres_day[0])] = res
        return result

    def get_category_by_id(self, category_id):
        """
        Достает категорию по айди
        """
        category = self.cursor.execute(
            f"SELECT * FROM traning_category WHERE id = '{category_id}'").fetchall()
        result = dict()
        for i in range(len(category)):
            res = dict()
            res["name"] = category[i][1]
            result[str(category[i][0])] = res
        return result

    def get_all_group(self):
        """
        Достает все группы
        """
        group = self.cursor.execute(
            f"SELECT * FROM traning_group").fetchall()
        result = dict()
        for i in range(len(group)):
            res = dict()
            res["name"] = group[i][1]
            result[str(group[i][0])] = res
        return result

    def get_exircices_from_group(self, group_id):
        """
        Достает задания одной группы
        """

        exircices_id = self.cursor.execute(
            f"SELECT traning_id FROM traning_traning_group WHERE traning_group_id = '{group_id}'").fetchall()
        result = dict()
        for exircices in exircices_id:
            ex_id = exircices[0]
            ex = self.cursor.execute(
                f"SELECT * FROM traning WHERE id = '{ex_id}'").fetchall()
            res = dict()
            res["id"] = ex[0][0]
            res["category"] = self.cursor.execute(
                f"SELECT name FROM traning_category WHERE id = '{ex[0][1]}'").fetchall()[0][0]
            res["name"] = ex[0][2]
            res["discription"] = ex[0][3]
            res["photo"] = ex[0][4]
            res["time"] = ex[0][5]
            result[str(ex[0][0])] = res
        return result

    def get_sber_id(self, sber_id):
        """
        Вставка в БД нового пользователя
        :param int: id пользователя
        """
        devise = self.cursor.execute(
            f"SELECT * FROM devise WHERE sber_id = '{sber_id}'").fetchall()
        return devise

    def get_motivations_id(self, id):
        """
        Достает мотивационную фразу из бд
        """
        phras = self.cursor.execute(
            f"SELECT * FROM motivation WHERE id = '{id}'").fetchall()
        result = dict()
        res = dict()
        res["id"] = phras[0][0]
        res["name"] = phras[0][1]
        res["discription"] = phras[0][2]
        res["author"] = phras[0][3]
        result[str(phras[0][0])]  = res
        return result


    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()