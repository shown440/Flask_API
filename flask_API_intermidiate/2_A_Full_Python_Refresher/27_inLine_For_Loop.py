player_price = [
    {
    "name" : "Shown",
    "price" : 100
    },
    {
        "name" : "Shown",
        "price" : 50
    },
    {
        "name" : "Shown",
        "price" : 150
    }
]
def price_player():
    list = []
    for price in player_price:
        list.append(price["price"])
    return list
print(price_player())

def price_player2():
    return [price["price"] for price in player_price]
print(sum(price_player2()))
