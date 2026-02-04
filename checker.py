import whois
import datetime
import requests
import os

# DAFTAR DOMAIN DANONE/SN
DOMAINS = [
    "danone.co.id", "icaresn.co.id", "nutricia.co.id", "nutrishop.co.id", 
    "bebeclub.co.id", "nutriclub.co.id", "danone.id", "vms-sn.id", 
    "daninaportal.id", "minumvit.co.id", "sehataqua.co.id", "mizone.co.id", 
    "sarihusada.co.id", "generasimaju.co.id", "daiaccess.co.id", 
    "nutriciaprofessional.id", "adop.co.id", "diom.co.id", "snlogvms.co.id", 
    "aqua.co.id", "optima-system.co.id", "danhrtalent.id", "snqfs.co.id", 
    "sehataqua.com", "nutriday.co.id", "teguklevite.co.id", "actimel.co.id", 
    "activia.co.id", "dancommunity.com", "aquadashboard.co.id", "sgm.id", 
    "adaaqua.co.id", "nutriciaprofessional.co.id", "minumvit.com", "aqua.com", 
    "fortifit.id", "aquadnc.com", "akuanaksgm.co.id", "akuanaksgm.com", 
    "aqua242.com", "bebebook.co.id", "temukanindonesiamu.com", "adaaqua.com", 
    "adaaqua.id", "aquadnc.co.id", "aquaitsinme.co.id", "aquaitsinme.com", 
    "aquamenyapa.co.id", "aquamenyapa.com", "bagaikanair.co.id", "bagaikanair.id", 
    "bijakberplastik.co.id", "bijakberplastik.com", "itsinme.co.id", 
    "kebaikanhidup.co.id", "kebaikanhidup.com", "mizone.id", "museumair.co.id", 
    "museum-air.co.id", "museumair.com", "museum-air.com", 
    "temukanindonesiamu.co.id", "vit.id", "kasihibu.co.id", "kasihibu.com", 
    "aquanet.co.id", "fresingratis.com", "daiaccess.id", "aqualestari.com", 
    "aquadnc.id", "aquamenyapa.id", "caaya.co.id", "kasihibu.id", 
    "reflections.id", "sehataqua.id", "bebeclub.id", "nutricia.id", 
    "nutriclub.id", "cekberatanak.co.id", "nutriexpert.co.id", "lactamil.co.id", 
    "lactamil.id", "mamacare.co.id", "sarihusada.id", "sgmboard.com", 
    "tanyasgm.co.id", "tanyasgm.com", "tanyasgm.id", "vitalac.co.id", 
    "vitalac.id", "ayomelekgizi.co.id", "nutrisiuntukbangsa.id", "5starnutri.com", 
    "id-otm.danone.com", "makingadifference2022.co.id", "bbl.promo", 
    "bblc.app", "bblc.love", "mynutri.club", "aquadulu.id", 
    "dancommunity.co.id", "fortifit.co.id", "aquadashboard.id", 
    "reflections.co.id", "snlogcontroltower.co.id"
]

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Gagal kirim Telegram: {e}")

print(f"Memulai pengecekan {len(DOMAINS)} domain...")

for dom in DOMAINS:
    try:
        w = whois.whois(dom)
        exp_date = w.expiration_date
        
        if isinstance(exp_date, list):
            exp_date = exp_date[0]
            
        if exp_date:
            days_left = (exp_date - datetime.datetime.now()).days
            
            # Log ke GitHub Console agar bisa dipantau
            print(f"{dom}: {days_left} hari tersisa.")
            
            # Alert jika expired kurang dari 30 hari
            if days_left <= 30:
                msg = f"⚠️ ALERT DOMAIN EXPIRED!\n\nDomain: {dom}\nSisa: {days_left} hari\nExp: {exp_date.date()}"
                send_telegram(msg)
        else:
            print(f"Skipping {dom}: Data expired tidak ditemukan.")
            
    except Exception as e:
        print(f"Error pada {dom}: {e}")

print("Pengecekan selesai.")
