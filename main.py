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
                hospital_db.pesquisar_paciente(conexao, cpf)