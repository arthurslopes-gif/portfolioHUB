import os

# Lista principal para armazenar as tarefas em memória
tarefas = []

def limpar_tela():
    # Limpa o terminal para melhorar a experiência visual
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    print("=" * 40)
    print("        TASKTRACKER - GERENCIADOR")
    print("=" * 40)

def cadastrar_tarefa():
    limpar_tela()
    print("--- CADASTRAR NOVA TAREFA ---")
    
    # Validação do Título (Regra: não pode estar vazio)
    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo == "":
            print("[ERRO] O título da tarefa não pode estar vazio. Tente novamente.")
        else:
            break

    descricao = input("Digite a descrição detalhada: ").strip()

    # Validação da Prioridade (Regra: estritamente Alta, Média ou Baixa)
    while True:
        prioridade = input("Informe a prioridade (Alta / Média / Baixa): ").strip().capitalize()
        if prioridade in ["Alta", "Média", "Baixa"]:
            break
        print("[ERRO] Prioridade inválida! Digite exatamente: Alta, Média ou Baixa.")

    data_limite = input("Informe a data limite (ex: DD/MM/AAAA): ").strip()

    # Estruturando os dados da tarefa (Status padrão: Pendente)
    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(nova_tarefa)
    print("\n[SUCESSO] Tarefa cadastrada com sucesso!")
    input("\nPressione Enter para voltar ao menu...")

def listar_tarefas():
    limpar_tela()
    print("--- LISTA DE TAREFAS CADASTRADAS ---")
    
    if len(tarefas) == 0:
        print("\n[AVISO] Não há tarefas cadastradas no sistema no momento.")
    else:
        print(f"\nTotalizador: {len(tarefas)} tarefa(s) encontrada(s).\n")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"[{i}] Título: {tarefa['titulo']}")
            print(f"    Descrição: {tarefa['descricao']}")
            print(f"    Prioridade: {tarefa['prioridade']}")
            print(f"    Data Limite: {tarefa['data_limite']}")
            print(f"    Status: {tarefa['status']}")
            print("-" * 35)
            
    input("\nPressione Enter para voltar ao menu...")

def main():
    while True:
        limpar_tela()
        exibir_cabecalho()
        print("1. Cadastrar Nova Tarefa")
        print("2. Listar Tarefas")
        print("3. Sair")
        print("=" * 40)
        
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            limpar_tela()
            print("Obrigado por usar o TaskTracker. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida! Escolha entre 1 e 3.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()