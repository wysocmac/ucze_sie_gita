import random
import string

n_znakow = int(input('Podaj długość hasła: '))
dzielenie = int(n_znakow /4)
reszta_dzielenie = n_znakow % 4
dzielenie_male = dzielenie + reszta_dzielenie

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation= string.punctuation
digits= string.digits

losowe_znaki_1 = random.sample(lowercase,dzielenie_male)
losowe_znaki_2 = random.sample(uppercase,dzielenie)
losowe_znaki_3 = random.sample(punctuation,dzielenie)
losowe_znaki_4 = random.sample(digits,dzielenie)

if n_znakow < 8 or n_znakow > 24:
    print('Hasło powinno mieć przynajmniej 8 znaków i max 24')
else:
    haslo_s = random.sample((losowe_znaki_1+losowe_znaki_2+losowe_znaki_3+losowe_znaki_4),n_znakow)
    haslo = "".join(haslo_s)
    print("Ile znaków w grupie",dzielenie, 'Ile małych liter',dzielenie_male)
    print()
    print(haslo)
