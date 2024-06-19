# hospital_db.py

import mysql.connector
from mysql.connector import Error



# Configuração da conexão ao MySQL
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='hospital',
            user='leticia',    # Substitua por seu usuário
            password='080507'   # Substitua por sua senha
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Função para adicionar um novo paciente
def adicionar_paciente(conexao, cpf, nome, idade, endereco, telefone):
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO pacientes (cpf, nome, idade, endereco, telefone) VALUES (%s, %s, %s, %s, %s)",
                       (cpf, nome, idade, endereco, telefone))
        conexao.commit()
        print("Novo paciente cadastrado com sucesso!")
    except Error as e:
        if "UNIQUE" in str(e):
            print("Operação falhou: paciente já cadastrado.")
        else:
            print(f"Erro ao adicionar paciente: {e}")

# Função para adicionar um novo médico
def adicionar_medico(conexao, crm, nome, especialidade, telefone):
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO medicos (crm, nome, especialidade, telefone) VALUES (%s, %s, %s, %s)",
                       (crm, nome, especialidade, telefone))
        conexao.commit()
        print("Novo médico cadastrado com sucesso!")
    except Error as e:
        if "UNIQUE" in str(e):
            print("Operação falhou: médico já cadastrado.")
        else:
            print(f"Erro ao adicionar médico: {e}")

# Função para pesquisar um paciente por CPF
def pesquisar_paciente(conexao, cpf):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM pacientes WHERE cpf = %s", (cpf,))
        paciente = cursor.fetchone()
        if paciente:
            print("Paciente encontrado:", paciente)
        else:
            print("Operação falhou: paciente não encontrado.")
    except Error as e:
        print(f"Erro ao pesquisar paciente: {e}")

# Função para pesquisar um médico por CRM
def pesquisar_medico(conexao, crm):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM medicos WHERE crm = %s", (crm,))
        medico = cursor.fetchone()
        if medico:
            print("Médico encontrado:", medico)
        else:
            print("Operação falhou: médico não encontrado.")
    except Error as e:
        print(f"Erro ao pesquisar médico: {e}")

# Função para excluir um paciente por CPF
def excluir_paciente(conexao, cpf):
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM pacientes WHERE cpf = %s", (cpf,))
        conexao.commit()
        if cursor.rowcount > 0:
            print("Registro de paciente excluído com sucesso!")
        else:
            print("Operação falhou: paciente não encontrado.")
    except Error as e:
        print(f"Erro ao excluir paciente: {e}")

# Função para excluir um médico por CRM
def excluir_medico(conexao, crm):
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM medicos WHERE crm = %s", (crm,))
        conexao.commit()
        if cursor.rowcount > 0:
            print("Registro de médico excluído com sucesso!")
        else:
            print("Operação falhou: médico não encontrado.")
    except Error as e:
        print(f"Erro ao excluir médico: {e}")

# Função para agendar consulta
def agendar_consulta(conexao, paciente_id, medico_id, data):
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO agendamentos (paciente_id, medico_id, data) VALUES (%s, %s, %s)",
                       (paciente_id, medico_id, data))
        conexao.commit()
        print("Consulta agendada com sucesso!")
    except Error as e:
        print(f"Erro ao agendar consulta: {e}")

# Função para registrar procedimento médico
def registrar_procedimento(conexao, paciente_id, medico_id, descricao, data):
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO procedimentos (paciente_id, medico_id, descricao, data) VALUES (%s, %s, %s, %s)",
                       (paciente_id, medico_id, descricao, data))
        conexao.commit()
        print("Procedimento registrado com sucesso!")
    except Error as e:
        print(f"Erro ao registrar procedimento: {e}")

# Função para encerrar a conexão
def encerrar_conexao(conexao):
    if conexao.is_connected():
        conexao.close()
