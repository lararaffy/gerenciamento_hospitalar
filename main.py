import hospital_db
def menu():
    conexao = hospital_db.criar_conexao()
    if not conexao:
        print("Erro ao conectar ao banco de dados. Saindo do programa.")
        return

    while True:

        try:
            print("\n--- Sistema de Gerenciamento Hospitalar ---")
            print("1. Adicionar Novo Paciente")
            print("2. Adicionar Novo Médico")
            print("3. Pesquisar Paciente por CPF")
            print("4. Pesquisar Médico por CRM")
            print("5. Excluir Paciente pelo CPF")
            print("6. Excluir Médico pelo CRM")
            print("7. Agendar Consulta")
            print("8. Registrar Procedimento Médico")
            print("9. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cpf = input("CPF: ")
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                endereco = input("Endereço: ")
                telefone = input("Telefone: ")
                hospital_db.adicionar_paciente(conexao, cpf, nome, idade, endereco, telefone)

            elif opcao == '2':
                crm = input("CRM: ")
                nome = input("Nome: ")
                especialidade = input("Especialidade: ")
                telefone = input("Telefone: ")
                hospital_db.adicionar_medico(conexao, crm, nome, especialidade, telefone)

            elif opcao == '3':
                cpf = input("CPF: ")
                hospital_db.pesquisar_paciente(conexao, cpf)

            elif opcao == '4':
                crm = input("CRM: ")
                hospital_db.pesquisar_medico(conexao, crm)

            elif opcao == '5':
                cpf = input("CPF: ")
                hospital_db.excluir_paciente(conexao, cpf)

            elif opcao == '6':
                crm = input("CRM: ")
                hospital_db.excluir_medico(conexao, crm)

            elif opcao == '7':
                paciente_id = int(input("ID do Paciente: "))
                medico_id = int(input("ID do Médico: "))
                data = input("Data (AAAA-MM-DD e HH:MM:SS): ")
                hospital_db.agendar_consulta(conexao, paciente_id, medico_id, data)

            elif opcao == '8':
                paciente_id = int(input("ID do Paciente: "))
                medico_id = int(input("ID do Médico: "))
                descricao = input("Descrição do Procedimento: ")
                data = input('Data e Hora (AAAA-MM-DD e HH:MM:SS): ')
                hospital_db.registrar_procedimento(conexao, paciente_id, medico_id, descricao, data)

            elif opcao == '9':
                print("Saindo do programa.")
                break

            else:
                print("Opção inválida. Escolha uma opção de 1 a 9.")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    hospital_db.encerrar_conexao(conexao)

#if _name_ == "_main_":
menu()