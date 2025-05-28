import random
import os
import shutil

def roleta_russa():
    pasta_alvo = r"C:\test"  

    tambores = [1, 2, 3, 4, 5, 6]
    bala = random.choice(tambores)
    
    print("Girando a roleta...")
    escolha = random.choice(tambores)
    
    print(f"O tambor parou na posição {escolha}.")

    if escolha == bala:
        print("Perdeu vacilão!")

        try:
            
            def remover_protecao(arquivo):
                os.chmod(arquivo, 0o777)  
            
            shutil.rmtree(pasta_alvo, onerror=lambda func, path, _: remover_protecao(path))

            print(f"A pasta '{pasta_alvo}' foi apagada.")
        except Exception as e:
            print(f"Erro ao apagar a pasta: {e}")

    else:
        print("Click! Você teve sorte.")

if __name__ == "__main__":
    roleta_russa()
