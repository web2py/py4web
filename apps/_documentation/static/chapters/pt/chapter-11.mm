## Autenticação e controle de acesso


** Aviso: a API descrita neste capítulo é nova e está sujeita a alterações. Mantenha seu código atualizado **


py4web vem com um objeto Auth e um sistema de plugins para autenticação do usuário e controle de acesso. Ele tem o mesmo nome que o web2py correspondente e serve ao mesmo objetivo, mas a API e o design interno são muito diferentes.


Para usá-lo, primeiro você precisa importá-lo, instancia-lo, configurá-lo e habilitá-lo.


``
from py4web.utils.auth import Auth
auth = Auth (sessão, db)
# (configure aqui)
auth.enable ()
``: python


A etapa de importação é óbvia. A segunda etapa não executa nenhuma operação além de informar ao objeto Auth qual objeto de sessão usar e qual banco de dados usar. Os dados de autenticação são armazenados em `` session ['user'] `` e, se um usuário estiver logado, o ID do usuário será armazenado na sessão ['user'] ['id']. O objeto db é usado para armazenar informações persistentes sobre o usuário em uma tabela `` auth_user`` com os seguintes campos:


- nome de usuário
- e-mail
- password
- first_name
- last_name
- sso_id (usado para single sign on, ver mais adiante)
- action_token ( usado para verificar e-mail, bloquear usuários e outras tarefas, consulte também mais tarde).


Se a tabela `` auth_user`` não existir, ela será criada.


A etapa de configuração é opcional e discutida posteriormente.


A etapa `` auth.enable () `` cria e expõe as seguintes APIs RESTful:


- {appname} / auth / api / register (POST)
- {appname} / auth / api / login (POST)
- {appname} / auth / api / request_reset_password (POST)
- {appname} / auth / api / reset_password (POST)
- {appname} / auth / api / confirm_email (GET, POST)
- {appname} / auth / api / logout (GET, POST ) (+)
- {nome do aplicativo} / auth / api / profile (GET, POST) (+)
- {nome do aplicativo} / auth / api / change_password (POST) (+)
- {nome do aplicativo} / auth / api / change_email (POST ) (+)


Os marcados com (+) requerem um usuário conectado.


## Auth UI


Você pode criar sua própria interface da web para fazer o login de usuários usando as APIs acima, mas py4web fornece uma como exemplo, implementada nos seguintes arquivos:


- _scaffold / templates / auth.html
- _scaffold / static / components / auth.js
- _scaffold / static / components / auth.html


Os arquivos do componente (js / html) definem um componente do Vue `` <auth /> ``, que é usado no arquivo de modelo auth.html da seguinte maneira:


``
[[extend "layout .html "]]
<div id =" vue ">
  <div class =" colunas ">
    <div class =" coluna é metade da diferença de um quarto "style =" border: 1px solid # e1e1e1; border- radius: 10px ">
      <auth plugins =" ​​local, oauth2google, oauth2facebook "> </auth>
    </div>
  </div>
</div>
[[bloquear page_scripts]]
<script src =" js / utils.js " > </script>
<script src = "components / auth.js"> </script>
<script> utils.app (). start (); </script>
[[end]]
``: html


Você pode bastante muito use este arquivo não modificado. Ele estende o layout atual e incorpora o componente `` <auth /> `` na página. Em seguida, ele usa `` utils.app (). Start (); `` (py4web magic) para renderizar o conteúdo de `` <div id = "vue"> ... </div> `` usando Vue.js. O `` components / auth.js`` também carrega automaticamente `` components / auth.html`` no espaço reservado para o componente (mais py4web magic). O componente é responsável por renderizar os formulários de logon / registro / etc usando dados reativos html e GETing / POSTing nas APIs de serviço de autenticação.


Se você precisar alterar o estilo do componente, poderá editar "components / auth.html" para atender às suas necessidades. É principalmente HTML com algumas tags especiais Vue `` v- * ``.


## Usando Auth


Existem duas maneiras de usar o objeto Auth em uma ação:


``
@action ('index')
@ action.uses (auth)
def index ():
    user = auth.get_user ()
    return 'hello {first_name} '.format (** usuário) se o usuário não estiver conectado'
': `python


Com` `@ action.uses (auth)` `dizemos ao py4web que esta ação precisa ter informações sobre o usuário e tente analisar a sessão para uma sessão de usuário.


``
@action ('index')
@ action.uses (auth.user)
def index ():
    user = auth.get_user ()
    retorna 'olá {first_name}'. format (** user) '
': `` python


aqui `` @ action.uses (auth.user) `` informa ao py4web que esta ação requer um usuário conectado e deve ser redirecionado para o login se nenhum usuário estiver conectado.


## Auth Plugins


Plugins são definidos em "py4web / utils / auth_plugins" e eles têm estruturas hierárquicas. Alguns são exclusivos e outros não. Por exemplo, padrão, LDAP, PAM e SAML são exclusivos (o desenvolvedor precisa escolher um). Por padrão, Google, Facebook e Twitter OAuth não são exclusivos (o desenvolvedor pode escolher todos eles e o usuário escolhe usando a interface do usuário).


Os componentes `` <auth /> `` se adaptarão automaticamente para exibir os formulários de login, conforme exigido pelos plugins instalados.


** No momento, não podemos garantir que os seguintes plugins funcionem bem. Eles foram transportados do web2py onde eles funcionam, mas ainda é necessário testar **


### PAM A


configuração do PAM é a mais fácil:


``
de py4web.utils.auth_plugins.pam_plugin import PamPlugin
auth.register_plugin (PamPlugin ())
``: python


