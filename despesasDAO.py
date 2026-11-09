import csv
import os

def visualizar_saldo():
  pass

def anotar_despesa():
  while True:
    try:
      valor = float(input("Digite o valor da despesa: ").replace(",", "."))
      if valor <= 0:
        print("Digite um valor maior ou igual a zero!")
        continue
      valor *= -1

      descricao = input("Digite a descrição: ")

      verificar_csv()
      with open("despesas.csv", "a", newline="", encoding="utf-8") as arq:
        c = csv.writer(arq)
        c.writerow([valor, descricao])

      break

    except ValueError:
      print("Valor Inválido! Digite novamente...")


  
    
def anotar_receita():
  pass

def verificar_csv():
  if not os.path.exists("despesas.csv"):
    open("despesas.csv", "w")

  if os.path.getsize("despesas.csv") == 0:
    with open("despesas.csv", "w", newline="", encoding="utf-8") as arq:
      c = csv.writer(arq)
      c.writerow(["valor", "descricao"])
