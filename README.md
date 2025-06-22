🚗 Concessionária Web
Bem-vindo(a) ao repositório da Concessionária Web , um projeto pessoal desenvolvido para simular um site moderno e funcional de uma entrega de veículos. Este projeto faz parte do meu portfólio e tem como objetivo demonstrar minhas habilidades com desenvolvimento web, design responsivo.

<img src="/img/menu.png">


🛠️ Tecnologias Utilizadas
Front-end:

HTML5
CSS3
JavaScript
Django (Modelos)
Backend:

Pitão
Django
Banco de Dados:
Postgres


💻 Como rodar o projeto localmente
1. Clonar ou repositório
git clone https://github.com/kleitonmac/carros-dev.git
cd carros-dev
2. Crie um ambiente virtual
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
3. Instalar as dependências
pip install -r requirements.txt
💡 Para visualizar o banco de dados Postgres faça as próximas alterações. BANCO DE DADOS = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'carros', 'USER': 'User_name_Postgres', 'PASSWORD': 'Sua_senha', 'HOST': 'localhost', 'PORT': '5432', } }

<<<<<<< HEAD
4. Configurar o ambiente
Crie um arquivo .envcom sua variável OPENAI_API_KEY.

5. Executar as migrações
=======
> 💡 Para visualizar o banco de dados Postgres faça a seguinte alterações.
> DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carros',
        'USER': 'User_name_Postgres',
        'PASSWORD': 'Sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

---

### 4. Configure o ambiente

Crie um arquivo `.env` com sua variável `OPENAI_API_KEY`.

### 5. Execute as migrações

```bash
>>>>>>> 56c9f5c4f2edd0395f39412dcce4380ff0ee5f28
python manage.py migrate
6. Iniciar o servidor de desenvolvimento
python manage.py runserver
Acesse o projeto em: http://127.0.0.1:8000/ para iniciar o login e navegar no repositório pelas URLs de new_car, cars.

🔽 Instalação rápida (linha direta)
Caso deseje instalar todas as dependências de uma vez, use o comando:

pip install -r .\requirements.txt
🚀 Em desenvolvimento
Área administrativa personalizada
Melhorias no sistema de financiamento
Painel de vendas
Login com autenticação social (Google, Facebook)
📫 Contato
Caso tenha dúvidas, sugestões ou queira colaborar com o projeto, entre em contato comigo:

<<<<<<< HEAD
GitHub: kleitonmac
E-mail: kdevprofissional@gmail.com
📝 Licença
Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.
=======
- GitHub: [kleitonmac](https://github.com/kleitonmac)
- Email: kdevprofissional@gmail.com

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
>>>>>>> 56c9f5c4f2edd0395f39412dcce4380ff0ee5f28
