## Criando seu primeiro aplicativo


### Do zero, os


aplicativos podem ser criados usando o painel ou diretamente do sistema de arquivos. Aqui, faremos isso manualmente, como o Painel é descrito em seu próprio capítulo.


Lembre-se de que um aplicativo é um módulo Python; portanto, ele precisa apenas de uma pasta e um arquivo `` __init __. py`` nessa pasta:


``
mkdir apps / myapp
echo ''> apps / myapp / __ init__.py
``: bash


Se você agora reiniciar o py4web ou pressione o botão " Recarregar aplicativos "no painel, o py4web encontrará esse módulo, importará e reconhecerá como um aplicativo, simplesmente por causa de sua localização. Um aplicativo não é necessário para fazer nada. Pode ser apenas um contêiner para arquivos estáticos ou código arbitrário que outros aplicativos podem querer importar e acessar. No entanto, geralmente a maioria dos aplicativos é projetada para expor páginas da web estáticas ou dinâmicas.


### Páginas estáticas da Web


Para expor as páginas estáticas da Web, basta criar uma subpasta `` static '', e qualquer arquivo será automaticamente publicado:


``
mkdir apps / myapp / static
eco 'Hello World'> apps / myapp / static / hello.txt
``: bash


O arquivo recém-criado estará acessível em


``
http: // localhost: 8000 / myapp / static / hello.txt
``: bash


Observe que `` static`` é um especial caminho para py4web e apenas os arquivos na pasta `` static`` são servidos.


Para criar uma página dinâmica, você deve criar uma função que retorne o conteúdo da página. Por exemplo, copie o `` myapp / __ init __. Py`` da seguinte maneira:


``
import datetime
from py4web import action


@action ('index')
def page ():
    retorne "olá, agora é% s"% datetime.dateime. now ()
``: python


Reinicie o py4web ou pressione o botão "recarregar aplicativos" do painel e esta página estará acessível em


``
http: // localhost: 8000 / myapp / index
``


ou


``
http: // localhost: 8000 / myapp
``
(observe que o índice é opcional)


Ao contrário de outras estruturas, não importamos ou iniciamos o servidor da web dentro do código `` myapp``. Isso ocorre porque o py4web já está em execução e pode estar servindo vários aplicativos. py4web importa nosso código e expõe funções decoradas com `` @action () ``. Observe também que o py4web anexa `` / myapp`` (ou seja, o nome do aplicativo) ao caminho do URL declarado na ação. Isso ocorre porque existem vários aplicativos e eles podem definir rotas conflitantes. Anexar o nome do aplicativo remove a ambiguidade. Mas há uma exceção: se você chamar seu aplicativo como `` _default``, ou se criar um link simbólico de `` _default`` para `` myapp``, o py4web não acrescentará nenhum prefixo às rotas definidas dentro do aplicativo .


#### Em valores de retorno,


as ações py4web devem retornar uma string ou um dicionário. Se eles retornarem um dicionário, você deve informar ao py4web o que fazer com ele. Por padrão, o py4web o serializará em json. Por exemplo, edite `` __init __. Py`` novamente e adicione


``
@action ('colors')
def colours ():
    return {'colors': ['red', 'blue', 'green']}
``: python


Esta página estará visível em


``
http: // localhost: 8000 / myapp / colors
``


e retorna um objeto JSON `` {"colors": ["red", "blue", "green"]} `` . Observe que optamos por nomear a função da mesma forma que a rota. Isso não é necessário, mas é uma convenção que seguiremos com frequência.


Você pode usar qualquer linguagem de modelo para transformar seus dados em uma string. O PY4WEB vem com yatl e forneceremos um exemplo em breve.


#### Rotas


É possível mapear padrões na URL em argumentos da função. Por exemplo:


``
@action ('color / <name>')
def color (name):
    if name in ['red', 'blue', 'green']:
        return 'Você escolheu a cor% s'% name
    return 'Unknown color% s'% name
