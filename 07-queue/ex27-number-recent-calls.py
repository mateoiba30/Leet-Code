#You have a RecentCounter class which counts the number of recent requests within a certain time frame.
#Implement the RecentCounter class:
#RecentCounter() Initializes the counter with zero recent requests.
#int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
#It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

#excercise 933

from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque() #is more efficient than list() for queue operations, because it allows appending and popping from both ends in O(1) time

    def ping(self, t: int) -> int:
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()#delete the older values
        self.requests.append(t) #put the new value at the end, i do this at the end of the loop because im sure is going to be included on the new range
        return len(self.requests)