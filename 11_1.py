class Date:
    def __init__(self, date: str):
        nums = Date.extract(date)
        self.validate(nums)

    @classmethod
    def extract(cls, date: str) -> list:
        return [int(n) for n in date.split('-')]

    @staticmethod
    def validate(nums: list):
        day, month, year = nums
        assert 1 <= day <= 31, "В месяце 31 день максимум"
        assert 1 <= month <= 12, "Год состоит из 12 месяцев"
        assert 0 <= year <= 2022, "Ошибка же"


Date1 = Date("21-06-1993")
print(Date.extract('03-03-2022'))
#Date2 = Date("32-11-2011")
#Date3 = Date("03-13-2001")
#Date4 = Date("03-11-101000")
