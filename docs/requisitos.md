# Requisitos do produto

## Objetivo

Ajudar uma pequena ou média empresa a entender seu momento ESG, escolher ações viáveis e acompanhar os benefícios gerados por essas ações.

## Requisitos funcionais não triviais

Os requisitos abaixo foram escolhidos para que o produto faça mais do que apenas apresentar informações. Eles envolvem personalização, cálculo, priorização, acompanhamento e registro de dados.

### RF01: cadastro do contexto da empresa

O sistema deve permitir registrar nome, setor, porte e quantidade aproximada de pessoas da empresa. Esses dados devem ser persistidos para personalizar o diagnóstico e o plano.

### RF02: diagnóstico por dimensão

O sistema deve apresentar perguntas sobre Ambiental, Social e Governança. A empresa deve poder responder, salvar parcialmente e retomar o diagnóstico depois.

### RF03: índice explicável

O sistema deve calcular um índice geral e um resultado separado por dimensão. A tela deve mostrar como o resultado foi formado e qual dimensão deve receber atenção primeiro.

### RF04: plano priorizado

O sistema deve sugerir ações considerando impacto esperado, esforço, prazo e benefício. As ações devem ser ordenadas para que a empresa tenha um próximo passo claro.

### RF05: acompanhamento de ação

O sistema deve permitir iniciar, pausar e concluir uma ação, registrando a data da mudança e a pessoa responsável.

### RF06: indicadores e linha de base

O sistema deve permitir registrar um indicador com unidade, período, valor atual, meta e fonte. O painel deve comparar a linha de base com o valor mais recente.

### RF07: evidências

O sistema deve permitir registrar uma evidência textual para uma ação ou indicador, incluindo descrição, data e responsável. O upload de arquivos fica como evolução posterior.

### RF08: conteúdos práticos

O sistema deve listar conteúdos curtos relacionados a cada dimensão, com linguagem direta e uma sugestão de aplicação.

## Requisitos não funcionais

### RNF01: usabilidade e responsividade

As principais tarefas devem funcionar em telas de celular, tablet e desktop, com hierarquia visual clara e linguagem em português do Brasil.

### RNF02: acessibilidade

O sistema deve usar HTML semântico, labels associados aos campos, foco visível, contraste adequado e navegação básica por teclado.

### RNF03: segurança

O sistema deve usar proteção CSRF nos formulários, validar dados recebidos no servidor e restringir alterações ao usuário autorizado quando a autenticação for implementada.

### RNF04: manutenibilidade acadêmica

As funcionalidades devem ser implementadas com views e funções explícitas em Python, sem generic views e sem Django Forms, conforme a orientação da disciplina.

### RNF05: persistência

Dados do diagnóstico, respostas, ações, indicadores e evidências devem sobreviver a recarregamentos e novas sessões por meio de um banco de dados relacional.

### RNF06: qualidade

O projeto deve possuir testes unitários das regras de negócio, testes de integração das views e testes E2E com Selenium para as histórias implementadas.
