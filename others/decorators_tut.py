"""
    how to work with decorators.
    basic, chaining, args & kwargs
"""

# ---------------- Example 1 --------------
print('Example 1:')


# basic usage of decorator syntax and how to pass a function ref
def add_1(num):
    return num + 1


# decorate a function result
print(add_1(1))  # == 2


# the pythonic syntax - (annotation + pass function ref + )

def add_1(fn):
    def wrapper(num):
        return fn(num + 1)

    return wrapper


# use with annotation:
@add_1
def get_num(num):
    return num


print(get_num(1))  # == 2


# use without annotation:
def get_num(num):
    return num


print(add_1(get_num)(1))  # == 2

print('END Example 1;')
# ---------------- END Example 1 --------------

# ---------------- Example 2 --------------
# 2 chained decorators. always remember that the order is FROM THE INSIDE TO THE OUTSIDE.

print('Example 2:')


def add_1(fn):
    def wrapper(num):
        return fn(num + 1)

    return wrapper


def minus_5(fn):
    def wrapper(num):
        return fn(num - 5)

    return wrapper


@add_1
@minus_5
def get_num(num):
    return num


print(get_num(10))


def get_num(num):
    return num


print(add_1(minus_5(get_num))(10))

print('END Example 2;')
# ---------------- END Example 2 --------------

# ---------------- Example 3 --------------
# decorator with arguments. Required a new function level for the input params

print('Example 3:')


def add_something(something):
    def decorate_with_something(fn):
        def wrapper(num):
            return fn(num + something)

        return wrapper

    return decorate_with_something


@add_something(10)
def get_number(num):
    return num


print(get_number(10))

print('END Example 3;')
# ---------------- END Example 3 --------------
# ---------------- Example 4 --------------
# a decorators with kwargs and args

print('Example 4:')


class Coffee:

    def __init__(self, **kwargs):
        self.options = kwargs

    def __str__(self):
        return str(self.options)


def coffee_decorator(**kwargs):
    def decorate_a_coffee(fn):
        def wrapper(c: Coffee):
            c.options = kwargs
            return fn(c)

        return wrapper

    return decorate_a_coffee


@coffee_decorator(sugar=1, milk=0.5, temp='boiled', based_water=True, intense_level='max')
def get_coffee(c: Coffee):
    return c


print(get_coffee(Coffee()))
print('END Example 4;')

# ---------------- END Example 4 --------------

# ---------------- Example 5 --------------
print('Example 5:')
# a decorator with kwargs and args. function with kwargs and args
SHIFT_MANAGER = "SHIFT_MANAGER"


def notify_boss():
    print("Notified Boss")


def discount_club(*args, **kwargs):
    def decorate_discount(fn):
        def wrapper(*products, **payment_data):
            approver, discount = args
            print(f"Approved by:{approver}. Total Discount: {discount}")
            products = list(map(lambda p: Product(p.name, p.price - (p.price * discount / 100)), products))

            if kwargs['notify_big_boss']:
                notify_boss()

            return fn(*products, **payment_data)

        return wrapper

    return decorate_discount


@discount_club(SHIFT_MANAGER, 30, notify_big_boss=True)
def pay_bill(*products, **payment_data):
    [print(f"You paid for: {p}") for p in products]
    print(f"Payment_data: {payment_data}")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"


products = [Product('coffee', 100), Product('Tuna', 200), Product('Choclate', 300)]
payment_data = {'name': 'DaniDin', 'credit_card': '12345678'}
print(pay_bill(*products, **payment_data))

print('END Example 5;')
# ---------------- END Example 5 --------------
