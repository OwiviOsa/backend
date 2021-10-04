import datetime


class Date:
    def __init__(self, *args):
        if len(args) >= 3:
            self.year, self.month, self.day = args
        elif len(args) == 1 and isinstance(args, str):
            self.year, self.month, self.day = args.split('-')
        self.date = datetime.date(self.year, self.month, self.day)

    def get_date(self):
        return self.date

    def plus_days(self, days: int):
        self.date += datetime.timedelta(days=days)

    def __str__(self, date_format: str = "%Y-%m-%d"):
        return self.date.strftime(date_format)
