from collections import deque
import time
class FraudDetector:
    def __init__(self):

        self.history = {}
        self.max_amount = 50000
        self.blacklist = { "friend", "user"}
 
    def check(
            self,
            transaction):
	    current_time = time.time()
	    username = transaction.name
        if transaction.user in self.blacklist:
            
            raise Exception(
                   "user is blacklisted" )
        elif transaction.amount > self.max_amount:
            raise Exception(
                    "amount exceeded maximum amount")
        elif transaction.username not in self.history:
            self.history[transaction.username] = deque()
		if len(self.history[transaction.username] >= 3 and current_time - self.history[transaction.username][0] >= 30
       			self.history[transaction.username].popleft()
            
            current_time = time.time()
                               raise Exception(
                       "too many attempts in 30 sec"
            self.history[transaction.username].append(current_Time)

        return True
