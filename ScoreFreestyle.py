"""
Kerli Otti ja Grete Rannu

Programmi abi saab hinnata trikipõhiseid spordialasid. Kahte võistlejat hinnatakse
paralleelselt (kuni katsete arvu täitumiseni või katkestuseni), igast paarist võistlejatest üks saab
edasi järgmisesse roundi, kuni selgub võitja (singel elimination süsteem).
Viigi korral otsustab kohtunik, kumb võistleja võidab.
Seadistada on võimalik katsete arvu voorus. Programmi on kirjutatud vaikeväärtusena 3 katset ühele võistlejale. Võistluse keskel on võimalik
katsete arvu muuta vaid enne seda, kui kumbki võistleja ei ole veel ühtegi trikki sooritanud (antud sõidus).
Programm kirjutab protokollid võistlejate tulemustest, katkestustest, jne.
Võimalikud trikid, võistlejate nimed ja pildid saadakse failidest. Nupud genereeritakse ja kohandatakse vastavalt ette antud trikkide nimedele
ja vastavatele punktidele. Nupud jaotatakse 3 veergu.
Kohtunik näeb reaalajas võistleja katsete arvu, miinuseid ja punktisummat.

Selleks, et kohtunikul oleks lihtsam märgata võistlejate vahetust ekraanil on loodud vaheekraanid mõrguannetega vooru ja roundi lõpust.
"""
from easygui import *
from tkinter import *
from datetime import datetime
import tkinter as tk
from PIL import ImageTk, Image
import time

def failist_sonastik(f):  #võtab triki nime ja selle hinde failist
    f=open("trikid.txt", "r", encoding="UTF-8")
    a=[]                                        #tekib kahekordne järjend
    for rida in f:                       #eemaldatakse realõpu märgid
        a+=([rida.strip().split(" ", 1)])              #poolitatakse esimese tühiku juures
    vaartus={}                                  #siia kogutakse sõnastik {triki nimi:hinne}
    j=0
    i=0
    for i in range(len(a)):
        voti= str(a[i][j])
        vaartus[voti]=a[i][j+1]
    return vaartus

def muuda_katseid():
    global katseidA
    global katseidB
    global n_katseid
    if len(katseidA) > 0 or len(katseidB) > 0:
        return msgbox("""Kahjuks ei saa vooru toimumis ajal katsete arvu muuta!
                      Muuda katsete arv peale vooru lõppu!""")
    msg ="Muuda katsete arvu:"
    title = "ScoreFreestyle"
    n_katseid = enterbox(msg, title).upper() 
    while n_katseid == None or n_katseid == "":
        msgbox("Te ei sisetanud midagi!")
        n_katseid = int(enterbox(msg, title))
    while n_katseid.isnumeric() == False:
        msgbox("Sisestus peab olema number!")
        n_katseid = int(enterbox(msg, title))
    else:
        Label(win, text="Lubatud: "+str(n_katseid), foreground="white", background="black").grid(row=10, column=0, pady=(50, 0))
    n_katseid = int(n_katseid)
 
def set_kohtunik():
    global kohtunik
    kohtunik = kohtunik_sisend.get()
    set.destroy()
 
def nupp(nupp, voistleja, trikk):
    A=katseidA.count(1)
    B=katseidB.count(1)
    global tehtud_trikidA
    global tehtud_trikidB
    if voistleja == "a":
        if A>=n_katseid:
            for el in range(len(c)):
                sõnastikA[c[el]].configure(command= lambda :None)
        else:
            tehtud_trikidA.append(trikk)
            a.append(float(nupp))
            lisa_katse("a")
        
    if voistleja == "b":
        if B>=n_katseid:
            for el in range(len(c)):
                sõnastikB[c[el]].configure(command= lambda: None)
        else:
            tehtud_trikidB.append(trikk)
            teine.append(float(nupp))
            lisa_katse("b")
            
