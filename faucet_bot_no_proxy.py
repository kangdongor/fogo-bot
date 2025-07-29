import requests
import time

# Alamat wallet Fogo kamu
wallet_address = "4hgVomMpKCSj337gNCRwhcJ9uCNZdC..."

# URL faucet
faucet_url = "https://faucet.fogo.io/api/faucet"

# Header standar
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

# Data request
payload = {
    "address": wallet_address
}

# Fungsi untuk klaim faucet tanpa proxy
def claim_faucet():
    print("🔄 Sending request without proxy...")

    try:
        response = requests.post(faucet_url, json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            print("✅ Faucet claimed successfully!")
            print("Response:", response.json())
        elif response.status_code == 429:
            print("⚠️ Too many requests. Waiting before retrying...")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
    except requests.exceptions.ConnectTimeout:
        print("⏰ Timeout. Server may be slow.")
    except Exception as e:
        print("❌ Unexpected error:", e)

# Looping setiap 10 menit
while True:
    claim_faucet()
    time.sleep(600)
