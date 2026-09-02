# Histórias de usuário

As histórias seguem o formato solicitado nos slides: post-it curto, seguido de cenários de validação em BDD.

## US01: responder o diagnóstico

**Post-it**

Como pessoa responsável pela gestão da PME, quero responder perguntas simples sobre Ambiental, Social e Governança para descobrir onde minha empresa deve começar.

**Cenários de validação**

```gherkin
Cenário: iniciar um diagnóstico ainda não respondido
  Dado que a gestora acessou o diagnóstico da empresa
  Quando a página for carregada
  Então o sistema deve exibir as perguntas agrupadas por dimensão
  E cada pergunta deve permitir selecionar um nível de prática

Cenário: salvar respostas do diagnóstico
  Dado que a gestora respondeu parte das perguntas
  Quando ela clicar em "Salvar diagnóstico"
  Então o sistema deve persistir as respostas no banco de dados
  E deve informar que o diagnóstico pode ser retomado depois
```

## US02: visualizar índice e prioridades

**Post-it**

Como pessoa responsável pela gestão da PME, quero visualizar meu índice ESG e a pontuação por dimensão para entender qual tema merece atenção primeiro.

**Cenários de validação**

```gherkin
Cenário: consultar o índice da empresa
  Dado que existem respostas salvas para a empresa
  Quando a gestora acessar a visão geral
  Então o sistema deve calcular o índice geral
  E deve exibir os resultados de Ambiental, Social e Governança separadamente

Cenário: identificar a dimensão prioritária
  Dado que uma dimensão possui o menor resultado
  Quando a gestora visualizar o mapa ESG
  Então o sistema deve destacar essa dimensão
  E deve apresentar uma explicação em linguagem simples
```

## US03: receber um plano priorizado

**Post-it**

Como pessoa responsável pela gestão da PME, quero receber ações ordenadas por impacto e esforço para saber qual melhoria cabe na minha rotina.

**Cenários de validação**

```gherkin
Cenário: gerar plano após o diagnóstico
  Dado que a empresa possui um diagnóstico salvo
  Quando a gestora abrir o plano de ação
  Então o sistema deve listar ações relacionadas às dimensões avaliadas
  E cada ação deve mostrar esforço, prazo e benefício esperado

Cenário: priorizar uma ação de alto impacto e baixo esforço
  Dado que existem duas ações disponíveis
  E uma delas possui maior impacto e menor esforço
  Quando o plano for organizado
  Então essa ação deve aparecer antes da outra
```

## US04: atualizar o andamento de uma ação

**Post-it**

Como pessoa responsável pela gestão da PME, quero iniciar, pausar ou concluir uma ação para acompanhar o avanço do plano.

**Cenários de validação**

```gherkin
Cenário: iniciar uma ação
  Dado que uma ação está com status "Próxima"
  Quando a gestora clicar em "Iniciar"
  Então o sistema deve alterar o status para "Em andamento"
  E deve registrar a data da alteração no banco

Cenário: concluir uma ação
  Dado que uma ação está em andamento
  Quando a gestora clicar em "Concluir"
  Então o sistema deve alterar o status para "Concluída"
  E deve atualizar o percentual do plano
```

## US05: acompanhar indicadores

**Post-it**

Como pessoa responsável pela gestão da PME, quero registrar indicadores com valor atual e meta para perceber os benefícios concretos das práticas ESG.

**Cenários de validação**

```gherkin
Cenário: cadastrar uma medição
  Dado que a gestora escolheu um indicador de consumo de energia
  Quando ela informar período, valor, unidade e fonte
  E salvar a medição
  Então o sistema deve persistir o registro
  E deve mostrar a medição no histórico do indicador

Cenário: comparar medição com meta
  Dado que existe uma linha de base e uma meta cadastradas
  Quando a gestora abrir os indicadores
  Então o sistema deve mostrar a distância até a meta
  E deve indicar se houve evolução ou piora
```

## US06: aprender o próximo passo

**Post-it**

Como pessoa responsável por uma PME, quero acessar conteúdos curtos e ligados ao meu diagnóstico para aprender sem me perder em termos técnicos.

**Cenários de validação**

```gherkin
Cenário: consultar conteúdo por dimensão
  Dado que a gestora está com dificuldade na dimensão Social
  Quando ela abrir os conteúdos práticos
  Então o sistema deve listar conteúdos relacionados a pessoas e comunidade
  E deve mostrar o tempo estimado de leitura

Cenário: transformar conteúdo em ação
  Dado que a gestora abriu um conteúdo recomendado
  Quando ela clicar em "Aplicar no meu plano"
  Então o sistema deve sugerir a ação relacionada
  E deve permitir adicioná-la ao plano da empresa
```
