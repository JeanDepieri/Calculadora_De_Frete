def FreteFinal(Nome_Empresa,Peso, KmTotal, PedagioTotal):
    Nome_Empresa = str(Nome_Empresa)
    Peso = float(Peso)
    KmTotal = float(KmTotal)
    PedagioTotal = float(PedagioTotal)
    frete = 0

    if  KmTotal <= 100:
        
        frete = (5 * KmTotal) + PedagioTotal

    elif KmTotal >= 100:

        frete = (5.5 * KmTotal) + PedagioTotal 

    return frete

def gerar_id():
    try:
        with open("frete_resultado.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            ids = [int(linha.strip().split(":")[1]) for linha in linhas if "Frete ID" in linha]
            return max(ids) + 1 if ids else 1
    except FileNotFoundError:
        return 1

def salvar_em_txt(id_frete,nome_Empresa, peso, km, pedagio, frete):
    with open("frete_resultado.txt", "a") as arquivo:
        arquivo.write(f"Frete ID: {id_frete}\n")
        arquivo.write(f"nome_Empresa: {nome_Empresa}\n")
        arquivo.write(f"Peso: {peso} kg\n")
        arquivo.write(f"Distancia: {km} km\n")
        arquivo.write(f"Pedagio: R${pedagio}\n")
        arquivo.write(f"Valor do frete: R${frete:.2f}\n")
        arquivo.write("-" * 30 + "\n")

def buscar_frete_por_id(id_procurado):
    try:
        with open("frete_resultado.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            frete_info = []
            encontrado = False

            for linha in linhas:
                if f"Frete ID: {id_procurado}" in linha:
                    encontrado = True
                    frete_info.append(linha)
                elif encontrado:
                    if "-" in linha:
                        break
                    frete_info.append(linha)

            if frete_info:
                print("\n Informações do Frete:")
                for info in frete_info:
                    print(info.strip())
            else:
                print("Frete não encontrado.")

    except FileNotFoundError:
        print("Arquivo de fretes não encontrado.")

def apagar_frete_por_id(id_procurado):
    try:
        with open("frete_resultado.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        novo_conteudo = []
        dentro_do_bloco = False

        for linha in linhas:
            if f"Frete ID: {id_procurado}" in linha:
                dentro_do_bloco = True
                continue
            if dentro_do_bloco:
                if "-" in linha:
                    dentro_do_bloco = False
                    continue
                continue
            novo_conteudo.append(linha)

        with open("frete_resultado.txt", "w") as arquivo:
            arquivo.writelines(novo_conteudo)

        print(f"Frete ID {id_procurado} apagado com sucesso!")

    except FileNotFoundError:
        print("Arquivo de fretes não encontrado.")

def menu():
    while True:
        print("\n=== MENU FRETE ===")
        print("1 - Criar novo frete")
        print("2 - Consultar frete por ID")
        print("3 - Sair")
        print("4 - Apagar frete por ID")
        print("===================")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_Empresa = input("Nome da empresa: ")
            Peso = input("Peso da máquina (kg): ")
            KmTotal = input("Distância total (km): ")
            PedagioTotal = input("Total em pedágios (R$): ")

            valor_frete = FreteFinal(nome_Empresa,Peso, KmTotal, PedagioTotal)
            id_frete = gerar_id()

            salvar_em_txt(id_frete,nome_Empresa, Peso, KmTotal, PedagioTotal, valor_frete)
            print(f"\nFrete salvo com ID: {id_frete}")
            print(f"Valor final do frete: R${valor_frete:.2f}")

        elif opcao == "2":
            id_procurado = input("Digite o ID do frete: ")
            buscar_frete_por_id(id_procurado)

        elif opcao == "3":
            print("Saindo...")
            break
        elif opcao == "4":
            apagar_frete_por_id(input("Digite o ID do frete a ser apagado: "))
            apagar_frete_por_id(id_procurado)   
        
        else:
            print("Opção inválida. Tente novamente.")

menu()
