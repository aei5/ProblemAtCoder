
from player import Player
from MAP import Map


def showText(text, playerName):
    print(text.format(playerName))

def main():
    print("== hello world ==")

    text = "hello {}!"
    playerName = input("please enter your name\n")
    player = Player(playerName)
    showText(text, player.name)

    print("HP: [{}/{}]".format(player.hp, player.max_hp))
    input()

    print("MP: [{}/{}]".format(player.mp, player.max_mp))
    input()

    print("POW: {}".format(player.power))
    input()

    print("DEF: {}".format(player.defense))
    input()

    print("LEVEL: {}".format(player.level))
    input()

    print("EXP: {}".format(player.exp))
    input()

    MAP = Map()
    MAP.show()
    input()


if __name__ == "__main__":
    main()

