q1=int(input("Q1 Puan satış hedefini giriniz: "))
q2=int(input("Q2 Puan satış hedefini giriniz: "))
q3=int(input("Q3 Puan satış hedefini giriniz: "))
q5=int(input("Q5 Puan satış hedefini giriniz: "))
qa=int(input("QA Puan satış hedefini giriniz: "))
qt=int(input("QT ADV Puan satış hedefini giriniz: "))
print("Performans Puanları")
kisiadi=input(str("Kişi Adı: "))
kisiq=int(input("Kişi Q'sunu giriniz: "))
if kisiq == "q1" or kisiq == 1:
    kisi=q1
elif kisiq == "q2" or kisiq == 2:
    kisi=q2
elif kisiq == "q3" or kisiq == 3:
    kisi=q3
elif kisiq == "q5" or kisiq == 5:
    kisi=q5
elif kisiq == "qa" or kisiq == "a":
    kisi=qa
elif kisiq == "qt" or kisiq == "t":
    kisi=qt
else:
    print("hata meydana geldi: code:1 böyle bir q grubu yok")
cagri=int(input("çağrı kalite ortalamasını giriniz: "))
if cagri < 85:
    cagrisonuc=70*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 86:
    cagrisonuc=85*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 87:
    cagrisonuc=86*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 88:
    cagrisonuc=87*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)        
elif cagri < 89:
    cagrisonuc=88*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 90:
    cagrisonuc=89*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 91:
    cagrisonuc=90*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 92:
    cagrisonuc=91*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 93:
    cagrisonuc=92*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 94:
    cagrisonuc=93*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 95:
    cagrisonuc=94*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 96:
    cagrisonuc=95*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 97:
    cagrisonuc=96*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 98:
    cagrisonuc=97*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 99:
    cagrisonuc=98*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 100:
    cagrisonuc=99*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
elif cagri < 101:
    cagrisonuc=100*20/100
    print("Çağrı Kalite puanı:" , cagrisonuc)
else:
    cagrisonuc=20
satis=int(input("Satış Puanını giriniz: "))
satissonuc=satis*100/kisiq
satissonuc1=satissonuc*20/100
if satissonuc1 < 10:
    satissonuc1 = 0
elif satissonuc1 < 20 or satissonuc1 > 9:
    satissonuc1 = 10
elif satissonuc1 < 30 or satissonuc1 > 19:
    satissonuc1 = 20
elif satissonuc1 < 40 or satissonuc1 > 29:
    satissonuc1 = 30
elif satissonuc1 < 50 or satissonuc1 > 39:
    satissonuc1 = 40
elif satissonuc1 < 60 or satissonuc1 > 49:
    satissonuc1 = 50
elif satissonuc1 < 70 or satissonuc1 > 59:
    satissonuc1 = 60
elif satissonuc1 < 80 or satissonuc1 > 69:
    satissonuc1 = 70
elif satissonuc1 < 90 or satissonuc1 > 79:
    satissonuc1 = 80
elif satissonuc1 < 100 or satissonuc1 > 89:
    satissonuc1 = 90
else:
    satissonuc1 = 100
print("Satış puanı : ",satissonuc1)
talepk=int(input("Talep Kalitesini Giriniz: "))
if talepk < 85:
    talepsonuc=70*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 86:
    talepsonuc=85*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 87:
    talepsonuc=86*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 88:
    talepsonuc=87*20/100
    print("Talep Kalite puanı:" , talepsonuc)        
elif talepk < 89:
    talepsonuc=88*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 90:
    talepsonuc=89*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 91:
    talepsonuc=90*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 92:
    talepsonuc=91*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 93:
    talepsonuc=92*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 94:
    talepsonuc=93*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 95:
    talepsonuc=94*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 96:
    talepsonuc=95*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 97:
    talepsonuc=96*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 98:
    talepsonuc=97*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 99:
    talepsonuc=98*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 100:
    talepsonuc=99*20/100
    print("Talep Kalite puanı:" , talepsonuc)
elif talepk < 101:
    talepsonuc=100*20/100
    print("Talep Kalite puanı:" , talepsonuc)
else:
    talepsonuc=20
    print("Talep Kalite puanı:" , talepsonuc)
talep=int(input("Talep Sayısını giriniz: "))
calisma=int(input("Çalışma Gününü Giriniz: "))
talepsay=talep/calisma
if talepsay < 10:
    talepson = 0
elif talepsay < 14:
    talepson = 5*25/100
elif talepsay < 16:
    talepson = 10*25/100
elif talepsay < 18:
    talepson = 15*25/100
elif talepsay < 20:
    talepson = 20*25/100
elif talepsay < 22:
    talepson = 25*25/100
elif talepsay < 24:
    talepson = 30*25/100
elif talepsay < 26:
    talepson = 35*25/100
elif talepsay < 28:
    talepson = 40*25/100
elif talepsay < 30:
    talepson = 45*25/100
elif talepsay < 32:
    talepson = 50*25/100
elif talepsay < 34:
    talepson = 55*25/100
elif talepsay < 36:
    talepson = 60*25/100
elif talepsay < 38:
    talepson = 65*25/100
elif talepsay < 40:
    talepson = 70*25/100
elif talepsay < 42:
    talepson = 75*25/100
elif talepsay < 44:
    talepson = 80*25/100
elif talepsay < 46:
    talepson = 85*25/100
elif talepsay < 48:
    talepson = 90*25/100
elif talepsay < 50:
    talepson = 95*25/100
else:
    talepson = 20
