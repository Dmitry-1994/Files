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
                dishName = line.strip()
                cookBook[dishName] = []
            # elif line.isdigit():
            #     countIngredient = int(line)
            #     print(countIngredient)
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

print(readReciepes("recipes.txt"))

