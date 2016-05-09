# zad 1 lista 1 pwiz

'''1. Przygotować program do wpisywania numerów kont.
        a) Jedno pole do wprowadzania.
        b) Jedno pole do wyświetlania informacji.
        c) Przycisk do zatwierdzania wpisanego numeru
        d) po naciśnięciu przycisku zwerykować, czy długość wpisanego numeru
        to 26 znaków
        e) jeśli długośc wpisanego ciągu nie jest równa 26 znaków to podświetlić
        pole do wpisywania na czerwono, wyświetlić odpowiedni komunikat w
        polu do wyświetlania,
        f ) jeśli długość jest prawidłowa, podświetlić numer na zielono, wyświetlić
        komunikat w polu do wyświetlania.

   2. Zmodykować poprzedni program, tak aby wywoływał lepszą werykację
      numeru:
        a) Zwerykować, czy numer zawiera cyfry i spacje, kod funkcji załączony
        jest na ko«cu pliku
        b) Zmodykować funkcję tak, aby sprawdzała liczbę cyfr (powinno być 26
        cyfr i dowolna liczba spacji).
        c) zmodykować kolorowanie (np. oletowy dla znaku, który nie jest cyfrą,
        brązowy dla złej długości).
'''

import tkinter as tk

def enter_pressed(zdarzenie):
    ok_pressed()

def ok_pressed():
    if input_field.get():
        wprowadzone = input_str.get()
        znaki = list(wprowadzone)

        wynik = 0 
        for el in znaki:
            print(el)
            if el.isdigit():
                wynik += len(el)
            if el.isalpha():
                wynik = 0
                break
                
        if wynik == 5: # do testów przyjęto 5 zamiast 26 cyfr
            label.config(text='Dobrze\nWprowadzono prawidłowy 5-cyfrowy numer konta')
            input_field.config(bg='springgreen')
            label.config(fg='black')
        else:
            input_field.config(bg='indian red')
            label.config(fg='red')
            if wynik == 0:
                label.config(text='Wprowadzono nieprawidłowe znaki w numerze' )
            else:
                #label_txt = label.cget('text')
                label.config(text='Wprowadzono ' + str(wynik) + ' cyfr' )


main_window = tk.Tk()

input_str = tk.StringVar()

label_title = tk.Label(main_window, text='Wprowadź 5-cyfrowy numer konta:')
input_field = tk.Entry(main_window, width=26, textvariable = input_str)
label = tk.Label(main_window, text='Informacje dla Uzytkownika:\n (brak)')
ok_button = tk.Button(main_window, text='Wprowadź', command=ok_pressed)

win_obj = [input_field, label, ok_button]

label_title.pack()
input_field.pack()
label.pack(fill=tk.X)
ok_button.pack(fill=tk.X)

label_title.config(font='Helvetica 14')
input_field.config(font='Helvetica 14 bold')
label.config(font='Helvetica 14')
ok_button.config(font='Helvetica 14')


# events
input_field.bind('<Return>', enter_pressed)
ok_button.bind('<Return>', ok_pressed)
