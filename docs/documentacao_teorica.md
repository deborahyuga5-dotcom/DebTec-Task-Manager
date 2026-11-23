# Documentação do Projeto — DebTec Task Manager

## 1. Apresentação do projeto

O DebTec Task Manager é um sistema que desenvolvi como parte do projeto da faculdade, utilizando a empresa fictícia DebTec Solutions. A ideia surgiu para criar uma ferramenta que ajudasse uma pequena empresa de logística a organizar melhor suas tarefas do dia a dia. Com o sistema, o usuário consegue cadastrar novas tarefas, visualizar as atividades, editar informações, excluir tarefas e acompanhar o andamento de cada uma. Também desenvolvi um painel que mostra a quantidade de tarefas pendentes, em andamento e concluídas.

## 2. Objetivo do projeto
O objetivo principal foi criar um sistema simples, que facilitasse a organização das atividades e ajudasse o usuário a acompanhar o que precisa ser feito. Procurei desenvolver uma aplicação fácil de usar, na qual as tarefas pudessem ser organizadas de acordo com sua prioridade e seu status.

## 3. Escopo do projeto

No início, a proposta era desenvolver um sistema para cadastrar e gerenciar tarefas. Durante o desenvolvimento, foram implementadas as seguintes funcionalidades:

- Cadastrar novas tarefas.
- Visualizar as tarefas cadastradas.
- Editar informações das tarefas.
- Excluir tarefas.
- Definir prioridades entre baixa, média e alta.
- Acompanhar o status das atividades.
- Filtrar tarefas de acordo com o status.
- Visualizar indicadores com o resumo das tarefas.

O sistema foi desenvolvido para ser acessado pelo navegador e utiliza o banco de dados SQLite para armazenar as informações.

## 4. Metodologia ágil

Para organizar o desenvolvimento, utilizei o GitHub Projects, por meio de um quadro Kanban. As atividades foram divididas em três etapas: A Fazer, Em Andamento e Concluído. Dessa forma, consegui acompanhar o que já havia sido realizado e identificar o que ainda precisava ser desenvolvido. Essa organização também ajudou a dividir o projeto em tarefas menores, facilitando o acompanhamento de cada etapa.

## 5. Modelagem UML

A modelagem UML foi importante para entender melhor como o sistema seria organizado e quais funcionalidades precisariam ser desenvolvidas. Foram criados dois diagramas. O diagrama de casos de uso mostra as ações que o usuário pode realizar no sistema, como cadastrar, visualizar, editar, excluir e filtrar tarefas.

**Diagrama de Casos de Uso:**

![Diagrama de Casos de Uso](diagrama_casos_de_uso.png)

Já o diagrama de classes apresenta as informações que compõem uma tarefa, como identificador, título, descrição, prioridade e status, além da estrutura relacionada ao banco de dados.

**Diagrama de Classes:**

![Diagrama de Classes](diagrama_de_classes.png)

Com esses diagramas, foi possível representar melhor a estrutura e o funcionamento da aplicação.

## 6. Mudança de escopo

Durante o desenvolvimento, percebi que seria interessante acrescentar algumas funcionalidades para deixar o sistema mais completo. Uma das mudanças foi a criação de um painel de indicadores, que mostra a quantidade total de tarefas, as pendentes, as que estão em andamento e as concluídas. Também foi desenvolvido um filtro por status, permitindo encontrar as tarefas com mais facilidade. Essas melhorias não estavam detalhadas na proposta inicial, mas foram acrescentadas porque ajudam bastante na organização e na visualização das atividades.

## 7. Testes automatizados

Para verificar se as funcionalidades estavam funcionando corretamente, utilizei o Pytest, uma ferramenta que permite executar testes automatizados em Python. Foram criados testes para verificar se a página inicial abre corretamente, se é possível cadastrar, editar e excluir tarefas e se o sistema impede o cadastro quando o título está vazio. Os cinco testes automatizados executados passaram com sucesso, incluindo a validação de título vazio.

## 8. GitHub Actions

Também configurei o GitHub Actions para executar os testes automaticamente quando são realizadas alterações na branch principal do projeto ou quando um pull request é aberto. Assim, consigo verificar se as alterações feitas no código continuam funcionando corretamente, sem precisar executar todos os testes manualmente a cada atualização do repositório.

## 9. Tecnologias utilizadas

Durante o desenvolvimento, utilizei as seguintes tecnologias:

- **Python:** utilizado para desenvolver a lógica do sistema.
- **Flask:** utilizado para criar a aplicação web.
- **HTML:** utilizado para montar a estrutura das páginas.
- **CSS:** utilizado para personalizar a aparência do sistema.
- **JavaScript:** utilizado para criar o filtro de tarefas e as mensagens temporárias.
- **SQLite:** utilizado para armazenar os dados das tarefas.
- **Pytest:** utilizado para realizar os testes automatizados.
- **Git e GitHub:** utilizados para controlar as alterações e armazenar o projeto.
- **GitHub Actions:** utilizado para automatizar a execução dos testes.

## 10. Conclusão

Desenvolver o DebTec Task Manager foi uma oportunidade de colocar em prática alguns dos conhecimentos que estou aprendendo no curso de Análise e Desenvolvimento de Sistemas. Durante o projeto, tive contato com ferramentas e tecnologias que ainda estou aprendendo a utilizar, principalmente Python, Flask, banco de dados e GitHub. Também percebi que desenvolver um sistema envolve muito mais do que escrever código. É necessário planejar, organizar as tarefas, testar as funcionalidades e corrigir os problemas que aparecem durante o processo. Apesar das dificuldades encontradas, consegui desenvolver uma aplicação funcional e aprender um pouco mais sobre como funciona o desenvolvimento de software na prática
