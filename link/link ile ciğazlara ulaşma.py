#!/usr/bin/env python

import os
import subprocess
import time
from time import sleep
import webbrowser

print("""
Öncelikle Bir Ngrok Hesabı Açıp Dosya İndirmeniz Gerekmekte
Ve o Dosyaya Authen Tokenininiz Sadece Birkez Girceksiniz
Tekrardan Girmenize Gerek yok Sonraki İşlemleri Hızlı yaparsınız
""")

print("Araç Çalıştırılıyor")
sleep(1)

if not os.path.exists("Storm-Breaker"):
    print("Hata: 'Storm-Breaker' klasörü bulunamadı!")
    exit(1)

os.chdir("Storm-Breaker")

print("Sanal ortam kuruluyor...")
sleep(1)
subprocess.run(["python3", "-m", "venv", ".venv"])
sleep(1)
print("Gerekli Kütüphaneler İndiriliyor (Sanal ortam üzerinden)...")
pip_path = os.path.join(".venv", "bin", "pip")
if os.name == "nt":  # Windows desteği için (gerekirse)
    pip_path = os.path.join(".venv", "Scripts", "pip.exe")

subprocess.run([pip_path, "install", "-r", "requirements.txt"])
print("Araç çalıştırılıyor...")
sleep(1)
print("Ngrok aktifleştiriliyor ve sunucu açılıyor...")
webbrowser.open("http://127.0.0.1:2525")