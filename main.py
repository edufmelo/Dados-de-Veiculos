# DUPLA 17 - Nome: Eduardo Ferreira de Melo - Turma: Benz

# Função para calcular o desvio padrão do consumo cidade dos veículos
def desvio(matriz):
    media = 0
    desvio = 0
    raiz = 0
    formulasup = 0
    for i in range(len(matriz)):
        media += matriz[i][7]
    media = media / len(matriz)
    for i in range(len(matriz)):
        formulasup += (matriz[i][7] - media) ** 2
    raiz = formulasup / (len(matriz) - 1)
    desvio = (raiz) ** 0.5
    desvio = round(desvio, 5)
    return desvio

# Função para os preços dos carros em ordem crescente
def precoV(matriz, indice):
    m = len(matriz)
    for i in range(m):
        for j in range(0, m - i - 1):
            if int(matriz[j][indice]) > matriz[j + 1][indice]:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
    return matriz

# Função para os carros com o maior potência e menor consumo (ordem decrescente)
# (COMO A FUNÇÃO É A MESMA, DEIXEI EM APENAS 1 FUNÇÃO AO INVÉS DE 2):
def potenciaeconsumo(matriz, indice):
    m = len(matriz)
    for i in range(m):
        for j in range(0, m - i - 1):
            if int(matriz[j][indice]) < matriz[j + 1][indice]:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
    return matriz

# Função para os carros com o mesmo estilo
def estilo(matriz):
    suv = 0
    hatch = 0
    conversível = 0
    wagon = 0
    pickup = 0
    sedan = 0
    for i in range(len(matriz)):
        if matriz[i][4] == 'suv':
            suv += 1
        elif matriz[i][4] == 'hatch':
            hatch += 1
        elif matriz[i][4] == 'conversível':
            conversível += 1
        elif matriz[i][4] == 'wagon':
            wagon += 1
        elif matriz[i][4] == 'pick-up':
            pickup += 1
        else:
            sedan += 1
    return suv, hatch, conversível, wagon, pickup, sedan

# Função para obter os dados do veículo
def dadosV(matriz, modelo):
    linha = 0
    for i in range(len(matriz)):
        if modelo == matriz[i][1]:
            linha = matriz[i]
    return linha

# Lista de dados (veículos)
dados = [
    ['Alfa-romero', '156 Sport', 'gas', 2, 'conversível', 111, 4850, 8.8, 11.4, 132000],
    ['Alfa-romero', '145 Elegant', 'gas', 2, 'hatch', 154, 4900, 8, 10.9, 132000],
    ['Audi', 'A4 Avant', 'gas', 4, 'wagon', 110, 5430, 8, 10.5, 151360],
    ['Audi', 'A3 Turbo', 'flex', 4, 'sedan', 140, 5450, 7.2, 8.4, 191000],
    ['Bmw', '118iA', 'flex', 2, 'sedan', 118, 5800, 9.7, 12.2, 131440],
    ['Bmw', '120iA', 'gas', 4, 'sedan', 120, 5850, 9.7, 12.2, 135400],
    ['Chevrolet', 'Celta 2022', 'flex', 4, 'hatch', 77, 5800, 9.5, 12.2, 34941],
    ['Dodge', 'Dakota', 'gas', 2, 'hatch', 145, 4950, 8, 10.1, 103712],
    ['Fiat', 'Toro', 'diesel', 4, 'pick-up', 170, 3750, 10.1, 12.6, 192900],
    ['Fiat', 'Fastback', 'etanol', 4, 'suv', 130, 5750, 8.4, 10.2, 142490],
    ['Fiat', 'Palio Weekend 2021', 'flex', 4, 'sedan', 130, 5250, 10.5, 11.6, 69000],
    ['Ford', 'Ka', 'etanol', 4, 'sedan', 136, 4600, 7.8, 10.1, 56790],
    ['Honda', 'Fit', 'flex', 4, 'wagon', 76, 6000, 12.6, 14.3, 58360],
    ['Honda', 'City', 'flex', 2, 'sedan', 100, 5500, 10.5, 13.1, 82760],
    ['Honda', 'Civic', 'flex', 4, 'sedan', 143, 600, 21.3, 21.3, 166097],
    ['Hyundai', 'HB20 2023', 'gas', 4, 'sedan', 75, 6200, 12.2, 13.9, 76690],
    ['Jaguar', 'E-Pace', 'gas', 2, 'sedan', 262, 4960, 5.5, 7.2, 288000],
    ['Mazda', '626 GT', 'diesel', 4, 'sedan', 72, 4200, 13.1, 16.4, 146752],
    ['Mercedes-benz', '180-D Van', 'diesel', 4, 'wagon', 123, 4350, 9.3, 10.5, 225984],
    ['Mercedes-benz', '180-D', 'diesel', 2, 'conversível', 122, 4350, 9.3, 10.5, 225408],
    ['Mercedes-benz', 'CLA-180', 'gas', 2, 'conversível', 155, 4750, 6.7, 7.6, 280448],
    ['Mitsubishi', '3000 GT', 'gas', 2, 'hatch', 145, 5000, 8, 10.1, 118952],
    ['Mitsubishi', 'ASX', 'gas', 4, 'sedan', 88, 5200, 10.5, 13.5, 65512],
    ['Mitsubishi', 'Eclipse', 'flex', 4, 'sedan', 116, 5550, 9.7, 12.6, 74232],
    ['Porsche', '718 Boxster', 'gas', 2, 'hatch', 143, 5600, 8, 11.4, 176144],
    ['Porsche', '911 Carrera', 'gas', 2, 'sedan', 207, 5900, 7.2, 10.5, 272224],
    ['Porsche', '911 Carrera Cabriolet', 'gas', 2, 'conversível', 208, 5950, 7.2, 10.5, 296224],
    ['Toyota', 'Corolla', 'flex', 4, 'sedan', 169, 4400, 14.5, 16.3, 102990],
    ['VolksWagen', 'Golf 2021', 'flex', 4, 'hatch', 128, 3000, 10.7, 15, 93390],
    ['Volkswagen', 'Amarok', 'diesel', 4, 'pick-up', 225, 5200, 8.4, 8.8, 294590],
    ['Volvo', '850 GLT', 'gas', 4, 'sedan', 114, 5400, 9.7, 11.8, 103520],
    ['Volvo', 'S40', 'diesel', 4, 'sedan', 106, 4800, 10.9, 11.4, 179760]
]

