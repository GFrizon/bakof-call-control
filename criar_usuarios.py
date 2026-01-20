from werkzeug.security import generate_password_hash
import pymysql

# Configurações do banco
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '1235'  
DB_NAME = 'controle_ligacoes'

def criar_usuarios():
    """Cria usuários de teste no banco"""
    
    # Conectar ao banco
    conexao = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    
    cursor = conexao.cursor()
    
    # Limpar usuários existentes (opcional)
    print("Limpando usuários antigos...")
    cursor.execute("DELETE FROM usuarios")
    
    # Criar supervisor
    senha_supervisor = generate_password_hash('admin123')
    cursor.execute("""
        INSERT INTO usuarios (nome, email, senha_hash, tipo)
        VALUES (%s, %s, %s, %s)
    """, ('Supervisor', 'supervisor@bakof.com.br', senha_supervisor, 'supervisor'))
    print("✅ Supervisor criado: supervisor@bakof.com.br / admin123")
    
    # Criar consultor Gabriel
    senha_gabriel = generate_password_hash('123456')
    cursor.execute("""
        INSERT INTO usuarios (nome, email, senha_hash, tipo)
        VALUES (%s, %s, %s, %s)
    """, ('Gabriel', 'gabriel@empresa.com', senha_gabriel, 'consultor'))
    print("✅ Consultor criado: gabriel@empresa.com / 123456")
    
    # Criar mais consultores de exemplo (opcional)
    consultores = [
        ('Maria Silva', 'maria@empresa.com', '123456'),
        ('João Santos', 'joao@empresa.com', '123456'),
        ('Ana Costa', 'ana@empresa.com', '123456'),
    ]
    
    for nome, email, senha in consultores:
        senha_hash = generate_password_hash(senha)
        cursor.execute("""
            INSERT INTO usuarios (nome, email, senha_hash, tipo)
            VALUES (%s, %s, %s, %s)
        """, (nome, email, senha_hash, 'consultor'))
        print(f"✅ Consultor criado: {email} / {senha}")
    
    # Salvar mudanças
    conexao.commit()
    
    # Fechar conexão
    cursor.close()
    conexao.close()
    
    print("\n🎉 Todos os usuários foram criados com sucesso!")
    print("\nPara fazer login, use:")
    print("Supervisor: supervisor@empresa.com / admin123")
    print("Consultores: use qualquer email acima / 123456")

if __name__ == '__main__':
    print("=== Criador de Usuários ===\n")
    
    try:
        criar_usuarios()
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("\nVerifique:")
        print("1. MySQL está rodando?")
        print("2. Banco 'controle_ligacoes' foi criado?")
        print("3. Usuário e senha estão corretos no script?")