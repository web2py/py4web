## Luminárias


Uma luminária é definida como "uma peça de equipamento ou mobília fixada em posição em um edifício ou veículo". No nosso caso, um dispositivo elétrico é algo anexado à ação que processa uma solicitação HTTP para produzir uma resposta.


Ao processar qualquer solicitação HTTP, existem algumas operações opcionais que podemos querer executar. Por exemplo, analise o cookie para procurar informações da sessão, confirme uma transação do banco de dados, determine o idioma preferido no cabeçalho HTTP e procure a internacionalização adequada, etc. Essas operações são opcionais. Algumas ações precisam delas e outras não. Eles também podem depender um do outro. Por exemplo, se as sessões forem armazenadas no banco de dados e a nossa ação precisar dele, talvez seja necessário analisar o cookie da sessão no cabeçalho, pegar uma conexão no pool de conexões do banco de dados e - após a ação ter sido executada - salvar a sessão de volta ao banco de dados se os dados foram alterados.


Os equipamentos PY4WEB fornecem um mecanismo para especificar o que uma ação precisa para que o py4web possa realizar as tarefas necessárias (e pular as não necessárias) da maneira mais eficiente. As luminárias tornam o código eficiente e reduzem a necessidade de código padrão.


As luminárias PY4WEB são semelhantes ao middleware WSGI e ao plugin BottlePy, exceto que se aplicam a ações individuais, não a todas elas, e podem depender umas das outras.


O PY4WEB vem com alguns acessórios predefinidos para ações que precisam de sessões, conexões com o banco de dados, internacionalização, autenticação e modelos. Seu uso será explicado neste capítulo. O desenvolvedor também pode adicionar acessórios, por exemplo, para manipular uma linguagem de modelo de terceiros ou lógica de sessão de terceiros.


### Templates


PY4WEB, por padrão, usa a linguagem de modelos yatl e fornece um suporte para ela.


``
De acção a importação py4web, Modelo


