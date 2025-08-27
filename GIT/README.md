# Git e GitHub

Git é um sistema de controle de versões distribuído que registra alterações no código, permitindo trabalhar em ramos independentes e voltar a estados anteriores.

GitHub é uma plataforma de hospedagem de código que usa Git para controle de versão e colaboração. Ele registra todo o histórico de alterações, identifica quem fez cada modificação e facilita o trabalho conjunto em projetos de software.

Github utiliza Git para funções de versionamento de código

Principais características do Github:

- Rede social
- Armazenamento remoto de repositórios  
- Visualização de histórico de commits  
- Ferramentas de revisão de código (pull requests)  
- Integração com CI/CD e automações  

>Exemplo de cenário: Você e seu colega trabalham no mesmo projeto. Cada um faz commits locais e empurra (push) para o GitHub. A plataforma mostra quem alterou cada linha, permitindo reverter mudanças ou debater melhorias.

## ReferÊncias online

* Para consultar a lista de comandos acessar https://git-scm.com/docs


## Instalação e Configuração Inicial

Antes de tudo, instale o Git e configure suas credenciais para que o GitHub associe seus commits ao seu perfil.

Passos:

1. Baixar e instalar Git  
   - macOS: `brew install git`  
   - Windows: execute o instalador em git-scm.com  
2. Configurar nome e e-mail:

   ```bash
   git config --global user.name "Seu Nome"
   git config --global user.email "seu@email.com"
   ```

3. Testar instalação:

   ```bash
   git --version
   ```

4. Criar conta no GitHub em github.com

Exemplo prático:  
Após configurar, abra um terminal e faça um commit teste:

```bash
mkdir projeto-teste
cd projeto-teste
git init
touch README.md
git add README.md
git commit -m "Primeiro commit no repositório de teste"
```

## Criando um Repositório

O repositório (repo) é o container do seu projeto.

### Pelo site

1. Clique em New repository  
2. Defina nome e descrição  
3. Selecione visibilidade (público ou privado)  
4. Clique em Create repository  

### Localmente

```bash
git init                               # inicia repositório local
git remote add origin <URL-do-repo>    # vincula ao GitHub
git add .                              # prepara arquivos
git commit -m "Configuração inicial"   # grava commit
git push -u origin main                # envia para o GitHub
```

Exemplo prático:  
Depois de `git push -u origin main`, você verá todos os arquivos no GitHub, prontos para colaboração.

## O que é um commit?

Um commit é uma foto do estado do seu projeto em um momento específico. Ele registra quais arquivos foram alterados, quem fez a mudança, quando foi feita e a mensagem que descreve o propósito da modificação.

### Componentes de um commit

- Hash (ID único): identifica de forma imutável o commit  
- Autor e data: quem fez e quando foi feita a alteração  
- Mensagem: explica o porquê das mudanças  
- Ponteiros para objetos Git:  
  - Snapshot (árvore de arquivos)  
  - Commit pai (histórico anterior)  

### Fluxo de trabalho com commits

1. Você altera, adiciona ou remove arquivos no diretório de trabalho.  
2. Prepara essas alterações para “stage” com `git add`.  
3. Registra tudo com `git commit -m "Descrição da mudança"`.  
4. O Git gera o objeto de commit e atualiza o branch atual para apontar para ele.  

Exemplo de uso:

```bash
git add src/app.js
git commit -m "feat: adiciona validação de formulários"
```

### Por que commits são importantes

- Histórico: volta a qualquer estado anterior com segurança  
- Colaboração: outros devs entendem o contexto das mudanças  
- Rastreabilidade: cada funcionalidade ou correção fica documentada  
- Automação: triggers de CI/CD podem agir sobre commits específicos  

## Principais Comandos Git

Aqui estão comandos essenciais, com descrição e exemplo de uso:

| Comando               | Descrição                                       | Exemplo                         |
|-----------------------|-------------------------------------------------|---------------------------------|
| `git clone <URL>`     | Clona repositório remoto para sua máquina       | `git clone https://github.com/u/r.git` |
| `git status`          | Exibe o estado atual (modificações, staged)     | `git status`                    |
| `git add <arquivo>`   | Adiciona arquivo ao próximo commit              | `git add index.html`            |
| `git commit -m "msg"` | Cria commit local com mensagem                  | `git commit -m "Adiciona página inicial"` |
| `git pull`            | Atualiza repositório local a partir do remoto   | `git pull origin main`          |
| `git push`            | Envia commits locais para o remoto              | `git push origin feature-xyz`   |
| `git log`             | Mostra histórico de commits                     | `git log --oneline --graph`     |

