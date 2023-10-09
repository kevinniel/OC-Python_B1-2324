# Instruction : affichage
# print( "coucou les B1" )

# # décalaration de variable
# var1 = "toto"
# print(var1)
# var1 = "tata"
# print(var1)

# # calculs de base
# a = 12
# b = 3
# print( a + b )
# print( a - b )
# print( a * b )
# print( a / b )
# # puissance
# print( a ** b )
# # résultat de la division entière
# print( a // b )
# # résultat de la division entière (modulo)
# print( a % b )


# # récupération informations utilisateur
# nom = input("comment t'appelles-tu ?")
# print("enchenté, ", nom)

# # conditions
# if (1 == 1):
#     print("vrai")
# else:
#     print("false")

# print("niveau de base")

# demande l'age de l'utilisateur et dis moi s'il est majeur ou non ?
# age = input("quel age as-tu ?")

# if(int(age) > 100):
#     print("bienvenue au paradis : tu est mort :D ")
# elif (int(age) < 18):
#     print("tu es mineur")
# else:
#     print("tu es majeur")

# tableau [] = liste
# var = "toto"
# tableau = ["a", "bcd", 12, var]
# print(tableau[2])
# numéros de case : [0, 1, 2, 3]
# print(tableau)

# for i in tableau:
#     print(i)

# tableau {} = dictionnaire
# dic = {
#     "a": "toto",
#     4: 157,
#     345: "tata"
# }
# # affichage du tableau
# print(dic)
# # afficher "toto"
# print( dic["a"])
# # afficher tata
# print( dic[345])
# # affcher tous les éléments du tableau : 
# for cle, valeur in enumerate(dic):
#     print(cle, valeur, dic[valeur])

# soit le tableau suivant, afficher tous les éléments 1 par 1 :
# (tableau à 2 dimensions)
# tablo = [
#     1,
#     "test",
#     [
#         "a",
#         "z",
#         "e"
#     ],
#     "r",
#     "t",
#     "y"
# ]
# solution 1
# for valeur in tablo:
#     if( type(valeur) is list ):
#         for v in valeur:
#             print(v)
#     else:
#         print(valeur)

# solution 2
# for i in range(0, len(tablo)):
#     print("i", i)
#     print("tablo[i]", tablo[i])
    # non faisable en python sans vérifier le type !



# connaitre la longueur d'un tableau ou d'une String
# string = "mastring"
# tablo = ["a", "bcd", 12, 35, 79, "azeutyg"]
# print( len(string) )
# print( len(tablo) )

# demander à 3 utilisateurs différents leur age pour leur dire
# s'ils sont majeur ou non ?

# créer une fonction is_majeur
# renvoie "-1" si mort
# renvoie "0" si mineur
# renvoie "1" si majeur
def is_majeur( age ):
    if(int(age) > 100):
        print("bienvenue au paradis : tu est mort :D ")
        return -1
    elif (int(age) < 18):
        print("tu es mineur")
        return 0
    else:
        print("tu es majeur")
        return 1

age1 = input("quel age as-tu ? (age1)")
is_1 = is_majeur(age1)
print(is_1)

age2 = input("quel age as-tu ? (age2)")
is_2 = is_majeur(age2)
print(is_2)

age3 = input("quel age as-tu ? (age3)")
is_3 = is_majeur(age3)
print(is_3)
