"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

from time import sleep


def get_seconds_from_milliseconds(time_mil):
    return time_mil / 1000


def job_scheduler(function, delay):
    sleep(get_seconds_from_milliseconds(delay))
    function()


# function to test the job scheduler
def print_hello():
    print("Hello!")


job_scheduler(print_hello, 10000)
