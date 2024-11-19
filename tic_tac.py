import random

l_casillas = [[1,4,7],[2,5,8],[3,6,9]]
pc_alterntives = [1,2,3,4,5,6,7,8,9]
aviable_casillas = [[True,True,True],[True,True,True],[True,True,True]]
d_casillas = {
    "1":(0,0),
    "4":(0,1),
    "7":(0,2),
    "2":(1,0),
    "5":(1,1),
    "8":(1,2),
    "3":(2,0),
    "6":(2,1),
    "9":(2,2)
}
linea_superior = ("+"+"-"*7)*3+"+"
linea_vacia = (("|"+" "*7)*3+"|"+"\n")
player_turn = True

def draw_board():
    print("turno del jugador") if player_turn else print("turno de la pc")
    for i in range(3):
        print(linea_superior)
        print(linea_vacia,end="")
        print(f"|   {l_casillas[0][i]}   |   {l_casillas[1][i]}   |   {l_casillas[2][i]}   |")
        print(linea_vacia,end="")

def change_board(valor_input,character_select):
    row, files = d_casillas[valor_input]
    l_casillas[row][files] = character_select
    aviable_casillas[row][files] = False
    pc_alterntives.remove(int(valor_input))


def valid_change(valor_input):
    row, files = d_casillas[valor_input]
    if aviable_casillas[row][files]:
        return True
    else:
        print("la casilla esta ocupadda")
        return False


def check_winner():
    #revisamos columnas
    for row in l_casillas:
        if len(set(row)) == 1:
            return True
    #revisamos filas
    for files in range(3):
        if len(set([l_casillas[0][files],l_casillas[1][files],l_casillas[2][files]])) == 1:
            return True
    #revisamos diagonales
    if len(set([l_casillas[0][0], l_casillas[1][1], l_casillas[2][2]])) == 1:
        return True
    if len(set([l_casillas[0][2], l_casillas[1][1], l_casillas[2][0]])) == 1:
        return True

    return False


def change_turne(player_turn):
    return not player_turn


def input_select(player_turn):
    if player_turn:
        character_select = "X"
        while True:
            valor_input = input("ingrese el valor de la casilla ")
            if valid_input(valor_input):
                if valid_change(valor_input):
                    change_board(valor_input, character_select)
                    break
    else:
        character_select = "O"
        valor_input = pc_selection()
        change_board(valor_input, character_select)
    player_turn = change_turne(player_turn)
    return valor_input, player_turn

def pc_selection():
    valor_input = random.choice(pc_alterntives)
    return str(valor_input)


def valid_input(valor_input):
    if valor_input.isdigit() and int(valor_input) in range(1,10):
        return True
    else:
        print("el valor ingresado no es un digito o esta fuera de rango valido")
        return False

while True:
    draw_board()  # Muestra el tablero antes de cada jugada
    valor_input, player_turn = input_select(player_turn)
    print("2")
    if check_winner():
        draw_board()  # Muestra el tablero final
        print(f"¡{l_casillas[d_casillas[valor_input][0]][d_casillas[valor_input][1]]} ha ganado!")
        break
    elif len(pc_alterntives) == 0:
        draw_board()  # Muestra el tablero final
        print("¡Es un empate!")
        break