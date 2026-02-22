# if-elif-else statement in python
from pyscript import display, document


def display_numbers(e):
    document.getElementById('result').innerHTML = " "

    students = [
    "Abdullah, Jalainie",
    "Abeleda, Leona",
    "Arce, Renzo",
    "Arias, Caleb",
    "Bonzon, Cedric",
    "Cajucom, Martina",
    "Catimbang, Phoebe",
    "Choi, Sang-Heon",
    "Cotioco, Sean",
    "Daradal, Allen",
    "Enriquez, Alejandro",
    "Escobar, Skyler",
    "Espina, Khloe",
    "Gano, Shino",
    "Garcia, Calvin",
    "Kaur, Simrandip",
    "Ong, Sebastian",
    "Rufo, Carl",
    "Sanchez, Miguel",
    "Santos, Ramon",
    "Tan, Deryck",
    "Vilale, Beatrix",
    "Yao, Harmony",
    "Zosa, Ivy"
]

    count = 0

    while True:
        display(f'{count + 1}. {students[count]}', target='result')
        count += 1

        if count == 24:
            break