def lisa_katse(kellele):# def loendab katseid kuni n_katseid-meni ja
    if kellele == "a":
        katseidA.append(1)
        for el in a:
            "\n".join
            Label(win, text = len(a), foreground="white", background="black"). grid(row = 6, column = 0)
        Label(win, text = sum(a)-miinusedA.count(1), foreground="white", background="black") .grid(row = 8, column = 0)
    if kellele == "b":
        katseidB.append(1)
        for el in teine:
            "\n".join
            Label(win, text = len(teine), foreground="white", background="black"). grid(row = 6, column = 4)
        Label(win, text = sum(teine)-miinusedB.count(1), foreground="white", background="black") .grid(row = 8, column = 4)

    kas_lõpp = kas_vooru_lõpp() #True or False
    if kas_lõpp == True:
        if sum(a) - miinusedA.count(1) == sum(teine) - miinusedB.count(1) and sum(a) - miinusedA.count(1) > 0.0:
            viik()
        elif kellele == "otsus":
            loo_protokollid()
            võitjad_listi()
            update()
        else:
            loo_protokollid()
            võitjad_listi()
            update()
    else:
        pass
def kas_vooru_lõpp(): #Kontrollib kas katsete arv täis või üks või mõmlemad võistlejad katkestasid
    global katkestasA
    global katkestasB
    A=katseidA.count(1)
    B=katseidB.count(1)    
    if A >= n_katseid and B >= n_katseid:
        return True
    elif A>=n_katseid and katkestasB == True: #Kui üks võistlejatest katkesta
        return True
    elif katkestasA == True and B>=n_katseid:
        return True
    elif katkestasA == True and katkestasB == True: #Kui mõlemad võistlejad katkestavad
        return True
    else:
        return False
    
def katkestus(kellele):
    global katkestasA
    global katkestasB
    global a, teine
    global katseidA, katseidB
    if kellele == "a":
        katkestasA = True
        for m in range(n_katseid-len(a)):
            katseidA.append(1)
    elif kellele == "b":
        katkestasB = True
        for m in range(n_katseid-len(teine)):
            katseidB.append(1)
    kas_vooru_lõpp()
    kas_lõpp = kas_vooru_lõpp() #True or False
    if kas_lõpp == True:
        if sum(a) - miinusedA.count(1) == sum(teine) - miinusedB.count(1) and sum(a) - miinusedA.count(1) > 0.0:
            viik()
        elif kellele == "otsus":
            loo_protokollid()
            võitjad_listi()
            update()
        else:
            loo_protokollid()
            võitjad_listi()
            update()  
    
