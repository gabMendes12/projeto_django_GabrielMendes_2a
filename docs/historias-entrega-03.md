# Histórias de usuário — Entrega 03

As histórias abaixo usam o formato de post-it e cenários BDD. As três primeiras
foram selecionadas para implementação nesta entrega.

## US01 — Enviar mensagem de contato (implementada)

**Post-it:** Como pessoa interessada no Impacta ESG, quero enviar uma mensagem
pela página Fale Conosco para tirar uma dúvida ou sugerir uma melhoria.

```gherkin
Cenário: enviar uma mensagem válida
  Dado que a pessoa acessou a página Fale Conosco
  Quando preencher nome, e-mail, assunto e mensagem corretamente
  E clicar em "Enviar mensagem"
  Então o sistema deve registrar a mensagem
  E deve confirmar que o envio foi realizado

Cenário: tentar enviar sem preencher os campos obrigatórios
  Dado que a pessoa acessou a página Fale Conosco
  Quando clicar em "Enviar mensagem" com algum campo obrigatório vazio
  Então o sistema deve manter os dados já preenchidos
  E deve informar quais campos precisam ser preenchidos

Cenário: informar um e-mail inválido
  Dado que a pessoa preencheu os demais campos do formulário
  Quando informar um e-mail em formato inválido
  E clicar em "Enviar mensagem"
  Então o sistema não deve salvar a mensagem
  E deve solicitar um e-mail válido
```

## US02 — Consultar a equipe (implementada)

**Post-it:** Como pessoa visitante, quero consultar a página Equipe para saber
quem participa da construção do Impacta ESG.

```gherkin
Cenário: visualizar os integrantes da equipe
  Dado que existem integrantes cadastrados no banco de dados
  E a pessoa acessou a página Equipe
  Quando a página for carregada
  Então o sistema deve exibir o nome, a atuação e o e-mail dos integrantes

Cenário: acessar a página pela navegação
  Dado que a pessoa está em uma página do site
  Quando clicar em "Equipe" no menu principal
  Então o sistema deve abrir a página Equipe
  E deve manter a navegação principal disponível

Cenário: usar o e-mail disponibilizado
  Dado que a pessoa está visualizando um integrante
  Quando clicar no endereço de e-mail exibido
  Então o sistema deve disponibilizar um link de contato por e-mail
```

## US03 — Pesquisar perguntas no fórum (implementada)

**Post-it:** Como pessoa responsável por uma PME, quero pesquisar perguntas no
fórum para encontrar orientações sobre um tema ESG específico.

```gherkin
Cenário: pesquisar uma pergunta por termo
  Dado que existem perguntas cadastradas no fórum
  Quando a pessoa pesquisar por um termo presente no título ou na descrição
  Então o sistema deve exibir apenas perguntas relacionadas ao termo
  E deve informar qual termo foi pesquisado

Cenário: pesquisar sem informar um termo
  Dado que a pessoa acessou o fórum
  Quando clicar em "Pesquisar" sem preencher o campo de busca
  Então o sistema deve informar que é necessário digitar um termo
  E deve manter a lista de perguntas disponível

Cenário: não encontrar resultados
  Dado que a pessoa informou um termo sem correspondência
  Quando executar a pesquisa
  Então o sistema deve informar que não há perguntas disponíveis
  E deve permitir uma nova pesquisa
```

## US04 — Publicar uma pergunta

**Post-it:** Como pessoa responsável por uma PME, quero publicar uma pergunta
no fórum para receber ajuda da comunidade.

```gherkin
Cenário: publicar uma pergunta completa
  Dado que a pessoa acessou a página Nova pergunta
  Quando preencher título e detalhe
  E salvar a pergunta
  Então o sistema deve registrar a pergunta
  E deve abrir a página de detalhe da publicação

Cenário: salvar sem título
  Dado que a pessoa acessou a página Nova pergunta
  Quando tentar salvar sem preencher o título
  Então o sistema não deve registrar a pergunta
  E deve solicitar o preenchimento dos campos obrigatórios

Cenário: salvar sem detalhe
  Dado que a pessoa preencheu apenas o título
  Quando tentar salvar a pergunta
  Então o sistema não deve registrar a pergunta
  E deve solicitar o detalhe da dúvida
```

## US05 — Responder uma pergunta

**Post-it:** Como pessoa participante do fórum, quero responder uma pergunta
para compartilhar uma orientação prática sobre ESG.

```gherkin
Cenário: enviar uma resposta válida
  Dado que existe uma pergunta publicada
  Quando a pessoa escrever uma resposta e salvar
  Então o sistema deve registrar a resposta vinculada à pergunta
  E deve exibi-la na página de detalhe

Cenário: enviar uma resposta vazia
  Dado que a pessoa acessou o formulário de resposta
  Quando tentar salvar sem escrever o texto
  Então o sistema não deve registrar uma resposta
  E deve solicitar o preenchimento do texto

Cenário: acessar uma pergunta inexistente
  Dado que a pessoa acessou uma URL de pergunta que não existe
  Quando a página for carregada
  Então o sistema deve informar que a pergunta não foi encontrada
```

## US06 — Votar em uma resposta

**Post-it:** Como pessoa participante do fórum, quero votar em uma resposta
útil para destacar orientações relevantes para a comunidade.

```gherkin
Cenário: votar em uma resposta existente
  Dado que uma resposta está exibida na pergunta
  Quando a pessoa clicar em "Votar nesta resposta"
  Então o sistema deve acrescentar um voto à resposta
  E deve mostrar a quantidade atualizada de votos

Cenário: votar em uma resposta inexistente
  Dado que a pessoa acessou uma URL de voto inválida
  Quando tentar registrar o voto
  Então o sistema deve informar que a resposta não foi encontrada

Cenário: consultar a quantidade de votos
  Dado que uma resposta recebeu votos
  Quando a pessoa acessar a pergunta relacionada
  Então o sistema deve mostrar a quantidade de votos da resposta
```
