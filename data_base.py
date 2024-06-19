import mysql.connector
from mysql.connector import Error


def criar_banco_e_tabelas():
    try:
        # Conexão inicial sem selecionar um banco de dados
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='leticia',  # Substitua por seu usuário
            password='080507'  # Substitua por sua senha
        )

        if conexao.is_connected():
            cursor = conexao.cursor()

            # Comandos SQL para criar banco de dados e tabelas
            comandos_sql = """
            CREATE DATABASE IF NOT EXISTS hospital;
            USE hospital;
            CREATE TABLE IF NOT EXISTS pacientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                nome VARCHAR(100) NOT NULL,
                idade INT NOT NULL,
                endereco VARCHAR(200) NOT NULL,
                telefone VARCHAR(15) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS medicos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                crm VARCHAR(10) UNIQUE NOT NULL,
                nome VARCHAR(100) NOT NULL,
                especialidade VARCHAR(100) NOT NULL,
                telefone VARCHAR(15) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS agendamentos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                paciente_id INT,
                medico_id INT,
                data DATETIME NOT NULL,
                FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
                FOREIGN KEY (medico_id) REFERENCES medicos(id)
            );
            CREATE TABLE IF NOT EXISTS procedimentos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                paciente_id INT,
                medico_id INT,
                descricao TEXT NOT NULL,
                data DATETIME NOT NULL,
                FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
                FOREIGN KEY (medico_id) REFERENCES medicos(id)
            );
            """

            # Executa cada comando SQL separadamente
            for comando in comandos_sql.split(';'):
                if comando.strip():  # Ignora comandos vazios
                    cursor.execute(comando)

            print("Banco de dados e tabelas criados com sucesso!")
    except Error as e:
        print(f"Erro ao criar banco de dados ou tabelas: {e}")
    finally:
        if (conexao.is_connected()):
            cursor.close()
            conexao.close()


if __name__ == "__main__":
    criar_banco_e_tabelas()