print("Talep Sayısı puanı: " , talepson)
konusma=int(input("Konuşma sürsini giriniz: "))
if konusma < 200:
    konusmasonuc = 50*15/100
elif konusma < 205:
    konusmasonuc = 55*15/100
elif konusma < 210:
    konusmasonuc = 60*15/100
elif konusma < 215:
    konusmasonuc = 65*15/100
elif konusma < 220:
    konusmasonuc = 70*15/100
elif konusma < 226:
    konusmasonuc = 75*15/100
elif konusma < 232:
    konusmason = 80*15/100
elif konusma < 238:
    konusmason = 85*15/100
elif konusma < 244:
    konusmason = 90*15/100
elif konusma < 250:
    konusmason = 95*15/100
elif konusma < 255:
    konusmason = 100*15/100
elif konusma < 260:
    konusmason = 95*15/100
elif konusma < 265:
    konusmason = 90*15/100
elif konusma < 270:
    konusmason = 85*15/100
elif konusma < 276:
    konusmason = 80*15/100
elif konusma < 282:
    konusmason = 75*15/100
elif konusma < 288:
    konusmason = 70*15/100
elif konusma < 294:
    konusmason = 65*15/100
elif konusma < 300:
    konusmason = 60*15/100
elif konusma < 306:
    konusmason = 55*15/100
else:
    konusmason = 50*15/100
print("Konuşma süresi Puanı: ", konusmason)
musterikart=int(input("Müşteri kartı puanını giriniz: "))
if musterikart < 80:
     musterikartsonuc = 79*5/100
elif musterikart < 81:
     musterikartsonuc = 80*5/100
elif musterikart < 82:
     musterikartsonuc = 81*5/100
elif musterikart < 83:
     musterikartsonuc = 82*5/100
elif musterikart < 84:
     musterikartsonuc = 83*5/100
elif musterikart < 85:
     musterikartsonuc = 84*5/100
elif musterikart < 86:
     musterikartsonuc = 85*5/100
elif musterikart < 87:
     musterikartsonuc = 86*5/100
elif musterikart < 88:
     musterikartsonuc = 87*5/100
elif musterikart < 89:
     musterikartsonuc = 88*5/100
elif musterikart < 90:
     musterikartsonuc = 89*5/100
elif musterikart < 91:
     musterikartsonuc = 90*5/100
elif musterikart < 92:
     musterikartsonuc = 91*5/100
elif musterikart < 93:
     musterikartsonuc = 92*5/100
elif musterikart < 94:
     musterikartsonuc = 93*5/100
elif musterikart < 95:
     musterikartsonuc = 94*5/100
elif musterikart < 96:
     musterikartsonuc = 95*5/100
elif musterikart < 97:
     musterikartsonuc = 96*5/100
elif musterikart < 98:
     musterikartsonuc = 97*5/100
elif musterikart < 99:
     musterikartsonuc = 98*5/100
elif musterikart < 100:
     musterikartsonuc = 99*5/100
elif musterikart < 101:
    musterikartsonuc=5
print("Müşteri kartı puanı: ",musterikartsonuc)
cevap=int(input("Cevap Hızını Giriniz: "))
if cevap < 6:
    cevapsonuc=0
elif cevap < 7:
    cevapsonuc=-1
elif cevap < 8:
    cevapsonuc=-2
elif cevap < 9:
    cevapsonuc=-3
elif cevap < 10:
    cevapsonuc=-4
elif cevap < 11:
    cevapsonuc=-5
else:
    cevapsonuc=10
print("Cevap Hızı: -",cevapsonuc)
devamsizlik=int(input("Devamsızlığını Giriniz: "))
if devamsizlik < 2:
    devamsizliksonuc=-1
elif devamsizlik < 3:
    devamsizliksonuc=-2
elif devamsizlik < 4:
    devamsizliksonuc=-3
elif devamsizlik < 5:
    devamsizliksonuc=-4
else:
    devamsizliksonuc=-5
print("Devamsızlık: -",devamsizliksonuc)
login=int(input("Geç Login sayısını giriniz: "))
if login < 4:
    loginsonuc=-1
elif login < 5:
    loginsonuc=-2
elif login < 6:
    loginsonuc=-3
elif login < 7:
    loginsonuc=-4
elif login < 8:
    loginsonuc=-5
else:
    loginsonuc=-10
    print("...........HESAPLANIYOR........")
print("Geç Login Puanı: ",loginsonuc)
print("Devamsızlık: -",devamsizliksonuc)
print("Cevap Hızı: -",cevapsonuc)
print("Müşteri kartı puanı: ",musterikartsonuc)
print("Konuşma süresi Puanı: ", konusmason)
print("Talep Sayısı puanı: " , talepson)
print("Talep Kalite puanı:" , talepsonuc)
print("Satış puanı : ",satissonuc1)
print("Çağrı Kalite puanı:" , cagrisonuc)
round(musterikartsonuc,0)
round(cagrisonuc,0)
round(talepsonuc,0)
round(satissonuc1,0)
finalsonuc=musterikartsonuc+cevapsonuc+devamsizliksonuc+loginsonuc+talepsonuc+satissonuc1+cagrisonuc+talepson+konusmason
if finalsonuc < 65:
    harfnotu="BS"
elif finalsonuc < 75:
    harfnotu="BA"
elif finalsonuc < 85:
    harfnotu="B"
elif finalsonuc < 95:
    harfnotu="ÜB"
else:
    finalsonuc="OB"
print(kisiadi,"'nin Toplam Performans Puanı: ",finalsonuc, "Harf Notu ise: ",harfnotu)