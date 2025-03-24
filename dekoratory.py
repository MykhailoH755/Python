def counter(func):
    count = 0  

    def wrapper():
        nonlocal count  
        count += 1
        print(f"Функція '{func.__name__}' викликана {count} разів")
        func()

    return wrapper

@counter
def hello():
    print("Привіт!")

@counter
def bye():
    print("До побачення!")

hello()
hello()
bye()
hello()
bye()
bye()
