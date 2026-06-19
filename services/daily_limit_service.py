from datetime import date
from collections import deque
class DailyLimitService:
    def __init__(self):
        self.daily_usage = {}
        self.daily_limit = 100000
    def check(
            self,
            transaction):
        username = transaction.username
        today = date.today().isoformat()
        if username not in self.daily_usage:
            self.daily_usage[username] = { "date" : today, "amount": 0 }
        stored_date = self.daily_usage[username]["date"]
        if today != stored_date:
            self.daily_usage[username] = { "date" : today, "amount": 0 }
        elif self.daily_usage[username]["amount"] + transaction.amount > self.daily_limit:
            raise Exception(
                { "total limit exceeded by": (self.daily_usage[username]["amount"] + transaction.amount) - self.daily_limit})
        else:
            self.daily_usage[username]["amount"] += transaction.amount
        return True
