A_minha_escolha = 0
A_outra_escolha = 0

def on_button_pressed_a():
    global A_minha_escolha
    basic.show_icon(IconNames.SMALL_DIAMOND)
    A_minha_escolha = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global A_outra_escolha
    basic.clear_screen()
    basic.pause(2000)
    A_outra_escolha = randint(1, 3)
    if A_outra_escolha == 1:
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.pause(2000)
        if A_minha_escolha == 1:
            basic.show_string("Empataste")
        elif A_minha_escolha == 2:
            basic.show_string("Ganhaste")
        else:
            basic.show_string("Perdeste")
    elif A_outra_escolha == 2:
        basic.show_icon(IconNames.SQUARE)
        basic.pause(2000)
        if A_minha_escolha == 2:
            basic.show_string("Empataste")
        elif A_minha_escolha == 1:
            basic.show_string("Ganhaste")
        else:
            basic.show_string("Perdeste")
        basic.show_icon(IconNames.SCISSORS)
        basic.pause(2000)
    else:
        if A_minha_escolha == 3:
            basic.show_string("Empataste")
        elif A_minha_escolha == 2:
            basic.show_string("Ganhaste")
        else:
            basic.show_string("Perdeste")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global A_minha_escolha
    basic.show_icon(IconNames.SCISSORS)
    A_minha_escolha = 3
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global A_minha_escolha
    basic.show_icon(IconNames.SQUARE)
    A_minha_escolha = 2
input.on_button_pressed(Button.B, on_button_pressed_b)
