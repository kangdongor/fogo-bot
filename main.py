import cloudscraper
import time
import random

wallet_address = "ISI_WALLET_KAMU"
faucet_url = "https://faucet.fogo.io/api/faucet"
payload = {"address": wallet_address}

# Load proxies
with open("proxies.txt") as f:
    proxies_list = [line.strip() for line in f if line.strip()]

def get_random_proxy():
    proxy = random.choice(proxies_list)
    return {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

def claim_faucet():
    proxy = get_random_proxy()
    print(f"🔁 Using proxy: {proxy['http']}")
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.post(faucet_url, json=payload, proxies=proxy, timeout=15)
        if response.status_code == 200:
            print("✅ Claimed successfully!", response.json())
        elif response.status_code == 429:
            print("⚠️ Too many requests. Try later.")
        else:
            print(f"❌ Status {response.status_code}: {response.text}")
    except Exception as e:
        print("❌ Error:", e)

# Loop tiap 10 menit
while True:
    claim_faucet()
    time.sleep(600)
