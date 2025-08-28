def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        if coins > 1:
            print(f"{person} has {str(coins)} coins left")
        elif coins == 1:
            print(f"{person} has {str(coins)} coins left")
        else:
            print(f"{person} has 0 coins left")
        coins -= 1

    return play_game


amal = parent_function("amal", 1)
achu = parent_function("achu", 3)
amal()
amal()
achu()
