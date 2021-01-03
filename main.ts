let A_minha_escolha = 0
let A_outra_escolha = 0
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.SmallDiamond)
    A_minha_escolha = 1
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    basic.pause(2000)
    A_outra_escolha = randint(1, 3)
    if (A_outra_escolha == 1) {
        basic.showIcon(IconNames.SmallDiamond)
        basic.pause(2000)
        if (A_minha_escolha == 1) {
            basic.showString("Empataste")
        } else if (A_minha_escolha == 2) {
            basic.showString("Ganhaste")
        } else {
            basic.showString("Perdeste")
        }
    } else if (A_outra_escolha == 2) {
        basic.showIcon(IconNames.Square)
        basic.pause(2000)
        if (A_minha_escolha == 2) {
            basic.showString("Empataste")
        } else if (A_minha_escolha == 1) {
            basic.showString("Ganhaste")
        } else {
            basic.showString("Perdeste")
        }
        basic.showIcon(IconNames.Scissors)
        basic.pause(2000)
    } else {
        if (A_minha_escolha == 3) {
            basic.showString("Empataste")
        } else if (A_minha_escolha == 2) {
            basic.showString("Ganhaste")
        } else {
            basic.showString("Perdeste")
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Scissors)
    A_minha_escolha = 3
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Square)
    A_minha_escolha = 2
})
