print("Vypisovanie suctu predchadzajuceho a aktualneho cisla")

for i in range(10):
    if i==0:
        sucet=i
        print("Aktualny sucet current cisla a previous je: ", sucet)
    else:
        sucet=i+i-1
        print("Aktualny sucet current cisla a previous je: ", sucet)

