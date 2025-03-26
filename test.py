import random

attempts = 0


def rolls():
    global attempts
    count = 0
    while(count < 6):
        attempts += 1
        num = random.randint(1, 20)
        if(num == 20):
            count += 1
        else:
            count = 0

rolls()
print(f"Attemts: {attempts}")