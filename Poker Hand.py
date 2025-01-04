nilaiperingkat = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
nilailist = "2345678910JQKA"
suitelist = "HDCS"
nilaisuite = nilailist+suitelist
loop_program = True

def pokerhand(kartusplit):
    nilaiberurut = ""
    nilaitertinggi = 0
    nilaitertinggi0 = ""
    
    kartutinggi = True
    onepair = False
    twopairs = False
    threeofkind = False
    straight = False
    flush = False
    fourofkind = False
    fullhouse = False
    straightflush = False
    royalflush = False
    nilaikartu = {}
    suitekartu = {}
    
    for i in kartusplit:
        kartusatuan = i
        kartusatuan0 = len(kartusatuan)-1
        if i[:kartusatuan0] in nilailist:
            if i[:kartusatuan0] in nilaikartu.keys():
                nilaikartu[i[:kartusatuan0]] += 1
            else:
                nilaikartu[i[:kartusatuan0]] = 1
        if i[kartusatuan0] in suitelist:
            if i[kartusatuan0] in suitekartu.keys():
                suitekartu[i[kartusatuan0]] += 1
            else:
                suitekartu[i[kartusatuan0]] = 1
                
    if len(nilaikartu) == 5:
        for i in nilaikartu.keys():
            nilaiberurut = nilaiberurut + i
        if nilaiberurut in nilailist and nilaiberurut == "10JQKA" and len(suitekartu) == 1:
            royalflush = True #Royal Flush
            kartutinggi = False
        elif nilaiberurut in nilailist and len(suitekartu) == 1:
            straightflush = True #Straight Flush
            kartutinggi = False
        elif nilaiberurut in nilailist:
            straight = True #Straight
    elif len(nilaikartu) == 4:
        onepair = True #One Pair
        kartutinggi = False
    elif len(nilaikartu) == 3:
        for i in nilaikartu.keys():
            if nilaikartu[i] == 3:
                threeofkind = True #Three Of a kind
                kartutinggi = False
                break
            elif nilaikartu[i] == 2:
                twopairs = True #Two Pairs
                kartutinggi = False
                break
    elif len(nilaikartu) == 2 :
        for i in nilaikartu.keys():
            if nilaikartu[i] == 4 or nilaikartu[i] == 1:
                fourofkind = True #Four Of a kind
                kartutinggi = False
                break
            elif nilaikartu[i] == 3 or nilaikartu[i] == 2:
                fullhouse = True #Full House
                kartutinggi = False
                break
    if len(suitekartu) == 1:
        flush = True
        kartutinggi = False
    
    if onepair:
        print("One Pair")
    elif twopairs:
        print("Two Pairs")
    elif threeofkind:
        print("Three of a Kind")
    elif straight:
        print("Straight")
    elif fullhouse:
        print("Full House")
    elif fourofkind:
        print("Four of a Kind")
    elif straightflush:
        print("Straight Flush")
    elif royalflush:
        print("Royal Flush")
    elif flush:
        print("Flush")
    elif kartutinggi:
        for i in nilaikartu.keys():
            if nilaiperingkat[i] > nilaitertinggi:
                nilaitertinggi = nilaiperingkat[i]
                if i == "J":
                    nilaitertinggi0 = "Jack"
                elif i == "Q":
                    nilaitertinggi0 = "Queen"
                elif i == "K":
                    nilaitertinggi0 = "King"
                elif i == "A":
                    nilaitertinggi0 = "Ace"
                else:
                    nilaitertinggi0 = i
        print("High Card " + nilaitertinggi0)

if __name__ == "__main__":
    while loop_program:
        while True:
            try:
                kartu = input("Masukkan Tangan: ")
                kartusplit = kartu.split()
                if len(kartusplit) < 5:
                    print("Minimal 5 Kartu")
                    raise ValueError
                for i in kartusplit:
                    for j in i:
                        if j not in nilaisuite:
                            raise ValueError
            except ValueError:
                print("Input Tidak Valid")
            else:
                break
        pokerhand(kartusplit)
        while True:
            try:
                loop = input("Ulangi?(y/t): ")
                if loop != "y" and loop != "t":
                    raise ValueError
            except ValueError:
                print("Error: Input Tidak Valid, Pilih y/t.")
            else:
                if loop == "t":
                    print("Terima Kasih Menggunakan Program Ini")
                    loop_program = False
                break