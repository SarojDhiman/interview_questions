def addition(x):
    return x+1

def multiplication(func, y):
    result = func(y)
    return result

print(multiplication(addition,3))  #here i pass the function as an argument

#second way

def passin_msg(message):
    greeting = "hello"
    def my_personal_msg():
        print(greeting,message)
    # my_personal_msg()
    return my_personal_msg
# print(passin_msg("python is good language"))
# @passin_msg
sun = passin_msg("hello this")
sun()

#here all local vriable destroy prevously and this run the new one which we create