@Action ( 'index')
@ action.uses (molde ( 'index.html', delimitadores = '[[]]')
def index () retorno Dict ()
``:pitão


OO objeto Template é um Fixture. Ele transforma o `` dict () `` retornado pela ação em uma string usando o arquivo de modelo `` index.html``. Em um capítulo posterior, forneceremos um exemplo de como definir um acessório personalizado para usar uma linguagem de modelo diferente, por exemplo, o Jinja 2.


Observe que, como o uso de modelos é muito comum e, como é provável, todas as ações usam um modelo diferente, fornecemos algum açúcar sintático e as duas linhas a seguir são equivalentes:


``
@ action.uses ('index.html')
@ action.uses (Template ('index.html', delimiters = '[[]]' ')
``: python


Observe que os arquivos de modelo py4web estão armazenados em cache na RAM. O objeto de cache py4web é descrito posteriormente.


### Sessions


O objeto de sessão também é um dispositivo elétrico. Aqui está um exemplo típico de uso para implementar um contador.


``
from py4web import Session
session = Session (secret = 'minha chave secreta')


@action ('índice')
@ action.uses (sessão)
def index ():
    contador = sessão.get ('contador', -1)
    contador + = 1
    sessão ['contador'] =
    retorno do contador "counter =% i "%
counter` `


Observe que o objeto da sessão tem a mesma interface que um dicionário Python.


Por padrão, o objeto da sessão é armazenado em um cookie chamado, assinado e criptografado, usando o segredo fornecido. Se o segredo mudar, as sessões existentes serão invalidadas. Se o usuário alternar de HTTP para HTTPS ou vice-versa, a sessão do usuário será invalidada. A sessão nos cookies tem um limite de tamanho pequeno (4Kbytes depois de serializados e criptografados), portanto, não coloque muito neles.


Nas sessões py4web, são dicionários, mas eles são armazenados usando JSON (especificamente JWT), portanto, você deve armazenar apenas objetos que sejam JSON serializáveis. Se o objeto não for serializável em JSON, ele será serializado usando o operador `` __str__`` e algumas informações poderão ser perdidas.


Por padrão, as sessões py4web nunca expiram (a menos que contenham informações de login, mas isso é outra história), mesmo que uma expiração possa ser definida. Outros parâmetros também podem ser especificados:


``
session = Session (secret = 'minha chave secreta'.
                  = 3600,
                  Expirationalgoritmo = 'HS256',
                  storage = None,
                  same_site = 'Lax')
``


- Aqui `` algoritmo` `é o algoritmo a ser usado para a assinatura do token JWT. 
- `` storage`` é um parâmetro que permite especificar um método de armazenamento de sessão alternativo (por exemplo, redis ou banco de dados).
- `` same_site`` é uma opção que evita ataques CSRF e é ativada por padrão. Você pode ler mais sobre o assunto [aqui] (https://www.owasp.org/index.php/SameSite).


#### Sessão no memcache


``
import memcache, time
conn = memcache.Client (['127.0.0.1:11211'], debug = 0)
session = Session (storage = conn)
``: python


Observe que é um segredo não é necessário ao armazenar cookies no memcache porque, nesse caso, o cookie contém apenas o UUID da sessão.


#### Sessão em redis


``
import redis
conn = redis.Redis (host = 'localhost', porta = 6379)
conn.set = lambda k, v, e, cs = conn.set, ct = conn.ttl: (cs (k, v), e e ct (e))
session = Session (storage = conn)
``: python


Aviso: um objeto de armazenamento deve ter os métodos `` get`` e `` set`` e os `` O método set`` deve permitir especificar uma expiração. O objeto de conexão redis possui um método `ttl`` para especificar a expiração; portanto, aplicamos um patch no método` `set`` para ter a assinatura e a funcionalidade esperadas.


#### Sessão no banco de dados


``
from py4web import Session, DAL
from py4web.utils.dbstore import DBStore
db = DAL ('sqlite: memory')
session = Session (storage = DBStore (db))
``: python


A secret não é necessário ao armazenar cookies no banco de dados porque, nesse caso, o cookie contém apenas o UUID da sessão.


Além disso, este é um caso em que um dispositivo elétrico (sessão) requer outro dispositivo elétrico (db). Isso é tratado automaticamente pelo py4web e o seguinte é equivalente:


``
@ action.uses (session)
@ action.uses (db, session)
``: python




#### Session em qualquer lugar


Você pode facilmente armazenar sessões em qualquer lugar que desejar . Tudo que você precisa fazer é fornecer ao objeto `` Session`` um objeto `` storage`` com os métodos `` get`` e `` set``. Por exemplo, imagine que você deseja armazenar sessões em seu sistema de arquivos local:


``
import os
import json


class FSStorage:
   def __init __ (self, folder):
       self.folder = folder
   def get (self, key):
       filename = os.path. join (self.folder, key)
       se os.path.exists (filename):
           com open (filename) como fp:
              return json.load (fp)
       return None
   def set (self, key, value, expiration = None):
       filename = os.path.join (self.folder, key)
       com open (filename, 'w') como fp:
           json.dump (value, fp)


session = Session (storage = FSStorage ('/ tmp / sessions'))
` `: python


Deixamos a você como um exercício para implementar a expiração, limitar o número de arquivos por pasta usando subpastas e implementar o bloqueio de arquivos. No entanto, não recomendamos o armazenamento de sessões no sistema de arquivos: é ineficiente e não é dimensionável.




## Tradutor


Aqui está um exemplo de uso:


``
da ação de importação py4web, Tradutor
T_FOLDER = os.path.join (os.path.dirname (__ file__), 'traduções')
T = Tradutor (T_FOLDER)


@action ('index ')
@ action.uses (T)
def index (): retorna T (' Hello world ')
``: python


A string' hello world` será traduzida com base no arquivo de internacionalização na pasta "traduções" especificada que melhor corresponda o cabeçalho HTTP `` accept-language``.


Aqui, `` Translator`` é uma classe py4web que estende `` pluralize.Translator`` e também implementa a interface `` Fixture``.


Podemos facilmente combinar vários equipamentos. Aqui, como exemplo, agimos com um contador que conta "visitas".


``
from py4web import action, Session, Translator, DAL
from py4web.utils.dbstore import DBStore
db = DAL ('sqlite: memory')
session = Session (storage = DBStore (db))
T_FOLDER = os.path.join (os .path.dirname (__ arquivo__), 'traduções')
T = Tradutor (T_FOLDER)


@action ('index')
@ action.uses (sessão, T)
def index ():
    counter = session.get ('counter', - 1)
    contador + - 1
    sessão ['contador'] =contador
    retorno doT ("Você esteve aqui {n} vezes"). Format (n = contador)
``: python


Agora crie o seguinte arquivo de tradução `` traduções / pt .json``:


``
{"Você esteve aqui {n} vezes": 
  {
    "0": "Esta é sua primeira vez aqui", 
    "1": "Você já esteve aqui uma vez antes", 
    "2": " Você já esteve aqui duas vezes antes de ",
    " 3 ":" Você esteve aqui {n} vezes ",
    " 6 ":" Você esteve aqui mais de 5 vezes "
  }
}
` `: json


Ao visitar este site com o navegador preferência de idioma definida como inglês e recarregada várias vezes, você receberá as seguintes mensagens:


``
Esta é a sua primeira vez aqui
Você esteve aqui uma vez antes
Você esteve aqui duas vezes antes de e
Você esteve aqui 3 vezes
Você esteve aqui 4 vezes
Você esteve aqui 5 vezes
Você esteve aqui mais de 5 vezes
``


Agora tente criar um arquivo chamado `` translator / it.json`` que contém:


``
{ "Você já esteve aqui {n} vezes":"Você não viu mais
  {
    "0":nada",
    "1": "Você está vendo",
    "2": "Você está vendo 2 vezes" ,
    "3": "Você já viu {n} volte",
    "6": "Você já viu mais de 5 vezes"
  }
}
``: json


e defina a preferência do seu navegador para italiano.


### O acessório DAL


Já usamos o acessório `` DAL`` no contexto de sessões, mas talvez você queira acesso direto ao objeto DAL com o objetivo de acessar o banco de dados, não apenas sessões.


O PY4WEB, por padrão, usa o PyDAL (Python Database Abstraction Layer), que está documentado em um capítulo posterior. Aqui está um exemplo:


``
from datetime import datetime
da ação de importação py4web, request, DAL


DB_FOLDER = os.path.join (os.path.dirname (__ file__), 'database')
db = DAL ('sqlite: // storage .db ', pasta = DB_FOLDER, pool_size = 1)
db.define_table (' visit_log ', campo (' client_ip '), campo (' timestamp ',' datetime '))
db.commit ()


@action (' index ')
@ action.uses (db)
def index ():
    client_ip = request.environ.get ('REMOTE_ADDR')
    db.visit_log.insert (client_ip = client_id, timestamp = datetime.utcnow ())
    return "Sua visita foi armazenada no banco de dados "
` `: python


Observe que o equipamento de banco de dados define (cria / recria tabelas) automaticamente quando o py4web é iniciado (e toda vez que ele recarrega esse aplicativo) e escolhe uma conexão do pool de conexões a cada solicitação HTTP. Além disso, cada chamada para a ação `` index () `` é agrupada em uma transação e confirma `` on_success`` e reverte `` on_error``.


### Advertências sobre


acessórios Como os acessórios são compartilhados por várias ações, você não tem permissão para alterar seu estado porque não seria seguro para threads.
Há uma exceção a esta regra. As ações podem alterar alguns atributos dos campos do banco de dados:


``
db.define_table ('thing', Field ('name', writable = False))


@action ('index')
@ action.uses (db, 'generic.html')
def index ():
    db.thing.name.writable = True
    form = Form (db.thing)
    return dict (form = form)
)
``: python


O `` readable``, `` writable``, `` default Os atributos ``, `` update`` e `` require`` de `` db. {table}. {field} `` são objetos especiais da classe `` ThreadSafeVariable`` definiram o módulo `` threadsafevariable``. Esses objetos são muito parecidos com objetos locais de encadeamento do Python, mas são reinicializados a cada solicitação usando o valor especificado fora da ação. Isso significa que as ações podem alterar com segurança os valores desses atributos.


### Fixtures personalizadas


Um fixture é um objeto com a seguinte estrutura mínima:


``
from py4web importfixture


Classe doMyFixture (Fixture):
    def on_request (self): pass
    def on_success (self): pass
    def on_error (self): pass
    def transform (self, data): retorna dados
``: python


se uma ação usa este dispositivo:


``
@action ('index')
@ action.uses (MyFixture ())
def index (): return 'hello world'
' `


Então é garantido que` `on_request ()` `seja chamado antes que a função` `index ()` `seja chamada. É garantido que a `` on_success () `` seja chamada se a função `` index () `` retornar com sucesso ou gerar `` HTTP`` ou executar um `` redirecionamento``. O `` on_error () `` é garantido para ser chamado quando a função `` index () `` gera qualquer exceção diferente de `` HTTP``. A função `` transform`` é chamada para executar qualquer transformação desejada do valor retornado pela função `` index () ``.


### Auth e Auth.user


`` auth`` e `` auth.user`` são ambos acessórios. Dependem da `` sessão``. A função do acesso é fornecer à ação informações de autenticação. Ele é usado da seguinte maneira:


``
do py4web include action, redirect, Session, DAL, URL
from py4web.utils.auth import Auth


session = Session (secret = 'minha chave secreta')
db = DAL ('sqlite: // storage .db ', pasta = DB_FOLDER, pool_size = 1)
auth = Auth (sessão, db)
auth.enable ()


@action (' index ')
@ action.uses (auth)
def index ():
    user = auth.get_user ( ) ou redirecionar (URL ('auth / login'))
    print 'Welcome% s'% user.get ('first_name')
``: python


O construtor do objeto `` Auth`` define a tabela `` auth_user`` com os seguintes campos: nome de usuário, email, senha, nome, sobrenome, sobrenome, sso_id e action_token (os dois últimos são principalmente para uso interno).


`` auth.enable () `` registra várias ações, incluindo `` {appname} / auth / login`` e requer a presença do modelo `` auth.html`` e do componente de valor `` auth`` fornecido por o aplicativo `` _scaffold``.


O objeto `` auth`` é o dispositivo elétrico. Ele gerencia as informações do usuário. Ele expõe um único método:


``
auth.get_user ()
``


que retorna um dicionário python contendo as informações do usuário conectado no momento. Se o usuário não estiver logado, ele retornará `` Nenhum ''. O código do exemplo redireciona para a página 'auth / login' se não houver usuário.


Como essa verificação é muito comum, o py4web fornece um dispositivo adicional `` auth.user``:


``
@action ('index')
@ action.uses (auth.user)
def index ():
    user = auth.get_user ()
    print 'Welcome% s'% user.get ('first_name')
``: python


Este equipamento é redirecionado automaticamente para a página `` auth / login`` se o usuário não estiver logado. Depende de `` auth``, que depende de `` db`` e `` session``.


O dispositivo `` Auth`` é baseado em plugins e suporta vários métodos de plugins. Eles incluem Oauth2 (Google, Facebook, Twitter), PAM, LDAP e SMAL2.


Aqui está um exemplo de como usar o plug-in do Google Oauth2:


``
from py4web.utils.auth_plugins.oauth2google import OAuth2Google
auth.register_plugin (OAuth2Google (
    client_id = '...',
    client_secret = '...',
    callback_url = 'auth / plugin / oauth2google / callback '))
``: python


O `` client_id`` e o `` client_secret`` são fornecidos pelo google. O URL de retorno de chamada é a opção padrão para py4web e deve estar na lista de permissões do Google. Todos os plugins `` Auth`` são objetos. Plugins diferentes são configurados de maneiras diferentes, mas são registrados usando `` auth.register_plugin (...) ``. Exemplos são fornecidos em `` _scaffold / common.py``. 


O cache e o Memoize


py4web fornecem um cache no objeto ram que implementa o algoritmo Last Used Used (LRU). Pode ser usado para armazenar em cache qualquer função através de um decorador:


``
import uuid
from py4web import Cache
cache = Cache (size = 1000)


@action ('hello / <name>')
@ cache.memoize (expiration = 60)
def hello (name):
    return "Olá% s seu código é% s"% (name, uuid.uuid4 ())
``: python


Ele irá armazenar em cache (memorizar) o valor de retorno da função `` hello``, como função de a entrada `` name``, por até 60 segundos. Ele armazenará em cache os 1000 valores usados ​​mais recentemente. Os dados são sempre armazenados em memória ram.


O objeto Cache não é um dispositivo elétrico e não deve e não pode ser registrado usando o objeto `` @ action.uses``, mas o mencionamos aqui porque alguns dos equipamentos utilizam esse objeto internamente. Por exemplo, os arquivos de modelo são armazenados em cache no ram para evitar o acesso ao sistema de arquivos toda vez que um modelo precisa ser renderizado.