def get_number():
    #int(input("Number: "))
    number = 187
    get_starting_numbers(number)

def get_starting_numbers(number):
    start1 = number/2
    start2 = 2
    calculate_root(start1, start2, number)

def calculate_root(start1, start2, number):
    for i in range(100):
        start1 = (start1 + start2) /2
        start2 = number/start1
    print (f"{start2}")

get_number()