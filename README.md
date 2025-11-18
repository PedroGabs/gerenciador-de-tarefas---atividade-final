# 📝 TaskHub - Sistema de Tarefas em Python

Bem-vindo ao **TaskHub**, um sistema de gerenciamento de tarefas feito totalmente em **Python**, com foco em organização, simplicidade e escalabilidade. Este projeto possui funcionalidades completas de CRUD, interface via terminal e geração de relatórios.

---

## 🚀 Funcionalidades

### ✔ Criar Tarefas

* Título (máx. 50 caracteres)
* Descrição opcional
* Prioridade (urgente, alta, média, baixa)
* Status inicial: "pendente"
* Origem (email, telefone, chamado do sistema)
* Data e hora criadas automaticamente

---

### 📋 Visualizar Tarefas

* Exibe todas as tarefas ativas
* Ordena automaticamente por prioridade
* Interface com estilo usando ASCII

---

### 🔧 Atualizar Tarefas

Você pode editar:

* **Prioridade**
* **Status** (pendente, fazendo)

A busca para atualização é feita pelo **ID da tarefa**.

---

### ✅ Concluir Tarefas

* Marca a tarefa como **concluída**
* Registra automaticamente **data e hora da conclusão**
* Move a tarefa para a lista `Tasks_con`

---

### 🗑 Excluir Tarefas

* Marca a tarefa como **excluída**
* Registra data da exclusão
* Move para `Tasks_del`

---

### 📄 Geração de Relatório (TXT)

Com um clique, você gera um arquivo:

```
relatorio_tarefas.txt
```

O arquivo contém:

* Tarefas Ativas
* Tarefas Concluídas
* Tarefas Excluídas

Todas organizadas e formatadas com ASCII.

---

## 📂 Estrutura das Listas Internas

| Lista       | Função                       |
| ----------- | ---------------------------- |
| `ToDo`      | Armazena as tarefas ativas   |
| `Tasks_con` | Guarda as tarefas concluídas |
| `Tasks_del` | Guarda as tarefas excluídas  |

Cada tarefa é um dicionário:

```python
{
    "ID": int,
    "titulo": str,
    "desc": str,
    "prioridade": str,
    "status": str,
    "origemTar": str,
    "DataCreation": str,
    # campos adicionais dependendo da ação
}
```

---

## 🏗 Tecnologias Utilizadas

* **Python 3.13**
* `os` para limpar tela
* `time` para timers e experiência visual
* `datetime` para registrar data/hora

---

## 🖥 Interface (Menu Principal)

O sistema possui um menu central com as opções:

1. Criar tarefa
2. Ver lista de tarefas
3. Atualizar tarefas
4. Concluir tarefa
5. Excluir tarefa
6. Gerar relatório (txt)
7. Sair

A navegação é feita por números apenas.

---

## 👤 Autor

Desenvolvido com foco em aprendizado, organização e boas práticas de programação em Python.

<img 
    src="https://miro.medium.com/v2/resize:fit:960/0*9EPJGQNhpiAuHoIu.gif"
    alt="Tarefas"
    width="150px"
/>