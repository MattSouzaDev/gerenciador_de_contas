from rich.console import Console
from datetime import datetime
from rich.table import Table
from contas import Contas
import csv


ap1 = """
Escolha uma das opcões para continuar:
                             
1 - Adicionar contas
2 - Listar contas

Digite sua escolha: """

ap2 = """
Escolha uma das opcões para continuar:

0 - Sair                      
1 - Adicionar mais contas

Digite sua escolha: """

ap3 = """
Escolha uma das opcões para continuar:

0 - Sair                      
1 - Marcar conta como paga
2 - Ver lista de contas

Digite sua escolha: """

invalido = "❌ Essa opção é invalida"

def main():
    try:
        num: int = int(input(f"{ap1}"))
        print("\n", end="")
    except ValueError:
        print(f"{invalido}")

    match num:
        case 1:
            opcao: int = 1
            while True:
                match opcao:
                    case 1:
                        registrar_contas()
                    case 0:
                        num = 2
                        listar_contas()
                        return num
                    case _:
                        print(f"{invalido}")

                try:
                    opcao: int = int(input(f"{ap2}"))
                    print("\n", end="")
                except ValueError:
                    print(f"{invalido}")

        case 2:
            listar_contas()
            while True:

                try:
                    i: int = int(input(f"{ap3}"))
                    print("\n", end="")
                except ValueError:
                    print(f"{invalido}")

                match i:
                    case 0:
                        break
                    case 1:
                        query = input("Pesquisar Ex. aluguel: ")
                        value = input("Deseja marcar como paga? (sim): ")
                        pagar_conta(query, value)
                    case 2:
                        listar_contas()
                        break
                    case _:
                        print(f"{invalido}")
                    
        case _:
            print(f"{invalido}")

def get_contas():
    while True:
        try: 
            print("Adicione suas contas")
            valor: float = "{:.2f}".format(float(input("Valor: R$ ")))
            descricao = input("Descricao: ")

            data = input("Vencimento (DD/MM/AA): ")
            vencimento = datetime.strptime(data, "%d/%m/%y").date()
            conta_a_pagar = input("A pagar ( sim/não): ")
            if conta_a_pagar == "sim":
                a_pagar = True
            else:
                a_pagar = False

            contas = Contas(valor, descricao, vencimento, a_pagar)
            print("✅ Conta adicionada com sucesso!")
            return contas
        except ValueError:
            print("❌ Registro inválido, tente novamente")


def registrar_contas():
    contas = get_contas()
    with open("contas.csv", "a") as file:
        pen = csv.DictWriter(file, fieldnames=["valor", "descricao", "vencimento", "tipo", "status"])
        pen.writerow({"valor": contas.valor, 
                      "descricao": contas.descricao, 
                      "vencimento": contas.vencimento,
                      "tipo": contas.pagar,
                      "status": contas.status
                      })


def listar_contas():
    tabela = Table(title="Gerenciador de Contas")

    contas_a_pagar = 0
    contas_a_receber = 0
    soma_a_pagar = 0.0
    soma_a_receber = 0.0

    with open("contas.csv") as contas:
        reader = csv.DictReader(contas)

        #configuracao da tabela
        for i in reader.fieldnames:
            tabela.add_column(i)

        for row in sorted(reader, key=lambda x: x["valor"]):
            d_obj = datetime.strptime(row["vencimento"], "%Y-%m-%d").date()
            row["vencimento"] = d_obj.strftime("%d-%m-%Y")

            if row['status'] == "True":
                tabela.add_row(f"R$ {row['valor']}", 
                                f"{row['descricao']}", 
                                f"{row['vencimento']}", 
                                "",
                                f"✅ Pago", style='green')
                
            elif row['status'] == "False" and row["tipo"] == "True":
                row["status"] = "Pendente"
                tabela.add_row(f"R$ {row['valor']}", 
                                f"{row['descricao']}", 
                                f"{row['vencimento']}",
                                f"A pagar",
                                "❌ Pendente",
                                style='red')
                contas_a_pagar += 1
                soma_a_pagar += float(row["valor"])
            else:
                tabela.add_row(f"R$ {row['valor']}", 
                                f"{row['descricao']}", 
                                f"{row['vencimento']}",
                                f"A receber",
                                "❌ Pendente",
                                style='red')
                contas_a_receber += 1
                soma_a_receber += float(row["valor"])

    console = Console()
    console.print(tabela)

    print(f"""
Total a Pagar: {contas_a_pagar} valor total: R${soma_a_pagar}
Total a Receber: {contas_a_receber} valor total: R${soma_a_receber}

Soma total de contas pendentes {contas_a_pagar + contas_a_receber} total: R${soma_a_receber + soma_a_pagar}""")
    


import csv

def pagar_conta(query, value):
    n_csv = []
    
    with open("contas.csv", "r", newline='') as r:
        linhas = csv.DictReader(r)
        cabecalho = linhas.fieldnames

        for linha in linhas:
            if linha['descricao'] == query and value.lower() == "sim":
                linha['status'] = "True"
            n_csv.append(linha)
    
    if value.lower() == "sim":
        with open("contas.csv", "w", newline='') as w:
            writer = csv.DictWriter(w, fieldnames=cabecalho)
            writer.writeheader()
            writer.writerows(n_csv)
        print(f"A conta '{query}' foi atualizada com sucesso! ✅")
    else:
        print("\n🚩 Nenhuma mudança adicionada.")



if __name__ == "__main__":
    main()
