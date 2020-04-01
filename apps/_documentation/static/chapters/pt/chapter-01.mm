## Instalação e inicialização


### Plataformas e pré-requisitos suportados O


PY4WEB funciona bem no Windows, MacOS e Linux. Seu único pré-requisito é o Python 3, que deve ser instalado com antecedência.


### Instalando a partir do pip


Na linha de comando


``
python3 -m pip install --upgrade py4web
``: bash


(se o python3 não funcionar, tente usar o comando python).
Isso instalará o py4web e todas as suas dependências. Uma vez instalado, você pode iniciá-lo com:


``
py4web-start.py apps
``: bash


Isso deve produzir uma saída como:


``
██████╗ ██╗   ██╗██╗  ██╗██╗    ██╗███████╗██████╗
██╔══██╗╚██╗ ██╔╝██║  ██║██║    ██║██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ███████║██║ █╗ ██║█████╗  ██████╔╝
██╔═══╝   ╚██╔╝  ╚════██║██║███╗██║██╔══╝  ██╔══██╗
██║        ██║        ██║╚███╔███╔╝███████╗██████╔╝
╚═╝        ╚═╝        ╚═╝ ╚══╝╚══╝ ╚══════╝╚═════╝
painel está em: http://127.0.0.1:8000/_dashboard
[X] carregado _dashboard
[X] carregado _default
Padrão Bottle v0.12.16 server iniciando up (usando TornadoSer ver ()) ...
Escutando http://127.0.0.1:8000/
Pressione Ctrl-C para sair.
``


Aqui, `` apps`` é o nome da pasta onde você mantém seus aplicativos. Se a pasta não existir, ela será criada. O PY4WEB espera encontrar dois aplicativos nesta pasta: ** Painel ** (_dashboard) e ** Padrão ** (_default). Se não os encontrar, os instala.


Lembre-se de que, se você atualizar o py4web, ele não atualizará automaticamente o ** Dashboard ** e o ** Default **. Você precisa remover esses aplicativos para que o py4web os reinstale. Essa é uma precaução de segurança, caso você tenha feito alterações nesses aplicativos.


** Painel ** é um IDE baseado na Web. 


** Padrão ** é um aplicativo que nada mais é do que receber o usuário.


Observe que alguns aplicativos - como ** Dashboard ** e ** Default ** - têm uma função especial no py4web e, portanto, o nome real começa com `` _`` para evitar conflitos com os aplicativos criados por você.


Depois que o py4web estiver instalado, você poderá acessar os aplicativos nos seguintes URLs:


``
http: // localhost: 8000
http: // localhost: 8000 / _dashboard
http: // localhost: 8000 / {yourappname} / index
``


Observe que SOMENTE o aplicativo ** Padrão ** é especial porque, se não rqeuire o prefixo "{appname} /" no caminho, como todos os outros aplicativos.
Em geral, você pode querer vincular `` apps / _default`` ao seu aplicativo padrão.


Para todos os aplicativos, o `` / index`` à direita é opcional.


### Instalando a partir do código-fonte


Na linha de comando


``
git clone https://github.com/web2py/py4web.git
cd py4web
python3 -m pip install -r requirements.txt
``: bash


Depois de instalado, você deve começar com


``
./py4web-start.py apps
``: bash


Observe o ``. / ``; força a execução do py4web da pasta local e não o instalado.


### Atualizando


Se você instalou o py4web a partir da fonte, pode atualizá-lo com
``
python3 -m pip install -U py4web
``: bash
isso instalará as bibliotecas, mas não os aplicativos. Para atualizar os aplicativos incorporados, exclua-os e execute:
``
py4web-start -c apps
``: bash
A opção "-c" ou "--create" instrui o py4web a reinstalar os aplicativos ausentes.


### Senha do painel


Toda vez que o py4web é iniciado, ele solicita uma senha única para você acessar o painel. Isso é chato. Você pode evitá-lo criando um hash de senha em um arquivo:


