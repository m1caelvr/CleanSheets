# CleanSheets

CleanSheets é uma ferramenta para manipulação de planilhas Excel, permitindo a seleção e remoção de colunas de forma interativa.

## Como instalar

1. Baixe o executável mais recente [aqui](https://github.com/m1caelvr/CleanSheets/raw/main/dist/Cleansheets.exe).
2. Execute o arquivo baixado para instalar CleanSheets.

# Guia de Uso do CleanSheets

### Seleção manual das colunas

1. Após executar o programa, clique no botão (`Upload`) para carregar a planilha Excel na aba `Início`.
2. Selecione o arquivo `.xlsx` que você deseja processar.

### Selecionar Colunas a Serem Removidas

1. Após carregado, selecione a planilha desejada e a linha dos títulos ds colunas de forma manual ou automática.
2. Clcando em seguir, você verá uma lista das colunas presentes na planilha.
3. Agora só basta selecionar as colunas que deseja deletar ou manter.<br>
   (`Importante a atenção que caso escolhido manter, todas as outras colunas que não estiverem listadas, serão deletadas.`)

### Remova as colunas

1. Clique em `Deletar colunas` e o CleanSheets processará a planilha e removerá as colunas indesejadas conforme sua seleção.

## Aba presets

- Nesta aba você poderá deletar as colunas com base no preset escolhido e importar e exportar esses dados.

### Funcionalidades Avançadas

- **Criar Presets:**
1. Na interface do CleanSheets, vá até a seção de presets.
2. Adicione um novo preset e defina as colunas que devem ser removidas por padrão.
3. Salve o preset para uso futuro.

- **Importar e exportar presets:**
  #### Exportando presets:
  - Nesta funcionalidade, será criado um json com base nos presets que você selecionar.
  #### Importando presets:
  - Ao selecionar o arquivo JSON com os presets exportados, será integrado ao seu app esses novos presets. caso o programa achar 2 presets com o mesmo nome, ele renomeará automaicamente o nome do preset.
  
### Remoção de Linhas (Futuro):
  - Em futuras atualizações, a funcionalidade de remoção de linhas será adicionada. Fique atento às atualizações para mais informações sobre como utilizar essa funcionalidade.

### Solução de Problemas

- **Problemas ao Carregar a Planilha:**
  - Verifique se o arquivo está no formato `.xlsx` e se não está corrompido.

- **Lentidão no Processamento:**
  - Certifique-se de que sua máquina possui recursos suficientes para lidar com grandes volumes de dados.

### Contato e Suporte

Para mais informações ou suporte adicional, entre em contato com o desenvolvedor do CleanSheets:

- **E-mail:** micael.vitor222@gmail.com
- **GitHub:** [CleanSheets Repository](https://github.com/m1caelvr/CleanSheets)

## Como Contribuir

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou reportar problemas na seção de issues.

## Licença

Este projeto é licenciado sob a [Licença MIT](./LICENSE).

<br>

# Estudo de Caso: CleanSheets

## Contexto do Projeto

**Problema ou Necessidade:**
Trabalho em uma empresa de engenharia que lida com chamados. Para acessar os dados desses chamados, um site de uma outra empresa gera uma planilha XLSX com todos esses chamados. No entanto, essa planilha vem com 46 colunas, das quais apenas 10 são necessárias. Diariamente, os funcionários perdem um tempo considerável removendo manualmente as colunas indesejadas.

**Cliente e Público-Alvo:**
O cliente foi a própria empresa onde trabalho, e o público-alvo são os funcionários que manipulam esses dados diariamente.

**Objetivos Principais:**
Desenvolver um aplicativo que automaticamente remova as colunas indesejadas, economizando tempo e esforço dos funcionários.

## Planejamento e Desenvolvimento

**Tecnologias e Ferramentas Utilizadas:**
- Python com as bibliotecas pandas e openpyxl
- Interface desenvolvida com Flet em Python

**Processo de Definição dos Requisitos:**
A definição dos requisitos envolveu identificar as colunas necessárias e indesejadas e estabelecer a necessidade de uma interface que permitisse tanto a seleção manual das colunas quanto a criação de presets para automação.

**Desafios Enfrentados e Superação:**
O maior desafio foi lidar com o alto volume de dados, pois cada coluna do arquivo contém mais de 56.000 linhas. Inicialmente, o processamento e a remoção dessas colunas eram lentos. Superamos isso otimizando o código para melhorar a eficiência do processamento de dados.

**Metodologia de Desenvolvimento:**
Utilizamos a metodologia Scrum, que permitiu uma abordagem iterativa e incremental, facilitando a adaptação às mudanças e a rápida entrega de funcionalidades.

## Implementação

**Principais Funcionalidades Implementadas:**
- Seleção manual das colunas do arquivo
- Criação de presets que permitem definir colunas desejadas ou indesejadas para remoção automática

**Processo de Testes e Validação:**
Realizamos várias reuniões para avaliar a funcionalidade e a usabilidade do aplicativo. Os testes iniciais apresentaram alguns problemas, como a falha em salvar todos os dados, mas esses problemas foram resolvidos com ajustes no código.

## Resultados e Impacto

**Entrega dentro do Prazo:**
O projeto foi entregue dentro do prazo.

**Principais Resultados Obtidos:**
- Maior objetividade e facilidade na manipulação dos dados do sistema
- Redução significativa do tempo gasto na remoção manual de colunas

**Recepção pelo Cliente e Usuários Finais:**
O aplicativo foi bem recebido tanto pelo cliente quanto pelos usuários finais, que apreciaram a facilidade de uso.

## Lições Aprendidas

**Principais Lições Aprendidas:**
- Trabalhar com grandes volumes de dados é desafiador, mas gerenciável com a abordagem correta
- Adquiri conhecimentos valiosos em Python e novas tecnologias de frontend

**O que Faria Diferente em Projetos Futuros:**
Com base nessa experiência, agora tenho mais objetividade na criação de sistemas em Python e na implementação de sistemas escaláveis.

## Futuro do Projeto

**Planos para Melhorias ou Atualizações:**
Sim, há planos para adicionar a funcionalidade de filtros para remoção de linhas, além da remoção de colunas já existente.

**Potencial de Escalabilidade e Manutenção:**
Embora o aplicativo não tenha sido construído com orientação a objetos, a estrutura é bem dividida, o que facilita a escalabilidade e manutenções futuras.

