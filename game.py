from random import choice, randrange
from datetime import datetime
times = 5
operators = ["+", "-", "*", "/"]
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
mistake=5
sucess=0
for i in range(0, times):
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    if(operator=='+'):
        result=number_1 + number_2
    elif(operator=='-'):
        result=number_1 - number_2
    elif(operator=='*'):
        result=number_1 * number_2
    else:
        if(number_2==0):
            print("Operacion no posible, va otra")
            number_2 = randrange(9)+1
            print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
        result=number_1 / number_2
    user_result=input("resultado: ")
    user_result=int(user_result)
    result=int(result)
    if(result == user_result):
        sucess = sucess + 1
        mistake = mistake - 1
        print("Respuesta correcta")
    else:
        print("respuesta incorrecta")
end_time = datetime.now()
total_time = end_time - init_time
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"Aciertos: {sucess}")
print(f"Desaciertos: {mistake}")