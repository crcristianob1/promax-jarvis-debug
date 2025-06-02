from binance.client import Client
import os

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")
client = Client(api_key, api_secret)

# Pega saldo total estimado em USDT
conta = client.get_account()
total_usdt = sum(float(asset['free']) * float(client.get_symbol_ticker(symbol=asset['asset'] + 'USDT')['price'])
                 for asset in conta['balances']
                 if asset['asset'] not in ['USDT', ''] and float(asset['free']) > 0)

# Exibe saldo estimado
banca = round(total_usdt, 2)
print(f"[DEBUG] Saldo atual: ${banca}")
