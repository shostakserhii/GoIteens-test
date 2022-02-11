
'''
магазин для ігор
- вітання
- каталог ігор
- реєструвати нову гру
- категорії ігор
- пошук по характеристиках
'''


game_storage = []

def welcome(username):
    'welcoming user'
    print(f"""
    Hi {username}!
    Welcome to our Game Store! Enjoy your experience with us!
    """)

def username():
    'getting username'
    username = input("Enter your username: ")
    return username

def menu():
    'showing menu to user'
    option = input("""
    You can:
        - check all games in the store: check_all
        - add new game                : add_new_game
        - add discount to game        : add_discount_to_game
        - check games by category     : check_category
        - check games by discount     : check_discounted_games
        - check by characteristics    : under development
        
    q - quit
    
    Choose from the list: """)
    return option

def add_game():
    'add game to storage'
    game_name = input("Enter name of the game: ")
    game_price = input("Price: ")
    game_category = input("Category: ")
    game = {
        'name': game_name,
        'price': game_price,
        'category': game_category
    }
    game_storage.append(game)
    print(game_storage)
    return "...game successfully added"

def game_storage_filling(game_storage):
    'Fill out game_storage with games'
    games = [
        {'name': 'Stalker', 'price': '999', 'category': 'Survival'},
        {'name': 'FIFA', 'price': '499', 'category': 'Sport'},
        {'name': 'Dark Souls', 'price': '499', 'category': 'RPG'},
        {'name': 'CS', 'price': 'free', 'category': 'Shooter'},
        {'name': 'Stalker2', 'price': '999', 'category': 'Survival'},
        {'name': 'DOTA2', 'price': '199', 'category': 'MOBA'},
        {'name': 'Silent Hill', 'price': '99', 'category': 'Horror'},
        {'name': 'PORTAL', 'price': '299', 'category': 'Puzzle-platform'},
    ]
    for game in games:
        game_storage.append(game)

def show_all_games():
    for game in game_storage:
        for key, value in game.items():
            print(f"""\t{key}:{value}""")
        print()

def add_discounted_price_to_game(game_name):   # game_name = Stalker
    for game in game_storage:
        if game['name'] == game_name:
            price = input("Enter discounted price: ")
            game['discounted_price'] = price
            return game
    return None


welcome(username())
while True:
    option = menu()
    game_storage_filling(game_storage)
    if option == 'q':
        print('Ok bye')
        break
    elif option == 'add_new_game':
        add_game()
    elif option == 'check_all':
        show_all_games()
    elif option == 'add_discount_to_game':
        game_name = input("Enter game name: ") #   'stalker'
        print(add_discounted_price_to_game(game_name))
    elif option == 'check_discounted_games':
        pass
    else:
        print(f'{option} not supported')

