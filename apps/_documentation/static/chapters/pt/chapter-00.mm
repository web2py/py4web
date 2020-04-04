## O que é py4web?


O PY4WEB é um web framework para o desenvolvimento rápido de aplicativos web eficientes orientados a bancos de dados. É uma evolução do popular framework Web2py, mas muito mais rápido e mais rápido. Seu design interno foi muito simplificado em comparação com o web2py.


O PY4WEB pode ser visto como um concorrente de outros frameworks, como Django ou Flask, e pode realmente servir ao mesmo propósito. No entanto, o PY4WEB visa fornecer um recurso maior pronto para uso e reduzir o tempo de desenvolvimento de novos aplicativos.


De uma perspectiva histórica, nossa história começa em 2007, quando o web2py foi lançado. O web2py foi projetado para fornecer uma solução abrangente para o desenvolvimento da Web: um arquivo zip contendo o interpretador Python, a estrutura, um IDE baseado na Web e uma coleção de pacotes testados em batalha que funcionam bem juntos. De muitas maneiras, o web2py foi imensamente bem-sucedido. O Web2py conseguiu fornecer uma baixa barreira de entrada para novos desenvolvedores, uma plataforma de desenvolvimento muito segura, e permanece compatível com versões anteriores até hoje.


O Web2py sempre sofria de um problema: seu design monolítico. Os desenvolvedores de Python mais experientes não entenderam como usar seus componentes fora do framework e como usar componentes de terceiros dentro do framework. Isso foi por uma boa razão, pois não ligamos muito para eles. Pensamos no web2py como uma ferramenta perfeita que não precisava ser dividida em pedaços porque isso comprometeria sua segurança. Aconteceu que estávamos errados, e jogar bem com os outros é importante. Portanto, nos últimos dois anos, trabalhamos em três frentes:


- Portamos o web2py para o Python 3.
- Dividimos o web2py em módulos que podem ser usados ​​independentemente.
- Remontamos alguns desses módulos em uma novo framework mais modular ... PY4WEB.


O PY4WEB é mais do que uma reembalagem desses módulos. É um redesenho completo. Ele usa alguns dos módulos web2py, mas não todos. Em alguns casos, ele usa outros e melhores módulos. Algumas funcionalidades foram removidas e outras foram adicionadas. Tentamos preservar a maior parte da sintaxe e dos recursos que os usuários experientes do web2py adoravam. Aqui está uma lista mais explícita:


- O PY4WEB, ao contrário do web2py, requer o Python 3.
- O PY4WEB, ao contrário do web2py, pode ser instalado usando o pip e suas dependências são gerenciadas usando o arquivo.txt.
- Os aplicativos PY4WEB são módulos regulares do Python. Isso é muito diferente do web2py. Em particular, descartamos o importador personalizado e agora dependemos exclusivamente do mecanismo de importação regular do Python.
- O PY4WEB, como o web2py, pode atender a vários aplicativos simultaneamente, desde que os aplicativos sejam submódulos do módulo de aplicativos.
- O PY4WEB, diferentemente do web2py, é baseado no bottlepy e, em particular, usa o objeto de solicitação do Bottle e o mecanismo de roteamento do Bottle.
- O PY4WEB, diferentemente do web2py, não cria um novo ambiente a cada solicitação. Ele introduz o conceito de equipamentos para declarar explicitamente quais objetos precisam ser reinicializados quando uma nova solicitação http é processada. Isso torna muito mais rápido.
- PY4WEB, possui um novo objeto de sessão que, como o web2py, fornece forte segurança e criptografia dos dados da sessão, mas as sessões não são mais armazenadas no sistema de arquivos - o que criou problemas de desempenho. Ele fornece sessões em cookies, em redis, em memcache ou no banco de dados. Também limitamos os dados da sessão a objetos json serializáveis.
- O PY4WEB, como o web2py, possui um sistema de emissão de bilhetes integrado, mas, diferentemente do web2py, esse sistema é global e não por aplicativo. Os tickets não são mais armazenados no sistema de arquivos com os aplicativos individuais. Eles são armazenados em um único banco de dados.
- O PY4WEB, como o web2py, é baseado no pydal, mas usa alguns novos recursos do pydal (RESTAPI).
- O PY4WEB, como o web2py, usa a linguagem do modelo yatl, mas usa como padrão delimitadores [...] entre colchetes para [...] evitar conflitos com estruturas JS modelo, como Vue.js e angular.js. O Yatl inclui um subconjunto dos ajudantes do web2py.
- PY4WEB, diferentemente do web2py, usa a biblioteca de pluralização para internacionalização. Na prática, isso expõe um objeto T muito semelhante ao T do web2py, mas fornece melhor armazenamento em cache e recursos de pluralização mais flexíveis.
- O PY4WEB vem com um aplicativo de painel que substitui o administrador do web2py. Este é um IDE da web para upload / gerenciamento / edição de aplicativos.
- O painel do PY4WEB inclui uma interface de banco de dados baseada na web. Isso substitui a funcionalidade appadmin do web2py.
- O PY4WEB vem com um objeto Form que é semelhante ao SQLFORM do web2py, mas é muito mais simples e rápido. A sintaxe é a mesma. Isso foi fornecido para ajudar os usuários a portar aplicativos existentes; mas o PY4WEB recomenda o uso de formulários baseados em API sobre postagens.
- O PY4WEB vem com um objeto Auth que substitui o web2py. É mais modular e mais fácil de estender. Pronto para uso, ele fornece a funcionalidade básica de registro, login, logout, alteração de senha, solicitação de alteração de senha, edição de perfil e integração com PAM, SAML2, LDAP, OAUTH2 (google, facebook e twitter).
- O PY4WEB vem com alguns utilitários, como "tags", por exemplo, que permitem adicionar tags pesquisáveis ​​a qualquer tabela do banco de dados. Pode ser usado, por exemplo, para marcar usuários com grupos e pesquisar usuários por grupos e aplicar permissões com base na associação.
- O PY4WEB vem com alguns componentes personalizados do Vue.js., projetados para interagir com o PyDAL RESTAPI e com o PY4WEB em geral. Essas APIs são projetadas para permitir que o servidor defina políticas sobre quais operações um cliente pode executar, mas oferece flexibilidade ao cliente dentro dessas restrições. Os dois componentes principais são o mtable (que fornece uma interface baseada na Web para o banco de dados semelhante à grade do web2py) e auth (uma interface personalizável para a API de autenticação).


O objetivo do PY4WEB é e permanece o mesmo do web2py: tornar o desenvolvimento da Web fácil e acessível, enquanto produz aplicativos que são rápidos e seguros.