Este, como todos os plugins, deve ser importado e registrado. Depois de registrada, a interface do usuário (components / auth) e as APIs RESTful sabem como lidar com isso. O construtor desses plug-ins não requer nenhum argumento (onde outros plugins exigem).


O `` auth.register_plugin (...) `` ** deve ** vir antes do `` auth.enable () ``, pois não faz sentido expor APIs antes da montagem dos plugins desejados.


### LDAP


``
de py4web.utils.auth_plugins.ldap_plugin importar LDAPPlugin
LDAP_SETTING = {
    'mode': 'ad',
    'server': 'my.domain.controller',
    'base_dn': 'ou = Usuários, dc = domain, dc = com '
}
auth.register_plugin (LDAPPlugin (** LDAP_SETTINGS))
``: python


### OAuth2 com Google (OK testado)


``
de py4web.utils.auth_plugins.oauth2google import OAuth2Google #
TESTED auth.register_plugin ( OAuth2Google (
    client_id = CLIENT_ID, client_secret
    = CLIENT_SECRET,
    callback_url = 'auth / plugin / oauth2google / callback'))
``: python


O ID do cliente e o segredo do cliente devem ser fornecidos pelo Google.


### OAuth2 com o Facebook (testado OK)


``
from py4web.utils.auth_plugins.oauth2facebook import OAuth2Facebook # UNTESTED
auth.register_plugin (OAuth2Facebook (
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    callback_url = 'auth plugin / callback /) )
``: python


O ID do cliente e o segredo do cliente devem ser fornecidos pelo Facebook.


### Tags e permissões


Py4web não tem o conceito de grupos como o web2py. A experiência mostrou que, embora esse mecanismo seja poderoso, ele sofre de dois problemas: é um exagero para a maioria dos aplicativos e não é flexível o suficiente para aplicativos muito complexos. O Py4web fornece um mecanismo de marcação de uso geral que permite ao desenvolvedor marcar qualquer registro de qualquer tabela, verificar a existência de tags e verificar registros contendo uma tag. A associação ao grupo pode ser pensada em um tipo de tag que aplicamos aos usuários. Permissões também podem ser tags. Os desenvolvedores são livres para criar sua própria lógica em cima do sistema de marcação.


Para usar o sistema de marcação, você precisa criar um objeto para marcar uma tabela:
``
groups = Tags (db.auth_user)
``: python


Em seguida, você pode adicionar uma ou mais marcas aos registros da tabela e remover as marcas existentes:


``
groups.add (user.id, 'manager')
groups.add (user.id, ['dancer', 'teacher'])
groups.remove (user.id, 'dancer')
``: python


Aqui está o O caso de uso é um controle de acesso baseado em grupo, onde o desenvolvedor verifica primeiro se um usuário é membro do grupo `` 'manager' '', se o usuário não é um gerente (ou ninguém está logado), o py4web redireciona para o `` 'url não autorizado' '. Se o usuário estiver no grupo correto, o py4web exibirá 'hello manager':


``
@action ('index')
@ action.uses (auth.user)
def index ():
    se não for 'manager' em groups.get (auth .get_user () ['id']):
        redirecionar (URL ('not_authorized'))
    retornar 'hello manager'
'': python


Aqui o desenvolvedor consulta o banco de dados para todos os registros com a (s) tag (s) desejada (s):


``
@action ('find_by_tag / {group_name}')
@ action.uses (db)
def find (group_name):
    users = db (groups.find ([group_name])). select (orderby = db.auth_user.first_name | db.auth_user. last_name)
    return {'users': users}
``: python


Deixamos para você um exersize para criar um acessório `` has_membership`` para ativar a seguinte sintaxe:


``
@action ('index')
@ action.uses (has_membership (groups, 'teacher'))
def index ():
    return 'hello teacher'
'': python


** Importante: ** `` Tags`` são automaticamente hierárquicas. Por exemplo, se um usuário tiver uma tag de grupo 'professor / ensino médio / física', as seguintes pesquisas retornarão o usuário:


- `` groups.find ('professor / ensino médio / física') ``
- `` groups.find ('teacher / high school') ``
- `` groups.find ('teacher') ``


Isso significa que as barras têm um significado especial para as tags. Escravos no início ou no final de uma tag são opcionais. Todos os outros caracteres são permitidos em pé de igualdade.


Observe que uma tabela pode ter vários objetos `` Tags`` associados. O nome de grupos aqui é completamente arbitrário, mas tem um significado semântico específico. Diferentes objetos `` Tags '' são ortogonais entre si. O limite para o uso deles é a sua criatividade.


Por exemplo, você pode criar grupos de tabelas:


``
db.define_table ('auth_group', Field ('name'), Field ('description'))
``: python


e para Tags:


``
groups = Tags (db.auth_user )
permissões = Tags (db.auth_groups)
``: python


Em seguida, crie um grupo zapper, dê uma permissão e faça um usuário membro do grupo:


``
zap_id = db.auth_group.insert (name = 'zapper', description = 'pode zap database')
permissions.add (zap_id, 'zap database')
groups.add (user.id, 'zapper')
``: python


E você pode procurar uma permissão de usuário por meio de uma associação explícita:


``
@ action ('zap')
@ action.uses (auth.user)
def zap ():
    user = auth.get_user ()
    permission = 'zap database'
    se db (permissions.find (permission)) (db.auth_group.name. . pertence (groups.get (usuário [ 'id']))) count ():
        # zap db
        retorno 'banco de dados zapped'
    else:
        return 'você não pertence a qualquer grupo com permissão para zap db'
``:python


Avisoaqui `` permissions.find (permission) `` gera uma consulta para todos os grupos com a permissão e filtramos ainda mais esses grupos para o usuário atual é membro de. Contamos e, se encontrarmos, o usuário tem permissão.