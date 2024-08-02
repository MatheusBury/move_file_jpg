import os
import shutil

def mover_arquivos_jpg(pasta_origem, pasta_destino):
    # Verifica se a pasta de destino existe, se não, cria a pasta
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Caminha por todas as pastas e subpastas
    for root, _, files in os.walk(pasta_origem):
        for file in files:
            # Verifica se o arquivo é .JPG (case-insensitive)
            if file.lower().endswith('.jpg'):
                # Caminho completo do arquivo
                caminho_completo = os.path.join(root, file)
                # Move o arquivo para a pasta de destino
                shutil.move(caminho_completo, os.path.join(pasta_destino, file))
                print(f'Movido: {caminho_completo} -> {os.path.join(pasta_destino, file)}')

# Exemplo de uso
pasta_origem = r"F:\Vidya\Modec\MV33\IA descompactado\subpasta descompactadas"
pasta_destino = r"F:\Vidya\Modec\MV33\IA descompactado\todas as mask 3d"

mover_arquivos_jpg(pasta_origem, pasta_destino)
