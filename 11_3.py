class NotNumber(Exception):
    def __str__(self):
        return "Введено не число!"

    def detect(self):
        try:
            float(self)
            return True
        except ValueError:
            return False


my_list = []

while True:
    num = input("Введите число для добавления в список, для остановки введите 'stop': ")
    if NotNumber.detect(num):
        my_list.append(int(num))
    elif num == "stop":
        break
    elif not NotNumber.detect(num):
        print(NotNumber())

    print(f"Актуальный список: {my_list}")
