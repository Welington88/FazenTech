import equipamento
opcao = input("Digite a opcao:\n1 - Equipamentos\n2 - Funcionario\n3 - Producao\n4 - Produtos\n5 - Varejista\n")
if opcao==1:
    #equipamentos
    opcaoEquip = input("Digite a opcao para Equipamentos:\n1 - Inserir\n2 - Alterar\n3 - Excluir\n4 - Consultar\n")
    if opcaoEquip==1:
        nome = input("Digite Nome do Equipamento:\n")
        tipo = input("Digite Tipo do Equipamento:\n")
        equip = equipamento.Equipamento(nome,tipo)
        equip.inserir()    
    elif opcaoEquip==2:
        cod = input("Digite Numero do Equipamento:\n")
        nome = input("Digite Nome do Equipamento:\n")
        tipo = input("Digite Tipo do Equipamento:\n")
        equip = equipamento.Equipamento(nome,tipo)
        equip.alterar(cod)    
    elif opcaoEquip==3:
        cod = input("Digite Numero do Equipamento a ser excluido:\n")
        equip.excluir(cod)
    elif opcaoEquip==4:
        equipConsultar = equipamento.Equipamento
        equipConsultar.consultar(equipConsultar)
    else:
        print("Nenhuma opcao ou opcao invalida escolhida no sistema")
        exit()
    #fim equipamentos
elif opcao==2:
    pass
elif opcao==3:
    pass
elif opcao==4:
    pass
elif opcao==5:
    pass
else:
    print("Nenhuma opcao ou opcao invalida escolhida no sistema")
    exit()