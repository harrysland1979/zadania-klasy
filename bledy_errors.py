try:
    wynik = 2/0

except ZeroDivisionError:
    print("Nie dziel przez zero!")
    wynik = 0

print(wynik)
# except ZeroDivisionError: # nie można dodać drugiego except
#     print("Nie dziel przez zero!")

try:
    wynik2 = 1 + "1"
except TypeError:
    print("Nie można dodawać stringów do liczb!")
    wynik2 = 0

print(wynik2)

