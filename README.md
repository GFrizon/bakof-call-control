# 📞 Bakof Call Control

> Plataforma interna desenvolvida para controle comercial, registro de ligações e gestão de desempenho da equipe.  
> Atualmente implantado e rodando em produção no ambiente da Bakof.

---

<div align="center">

![Status](https://img.shields.io/badge/status-Em%20Produção-success?style=for-the-badge)
![Backend](https://img.shields.io/badge/backend-Python-blue?style=for-the-badge)
![Framework](https://img.shields.io/badge/framework-Flask-black?style=for-the-badge)
![Database](https://img.shields.io/badge/database-MySQL-orange?style=for-the-badge)

</div>

---

## 🚀 Funcionalidades

✔ Login com permissões (Consultor / Supervisor)  
✔ Dashboard com metas, conversão e ranking  
✔ CRUD de clientes e ligações  
✔ Importação de base via CSV  
✔ Gestão de usuários  
✔ Histórico detalhado de chamadas  
✔ Scheduler com envio automático de relatórios  
✔ Interface moderna e responsiva  

---

## 🏗️ Tecnologias Utilizadas

- Python + Flask  
- SQLAlchemy / MySQL  
- Bootstrap / Jinja2  
- APScheduler  
- Waitress  

---

## 📌 Estrutura do Projeto

```
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
├── docs/
│   └── screenshots/
├── uploads/
├── logs/
├── BKP/
│
└── legacy/
```

---

## ⚙️ Como executar localmente

```bash
git clone https://github.com/SEU_USUARIO/bakof-call-control.git
cd bakof-call-control

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

Acesse:  
👉 http://localhost:5000

---

# 📸 Preview do Sistema

> Adicione seus prints dentro da pasta: `docs/screenshots/`  
> e ajuste os nomes conforme necessário.

### 🔐 Login
![Login](docs/screenshots/login.png)

### 📊 Dashboard — Consultor
![DashboardConsultor](docs/screenshots/dashboard_consultor.png)

### 📈 Dashboard — Supervisor
![DashboardSupervisor](docs/screenshots/dashboard_supervisor.png)

### 📁 Importação CSV
![ImportarCSV](docs/screenshots/importar_csv.png)

### 👤 Minha Conta
![MinhaConta](docs/screenshots/minha_conta.png)

### 📞 Registrar Ligação
![RegistrarLigacao](docs/screenshots/registrando_ligacao.png)

### 📜 Histórico de Contato
![Historico](docs/screenshots/historico.png)

### 📋 Meus Clientes / Retorno
![Clientes](docs/screenshots/clientes.png)

### ➕ Adicionar Cliente
![AddCliente](docs/screenshots/adicionar_cliente.png)

---

## 🔐 Segurança Aplicada

✔ Auth com sessão  
✔ Hash de senhas  
✔ SQLAlchemy / ORM  
✔ Variáveis sensíveis via `.env`

---

## 📬 Relatórios Automáticos

Sistema envia e-mails automáticos com indicadores comerciais através de APScheduler.

---

## 📌 Roadmap de melhorias

🔹 Exportação Excel/CSV avançada  
🔹 API REST para integrações externas  
🔹 Painéis adicionais para supervisores  

---

## 👨‍💻 Autor

**Gabriel Frizon**  
Analista de TI | Python | Automação  

---

## 📌 Licença

Sistema corporativo — uso interno © Bakof
