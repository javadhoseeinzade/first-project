import random
from Forms.models import info

def randomi():
    value = random.randint(1,1999)
    valuea = random.randint(1,1999)
    print(str(value) + "-" + str(valuea))
