def checkMagazine(magazine, note):

    magdictionary = makehashmap(magazine)
    notedictionary = makehashmap(note)

    count = 0
    r = 'No'

    for i in notedictionary:
        if i in magdictionary and magdictionary[i] >= notedictionary[i]:
            count += 1
            if count == len(note):
                r = 'Yes'

    print(r)

def makehashmap(arr):
    dictionary = dict()

    for i in range(len(arr)):
        if arr[i] not in dictionary:
            dictionary[arr[i]] = 1
        else:
            dictionary[arr[i]] += 1

    print(dictionary)
    return dictionary


checkMagazine(['two', 'times', 'three', 'is', 'not', 'four'],['two', 'times', 'two', 'is', 'four'])
