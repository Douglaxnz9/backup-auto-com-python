import shutil
import os
import schedule
import time
from datetime import datetime

# Diretório de origem (a pasta que você quer fazer backup)
origem = r"C:\Users\MARONI PCP-02\Desktop\aqui"  #Lembrar de alterar

# Diretório base onde os backups serão armazenados
destino_base = r"C:\Users\MARONI PCP-02\Desktop\teste"  #Lembrar de alterar

def fazer_backup():
    # Criando um nome único para o backup com data e hora
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destino = os.path.join(destino_base, f"backup_{data_hora}")

    try:
        # Verificando se a pasta de destino já existe
        if os.path.exists(destino):
            print(f"⚠ A pasta de destino já existe. Removendo a pasta...")
            shutil.rmtree(destino)  # Remove a pasta existente
        shutil.copytree(origem, destino)
        print(f"✅ Backup concluído com sucesso! Arquivos salvos em: {destino}")
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

# Agendar para rodar a cada 30 dias às 02:00 da manhã
#schedule.every(30).days.at("02:00").do(fazer_backup)

print("🕒 Aguardando o momento do backup...")

# Rodar o backup imediatamente
fazer_backup()

# Loop para manter o script rodando
while True:
    schedule.run_pending()
    time.sleep(60)  # Verifica a cada minuto
