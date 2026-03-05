import os
# Задача 1
def readReciepes(filename: str):
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

# Задача 2
file = "recipes.txt" # Исходные данные для задачи
def getShopListByDishes(dishes: list, personCount: int):
    cookBook = readReciepes(file)
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

# Задача 3
# Исходные данные для задачи
inputFiles = ["1.txt", "2.txt", "3.txt"]
outputFile = "result.txt"

def getCountLinesByFile(filename: str):
    with open(filename, "r", encoding='utf-8') as f:
        return len(f.readlines())
def readFile (filename: str):
    with open(filename, "r", encoding='utf-8') as f:
        return f.read()
def creationFile(filesList: list, createFile: str):
    countLineInFiles = []
    for file in filesList:
        countLine = getCountLinesByFile(file)
        countLineInFiles.append((countLine, file))
    countLineInFiles.sort()
    with open(createFile, "w", encoding='utf-8') as f:
        for countLine, fileName in countLineInFiles:
            f.write(f"{fileName}\n")
            f.write(f"{countLine}\n")
            for line in readFile(fileName):
                f.write(line)

creationFile(inputFiles, outputFile)
