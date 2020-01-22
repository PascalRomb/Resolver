import string

def isVocale(lettera):
    if lettera == 'a' or lettera == 'e' or lettera == 'i' or lettera == 'o' or lettera == 'u':
        return True
    return False

def isConsonante(lettera):
    return not isVocale(lettera)

#condizione dell'ultima parola
def isValidLastWord(word):
    return (
        len(word) == 10 and #lunghezza 10
        word[1] == word[2] and #prima doppia
        word[4] == word[5] and #seconda doppia
        word[0] == word[6] and #la prima e la settima lettera sono uguali
        
        word[1] != word[4] and #prima doppia differente da seconda doppia
        word[1] != word[0] and word[4] != word[0] and#le doppie sono differenti da 0 e 6
        word[3] != word[0] and word[3] != word[1] and word[3] != word[4] and word[3] != word[7] and word[3] != word[8] and word[3] != word[9] and #3 diverso da tutti
        word[7] != word[0] and word[7] != word[1] and word[7] != word[4] and word[7] != word[8] and word[7] != word[9] and #7 diverso da tutti
        word[8] != word[0] and word[8] != word[1] and word[8] != word[4] and word[8] != word[9] and #8 diverso da tutti
        word[9] != word[0] and word[9] != word[1] and word[9] != word[4] #9 diverso da tutti

        #le doppie sono consonanti, però controlliamo lo stesso
        and isConsonante(word[1]) and isConsonante(word[4])

        #ipotizzo che l'ultima sia una vocale, dimostro per negazione
        # DIMOSTRATO, quindi per forza vocale
        #and isConsonante(word[9]), 
    )

#condizioni della prima parola
def isValidFirstWord(word):
    return (
        len(word) == 4 and #lunghezza 4
        word[1] == word[3] and #la seconda e ultima lettera sono uguali
        word[0] != word[1] and word[0] != word[2] and #0 diverso da tutti
        word[1] != word[2] #1 diverso da tutti
    )

#condizioni della terza parola
def isValidThirdWord(word):
    return (
        len(word) == 3 and #lunghezza 3
        word[0] != word[1] and word[0] != word[2] and #0 diverso da tutti
        word[1] != word[2] #1 diverso da tutti
    )

prime_parole = []
terze_parole = []
ultime_parole = []

print("[*] inizio bruteForce")
#lettura dizionario
file = open("dizionario.txt", "r")
for line in file:
    word = line.rstrip('\n')

    #prime parole possibili
    if word.lower() not in prime_parole: 
        if isValidFirstWord(word.lower()):
            prime_parole.append(word.lower())

    #terze parole possibili
    if word.lower() not in terze_parole: 
        if isValidThirdWord(word.lower()):
            terze_parole.append(word.lower())

    #ultime parole possibili
    if word.lower() not in ultime_parole:
        if isValidLastWord(word.lower()):
            ultime_parole.append(word.lower())

file.close()
end = "[*] fine bruteForce. Sono state trovate %d prime parole, %d terze parole, %d ultime parole compatibili" %(len(prime_parole), len(terze_parole), len(ultime_parole) ) 
print(end)
 
#tutte le lettere dell'alfabeto
AllLetters = list(string.ascii_lowercase)

#parole che posso ricostruire nella frase
first = ['*','*','*','*']
second = ['*','*','*']
third = ['*','*','*']

print("[*] Costruzione altre parole")
index_frase = 1
for parola in ultime_parole:
    first = ['*','*','*','*']
    second = ['*','*','*']
    third = ['*','*','*']
    
    #costruzione delle altre parole in base all'ultima parola
    #utilizzo le lettere ripetute
    first[1] = parola[9]
    first[2] = parola[7]
    first[3] = parola[9]

    second[1] = parola[3]
    second[2] = parola[7]
    
    third[1] = parola[1]
    third[2] = parola[9]
    
    #lettere utilizzate nella parola e lettere che rimangono
    usedLetter = list(dict.fromkeys(parola))
    availableLetter = [letter for letter in AllLetters if letter not in usedLetter]

    #provo le combinazioni di tutte le consonanti disponibili per ricostruire prima e terza parola
    for letter in availableLetter:
        #vedo i casi in cui inizia la prima parola con consonante, 
        #avendo ipotizzato che la seconda lettera della prima parola risulta vocale
        if(isConsonante(letter)):
            first[0] = third[0] = letter
            prima = ''.join(first)
            terza = ''.join(third)
            
            #voglio che sia il programma a capire se funzionerebbe come frase
            #cerca se le parole costruite esistono nel dizionario
            if (prima in prime_parole and terza in terze_parole):
                frase = str(index_frase) + ") " + ''.join(first) + " " + ''.join(second) + " " + ''.join(third) + " " + parola
                index_frase += 1
                print(frase + " " + str(availableLetter))