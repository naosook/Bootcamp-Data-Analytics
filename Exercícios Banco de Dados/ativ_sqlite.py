import sqlite3

# Conectando ao banco de dados (ou criando, se não existir)
conn = sqlite3.connect('meubanco.db')
cursor = conn.cursor()

# 1. Criação da Tabela "alunos"
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    curso TEXT
)
''')

# 2. Inserir registros na tabela "alunos"
cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (1, 'Maria', 22, 'Engenharia')")
cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (2, 'João', 19, 'Direito')")
cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (3, 'Ana', 21, 'Engenharia')")
cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (4, 'Pedro', 25, 'Medicina')")
cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (5, 'Lucas', 18, 'Ciência da Computação')")
conn.commit()

# 3. Consultas Básicas
# a) Selecionar todos os registros da tabela "alunos"
cursor.execute("SELECT * FROM alunos")
print("Todos os registros da tabela 'alunos':")
print(cursor.fetchall())

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos
cursor.execute("SELECT nome, idade FROM alunos WHERE idade > 20")
print("\nAlunos com mais de 20 anos:")
print(cursor.fetchall())

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
cursor.execute("SELECT nome FROM alunos WHERE curso = 'Engenharia' ORDER BY nome")
print("\nAlunos do curso de Engenharia:")
print(cursor.fetchall())

# d) Contar o número total de alunos na tabela
cursor.execute("SELECT COUNT(*) FROM alunos")
print("\nNúmero total de alunos:")
print(cursor.fetchone()[0])

# 4. Atualização e Remoção
# a) Atualizar a idade de um aluno específico (aluno com id 3)
cursor.execute("UPDATE alunos SET idade = 22 WHERE id = 3")
conn.commit()

# b) Remover um aluno pelo seu ID (aluno com id 5)
cursor.execute("DELETE FROM alunos WHERE id = 5")
conn.commit()

# 5. Criação da Tabela "clientes"
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    saldo FLOAT
)
''')

# Inserindo registros na tabela "clientes"
cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, 'Carlos', 35, 1500.50)")
cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, 'Fernanda', 28, 500.75)")
cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, 'Rafael', 42, 2000.00)")
conn.commit()

# 6. Consultas e Funções Agregadas
# a) Selecionar o nome e a idade dos clientes com idade superior a 30 anos
cursor.execute("SELECT nome, idade FROM clientes WHERE idade > 30")
print("\nClientes com mais de 30 anos:")
print(cursor.fetchall())

# b) Calcular o saldo médio dos clientes
cursor.execute("SELECT AVG(saldo) FROM clientes")
print("\nSaldo médio dos clientes:")
print(cursor.fetchone()[0])

# c) Encontrar o cliente com o saldo máximo
cursor.execute("SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1")
print("\nCliente com o saldo máximo:")
print(cursor.fetchone())

# d) Contar quantos clientes têm saldo acima de 1000
cursor.execute("SELECT COUNT(*) FROM clientes WHERE saldo > 1000")
print("\nNúmero de clientes com saldo acima de 1000:")
print(cursor.fetchone()[0])

# 7. Atualização e Remoção com Condições
# a) Atualizar o saldo de um cliente específico (cliente com id 1)
cursor.execute("UPDATE clientes SET saldo = 1600.00 WHERE id = 1")
conn.commit()

# b) Remover um cliente pelo seu ID (cliente com id 2)
cursor.execute("DELETE FROM clientes WHERE id = 2")
conn.commit()

# 8. Junção de Tabelas (Tabela "compras")
# Criação da tabela "compras"
cursor.execute('''
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    produto TEXT,
    valor REAL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
''')

# Inserindo registros na tabela "compras"
cursor.execute("INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, 'Notebook', 2500.00)")
cursor.execute("INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 3, 'Celular', 1200.00)")
conn.commit()

# Consulta para exibir o nome do cliente, o produto e o valor de cada compra
cursor.execute('''
SELECT clientes.nome, compras.produto, compras.valor 
FROM compras 
JOIN clientes ON compras.cliente_id = clientes.id
''')
print("\nCompras realizadas pelos clientes:")
print(cursor.fetchall())

# Fechando a conexão
conn.close()
