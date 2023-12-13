class Worker:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f"{self.name} {self.surname}, Возраст: {self.age}"


class Boss:
    def __init__(self):
        return

    def __str__(self):
        return


class Work:
    def __init__(self):
        return


def create_work():
    return


def create_boss():
    return


def create_worker():
    return


def menu():
    work = None
    boss = None

    while True:
        print("Главное меню:")
        print("1. Создать фирму.")
        print("2. Создать директора(количество - 1).")
        print("3. Создать сотрудника.(количество - не ограничено)")
        print("4. Вывести информацию о сотруднике.")
        print("5. Вывести информацию о директоре.")
        print("6. Вывести информацию о фирме.")
        print("7. Выход из программы ")

        choose = input("Выберите пункт меню: ")

        if choose == "1":
            pass
        elif choose == "2":
            pass
        elif choose == "3":
            pass
        elif choose == "4":
            pass
        elif choose == "5":
            pass
        elif choose == "6":
            pass
        elif choose == "7":
            pass
        else:
            pass


if __name__ == "__main__":
    menu()
