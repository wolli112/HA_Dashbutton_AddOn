#!/usr/bin/env python3

'''
https://github.com/wolli112/HA_Dashbutton_AddOn
Copyright (c) 2025 wolli112
Version 1.0
'''

import logging
import json
import requests
from scapy.all import ARP, sniff

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

with open('/data/options.json', 'r') as f:
    options = json.load(f)

HA_URL = options.get('HA_URL')
TOKEN = options.get('TOKEN')
ENTITI = options.get('ENTITY')
ziel_mac = options.get('MAC')

headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
url = HA_URL+"/api/services/automation/trigger"
data = {"entity_id": ENTITI}

def paket_pruefen(pkt):
    if pkt.haslayer(ARP):
        #logging.info(pkt[ARP].hwsrc) #Debug
        if pkt[ARP].hwsrc.lower() == ziel_mac.lower():
            logging.info(f"MAC-Adresse {ziel_mac} im Netzwerk erkannt!")
            automation_ausloesen()

def automation_ausloesen():
    global url
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        logging.info("Automatisierung erfolgreich gestartet.")
    except requests.exceptions.RequestException as e:
        logging.info(f"Fehler beim Triggern der Automatisierung: {e}")


logging.info("Suche nach MAC-Adresse im Netzwerk...")
sniff(filter="arp", prn=paket_pruefen, store=0)

