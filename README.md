# CleanSheets

CleanSheets é uma ferramenta para manipulação de planilhas Excel, que permite a seleção e remoção interativa de colunas indesejadas.

## Como Instalar

1. Baixe o executável mais recente [aqui](https://github.com/m1caelvr/CleanSheets/raw/main/dist/Cleansheets.exe).
2. Execute o arquivo baixado para instalar o CleanSheets.

# Guia de Uso do CleanSheets

### Seleção Manual das Colunas

1. Após iniciar o programa, clique no botão (`Upload`) para carregar a planilha Excel na aba `Início`.
2. Selecione o arquivo `.xlsx` que você deseja processar.

### Selecionar Colunas a Serem Removidas

1. Após carregar o arquivo, selecione a planilha desejada e a linha de títulos das colunas, de forma manual ou automática.
2. Clicando em seguir, você verá uma lista das colunas presentes na planilha.
3. Selecione as colunas que deseja remover ou manter. **Importante:** Caso escolha manter, todas as colunas não listadas serão deletadas.

### Remover as Colunas

1. Clique em `Deletar colunas`. O CleanSheets processará a planilha e removerá as colunas indesejadas conforme sua seleção.

### Aba Presets

- Nesta aba, você pode deletar colunas com base no preset escolhido e também importar e exportar esses dados.

### Funcionalidades Avançadas

- **Criar Presets:**
1. Na interface do CleanSheets, navegue até a seção de presets.
2. Adicione um novo preset e defina as colunas que devem ser removidas por padrão.
3. Salve o preset para uso futuro.

- **Importar e Exportar Presets:**
  - **Exportando Presets:** Um arquivo JSON será criado com base nos presets selecionados.
  - **Importando Presets:** Ao selecionar o arquivo JSON com os presets exportados, eles serão integrados ao aplicativo. Caso o programa encontre dois presets com o mesmo nome, ele renomeará automaticamente um deles.

### Remoção de Linhas (Futuro)

- Em futuras atualizações, a funcionalidade de remoção de linhas será adicionada. Fique atento às atualizações para mais informações sobre como utilizar essa funcionalidade.

### Solução de Problemas

- **Problemas ao Carregar a Planilha:**
  - Verifique se o arquivo está no formato `.xlsx` ou `.xls` e se não está corrompido.

- **Lentidão no Processamento:**
  - Certifique-se de que sua máquina possui recursos suficientes para lidar com grandes volumes de dados.

### Contato e Suporte

Para mais informações ou suporte adicional, entre em contato com o desenvolvedor do CleanSheets:

- **E-mail:** micael.vitor222@gmail.com
- **GitHub:** [CleanSheets Repository](https://github.com/m1caelvr/CleanSheets)

# Como Contribuir

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas na seção de issues.

# Licença

Este projeto é licenciado sob a [Licença MIT](./LICENSE).

<br>

# Estudo de Caso: CleanSheets

## Contexto do Projeto

**Problema ou Necessidade:**
Trabalho em uma empresa de engenharia que lida com chamados. Para acessar os dados desses chamados, um site de uma outra empresa gera uma planilha XLSX com todos os chamados. No entanto, essa planilha vem com 46 colunas, das quais apenas 10 são necessárias. Diariamente, os funcionários perdem um tempo considerável removendo manualmente as colunas indesejadas.

**Cliente e Público-Alvo:**
O cliente foi a própria empresa onde trabalho, e o público-alvo são os funcionários que manipulam esses dados diariamente.

**Objetivos Principais:**
Desenvolver um aplicativo que remove automaticamente as colunas indesejadas, economizando tempo e esforço dos funcionários.

## Planejamento e Desenvolvimento

**Tecnologias e Ferramentas Utilizadas:**
- Python com as bibliotecas pandas e openpyxl
- Interface desenvolvida com Flet em Python

**Processo de Definição dos Requisitos:**
A definição dos requisitos envolveu identificar as colunas necessárias e indesejadas e criar uma interface que permitisse tanto a seleção manual quanto a criação de presets para automação.

**Desafios Enfrentados e Superação:**
O principal desafio foi lidar com o alto volume de dados, pois cada coluna do arquivo contém mais de 56.000 linhas. Inicialmente, o processamento e a remoção dessas colunas eram lentos. Superamos isso otimizando o código para melhorar a eficiência no processamento de dados.

**Metodologia de Desenvolvimento:**
Utilizamos a metodologia Scrum, que permitiu uma abordagem iterativa e incremental, facilitando a adaptação às mudanças e a entrega rápida de funcionalidades.

## Implementação

**Principais Funcionalidades Implementadas:**
- Seleção manual das colunas do arquivo
- Criação de presets para definir colunas desejadas ou indesejadas para remoção automática

**Processo de Testes e Validação:**
Realizamos várias reuniões para avaliar a funcionalidade e a usabilidade do aplicativo. Os testes iniciais apresentaram alguns problemas, como falhas na salvamento dos dados, que foram resolvidos com ajustes no código.

## Resultados e Impacto

**Entrega dentro do Prazo:**
O projeto foi entregue dentro do prazo previsto.

**Principais Resultados Obtidos:**
- Maior objetividade e facilidade na manipulação dos dados
- Redução significativa do tempo gasto na remoção manual de colunas

**Recepção pelo Cliente e Usuários Finais:**
O aplicativo foi bem recebido pelo cliente e pelos usuários finais, que valorizaram a facilidade de uso.

## Lições Aprendidas

**Principais Lições Aprendidas:**
- Trabalhar com grandes volumes de dados é desafiador, mas pode ser gerenciado com a abordagem certa
- Adquiri conhecimentos valiosos em Python e novas tecnologias de frontend

**O que Faria Diferente em Projetos Futuros:**
Agora tenho mais objetividade na criação de sistemas em Python e na implementação de sistemas escaláveis.

## Futuro do Projeto

**Planos para Melhorias ou Atualizações:**
Há planos para adicionar a funcionalidade de filtros para remoção de linhas, além da remoção de colunas já existente.

**Potencial de Escalabilidade e Manutenção:**
Embora o aplicativo não tenha sido construído com orientação a objetos, a estrutura é bem dividida, o que facilita a escalabilidade e manutenção futuras.
