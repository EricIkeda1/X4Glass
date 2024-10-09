import os  # Módulo para interagir com o sistema de arquivos
import random  # Módulo para gerar números aleatórios
import barcode  # Módulo para gerar códigos de barras
from barcode.writer import ImageWriter  # Importa o escritor de imagens para os códigos de barras
import qrcode  # Módulo para gerar QR Codes
from datamatrix import DataMatrix  # Módulo para gerar DataMatrix

# Diretório para salvar as imagens geradas
output_dir = 'barcodes'
# Cria o diretório se ele não existir
os.makedirs(output_dir, exist_ok=True)

# Função para gerar um número EAN de 13 dígitos
def generate_ean_base():
    # Retorna uma string de 12 dígitos aleatórios, adicionando um dígito verificador
    return ''.join(str(random.randint(0, 9)) for _ in range(12))

# Função para gerar código UPC (12 dígitos, sendo os 11 primeiros gerados)
def generate_upc_code():
    # Retorna uma string de 11 dígitos aleatórios
    return ''.join(str(random.randint(0, 9)) for _ in range(11))

# Função para gerar código ITF-14 (14 dígitos)
def generate_itf14_code():
    # Retorna uma string de 13 dígitos aleatórios, sendo o último dígito o verificador
    return ''.join(str(random.randint(0, 9)) for _ in range(13))

# Função para gerar código Interleaved 25 (5 dígitos)
def generate_interleaved_25_code():
    # Retorna uma string de 5 dígitos aleatórios
    return ''.join(str(random.randint(0, 9)) for _ in range(5))

# Função para gerar código 128 (10 dígitos)
def generate_code128_code():
    # Retorna uma string de 10 dígitos aleatórios
    return ''.join(str(random.randint(0, 9)) for _ in range(10))

# Função para gerar um QR Code
def generate_qr_code(data, filename):
    # Cria um objeto QR Code
    qr = qrcode.QRCode(
        version=1,  # Versão do QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
        box_size=10,  # Tamanho de cada caixa do QR Code
        border=4,  # Largura da borda
    )
    # Adiciona os dados ao QR Code
    qr.add_data(data)
    qr.make(fit=True)  # Ajusta o QR Code para caber nos dados
    img = qr.make_image(fill='black', back_color='white')  # Cria a imagem
    img.save(filename)  # Salva a imagem no arquivo

# Função para gerar DataMatrix
def generate_datamatrix_code(data, filename):
    # Certifique-se de passar uma string válida para o DataMatrix
    dm = DataMatrix(data)
    img = dm.get_image()  # Gera a imagem do DataMatrix
    img.save(filename)  # Salva a imagem no arquivo

# Função para gerar e salvar diferentes tipos de códigos de barras
def generate_barcode_images():
    # Dicionário que associa tipos de códigos de barras às suas funções geradoras
    barcode_types = {
        'EAN': generate_ean_base,
        'UPC': generate_upc_code,
        'ITF-14': generate_itf14_code,
        'Interleaved 25': generate_interleaved_25_code,
        'Code 128': generate_code128_code
    }

    # Gerar e salvar códigos de barras
    for barcode_type, generator in barcode_types.items():
        for i in range(10):  # Gera 10 exemplos para cada tipo
            code = generator()  # Gera o código
            filename = os.path.join(output_dir, f'{barcode_type}_{code}.png')  # Define o nome do arquivo
            if barcode_type == 'EAN':
                # Gera e salva o código EAN
                ean = barcode.get('ean13', code, writer=ImageWriter())
                ean.save(filename)
            elif barcode_type == 'UPC':
                # Gera e salva o código UPC
                upc = barcode.get('upc', code, writer=ImageWriter())
                upc.save(filename)
            elif barcode_type == 'ITF-14':
                # Gera e salva o código ITF-14
                itf14 = barcode.get('itf', code, writer=ImageWriter())
                itf14.save(filename)
            elif barcode_type == 'Interleaved 25':
                # Gera e salva o código Interleaved 25
                interleaved25 = barcode.get('itf', code, writer=ImageWriter())  # Usar 'itf' para Interleaved 25
                interleaved25.save(filename)
            elif barcode_type == 'Code 128':
                # Gera e salva o código 128
                code128 = barcode.get('code128', code, writer=ImageWriter())
                code128.save(filename)

    # Gerar QR Codes
    for i in range(10):  # Gera 10 QR Codes
        qr_code = f'https://example.com/{i}'  # Exemplo de URL para o QR Code
        qr_filename = os.path.join(output_dir, f'QR_Code_{i}.png')  # Nome do arquivo para o QR Code
        generate_qr_code(qr_code, qr_filename)  # Gera e salva o QR Code

    # Gerar DataMatrix
    for i in range(10):  # Gera 10 DataMatrix
        datamatrix_code = f'DM{i}'  # Usando uma string simples para o DataMatrix
        dm_filename = os.path.join(output_dir, f'DataMatrix_{i}.png')  # Nome do arquivo para o DataMatrix
        generate_datamatrix_code(datamatrix_code, dm_filename)  # Gera e salva o DataMatrix

# Chama a função para gerar as imagens
generate_barcode_images()
# Imprime uma mensagem de confirmação
print("Códigos de barras gerados e salvos na pasta:", output_dir)
