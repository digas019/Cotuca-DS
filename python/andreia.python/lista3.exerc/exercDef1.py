def palindromo (palavra):

    for i in range(1):
        if palavra != palavra[::-1]:
            return False
        return True
palavra = input(">:")
palavra = palavra.replace (" " , "")
p = palindromo(palavra)
if (p):
    print("é palindromo")
else:
    print("nao é palindromo")