``: python


Esta página estará visível em


``
http: // localhost: 8000 / myapp / color / red
``


A sintaxe dos padrões é a mesma das rotas do Bottle. Um curinga de rota pode ser definido como 


- `` <name> `` ou
- `` <name: filter> `` ou
- `` <name: filter: config> ``


E esses são filtros possíveis (apenas ``: re : `` has a config):


- ``: int`` corresponde a dígitos (assinados) e converte o valor em número inteiro.
- ``: float`` semelhante a: int, mas para números decimais.
- ``: path`` corresponde a todos os caracteres, incluindo o caractere de barra de forma não gulosa, e pode ser usado para corresponder a mais de um segmento de caminho.
- ``: re [: exp] `` permite especificar uma expressão regular personalizada no campo de configuração. O valor correspondente não é modificado.


O padrão correspondente ao curinga é passado para a função sob a variável especificada `` name``.


Além disso, o decorador de ações usa um argumento opcional `` method`` que pode ser um método HTTP ou uma lista de métodos:


``
@action ('index', method = ['GET', 'POST', 'DELETE'] )
``


Você pode usar vários decoradores para expor a mesma função em várias rotas.


#### O objeto `` request``


Do py4web, você pode importar `` request``


``
do py4web import request


@action ('paint')
def paint ():
    if 'color' in request.query
       return 'Painting em% s '% request.query.get (' color ')
    return' Você não especificou uma cor '
': python


Esta ação pode ser acessada em:


``
http: // localhost: 8000 / myapp / paint? color = red
``


