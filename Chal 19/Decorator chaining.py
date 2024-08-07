def initialize(func):
    def internal(*args, **kwargs):
        print("$" *29)
        func(*args, **kwargs)
        print("$" *29)
    return internal


def hash_wise(func):
    def internal(*args, **kwargs):
        print("#" *29)
        func(*args, **kwargs)
        print("#" *29)
    return internal

@initialize
@hash_wise
def printer(msg):
    print(msg)

printer("Enableenglish is Awesome!")                