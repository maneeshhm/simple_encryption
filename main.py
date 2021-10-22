alphabet = 'abcdefghijklmnopqrstuvwxyz'

plaintext = input("enter text: ")
k= int(input("enter key: "))
cyper = []


def encrypt(plaintext, k):
    indexList = []

    for x in plaintext:
        indexNumber = alphabet.index(x)
        indexList.append(indexNumber-k)

    for y in indexList:
        cyper.append(alphabet[y])
    print(*cyper)

encrypt(plaintext, k)