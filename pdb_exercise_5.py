import time

def slow_subtractor(a, b):
    """Return a minus b."""
    time.sleep(5)
    return a - b

some = slow_subtractor(12, 8)
crazy = slow_subtractor(12, 78)
scientific = slow_subtractor(56, 31)
experiment = slow_subtractor(101, 64)

total = some + crazy + scientific + experiment

experimental_fraction = experiment / total
