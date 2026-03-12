# tpl = (26, 365, 78)

# print(type(tpl))

# a, b, c =  (25, 8, 65)
# print(a, b, c)

# numb1 = 26
# numb2 = 30
#
# print(numb1, numb2)

# tmp = numb1
# numb1 = numb2
# numb2 = tmp

# numb1 = numb1 + numb2
# numb2 = numb1 - numb2
# numb1 = numb1 - numb2

# numb1, numb2 = numb2, numb1
#
# print(numb1, numb2)

# def foo():
#     return 25, 98, 78, 18
#
# print(type(foo()))
#
# a, _, _, d = foo()


# def bar(*args):
#     print(type(args))
#
#
# bar(1,2,3,4,5)


# real using examples tuples

config = ("postgres", "db.example.com", 5432)

# host = config[1]

db_type, host, port = config

point3d = (12.0, 13.5, 14.0)
user_with_position = ("alice", point3d)

payment_service_config = ("Payment1", "payment.example.com", 443)
device_position = (55.26, 657, 5)
single_flag = ("READ_ONLY",)
limits = 1000, 10 # max_requests, per_minutes
