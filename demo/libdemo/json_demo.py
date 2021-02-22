import json


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s


t = Time(10, 20, 30)
print(json.dumps(t.__dict__))
