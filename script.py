# Lista de dicionários com os dados dos alunos
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 5.5},
    {"nome": "Carla", "nota": 9.0},
    {"nome": "Daniel", "nota": 6.0},
    {"nome": "Elena", "nota": 7.5}
]

# Define a média mínima para aprovação
media_minima = 7.0

# Filtra os alunos que atingiram ou superaram a média
aprovados = []
for aluno in alunos:
    if aluno["nota"] >= media_minima:
        aprovados.append(aluno)

# Exibe o resultado no terminal
print("=== Relatório de Alunos Aprovados ===")
for aluno in aprovados:
    print(f"Aluno: {aluno['nome']} - Nota: {aluno['nota']}")

