print("Program by Wojtekb30, Bird Tech, 06.01.2024, v1.0")
print("Visit https://birdtech.pl")
print("Welcome! This program allows you to encrypt messages inside images!")
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.title("RenderBird")
root.withdraw()
print("Choose image file to open:")
pliknazwa = filedialog.askopenfilename();
try:
    im = Image.open(pliknazwa).convert('RGBA')
    pix = im.load()
    szerokosc, wysokosc = im.size
except:
    print("Not an image! Try again!")
    input("Press ENTER/RETURN to close")
    exit()


def koduj(pix, draw, kanwa, szerokosc, wysokosc, tekst, rozmiarpliku):
    x=0
    y=0
    n=0
    znak = 0
    blokada = False
    testpiksel = True
    while (x<szerokosc and y<wysokosc):
        r,g,b,t = pix[x,y]
        if testpiksel == True:
            draw.point((x, y), fill=(r,g,b,253))
            testpiksel = False
            x=x+1
        if n<rozmiarpliku and blokada == False:
            tbin = str(bin(ord(tekst[n])))
            n=n+1
            #print(tbin)
            tbin=tbin[2:]
            while len(tbin)<8:
                tbin="0"+tbin
            if len(tbin)>8:
                tbin="00111111"
            #print(tbin)
            blokada = True
        if n>=rozmiarpliku:
            tbin="222222222"
        t = 255-int(tbin[znak])
        draw.point((x, y), fill=(r,g,b,t))
        znak = znak + 1
        if znak >= 8:
            znak = 0
            blokada = False
        
            
        x=x+1
        if x>=szerokosc:
            x=0
            y=y+1
    return pix, draw, kanwa

def dekoduj(pix, szerokosc, wysokosc):
    x=0
    y=0
    n=0
    n2=8
    wynik=""
    testpiksel = True
    while (x<szerokosc and y<wysokosc):
        #print("X:"+str(x)+" Y:"+str(y))
        r,g,b,t = pix[x,y]
        if testpiksel == True:
            if t==253:
                print("Seems fine. Decoding...")
                x=x+1
                testpiksel = False
                r,g,b,t = pix[x,y]
            else:
                return("Incorrect image")
        
        if t==255:
            wynik=wynik+"0"
        elif t==254:
            wynik=wynik+"1"
        else:
            break
        x=x+1
        if x>=szerokosc:
            y=y+1
            x=0
    dlugosc = len(wynik)
    tekst = ""
    #print(wynik)
    while n2<=dlugosc:
        fragment = wynik[n:n2]
        #print(fragment)
        liczba = int(fragment,2)
        #print(liczba)
        tekst=tekst+str(chr(liczba))
        n=n+8
        n2=n2+8
    return tekst

if str(input("Type 1 to decode: ")).strip()=="1":
    #print("Decoding...")
    tekstt = dekoduj(pix, szerokosc, wysokosc)
    print(tekstt)
    print(" ")
    if str(input("Type 1 to save to text file: ")).strip()=="1":
        print("Choose txt file name.")
        doc = open(filedialog.asksaveasfilename(filetypes=[("TXT","*.txt")], defaultextension = "*.txt"),'w')
        doc.write(tekstt)
        doc.close()
    input("Press ENTER/RETURN to end program.")
    exit()
else:
    rozmiar = szerokosc*wysokosc
    rozmiar = rozmiar//8
    print("You can code up to "+str(rozmiar-4)+" letters in this image.")
    if str(input("Type 1 to read from text file: ")).strip()=="1":
        print("Choose txt file.")
        doc = open(filedialog.askopenfilename(),'r')
        tekst = doc.read()
        doc.close()
    else: 
        tekst = str(input("Type text: "))
    #tekst = tekst.replace(" ","_")
    if len(tekst)>=rozmiar:
        tekst = tekst[0:rozmiar-4]
    tekst=tekst+"."
    rozmiarpliku = len(tekst)
    kanwa = Image.new("RGBA", (szerokosc, wysokosc), "white")
    draw = ImageDraw.Draw(kanwa)
    print("Processing...")
    pix, draw, kanwa = koduj(pix, draw, kanwa, szerokosc, wysokosc, tekst, rozmiarpliku)
    print("Done! Choose save destination.")
    zapisfilename = filedialog.asksaveasfilename(filetypes=[("PNG","*.png")], defaultextension = "*.png")
    kanwa.save(zapisfilename)
    #input("Saved. Press ENTER/RETURN to end program.")


        
            
        


