def readReciepes(filename):
    cookBook = {}
    with open(filename, "r", encoding='utf-8') as f:
        lines = f.readlines()
        dishName = ""
        for line in lines:
            line = line.strip()
            if not line:
                continue
            elif not line.isdigit() and not "|" in line:
                dishName = line
                cookBook[dishName] = []
            elif "|" in line:
                dictIngredient = parseIngridients(line)
                cookBook[dishName].append(dictIngredient)

    return cookBook

def parseIngridients(stringIngredient: str):
    parts = stringIngredient.split('|')
    ingredientName = parts[0].strip()
    ingredientQuantity = int(parts[1].strip())
    ingredientMeasure = parts[2].strip()
    return {
        'ingredient_name': ingredientName,
        'quantity': ingredientQuantity,
        'measure': ingredientMeasure
    }

def getShopListByDishes(dishes: list, personCount: int):
    cookBook = readReciepes("recipes.txt")
    shopList = {}
    for dish in dishes:
        for ingredient in cookBook[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * personCount
            measure = ingredient['measure']
            if name in shopList:
                shopList[name]['quantity'] += quantity
            else:
                shopList[name] = {'measure': measure, 'quantity': quantity}
    return shopList

print(getShopListByDishes(['Запеченный картофель', 'Омлет'], 2))

