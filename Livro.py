import mysql.connector

# 1. Conectar ao banco
conexao = mysql.connector.connect(
    	   host='localhost',       # ou IP do servidor
    	   user='root',     # ex: 'root'
    	   password='',   # ex: 'admin123'
    	   database='biblioteca'
)

# Cria o objeto responsável por executar comandos SQL dentro dessa conexão.
cursor = conexao.cursor()

# 2. Criar tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livro (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(50),
        autor VARCHAR(50),
        ano INT
    );
''')
# 3. Inserir dados
cursor.execute("INSERT INTO Livro (titulo, autor, ano) VALUES (%s, %s, %s)", ('As 48 leis do poder', 'Robert Greene', 1998))
cursor.execute("INSERT INTO Livro (titulo, autor, ano) VALUES (%s, %s, %s)", ('O príncipe', 'Maquiavel', 1532))
conexao.commit()

# 4. Consultar dados
cursor.execute("SELECT * FROM Livro")
for linha in cursor.fetchall():
    print(linha)

# 5. Fechar a conexão
cursor.close()
conexao.close()