# Função para a escolha da opção escolhida
def menu():
    print('=============== Escolha a opção desejada ===============')
    print('< 1 > Desvio padrão para o consumo do veículo na cidade')
    print('< 2 > Ordenação - Preço do veículo')
    print('< 3 > 5 Veículos com maior potência')
    print('< 4 > 5 Veículos com menor consumo na estrada')
    print('< 5 > Quantidade de veículos do mesmo estilo')
    print('< 6 > Dados do veículo (entrada de dados)')
    print('< 0 > Sair')
    print('========================================================')

    opcao = int(input('Digite a opção desejada: '))

    return opcao

# =-=-=-=-=-=-=-=-=-=-=-=-= Programa Principal =-=-=-=-=-=-=-=-=-=-=-=-=
while True:
    try:
        op = menu()
        if op == 0:  # Caso o usuário selecione a opção 0!
            print('Encerrando o programa...')
            break
        elif op == 1:  # Caso o usuário selecione a opção 1!
            print('O desvio padrão para o consumo dos veículos na cidade é: ', desvio(dados))
        elif op == 2:  # Caso o usuário selecione a opção 2!
            v = precoV(dados, 9)
            for i in range(len(dados)):
                print(i + 1, '-', v[i][0], v[i][1], 'com preço de R$', v[i][9])
        elif op == 3:  # Caso o usuário selecione a opção 3!
            v = potenciaeconsumo(dados, 5)
            for i in range(5):
                print('O carro em', i + 1, 'lugar com maior potência:', v[i][0], v[i][1], 'com', v[i][5], 'cv')
        elif op == 4:  # Caso o usuário selecione a opção 4!
            v = potenciaeconsumo(dados, 8)
            for i in range(5):
                print('O carro top', i + 1, 'de menor consumo na estrada é o:', v[i][0], v[i][1], 'fazendo:', v[i][8], 'Km/L')
        elif op == 5:  # Caso o usuário selecione a opção 5!
            suv, hatch, conversível, wagon, pickup, sedan = estilo(dados)
            print('A quantidade de carros SUV:', suv)
            print('A quantidade de carros hatch:', hatch)
            print('A quantidade de carros conversível:', conversível)
            print('A quantidade de carros wagon:', wagon)
            print('A quantidade de carros pick-up:', pickup)
            print('A quantidade de carros sedan:', sedan)
        elif op == 6:  # Caso o usuário selecione a opção 6!
            for i in range(len(dados)):
                print('Modelo -', i + 1, ':', dados[i][1])
            modelo = input('Digite o modelo desejado: ')
            variavel = dadosV(dados, modelo)
            if variavel == 0:
                print('Modelo não encontrado. Digite corretamente o modelo do veículo!')
                modelo = input('Digite o modelo desejado: ')
                variavel = dadosV(dados, modelo)
            if variavel != 0:
                print('Marca:', variavel[0])  # Mostrar a Marca do modelo selecionado
                print('Combustível:', variavel[2])  # Mostrar o Combustível do modelo selecionado
                print('Portas:', variavel[3])  # Mostrar as Portas do modelo selecionado
                print('Estilo:', variavel[4])  # Mostrar o Estilo do modelo selecionado
                print('Potência:', variavel[5], 'cv')  # Mostrar a Potência do modelo selecionado
                print('RPM:', variavel[6], 'rpm')  # Mostrar o RPM do modelo selecionado
                print('Consumo na cidade:', variavel[7], 'Km/L')  # Mostrar o Consumo na cidade do modelo selecionado
                print('Consumo na estrada:', variavel[8], 'Km/L')  # Mostrar o Consumo na estrada do modelo selecionado
                print('Preço: R$', variavel[9])  # Mostrar o Preço do modelo selecionado
                input('Tecle <ENTER> para continuar...')
        else:
            print('Opção inválida. Digite um número entre 0 e 6!')
    except ValueError:
        print('Erro - Digite um número válido!')