def viik():
    viik_win = Tk()
    viik_win.geometry("{0}x{1}".format(viik_win.winfo_screenwidth(), viik_win.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
    viik_win.title("Uus voor")
    viik_win.configure(background='black')
    Label(viik_win, text="# viigiolukord  - otsusta VÕITJA", font=("hevetica", 50), foreground="white", background="black").grid(columnspan=1, row=2, pady=50, ipadx=0)
    viik_nupp_võitjaA = Button(viik_win, text=võistlejaA, height=10, width= 20, command = lambda: lisapunkt("A", viik_win) , font=("hevetica", 30)).grid(column = 0, row=4, pady=5, padx=50)
    viik_nupp_võitjaB = Button(viik_win, text= võistlejaB, height=10, width= 20, command = lambda: lisapunkt("B", viik_win), font=("hevetica", 30)).grid(column= 1 , row=4, pady=5, padx=0)
      
def lisapunkt(kumb, viik_win):
    viik_win.destroy()
    global a
    global teine
    if kumb == "A":
        a[0]= a[0]+1
    else:
        teine[0]=teine[0]+1
    return lisa_katse("otsus")
    
def loo_protokollid():
    global võistleja
    global tehtud_trikidA, tehtud_trikidB
    summaA = sum(a)
    summaB = sum(teine)
    protokoll = open("protokollid.txt", "a", encoding="UTF-8")
    
    if katkestasA == True:
        protokoll.write("\nVõistleja: " + võistlejaA + ": Katkestas \n")
        protokoll.write("Hinne kokku " + str(summaA - miinusedA.count(1))+ "\n")
    else:
        protokoll.write("\nVõistleja: " + võistlejaA + " Hinded: " + str(a)[1:-1])
        protokoll.write("\nHinnete summa: " + str(summaA))
        protokoll.write("\nMiinuseid kokku: " + str(miinusedA.count(1)))
        protokoll.write("\nHinne kokku " + str(summaA - miinusedA.count(1))+ "\n")
        protokoll.write("Tehtud trikid:" + str(tehtud_trikidA)[1:-1] +"\n")   
    if katkestasB == True:
        protokoll.write("\nVõistleja: " + võistlejaB + ": Katkestas \n")
        protokoll.write("Hinne kokku " + str(summaB - miinusedB.count(1))+ "\n")
    else:
        protokoll.write("\nVõistleja: " + võistlejaB + " Hinded: " + str(teine)[1:-1])
        protokoll.write("\nHinnete summa: " + str(summaB))
        protokoll.write("\nMiinuseid kokku: " + str(miinusedB.count(1)))
        protokoll.write("\nHinne kokku " + str(summaB - miinusedB.count(1))+ "\n")
        protokoll.write("Tehtud trikid: " + str(tehtud_trikidB)[1:-1] +"\n")
    protokoll.close()

def võitjad_listi():
    tulemusA = sum(a)-miinusedA.count(1)
    tulemusB = sum(teine)-miinusedB.count(1)
    if tulemusA > tulemusB:
        võitjad.append(võistlejaA)
    else:
        võitjad.append(võistlejaB)

def update():
    global võitjad
    global võistlejaA, võistlejaB
    global võistleja
    global a, teine
    global tehtud_trikidA, tehtud_trikidB
    tehtud_trikidA = []
    tehtud_trikidB = []
    a=[]             #VõistlejaA hinded
    teine=[]         #VõistlejaB hinded   
    global katseidA
    katseidA=[]
    global katseidB
    katseidB=[]
    global i
    i=0 
    global miinusedA, miinusedB
    miinusedA=[]
    miinusedB=[]
    global img2
    global img1
    global katkestasA, katkestasB
    katkestasA = False
    katkestasB = False
        
    if len(võistleja)<=0:
        return viimaneRound() # kui osalejad otsas tuleb uus round
    elif len(võistleja)== 1:  #Kui osalejate listis järel üks võistleja on tema võitnud
            kuuluta_võitja()
    else:
        uusRound()
        võistlejaA = võistleja.pop(v)
        võistlejaB = võistleja.pop(v)
    
    A=Label(win, text=võistlejaA, foreground="white", background="black", width= 20).grid(column= 1, row=2)
    B=Label(win, text=võistlejaB, foreground="white", background="black", width= 20).grid(column=6, row=2 )

    img1 = ImageTk.PhotoImage(Image.open("./pildid/"+võistlejaA+".png"))
    img2 = ImageTk.PhotoImage(Image.open("./pildid/"+võistlejaB+".png"))
    Label(win, text="PILT", image=img1, height= 150, width= 150, background="black").grid(column=1, row=0, pady=(20, 0))
    Label(win, text="PILT", image=img2, height= 150, width= 150, background="black").grid(column=6, row=0, pady=(20, 0))
       
    Label(win, text = len(a), foreground="white", background="black"). grid(row = 6, column = 0)
    Label(win, text = sum(a)-miinusedA.count(1), foreground="white", background="black").grid(row = 8, column = 0)
    Label(win, text = len(teine), foreground="white", background="black"). grid(row = 6, column = 4)
    Label(win, text = sum(teine)-miinusedB.count(1), foreground="white", background="black") .grid(row = 8, column = 4)
    for el in range(len(c)):
        sõnastikA[c[el]].configure(command = lambda nuppu=b[c[el]], trikk=c[el]:nupp(nuppu, "a", trikk))
        sõnastikB[c[el]].configure(command = lambda nuppu=b[c[el]], trikk=c[el]:nupp(nuppu, "b", trikk))
 
def uusRound():
    round = Tk()
    round.geometry("{0}x{1}".format(round.winfo_screenwidth(), round.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
    round.title("Uus voor")
    round.configure(background='black')
    Label(round, text="# uus voor", font=("hevetica", 50), foreground="white", background="black").grid(column=6, row=2, pady=100, padx=550)
    round_nupp = Button(round, text='ALUSTA', height=2, width= 20, command = lambda: round.destroy()).grid(column=6, row=3, pady=0, padx=0)

def viimaneRound():
    viimane = Tk()
    viimane.geometry("{0}x{1}".format(viimane.winfo_screenwidth(), viimane.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
    viimane.title("Uus voor")
    viimane.configure(background='black')
    Label(viimane, text="# roundi lõpp #", font=("hevetica", 50), foreground="white", background="black").grid(column=6, row=2, pady=100, padx=550)
    viimase_round_nupp1 = Button(viimane, text='ALUSTA uut roundi', height=2, width= 20, command = lambda: uued_võistlejad(viimane)).grid(column=6, row=3, pady=0, padx=0)
    protokoll = open("protokollid.txt", "a", encoding="UTF-8")
    protokoll.write("\nROUNDI LÕPP------------------------------\n")
    protokoll.close()

def uued_võistlejad(viimane):
    global võistleja
    global võitjad 
    võistleja = võitjad
    print("VÕITSID", võitjad)
    protokoll = open("protokollid.txt", "a", encoding="UTF-8")
    protokoll.write("\nROUNDI VÕITSID\n"+ str(võitjad)+ "\n")
    protokoll.close()
    update()
    viimane.destroy()
       
def kuuluta_võitja():
    kuulutus = Tk()
    kuulutus.geometry("{0}x{1}".format(kuulutus.winfo_screenwidth(), kuulutus.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
    kuulutus.title("Võitja selgunud!")
    kuulutus.configure(background='black')
    esimene_koht = võistleja[0]
    Label(kuulutus, text="Võitja on: " + võistleja[0] + "!", font=("hevetica", 42), foreground="white", background="black").grid(column=2, row=2, pady=100, padx=550)
    välju_nupp = Button(kuulutus, text='OK', height=2, width= 20, command = lambda: välju2(kuulutus)).grid(column=2, row=3, pady=0, padx=0)   
    protokoll = open("protokollid.txt", "a", encoding="UTF-8")
    protokoll.write("\nVÕISTLUSE LÕPP------------------------------\n"+"VÕITJA: "+str(esimene_koht)+"\n")
    protokoll.close()
    
def miinus1(kellele):
    if kellele == "a":
        miinusedA.append(int(1))
        Label(win, text = sum(a)-miinusedA.count(1), foreground="white", background="black") .grid(row = 8, column = 0)
    elif kellele == "b":
        miinusedB.append(int(1))
        Label(win, text = sum(teine)-miinusedB.count(1), foreground="white", background="black") .grid(row = 8, column = 4)
    
def välju2(kuulutus):                     # rakendub kui katsete arv on täis
    kuulutus.destroy()
    win.destroy()

def välju1():                     # rakendub kui katsete arv on täis
    win.destroy()
    
"""
____________________________________________  Vaikeväärtused | kuupäev | katsete arv | vaikekohtunik  _____________________________________________________________
"""    

kuupäev_kellaeg = datetime.today()
kohtunik = "Registreerimata kohtunik"               #vaikeväärtus kohtunikul
n_katseid = 3                                      #vaikeväärtus katsete arvul
katkestasA = False    #Kui võistleja katkestab muutub True
katkestasB = False
tehtud_trikidA = []     #Kogutakse sooritatud trikkide nimed
tehtud_trikidB = []

"""
____________________________________________  1. aken ________  Siestus - Entry | Kohtunik  _____________________________________________________________
"""
set = Tk()
set.geometry("{0}x{1}+0+0".format(set.winfo_screenwidth(), set.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
set.title("HINDAMISLEHT")
set.configure(background='black')
img3 = ImageTk.PhotoImage(Image.open("./logo2.png"))  #Võistleja A
Label(set, text="PILT", image=img3, background="black").grid(column=1, row=0, pady=(0, 0))  #Võist

Label(set, text="KOHTUNIK:", foreground="white", background="black").grid(row=4, column=0, padx=(50, 0)) #Kohtunik
kohtunik_sisend = Entry(set,  text="Kohtunik", width=15)
kohtunik_sisend.focus_set()
kohtunik_sisend.grid(column=0, row=5, padx=(50, 0), pady=(15, 0))

sisestus = Button(set, text="Kinnita", width=10, command = lambda: set_kohtunik())
sisestus.grid(row=7, column=0, padx=(50, 0), pady=(15, 0))

set.mainloop( )

"""
____________________________________________________  Võistlejate nimekiri | failist _____________________________________________________________
"""    
f = open("võistlejad.txt", "r", encoding="UTF-8")   #registreerinud võistlejate nimekiri failis#
v=0
võistleja = [] #võistlejate list
for read in f:
    võistlejad = read.upper().strip()#loeb registreerinud võistlejate failist esimese võistleja nime. Peale tsükli läbimist järgmise võistleja.
    võistleja.append(võistlejad)
print("Võistlejad", võistleja)
f.close()

võistlejaA = võistleja.pop(v)
võistlejaB = võistleja.pop(v)
"""
______________________________________  Põhiprogrammi seadistamine | trikid failist, vaikeväärtused ___________________________________________________
"""
b=(failist_sonastik(f)) #sõnastik trikkide ja väärtustega
c=[]                    #list ainult trikkide nimedest 
for element in b:       #lisatakse nuppude (text= .....) muutuja nimendeks
    c.append(element)    
a=[]                    #VõistlejaA hinded
teine=[]                #VõistlejaB hinded   
katseidA=[]             #Mitu katset tehtud on
katseidB=[]
miinusedA=[]            #Miinuste arv
miinusedB=[]
võitjad = []           #Uude vooru pääsevad võistlejad
h=3                    #nuppude kõrgus
i=0                    #index listist lugemiseks (nt c)
r=20                   #nuppude laius
"""
____________________________________________ 1. aken  _____  Aken avaneb siin   ________________________________________
"""          
win = Tk()        
win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
win.title("HINDAMISLEHT")
win.configure(background='black')
print("KOHTUNIKUKS REGISTREERUS:", kohtunik.upper())

"""
                                            VÕISTLEJATE seadistamine avatud aknas 

__________________________________________________       Pildid     ______________________________________________________
"""
img1 = ImageTk.PhotoImage(Image.open("./pildid/"+võistlejaA+".png"))  #Võistleja A
img2 = ImageTk.PhotoImage(Image.open("./pildid/"+võistlejaB+".png"))  #Võistleja B
Label(win, text="PILT", image=img1, height= 150, width= 150, background="black").grid(column=1, row=0, pady=(20, 0))  #Võistleja A
Label(win, text="PILT", image=img2, height= 150, width= 150, background="black").grid(column=6, row=0, pady=(20, 0))  #Võistleja B
"""
__________________________________________________    Võistleja    A   ____________________________________________________
"""
Label(win, text="VÕISTLEJA A:", foreground="white", background="black").grid(column = 1, row=1, pady=(20, 0))
A=Label(win, text=võistlejaA, foreground="white", background="black", width= 20).grid(column= 1, row=2)

Label(win, text="Tehtud katseid A:", foreground="white", background="black").grid(row = 5, column = 0)
Label(win, text = len(a), foreground="white", background="black"). grid(row = 6, column = 0) #Võistleja A

Label(win, text="Hetkel pukte A:", foreground="white", background="black").grid(row = 7, column = 0)
Label(win, text = sum(a)-miinusedA.count(1), foreground="white", background="black").grid(row = 8, column = 0)

välju= Button(win, text='KATKESTAS', height= h-1, width= 10) 
välju.grid(row=3, column=0, pady=(2, 2), padx=(2, 2))
välju.configure(command= lambda: katkestus("a"))

min = Button(win, text=' LISA -1 ', height= h-1, width= 10)
min.grid(row=4, column=0, pady=(2, 2), padx=(2, 2))
min.configure(command= lambda: miinus1("a"))
"""
__________________________________________________    Võistleja    B   ____________________________________________________
"""
Label(win, text="VÕISTLEJA B:", foreground="white", background="black").grid(column=6, row=1, pady=(20, 0)) #Võistleja B
B=Label(win, text= võistlejaB, foreground="white", background="black", width= 20).grid(column=6, row=2)

Label(win, text="Tehtud katseid B:", height= h, width= 20, foreground="white", background="black").grid(row = 5, column = 4)
Label(win, text = len(teine), foreground="white", background="black"). grid(row = 6, column = 4) #Võistleja B

Label(win, text="Hetkel pukte B:", height= h, width= 20, foreground="white", background="black").grid(row = 7, column = 4)
Label(win, text = sum(teine)-miinusedB.count(1), foreground="white", background="black").grid(row = 8, column = 4)

välju= Button(win, text='KATKESTAS', height= h-1, width= 10)
välju.grid(row=3, column=4, pady=(2, 2), padx=(2, 2))
välju.configure(command= lambda: katkestus("b"))

min = Button(win, text=' LISA -1 ', height= h-1, width= 10)
min.grid(row=4, column=4, pady=(2, 2), padx=(2, 2))
min.configure(command= lambda: miinus1("b"))
"""
__________________________________________ Muud nupud | Muuda katsete arv |Uue roundi nupp_____________________________________________________________
"""
Label(win, text="Lubatud: "+str(n_katseid), foreground="white", background="black").grid(row=10, column=0, pady=(50, 0)) #N;itab lubatud katsete arvu 2 aknas
sisestus2 = Button(win, text="Muuda", width=10, command = lambda: muuda_katseid()).grid(row=12, column=0, pady=(0, 0))
uusRoundNupp = Button(win, text = 'Uus round', height = h-1, width = 10)
uusRoundNupp.grid(row=10, column=9)
uusRoundNupp.configure(command = update)
"""
____________________________________________ Nuppude genereerimine ja seadistamine  ____________________________________________________________________
"""
sõnastikA = {}   
sõnastikB = {}
if len(c) % 3 == 0:
    print('Nuppude arv jagub 3 veeru jaoks täpselt. Jääk on', len(c) % 3)
else:
    s = 3 - ((len(c))%3) 
    print('Nuppude arv ei jagu 3 veeru jaoks täpselt. Jääk on', (len(c))%3)
    print('Lahutame jäägi maha 3-mest ehk 3 -', (len(c))%3)
    print("Lisanuppe tehakse s tk ehk s=", s)
    while s > 0:
        c.append(str(""))
        b[str("")]= 0.0
        s -= 1
    
nuppe = len(c)
ridu= int(nuppe / 3) # i tsüklisse läheb 3 korda vähem kordi
el = 0 # list(range(nuppe))
for i in range(ridu):
    for j in range(3):
        nuppu=b[c[el]]
        trikk = c[el]
        sõnastikA[c[el]] = Button(win, text=c[el], height=h, width= r, command = lambda nuppu=b[c[el]], trikk=c[el]:nupp(nuppu, "a", trikk))
        sõnastikA[c[el]].grid(column=j+ 1, row= i+5, pady=(2, 2), padx=(2, 2))
        sõnastikB[c[el]] = Button(win, text=c[el], height=h, width= r, command = lambda nuppu=b[c[el]], trikk=c[el]:nupp(nuppu, "b", trikk))
        sõnastikB[c[el]].grid(column=j+6, row= i+5, pady=(2, 2), padx=(2, 2))
        j +=1
        el+=1

"""
____________________________________________    Protokollid  ____________________________________________________________________
"""
protokoll = open("protokollid.txt", "a", encoding="UTF-8")  #Sisestab protokolli faili kohtuniku nime
protokoll.write("\n-------------------------------------\n")
protokoll.write(("Hindamislehti täidab kohtunik: " + kohtunik) + "\n")
protokoll.write(str(kuupäev_kellaeg) + "\n")
protokoll.write(("VÕISTLUSES OSALEVAD: "+ "\n" + str(võistleja) + "\n"))
protokoll.close()

win.mainloop( )