Exemplo prático:  
Para atualizar seu repo local e começar a trabalhar:

```bash
git pull origin main
git checkout -b feature-login
```

### Branches (Ramificações)

Branches isolam mudanças sem afetar o código principal.

Passos básicos:

```bash
git checkout -b nome-da-branch   # cria e muda para a nova branch
# faça alterações...
git add .
git commit -m "Implementa login"
git switch main                  # volta à branch principal
git merge nome-da-branch         # mescla mudanças
```

Exemplo prático:  
Você está na `main` e cria `feature-login`. Ao terminar, faz merge:

```bash
git switch main
git merge feature-login
git branch -d feature-login      # exclui a branch de recurso
```

## Colaboração em Equipe

### Fork e Pull Request

1. Fork do repositório original para sua conta  
2. Clone o fork localmente  
3. Crie branch para sua feature  
4. Commit, push para seu fork  
5. No GitHub, abra um Pull Request apontando de `seu-user:branch` para `origem:main`  

Exemplo de Pull Request:

- Título: “Adiciona validação de formulário de login”  
- Descrição: explique o que mudou, links para issues relacionadas  

### Revisão de Código

- Colegas comentam linhas específicas  
- Você faz correções na mesma branch  
- Após aprovação, dono do repo faz merge  

## Issues e Projetos

### Issues

Use para relatar bugs ou solicitar novas funcionalidades.  

```markdown
Título: Erro ao enviar formulário
Descrição:
- Ambiente: Chrome 92
- Passos para reproduzir:
  1. Acessar página /contato
  2. Preencher campos
  3. Clicar em Enviar
- Resultado esperado: mensagem de sucesso
- Resultado atual: erro 500
```

### Labels e Milestones

- Labels: categorizam (`bug`, `enhancement`)  
- Milestones: agrupa issues por versão ou sprint  

### Projects (Kanban)

- Colunas: To do, In progress, Done  
- Arraste issues/cards entre colunas conforme avançam  

## GitHub Actions

Automatize desde testes até deploy.

Exemplo de workflow básico em `.github/workflows/ci.yml`:

```yaml
name: CI Pipeline
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm install
      - run: npm test
```

Exemplo prático:

- Ao push na branch `main`, o Action roda testes.
- Se algum teste falhar, o PR fica bloqueado até corrigir.

## Segurança e Permissões

### Repositórios privados

- Código invisível ao público  
- Convidados acessam apenas se você permitir  

### Permissões de equipe

- Read: ler conteúdo  
- Write: editar e push  
- Admin: gerenciar configurações e times  

### .gitignore

Evite commitar arquivos sensíveis:

```bash
# Exemplo .gitignore
.env
node_modules/
.DS_Store
```

Exemplo prático:

- Crie `.gitignore` antes do primeiro commit.

## Insights e Estatísticas

GitHub gera gráficos para analisar produtividade:

- Contributions heatmap  
- Gráfico de commits por dia  
- Estatísticas de pull requests e issues  

Isso ajuda a:

- Identificar períodos de pico  
- Entender quais áreas recebem mais atenção  
- Planejar deadlines realistas  

## Visual Studio Code (VS Code) + GitHub 

### O que você precisa

- VS Code instalado
- Git instalado no seu sistema
- Conta no GitHub
- Extensão **GitHub Pull Requests and Issues** instalada no VS Code

### Principais funcionalidades

- **Clonar repositórios** diretamente do GitHub usando o comando `Git: Clone`
- **Commit e push** de alterações sem sair do editor
- **Gerenciar branches** e visualizar histórico de commits
- **Abrir pull requests** e acompanhar issues com a extensão oficial
- **Autenticação integrada** com GitHub (via navegador ou token)

### Começando um projeto novo

1. Abra a pasta do projeto no VS Code
2. Vá até o painel de controle de versão (ícone de ramificação)
3. Clique em **"Initialize Repository"**
4. Faça seu primeiro commit
5. Clique em **"Publish Branch"** para criar e enviar o repositório para o GitHub


