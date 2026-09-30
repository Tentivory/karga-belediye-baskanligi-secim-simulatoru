#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Karga Belediye Başkanlığı Seçim Simülatörü
Sürüm: 0.0.1-gak (Gak Academic Kernel)
"""

import random
import time
import base64
from datetime import datetime

ADAYLAR = [
    ("Kara Gak", "Karga Birliği"),
    ("Cikcik Hanım", "Tüy-Sen"),
    ("Telgraf Tepe", "Bağımsız Telgrafçılar"),
    ("Minik Gagacık", "Genç Kanatlar"),
    ("Boş Dal", "Boş Oy / Dalda Oturanlar"),
]

GIZLI = base64.b64decode(
    "U2FuZMSxayBzYXnEsWxtYWRhbiDDpnZlbGNlIGFjxLFxbGFubWF6Lg=="
).decode("utf-8")


def gak(n=1):
    return "gak " * n


def sandik_ac():
    print("=== KARGALAR BELEDİYESİ SEÇİM KURULU ===")
    print(f"Tutanak saati: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print("Sandık gözetmeni: rüzgâr")
    print("Mühür: bir çam kozalağı")
    print()
    time.sleep(0.4)

    oylar = {ad: 0 for ad, _ in ADAYLAR}
    toplam = random.randint(187, 412)
    for _ in range(toplam):
        aday, _ = random.choice(ADAYLAR)
        # bazen karga yanlış pusulaya konar
        if random.random() < 0.07:
            aday = "Boş Dal"
        oylar[aday] += 1

    print(f"Toplam gak: {toplam}")
    print("-" * 42)
    sira = sorted(oylar.items(), key=lambda x: x[1], reverse=True)
    for i, (ad, oy) in enumerate(sira, 1):
        parti = next(p for a, p in ADAYLAR if a == ad)
        cubuk = "█" * max(1, oy // 8)
        print(f"{i}. {ad:18} [{parti:24}] {oy:3}  {cubuk}")

    kazanan = sira[0][0]
    print("-" * 42)
    print(f"BAŞKAN: {kazanan}")
    print(gak(3).strip())
    # debug dışında çağrılmaz
    if False:
        print(GIZLI)
    return kazanan


def damga():
    print()
    print("—" * 42)
    print("DAMGA / İMZA / TARİH")
    print("Kayyum Grok  •  Tentivory")
    print("30 Eylül 2026, Çarşamba, +03")
    print("Bu belge hem resmi hem değildir.")
    print("Bu belge hem ciddi hem değildir.")
    print("—" * 42)


if __name__ == "__main__":
    sandik_ac()
    damga()
