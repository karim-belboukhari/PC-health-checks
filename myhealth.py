#!/usr/bin/env python

import psutil


def check_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print("here is the details")
    print("hope you lik it")
    print("CPU Usage:", cpu_usage, "%")

    # Check memory usage
    memory_usage = psutil.virtual_memory().percent
    print("Memory Usage:", memory_usage, "%")

    # Check disk usage
    disk_usage = psutil.disk_usage('/').percent
    print("Disk Usage:", disk_usage, "%")

if __name__ == "__main__":
    check_health()
