# Definire i pattern per i numeri da 0 a 9 come LED
number_to_display = [
    ["####", "#  #", "#  #", "#  #", "####"], # 0
    ["   #", "   #", "   #", "   #", "   #"], # 1
    ["####", "   #", "####", "#   ", "####"], # 2
    ["####", "   #", "####", "   #", "####"], # 3
    ["#  #", "#  #", "####", "   #", "   #"], # 4
    ["####", "#   ", "####", "   #", "####"], # 5
    ["####", "#   ", "####", "#  #", "####"], # 6
    ["####", "   #", "   #", "   #", "   #"], # 7
    ["####", "#  #", "####", "#  #", "####"], # 8
    ["####", "#  #", "####", "   #", "####"]  # 9
]


# Funzione per visualizzare il numero con i LED
def display_number(num):
    # Convertire il numero in una lista per iterare sui singoli elementi
    digit = [int(digit) for digit in num]

    # Itero sulla singola linea e mostro ogni elemento in una riga
    for i in range(5):
        num_to_dig = " ".join([number_to_display[j][i] for j in digit])
        print(num_to_dig)


# Input dell'utente
number = input("Enter a number: ")

if int(number) >= 0:
    display_number(number)
else:
    print("Invalid input.")
