import game_modul,random
print("Добро пожаловать в пробное подобие игры.")
again = None
while again != "n":
    players = []
    num = game_modul.ask_number(question = "Сколько игроков участвует? (2 - 5)", low = 2, high = 5)
    for i in range(num):
        name = input("Имя игрока: ")
        score = random.randrange(101)
        player = game_modul.Player(name,score)
        players.append(player)
    print("Результаты: ")
    for player in players:
        print(player)

    again = game_modul.ask_yes_no("Хотите сыграть ещё? (y/n): ")
input("Нажмите Enter , чтобы выйти из игры.")
