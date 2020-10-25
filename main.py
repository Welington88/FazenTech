import equipamento
import funcionario
import producao
import produto
import varejista
opcao = 0
while opcao<6:
    opcao = int(input("Digite a opcao:\n1 - Equipamentos\n2 - Funcionario\n3 - Producao\n4 - Produtos\n5 - Varejista\n6 - Sair\n"))
    if opcao==1:
        #equipamentos
        opcaoEquip = int(input("Digite a opcao para Equipamentos:\n1 - Inserir\n2 - Alterar\n3 - Excluir\n4 - Consultar\n"))
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
            equipamento.excluir(cod)
        elif opcaoEquip==4:
            equipConsultar = equipamento.Equipamento
            equipConsultar.consultar(equipConsultar)
        else:
            print("Nenhuma opcao ou opcao invalida escolhida no sistema")
            exit()
        #fim equipamentos
    elif opcao==2:
        # funcionario
        opcaoEquip = int(input("Digite a opcao para Funcionario:\n1 - Inserir\n2 - Alterar\n3 - Excluir\n4 - Consultar\n"))
        if opcaoEquip == 1:
            nome = input("Digite Nome Funcionario:\n")
            cpf = input("Digite CPF Funcionario:\n")
            salario = input("Digite salario Funcionario:\n")
            cargo = input("Digite cargo Funcionario:\n")
            admissao = input("Digite admissao Funcionario:\n")
            nascimento = input("Digite nascimento Funcionario:\n")
            obj = funcionario.Funcionario(nome,cpf,salario,cargo,admissao,nascimento)
            obj.inserir()
        elif opcaoEquip == 2:
            cod = input("Digite Numero do Funcionario:\n")
            nome = input("Digite Nome Funcionario:\n")
            cpf = input("Digite CPF Funcionario:\n")
            salario = input("Digite salario Funcionario:\n")
            cargo = input("Digite cargo Funcionario:\n")
            admissao = input("Digite admissao Funcionario:\n")
            nascimento = input("Digite nascimento Funcionario:\n")
            obj = funcionario.Funcionario(nome, cpf, salario, cargo, admissao, nascimento)
            obj.alterar(cod)
        elif opcaoEquip == 3:
            cod = input("Digite Numero do Funcionario a ser excluido:\n")
            funcionario.excluir(cod)
        elif opcaoEquip == 4:
            relatorio = funcionario.Funcionario
            relatorio.consultar(relatorio)
        else:
            print("Nenhuma opcao ou opcao invalida escolhida no sistema")
            exit()
        # fim funcionario
    elif opcao==3:
        # Producao de leite
        opcaoEquip = int(input("Digite a opcao para Producao:\n1 - Inserir\n2 - Alterar\n3 - Excluir\n4 - Consultar\n"))
        if opcaoEquip == 1:
            especie = input("Digite Raca Especie da vaca:\n")
            data_ultima_ordenha = input("Digite Ultima Ordenha da vaca:\n")
            temperatura_do_leite = input("Digite temperatura do leite:\n")
            produtividade_de_cada_quarto = input("Digite Produtividade cada quarto:\n")
            inseminacao = input("Digite Inseminacao da vaca:\n")
            estimativa_do_parto = input("Digite estimativa de parto:\n")
            secagem_esperada = input("Digite Secagem Esperada:\n")
            minutos_de_ruminacao_por_dia = input("Digite Ruminacao da vaca:\n")

            obj = producao.ProducaoLeite(especie,data_ultima_ordenha,temperatura_do_leite,produtividade_de_cada_quarto,inseminacao,estimativa_do_parto,secagem_esperada,minutos_de_ruminacao_por_dia)
            obj.inserir()
        elif opcaoEquip == 2:
            cod = input("Digite Numero do Funcionario:\n")
            especie = input("Digite Raca Especie da vaca:\n")
            data_ultima_ordenha = input("Digite Ultima Ordenha da vaca:\n")
            temperatura_do_leite = input("Digite temperatura do leite:\n")
            produtividade_de_cada_quarto = input("Digite Produtividade cada quarto:\n")
            inseminacao = input("Digite Inseminacao da vaca:\n")
            estimativa_do_parto = input("Digite estimativa de parto:\n")
            secagem_esperada = input("Digite Secagem Esperada:\n")
            minutos_de_ruminacao_por_dia = input("Digite Ruminacao da vaca:\n")

            obj = producao.ProducaoLeite(especie,data_ultima_ordenha,temperatura_do_leite,produtividade_de_cada_quarto,inseminacao,estimativa_do_parto,secagem_esperada,minutos_de_ruminacao_por_dia)
            obj.alterar(cod)
        elif opcaoEquip == 3:
            cod = input("Digite Numero do Funcionario a ser excluido:\n")
            producao.excluir(cod)
        elif opcaoEquip == 4:
            relatorio = producao.ProducaoLeite
            relatorio.consultar(relatorio)
        else:
            print("Nenhuma opcao ou opcao invalida escolhida no sistema")
            exit()
        # fim producao de leite
    elif opcao==4:
        # produto
        opcaoEquip = int(input("Digite a opcao para Produto:\n1 - Inserir\n2 - Alterar\n3 - Excluir\n4 - Consultar\n"))
        if opcaoEquip == 1:
            nome = input("Digite Nome do Produto:\n")
            tipo = input("Digite Tipo do Produto:\n")
            qtd_em_estoque = input("Digite Quantidade Produto:\n")
            preco = input("Digite Preco do Produto:\n")
            obj = produto.Produto(nome,tipo,qtd_em_estoque,preco)
            obj.inserir()
        elif opcaoEquip == 2:
            cod = input("Digite Numero do Produto:\n")
            nome = input("Digite Nome do Produto:\n")
            tipo = input("Digite Tipo do Produto:\n")
            qtd_em_estoque = input("Digite Quantidade Produto:\n")
            preco = input("Digite Preco do Produto:\n")
            obj = produto.Produto(nome, tipo, qtd_em_estoque, preco)
            obj.alterar(cod)
        elif opcaoEquip == 3:
            cod = input("Digite Numero do Produto a ser excluido:\n")
            produto.excluir(cod)
        elif opcaoEquip == 4:
            relatorio = produto.Produto
            relatorio.consultar(relatorio)
        else:
            print("Nenhuma opcao ou opcao invalida escolhida no sistema")
            exit()
        # fim produto
    elif opcao==5:
        opcaoEquip = int(input("Digite a opcao para Varejo/Vendas:\n1 - Inserir\n2 - Alterar\n3 - Excluir\n4 - Consultar\n5 - Vendas\n"))
        if opcaoEquip == 1:
            nome = input("Digite Nome do Produto:\n")
            pf_pj = input("Digite pf pj do Produto:\n")
            status = input("Digite Status do Produto:\n")
            obj = varejista.Varejista(nome,pf_pj,status)
            obj.inserir()
        elif opcaoEquip == 2:
            cod = input("Digite Numero do Produto:\n")
            nome = input("Digite Nome do Produto:\n")
            pf_pj = input("Digite pf pj do Produto:\n")
            status = input("Digite Status do Produto:\n")
            obj = varejista.Varejista(nome, pf_pj, status)
            obj.alterar(cod)
        elif opcaoEquip == 3:
            cod = input("Digite Numero do Produto a ser excluido:\n")
            varejista.exclui(cod)
        elif opcaoEquip == 4:
            relatorio = varejista.Varejista
            relatorio.consultar(relatorio)
        elif opcaoEquip == 5:
            cod_produto = input("Digite Codigo do Produto:\n")
            cod_varejista = input("Digite Codigo do Varejista:\n")
            qtd = input("Digite QTD da Venda:\n")
            obj = varejista.Varejista
            obj.venda(varejista,cod_produto,cod_varejista,qtd)
        else:
            print("Nenhuma opcao ou opcao invalida escolhida no sistema")
            exit()
    elif opcao==6:
        print("Obrigado por utilizar o sistema!!!")
    else:
        print("Nenhuma opcao ou opcao invalida escolhida no sistema")
        exit()