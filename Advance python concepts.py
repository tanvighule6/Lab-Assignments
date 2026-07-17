def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#output
#Before the function
#Hello!
#After the function

#generator program
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
    
#output
#5
#4
#3
#2
#1


#iterator program
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
print(next(my_iter)) 
print(next(my_iter)) 
print(next(my_iter))

#output
#1
#2
#3