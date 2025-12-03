📞 Bakof Call Control

Plataforma interna desenvolvida para controle comercial, registro de ligações e gestão de desempenho da equipe.
Atualmente implantado e rodando em produção no ambiente da Bakof.

<div align="center">








</div>
🚀 Funcionalidades

✔ Login com permissões (Consultor / Supervisor)
✔ Dashboard com metas, conversão e ranking
✔ Crud de clientes e ligações
✔ Importação de base via CSV
✔ Gestão de usuários
✔ Histórico detalhado de chamadas
✔ Scheduler com envio automático de relatórios
✔ Interface moderna e responsiva

🏗️ Tecnologias Utilizadas

Python + Flask

SQLAlchemy / MySQL

Bootstrap / Jinja2

APScheduler

Waitress (Windows Service)

📌 Estrutura do Projeto
bakof-call-control/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── templates/
├── static/
├── scripts/
├── uploads/    # ignorado no Git
├── logs/       # ignorado no Git
├── BKP/        # ignorado no Git
│
└── legacy/

⚙️ Como executar localmente
git clone https://github.com/SEU_USUARIO/bakof-call-control.git
cd bakof-call-control


Crie e ative ambiente:

python -m venv .venv
.venv\Scripts\activate


Instale dependências:

pip install -r requirements.txt


Configure o .env baseado no .env.example
e execute:

python app.py


Acesse:

👉 http://localhost:5000

📸 Preview do Sistema

Aqui estão algumas telas da aplicação em produção:

🔐 Tela de Login

📊 Dashboard do Consultor

![Consultor](/mnt/data/DASHBOARD CONSULTOR.png)

🧮 Dashboard do Supervisor

![Supervisor](/mnt/data/DASHBOARD SUPERVISOR.png)
![SupervisorExtra](/mnt/data/DASHBOARD SUPERVISOR COMPLEMENTO 1.png)
![SupervisorExtra2](/mnt/data/DASHBOARD SUPERVISOR COMPLEMENTO 2.png)

📁 Importação de Clientes (CSV)

![Importar](/mnt/data/IMPORTAR CLIENTES CSV.png)

👤 Área do Usuário / Minha Conta

![MinhaConta](/mnt/data/MINHA CONTA.png)

📞 Registrar Ligação

![RegistrarLigacao](/mnt/data/REGISTRANDO UMA LIGAÇÃO.png)

📜 Histórico e edição de ligações

![Historico](/mnt/data/HISTORICO E EDIÇÃO .png)

📚 Meus Clientes (filtragem / retorno / ações)

![ClientesPendentes](/mnt/data/MEUS CLIENTES borrados.png)
![ClientesRetorno](/mnt/data/RETORNAR LIG.png)

➕ Adicionar Cliente

![AddCliente](/mnt/data/ADICIONAR CLIENTE.png)

🛡️ Segurança Aplicada

✔ Auth + sessão
✔ Hash de senhas
✔ SQLAlchemy ORM
✔ Variáveis sensíveis via .env

📬 Relatórios Automáticos

Sistema envia e-mails automaticamente com indicadores, usando APScheduler.

📌 Roadmap de melhorias

🔹 Exportação Excel/CSV avançada
🔹 API REST para integrações externas
🔹 Painéis adicionais para supervisores

👨‍💻 Autor

Gabriel Frizon
Analista de TI | Python | Automação

📌 Licença

Sistema corporativo — uso interno © Bakof.