Observe que o objeto request é o a [Bottle request object] (https://bottlepy.org/docs/dev/api.html#the-request-object)


#### Templates


Para usar um modelo yatl você deve declará-lo. Por exemplo, crie um arquivo `` apps / myapp / templates / paint.html`` que contenha:


``
<body>
  <head>
    <style>
      body {background: [[= color]]}
    </style>
  </ head >
  <body>
    <h1> Cor [[= color]] </h1>
 </body>
</html>
``: html


e modifique a ação da pintura para usar o modelo e o padrão para verde.


``
@Action ( 'pintar')
@ action.uses ( 'paint.html')
def paint ():
    retorno dict (color = request.query.get ( 'cor', 'verde'))
``: python


A A página agora exibirá o nome da cor em um plano de fundo da cor correspondente.


O ingrediente chave aqui é o decorador `` @ action.uses (...) ``. Os argumentos de `` action.uses`` são chamados de fixtures. Você pode especificar vários acessórios em um decorador ou pode ter vários decoradores. Os equipamentos são objetos que modificam o comportamento da ação, que podem precisar ser inicializados por solicitação, que podem filtrar a entrada e a saída da ação e que dependem um do outro (eles têm escopo semelhante aos plug-ins do Bottle, mas são declarado por ação e eles têm uma árvore de dependência que será explicada mais adiante).


O tipo mais simples de acessório é um modelo. Você o especifica simplesmente fornecendo o nome do arquivo a ser usado como modelo. Esse arquivo deve seguir a sintaxe yatl e deve estar localizado na pasta `` templates`` do aplicativo. O objeto retornado pela ação será processado pelo modelo e transformado em uma sequência.


Você pode definir facilmente acessórios para outros idiomas de modelo. Isto é descrito mais tarde.


Alguns equipamentossão:


internos- o objeto DAL (que instrui o py4web a obter uma conexão com o banco de dados a partir do pool a cada solicitação e confirma com êxito ou retrocede a falha)
- o objeto Session (que instrui o py4web a analisar o cookie e recuperar uma sessão a cada solicitação e salvá-la se alterada)
- o objeto Translator (que instrui o py4web a processar o cabeçalho do idioma de aceitação e determinar regras ótimas de internacionalização / pluralização)
- o objeto Auth (que instrui o py4web de que o aplicativo precisa acessar as informações do usuário)


Eles podem depender um do outro. Por exemplo, a sessão pode precisar do DAL (conexão com o banco de dados) e o Auth pode precisar de ambos. Dependências são tratadas automaticamente.


### Do _scaffold Na


maioria das vezes, você não deseja começar a escrever código do zero. Você também deseja seguir algumas convenções sãs descritas aqui, como não colocar todo o seu código em `` __init __. Py``. O PY4WEB fornece um aplicativo Andaime (_scaffold), onde os arquivos são organizados corretamente e muitos objetos úteis são predefinidos.


Observe que você não encontrará o aplicativo de andaime em aplicativos, a menos que tenha baixado o py4web da fonte. Mas você pode criar um usando o Painel.


Aqui está a estrutura em árvore do aplicativo `` _scaffold``:


``
├── README.md
─── __init__.py # importa todo o resto
├── common.py # define objetos úteis
├── controllers.py # your ações
├── bancos de dados # seus bancos de dados e metadados sqlite
models── models.py # seu modelo de tabela
pyDAL ─── settings.py # quaisquer configurações usadas pelo aplicativo
├── settings_private.py # (opcional) configurações que você deseja manterprivada
arquivos # estáticos├── estática
│├── README.md
│├── componente auth vue componentes do # py4web
│ │ ├── auth.html
│ │ └── auth.js
│ ├── css # arquivos CSS, enviamos bulma porque ele é um agnóstico de JS
bul└── bulma.css f
│─ favicon.ico
j ─── js # arquivos JS, enviamos com esses arquivos, mas você pode substituí-los
│ ├── axios.min. js
sugar── sugar.min.js │──
utils.js v
└── vue.min.js
├── templates # seus modelos vão aqui go
─── README.md       
│ ├── auth.html # a página de autenticação para register / logic / etc (usa vue)
generic ─── generic.html # um modelo de uso geral
│ └── layout.html # um exemplo de layout
bulma └── traduções # internacionalização / arquivos de pluralização aqui
    └── it.json # py4web arquivos de internacionalização / pluralização estão em JSON
``


O aplicativo de andaime contém um exemplo de uma ação mais complexa:


``
da ação de importação py4web, solicitação, resposta, anulação, redirecionamento, URL
de yatl.helpers importam A
de. importação comum db, sessão, T, cache, auth




@ action ('bem-vindo', método = 'GET')
@ action.uses ('generic.html', sessão, db, T, auth.user)
índice de definição ():
    user = auth.get_user ()
    message = T ('Hello {first_name}'. format (** user))
    return dict (message = message, user = user)
``: python


Observe o seguinte:


- `` request`` , `` response``, `` abort`` são definidos por Bottle
- `` redirect`` e `` URL`` são semelhantes aos seus equivalentes web2py
- helpers (`` A``, `` DIV``, ` `SPAN``,` `IMG``, etc) devem ser importados de` `yatl.helpers``. Eles funcionam da mesma forma que em web2py
- `` db``, `` session``, `` T``, `` cache``, `` auth`` são luminárias. Eles devem ser definidos em `` common.py``.
- `` @ action.uses (auth.user) `` indica que esta ação espera que um usuário logado válido possa ser recuperado por `` auth.get_user () ``. Se não for esse o caso, essa ação será redirecionada para a página de login (definida também em `` common.py`` e usando o componente Vue.js auth.html).


Ao iniciar a partir do andaime, convém editar `` settings.py``, `` templates``, `` models.py`` e `` controllers.py``, mas provavelmente você não precisará alterar nada em `` common.py``.


No seu html, você pode usar qualquer biblioteca JS que desejar, porque py4web é independente da sua escolha de JS e CSS, mas com algumas exceções. O `` auth.html`` que lida com o registro / login / etc. usa um componente vue.js. Portanto, se você quiser usar isso, não deve removê-lo.