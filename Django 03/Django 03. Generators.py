# Generators

import datetime

def infinite_days(start=None):
    if start is None:
        start = datetime.date.today()
        while True:
            yield start
            start += datetime.timedelta(days=1)

# days = infinite_days()
# while True:
#     print(next(days))
#     input()

def read_file_lines(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

# for line in read_file_lines("students.txt"):
#     print(f">> {line}")

# numbers_list = [i for i in range(10)]
# numbers_gen = (i for i in range(10))
#
# print(numbers_list)
# print(next(numbers_gen))
# pass
# pass
# pass
# print(next(numbers_gen))

def generate_events():
    events = [
        {"level": "INFO", "event":"user_login", "user_id":1},
        {"level": "ERROR", "event":"db_unavailable", "retry_in":5},
        {"level": "INFO", "event":"user_logout", "user_id":1},
        {"level": "WARNING", "event":"slow_request", "duration_ms":1200},
    ]
    for event in events:
        yield event


def filter_errors(events):
    for event in events:
        if event["level"] == "ERROR":
            yield event


def enrich_events(events):
    for event in events:
        enriched = dict(event)
        enriched["source"] = "app_server_1"
        yield enriched


def demo_pipline():
    print("Generators Pipline")
    source = generate_events()
    errors_only = filter_errors(source)
    enriched = enrich_events(errors_only)
    for event in enriched:
        print(f"event -> {event}")





