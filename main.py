import despesasDAO as dp

def main():
  dp.verificar_csv()
  
  while True:
    print("--- GERENCIADOR DE DESPESAS ---")
    print("[1] Ver saldo")
    print("[2] Anotar gastos")
    print("[3] Anotar receita")
    print("[4] Sair")
    op = input("Digite uma opção: ")
    
    if op == "1":
      dp.visualizar_saldo()
    elif op == "2":
      dp.anotar_despesa()
    elif op == "3":
      dp.anotar_receita()
    elif op == "4":
      print("Programa Encerrado")
      break
    else:
      print("Opção Inválida! Digite novamente...")

if __name__ == '__main__':
  main()