``
python3 -c "de pydal.validators import CRYPT; open ('password.txt', 'w'). Write (str (CRYPT () (input (' password: ')) [0])) "
` `: bash
(o pydal é instalado pelo py4web como uma dependência)
e solicite ao py4web que reutilize essa senha:


Pip Install:


` `
py4web-start -p password.txt apps
``: bash


Console:


``
py4web-start -p password.txt apps
``: bash


ou


``
py4web-start -p password.txt apps
``: bash


### Opções da linha de comando


py4web fornece várias opções de linha de comando que pode ser listado com `` -h``.


``
use: py4web-start.py [-h] [--host HOSTNAME] [--port PORT] [--headless] [-n NUMBER_WORKERS]


                       [--ssl_cert_filename SSL_CERT_FILENAME]
                       [--ssl_key_filename SSL_KEY_FILENAME]
                       [- service_db_uri SERVICE_DB_URI] [-d DASHBOARD_MODE]
                       [-p PASSWORD_FILE] [-c]
                       apps_folder


argumentos posicionais:
  caminho apps_folder para ospasta de aplicativos


argumentos opcionais da:
  -h, --help mostra essa mensagem de ajuda e sai do
  endereço --host HOSTNAME do servidor (IP ou hostname) -
  número da porta do servidor PORT (por exemplo, 8000)
  - arte oculta sem cabeçalho para servidores baseados em console
  -n NUMBER_WORKERS, --number_workers NUMBER_WORKERS
                        número de trabalhadores
  gunicorn --ssl_cert_filename
                        arquivo de certificado
  SSL_CERT_FILENAME--ssl_key_filename SSL_KEY_FILENssl_key_filename SSL_KEY_FILEN
                        SSLssl
  --service_db_uri SERVICE_DB_URI
                        db uri para login
  DASHBOARD_MODE -d, --dashboard_modeDASHBOARD_MODE
                        modopainel: demo, somente leitura, cheia (padrão), nenhum
  -p password_file,password_file --password_file
                        arquivocontendo ocriptografada (CRIPTA)
  -csenha,- criar criou a missin pasta g e aplicativos
``


## Implantação no GCloud (também conhecido como Google App Engine) Faça


login no console do Gcloud (https://console.cloud.google.com/) e crie um novo projeto. Você obterá um ID de projeto parecido com "{project_name} - {number}".




No sistema de arquivos local, crie uma nova pasta de trabalho e faça o CD nela:


``
mkdir gae
cd gae
``: bash


Copie os arquivos de exemplo do py4web (assumindo que você tenha a fonte do github)


``
cp / path / to / py4web / development_tools / gcloud / * ./
``


Copie ou faça o link simbólico de sua pasta `` apps`` para a pasta gae ou talvez crie uma nova pasta de aplicativos contendo um `` __init __. py`` vazio e faça um link simbólico dos aplicativos individuais que você deseja implantar . Você deve ver os seguintes arquivos / pastas:


``
Makefile
apps
  __init__.py
  ... seus aplicativos ...
lib
app.yaml
main.py
``


Instale o Google SDK, py4web e configure a pasta de trabalho:


``
make install- gcloud-linux
make setup
gcloud config set {seu email}
gcloud config set {ID do projeto}
``: bash
(substitua {seu email} pela sua conta de email do Google e {id do projeto} pela ID do projeto obtida do Google).


Agora, toda vez que você quiser implantar seus aplicativos, faça:


``
make deploy
``: bash


Você pode personalizar o Makefile e o app.yaml para atender às suas necessidades. Você não precisa editar `` main.py``.


## Implantação no PythonAnywhere.com


Assista ao vídeo: https://youtu.be/Wxjl_vkLAEY
O script bottle_app.py está em `` py4web / deployment_tools / pythonanywhere.com / bottle_app.py``