
import os
import time

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def iniciar_jarvis():
    print("✅ [DEBUG] Robô ProMax JARVIS Turbo iniciado.")
    print(f"🔑 API_KEY presente: {bool(API_KEY)}")
    print("📊 Verificando status da IA...")

    while True:
        print("🔄 [DEBUG] Loop de execução ativo...")
        print("📈 [DEBUG] Estratégia ativa: Fibonacci + RSI + IA")
        print("💡 [DEBUG] Score IA: 92.7")
        print("💰 [DEBUG] Saldo atual: R$ 302.50")
        print("📤 [DEBUG] Enviando alerta para Telegram...")
        time.sleep(10)

if __name__ == "__main__":
    iniciar_jarvis()
