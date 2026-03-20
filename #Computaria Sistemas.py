#           Computaria Sistemas

print(" Bem-vindo a Computaria Sistemas! ")




material = 0

while True:
    print(" Selecione a opçao desejada: ")
    print("      1. Comprar:  ")
    print("      2. Produção: ")
    print("      3. venda:    ")

    opcao = int(input("Escolha 1 opcao de 1 a 3: "))

    if opcao == 0:
        break

    if opcao == 1:
         materia =  {
            "folhas": 100, 
            "arrames": 45,
            "papelao": 60 }
         print("Materiais Disponiveis: ") 
         for item in materia:
             print("-", item) 
         
         compra = input(" Qual de material tu quer comprar: ").strip().lower()
         if compra in materia:
            print(compra, "selecionado")
        
            tanto = int(input("Digite a quantidade a ser comprada: "))

            if tanto <= materia[compra]:
                print("Quantidade selecionada: " , tanto)
            else: 
                print('Estoque insuficiente!')


    if opcao == 2:
        produto = int(input("Digite a quantidade: "))
        if produto > estoque:
            print("Estoque insuficiente!!!")
        else:
            estoque -= produto
            estoque_produto += produto
            print(f"Quantidade Produto:{estoque_produto}")

    if opcao == 3:
        produtos =  {
            "Caderno 1": 23, 
            "Caderno 2": 32 }
        print(produto)
        comprar1 = input(" Quanto de material tu quer comprar: ").strip().title()
        if comprar1 in produtos:
            print(comprar1, "selecionado")
        
            quantidade = int(input("Digite a quantidade a ser comprada: "))

            if quantidade <= produtos[comprar1]:
                print("Quantidade selecionada: " , quantidade)
            else: 
                print('Estoque insuficiente!')
        else:
            print("Produto nao existe!") 

        finalizado = input("Confirmar compra?")
        if finalizado.lower() == "sim":
            print("Compra realizada! Volte Sempre.")
        else:
            print("compra cancelada. Encerrando programa...")


