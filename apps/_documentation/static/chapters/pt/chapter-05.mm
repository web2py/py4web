## A camada de abstração do banco de dados
`` DAL``: inxx


### Dependências


py4web vem com um Database Abstraction Layer (DAL), uma API que mapeia objetos Python em objetos de banco de dados, como consultas, tabelas e registros. O DAL gera dinamicamente o SQL em tempo real usando o dialeto especificado para o back-end do banco de dados, para que você não precise escrever código SQL ou aprender dialetos SQL diferentes (o termo SQL é usado genericamente), e o aplicativo será portátil entre diferentes tipos de bancos de dados. Uma lista parcial de bancos de dados suportados é mostrada na tabela abaixo. Consulte o site py4web e a lista de correspondência para obter os adaptadores mais recentes. O Google NoSQL é tratado como um caso específico no capítulo 13.


A seção Gotchas, no final deste capítulo, contém mais informações sobre bancos de dados específicos.


A distribuição binária do Windows funciona imediatamente com SQLite, MSSQL, PostgreSQL e MySQL. A distribuição binária do Mac funciona imediatamente com o SQLite.
Para usar qualquer outro back-end do banco de dados, execute a partir da distribuição de origem e instale o driver apropriado para o back-end necessário.
`` drivers de banco de dados``: inxx


Depois que o driver apropriado estiver instalado, inicie o py4web a partir do código-fonte e ele encontrará o driver. Aqui está uma lista dos drivers que o py4web pode usar:


`` DAL``: inxx `` SQLite``: inxx `` MySQL``: inxx `` PostgresSQL``: inxx `` Oracle``: inxx `` MSSQL` `` Inxx `` FireBird``: inxx `` DB2``: inxx `` Informix``: inxx `` Sybase``: inxx `` Teradata``: inxx `` MongoDB``: inxx `` CouchDB`` : inxx `` SAPDB``: inxx `` Cubrid``: inxx


============
banco de dados | drivers (origem)
SQLite | sqlite3 ou pysqlite2 ou zxJDBC `` zxjdbc``: cite (no Jython)
PostgreSQL | psycopg2 `` psycopg2``: cite ou zxJDBC `` zxjdbc``: cite (no Jython)
MySQL | pymysql `` pymysql``: cite ou MySQLdb `` mysqldb``: cite
Oracle | cx_Oracle `` cxoracle``: cite o
MSSQL | pyodbc `` pyodbc``: cite ou pypyodbc``pypyodbc``: cite
FireBird | kinterbasdb `` kinterbasdb``: cite ou fdb ou pyodbc
DB2 | pyodbc `` pyodbc``: cite o
Informix | informixdb `` informixdb``: cite
Ingres | ingresdbi `` ingresdbi``: citar
Cubrid | cubriddb `` cubridb``: cite a
Sybase | Sybase `` Sybase``: citar
Teradata | pyodbc `` Teradata``: cite o
SAPDB | sapdb `` SAPDB``: cite o
MongoDB | pymongo `` pymongo``: citar
IMAP | O imaplib `` IMAP``: cite
============


`` sqlite3``, `` pymysql`` e `` imaplib`` são enviados com py4web. O suporte ao MongoDB é experimental. A opção IMAP permite usar o DAL para acessar o IMAP.


### O DAL: um tour rápido


py4web define as seguintes classes que compõem o DAL:


O objeto ** DAL ** representa uma conexão com o banco de dados. Por exemplo:
`` sqlite``: inxx
``
db = DAL ('sqlite: //storage.sqlite')
``: python


`` define_table``: inxx
** Tabela ** representa uma tabela do banco de dados. Você não instancia diretamente a tabela; em vez disso, `` DAL.define_table`` o instancia.
``
db.define_table ('mytable', Field ('myfield'))
``: python


Os métodos mais importantes de uma tabela são:
`` insert``: inxx
`` truncate``: inxx
`` drop``: inxx
`` import_from_csv_file``: inxx
`` count``: inxx
`` insert``, `` truncate``, `` drop`` e `` import_from_csv_file``.


`` Field``: inxx
** Field ** representa um campo do banco de dados. Pode ser instanciado e passado como argumento para `` DAL.define_table``.


`` Rows``: inxx
** DAL Rows ** `` Row``: inxx é o objeto retornado por uma seleção de banco de dados. Pode ser pensado como uma lista de linhas `` Row``:
``
lines = db (db.mytable.myfield! = None) .select ()
``: python


`` Row``: inxx
** Row * * contém valores de campo.
``
para linha em linhas:
    print row.myfield
``: python


`` Query``: inxx
** Query ** é um objeto que representa uma cláusula SQL "where":
``
myquery = (db.mytable.myfield! = Nenhum) | (db.mytable.myfield> 'A')
``: python


`` Set``: inxx
** Set ** é um objeto que representa um conjunto de registros. Seus métodos mais importantes são `` count``, `` select``, `` update`` e `` delete``. Por exemplo:
``
myset = db (myquery)
linhas = myset.select ()
myset.update (myfield = 'somevalue')
myset.delete ()
``: python


`` Expression``: inxx


** Expression ** is algo como uma expressão `` orderby`` ou `` groupby``. A classe Field é derivada da Expressão. Aqui está um exemplo.
``
myorder = db.mytable.myfield.upper () | db.mytable.id
db (). select (db.table.ALL, orderby = myorder)
``: python


### Usando o DAL "autônomo"


O DAL pode ser usado em um ambiente não py4web via
``
from pydal import DAL, Field
``: python


[[dal_constructor]]
### Construtor DAL


Uso básico:
``
>>> db = DAL ('sqlite: //storage.sqlite')
``: python


O banco de dados agora conectado e a conexão é armazenada na variável global `` db``.


A qualquer momento, você pode recuperar a cadeia de conexão.
`` _uri``: inxx
``
>>> db._uri
sqlite: //storage.sqlite
``: python


e o nome do banco de dados
`` _dbname``: inxx
``
>>> db._dbname
sqlite
``: python


A cadeia de conexão é chamada de `` _uri`` porque é uma instância de um Uniform Resource Identifier.


O DAL permite várias conexões com o mesmo banco de dados ou com bancos de dados diferentes, mesmo bancos de dados de tipos diferentes. Por enquanto, assumiremos a presença de um único banco de dados, pois essa é a situação mais comum.


#### Assinatura do DAL


``
DAL (uri = 'sqlite: //dummy.db',
    pool_size = 0,
    pasta = Nenhuma,
    db_codec = 'UTF-8',
    check_reserved = None,
    migrate = True,
    fake_migrate = False,
    migrate_enabled = True,
    fake_migrate_all = false,
    decode_credentials = false,
    driver_args = nenhum,
    adapter_args = nenhum,
    tentativas = 5,
    auto_import = False,
    bigint_id = false,
    depuração = false,
    lazy_tables = False,
    db_uid = None,
    do_connect = True,
    after_connection = None,
    tables = None,
    ignore_field_case = True,
    entity_quoting = False,
    table_hash = None)
``: python


[[connection_strings]]
#### Cadeias de conexão (o parâmetro uri)
`` connection strings``: inxx


Uma conexão com o O banco de dados é estabelecido criando uma instância do objeto DAL:
``
db = DAL ('sqlite: //storage.sqlite', pool_size = 0)
``: python
`` db`` não é uma palavra-chave; é uma variável local que armazena o objeto de conexão `` DAL``. Você é livre para dar um nome diferente. O construtor de `` DAL`` requer um único argumento, a cadeia de conexão. A cadeia de conexão é o único código py4web que depende de um banco de dados de back-end específico. Aqui estão exemplos de cadeias de conexão para tipos específicos de bancos de dados back-end suportados (em todos os casos, assumimos que o banco de dados está sendo executado a partir do host local em sua porta padrão e denominado "test"):


`` ndb``: index


=== =================
** SQLite ** | `` sqlite: // storage.sqlite``
** MySQL ** | `` mysql: // nome do usuário: senha @ localhost / test? set_encoding = utf8mb4``
** PostgreSQL ** | `` postgres: // nome do usuário: senha @ localhost / test``
** MSSQL (legado) ** | `` mssql: // nome do usuário: senha @ localhost / test``
** MSSQL (> = 2005) ** | `` mssql3: // nome do usuário: senha @ localhost / test``
** MSSQL (> = 2012) ** | `` mssql4: // nome do usuário: senha @ localhost / test``
** FireBird ** | `` firebird: // nome do usuário: senha @ localhost / test``
** Oracle ** | `` oracle: // nome de usuário / senha @ test``
** DB2 ** | `` db2: // nome do usuário: senha @ teste``
** Ingres ** | `` ingres: // nome do usuário: senha @ localhost / test``
** Sybase ** | `` sybase: // nome do usuário: senha @ localhost / test``
** Informix ** | `` informix: // nome do usuário: senha @ teste``
** Teradata ** | `` teradata: // DSN = dsn; UID = usuário; PWD = passa; DATABASE = test``
** Cubrid ** | `` cubrid: // nome do usuário: senha @ localhost / test``
** SAPDB ** | `` sapdb: // nome do usuário: senha @ localhost / test``
** IMAP ** | `` imap: // usuário: senha @ servidor: porta``
** MongoDB ** | `` mongodb: // nome do usuário: senha @ localhost / test``
** Google / SQL ** | `` google: sql: // project: instance / database``
** Google / NoSQL ** | `` google: datastore``
** Google / NoSQL / NDB ** | `` google: datastore + ndb``
==================


Observe que no SQLite o banco de dados consiste em um único arquivo. Se não existir, é criado. Este arquivo é bloqueado toda vez que é acessado. No caso do MySQL, PostgreSQL, MSSQL, FireBird, Oracle, DB2, Ingres e Informix, o "teste" do banco de dados deve ser criado fora do py4web. Depois que a conexão for estabelecida, o py4web criará, alterará e descartará as tabelas adequadamente.


Na cadeia de conexão do MySQL, o ``? Set_encoding = utf8mb4`` no final define a codificação para UTF-8 e evita uma `` Cadeia de caracteres utf8 inválida: `` erro nos caracteres Unicode que consistem em quatro bytes, por padrão , O MySQL pode lidar apenas com caracteres Unicode que consistem em um a três bytes. `` mathiasbyensbe``: cite


No caso do Google / NoSQL, a opção `` + ndb`` ativa o NDB. O NDB usa um buffer Memcache para ler dados que são acessados ​​com frequência. Isso é totalmente automático e é feito no nível do armazenamento de dados, não no nível py4web.


Também é possível definir a cadeia de conexão como `` None``. Nesse caso, o DAL não se conectará a nenhum banco de dados de back-end, mas a API ainda poderá ser acessada para teste.


Algumas vezes, pode ser necessário gerar o SQL como se você tivesse uma conexão, mas sem realmente conectar-se ao banco de dados. Isso pode ser feito com


``
db = DAL ('...', do_connect = False)
``: python


Nesse caso, você poderá chamar `` _select``, `` _insert``, `` _update` `e _delete`` para gerar SQL, mas não chamam` `select``,` `insert``,` `update`` e` `delete``. Na maioria dos casos, você pode usar `` do_connect = False`` mesmo sem os drivers de banco de dados necessários.


Observe que, por padrão, o py4web usa codificação de caracteres utf8 para bancos de dados. Se você trabalha com bancos de dados existentes que se comportam de maneira diferente, é necessário alterá-lo com o parâmetro opcional `` db_codec`` como


``
db = DAL ('...', db_codec = 'latin1')
``: python


Caso contrário, você ' receberá tíquetes UnicodeDecodeError.


#### Pool de conexões
`` connection pooling``: inxx


Um argumento comum do construtor DAL é o `` pool_size``; o padrão é zero.


Como é bastante lento estabelecer uma nova conexão com o banco de dados para cada solicitação, o py4web implementa um mecanismo para o pool de conexões. Depois que uma conexão é estabelecida e a página é veiculada e a transação concluída, a conexão não é fechada, mas entra em um pool. Quando a próxima solicitação http chegar, py4web tenta reciclar uma conexão do pool e usá-la para a nova transação. Se não houver conexões disponíveis no pool, uma nova conexão será estabelecida.


Quando o py4web é iniciado, o pool está sempre vazio. O pool cresce até o mínimo entre o valor de `` pool_size`` e o número máximo de solicitações simultâneas. Isso significa que, se `` pool_size = 10``, mas nosso servidor nunca receber mais de 5 solicitações simultâneas, o tamanho real do pool aumentará para 5. Se `` pool_size = 0``, o pool de conexões não será usado.


As conexões nos conjuntos são compartilhadas seqüencialmente entre os encadeamentos, no sentido de que podem ser usados ​​por dois encadeamentos diferentes, mas não simultâneos. Existe apenas um pool para cada processo py4web.


O parâmetro `` pool_size`` é ignorado pelo SQLite e pelo Google App Engine.
O pool de conexões é ignorado no SQLite, pois não traria nenhum benefício.


#### Falhas na conexão (parâmetro de tentativas)


Se o py4web não conseguir se conectar ao banco de dados, ele aguardará 1 segundo e, por padrão, tentará novamente até 5 vezes antes de declarar uma falha. No caso de pool de conexões, é possível que uma conexão em pool que permaneça aberta, mas não utilizada por algum tempo, seja fechada no final do banco de dados. Graças ao recurso de nova tentativa, o py4web tenta restabelecer essas conexões descartadas.
O número de tentativas é definido pelo parâmetro de tentativas.


#### ATabelas Preguiçosas


configuração de`` lazy_tables = True`` fornece um grande aumento de desempenho. Veja abaixo: [tabelas lazy] (# lazy_tables)


#### Aplicativos


sem modelo Usar o diretório de modelo do py4web para seus modelos de aplicativo é muito conveniente e produtivo. Com tabelas lentas e modelos condicionais, o desempenho geralmente é aceitável, mesmo para aplicativos grandes. Muitos desenvolvedores experientes usam esse ambiente de produção. 


No entanto, é possível definir tabelas DAL sob demanda nas funções ou módulos do controlador. Isso pode fazer sentido quando o número ou a complexidade das definições de tabela sobrecarregam o uso de tabelas lentas e modelos condicionais.


Isso é chamado de desenvolvimento "sem modelo" pela comunidade py4web.
Isso significa menos uso da execução automática de arquivos Python no diretório do modelo. 
Isso não implica abandonar o conceito de modelos, visualizações e controladores.


A execução automática do PY4WEB do código Python dentro do diretório do modelo faz isso para você:


+ os modelos são executados automaticamente toda vez que uma solicitação é processada
+ os modelos acessam o escopo global do py4web. 


Os modelos também oferecem sessões shell interativas úteis quando o py4web é iniciado com a opção de linha de comando -M. 


Além disso, lembre-se da capacidade de manutenção: outros desenvolvedores do py4web esperam encontrar definições de modelo no diretório do modelo.


Para usar a abordagem "sem modelo", você assume a responsabilidade de executar essas duas tarefas de limpeza. 
Você chama as definições da tabela quando precisa delas e fornece o acesso necessário ao escopo global por meio do objeto atual (conforme descrito no [Capítulo 4] (.. / 04 # current_object)).


Por exemplo, um aplicativo típico sem modelo pode deixar as definições dos objetos de conexão com o banco de dados no arquivo de modelo, mas define as tabelas sob demanda por função do controlador.


O caso típico é mover as definições da tabela para um arquivo de módulo (um arquivo Python salvo no diretório modules).


Se a função para definir um conjunto de tabelas for chamada `` define_employee_tables () `` em um módulo chamado "table_setup.py", seu controlador que deseja consultar as tabelas relacionadas aos registros de funcionários para fazer com que um SQLFORM precise chamar a função `` define_employee_tables () `` antes de acessar qualquer tabela. A função `` define_employee_tables () `` precisa acessar o objeto de conexão com o banco de dados para definir tabelas. É por isso que você precisa usar corretamente o objeto `` current`` no arquivo de módulo que contém `` define_employee_tables () `` (como mencionado acima).


#### Bancos de dados replicados


O primeiro argumento de `` DAL (...) `` pode ser uma lista de URIs. Nesse caso, o py4web tenta se conectar a cada um deles. O principal objetivo disso é lidar com vários servidores de banco de dados e distribuir a carga de trabalho entre eles). Aqui está um caso de uso típico:


``
db = DAL (['mysql: //...1', 'mysql: //...2', 'mysql: //...3'])
`` : python


Nesse caso, o DAL tenta se conectar ao primeiro e, em caso de falha,
tentará o segundo e o terceiro. Isso também pode ser usado para distribuir a carga
em uma configuração mestre-escravo do banco de dados. Falaremos mais sobre isso
no [Capítulo 13] (../13 # Utilizando bancos de dados replicados) no contexto de escalabilidade.


####
Palavras-chave reservadas `` Palavras-chave reservadas``: inxx


`` check_reserved`` informa ao construtor para verificar os nomes de tabelas e colunas em relação às palavras-chave SQL reservadas nos bancos de dados de destino de back-end. O padrão `` check_reserved`` é None.


Esta é uma lista de cadeias que contêm os nomes dos adaptadores de back-end do banco de dados.


O nome do adaptador é o mesmo usado na cadeia de conexão DAL. Portanto, se você quiser verificar o PostgreSQL e o MSSQL, sua cadeia de conexão será a seguinte:
``
db = DAL ('sqlite: //storage.sqlite', check_reserved = ['postgres', 'mssql'])
``: python


O DAL examinará as palavras-chave na mesma ordem que a lista.


Existem duas opções extras "all" e "common". Se você especificar tudo, ele comparará todas as palavras-chave SQL conhecidas. Se você especificar comum, ele só verificará palavras-chave SQL comuns, como `` SELECT``, `` INSERT``, `` UPDATE``, etc.


Para back-ends suportados, você também pode especificar se deseja verificar contra as palavras-chave SQL não reservadas também. Nesse caso, você acrescentaria `` _nonreserved`` ao nome. Por exemplo:
``
check_reserved = ['postgres', 'postgres_nonreserved']
``: python


O back-end do banco de dados a seguir suporta a verificação de palavras reservadas.


======
** PostgreSQL ** | `` postgres (_nonreserved) ``
** MySQL ** | `` mysql``
** FireBird ** | `` firebird (_nonreserved) ``
** MSSQL ** | `` mssql``
** Oracle ** | `` oracle``Citação do
======


####banco de dados e configurações de caso
`` entity_quoting``: inxx `` ignore_field_case``: inxx A citação


de entidades SQL é ativada por padrão no DAL, ou seja:


`` entity_quoting = True``


Desta forma, os identificadores são automaticamente citados no SQL gerado pelo DAL. No nível SQL, as palavras-chave e os identificadores não citados não diferenciam maiúsculas de minúsculas; portanto, citar um identificador SQL faz distinção entre maiúsculas e minúsculas.
-------
Observe que os identificadores não citados devem sempre ser dobrados em minúsculas pelo mecanismo de back-end de acordo com o padrão SQL, mas nem todos os mecanismos são compatíveis com isso (por exemplo, a dobra padrão do PostgreSQL é maiúscula).
-------


Por padrão, o DAL também ignora as maiúsculas e minúsculas do campo, para alterar esse uso:


`` ignore_field_case = False``


Para garantir o uso dos mesmos nomes em python e no esquema do DB, você deve organizar as duas configurações acima . Aqui está um exemplo:


``
db = DAL (ignore_field_case = False)
db.define_table ('table1', Field ('column'), Field ('COLUMN'))
query = db.table1.COLUMN! = Db.table1. coluna
``: python


#### Estabelecendo uma conexão segura


Às vezes é necessário (e aconselhado) conectar-se ao seu banco de dados usando uma conexão segura, especialmente se o banco de dados não estiver no mesmo servidor que seu aplicativo. Nesse caso, você precisa passar parâmetros adicionais para o driver do banco de dados. Você deve consultar a documentação do driver do banco de dados para obter detalhes. 


Para o PostgreSQL com psycopg2, deve ser assim:


``
DAL ('postgres: // user_name: user_password @ server_addr / db_name',
    driver_args = {'sslmode': 'require', 'sslrootcert': 'root.crt',
                 ' sslcert ':' postgresql.crt ',' sslkey ':' postgresql.key '})
``: python


onde os parâmetros `` sslrootcert``, `` sslcot`` e `` sslkey`` devem conter o caminho completo para o arquivo arquivos. Você deve consultar a documentação do PostgreSQL sobre como configurar o servidor PostgreSQL para aceitar conexões seguras. 


#### Outros parâmetros do construtor DAL


##### O local da pasta do banco de dados
`` folder`` define o local onde os arquivos de migração serão criados (consulte a seção [Migrations] (# table_migrations) neste capítulo para obter detalhes). Também é usado para bancos de dados SQLite. Definido automaticamente no py4web. Defina um caminho ao usar o DAL fora do py4web.


##### Configurações de migração padrãoconfigurações de migração do
Asconstrutor DAL são booleanos que afetam os padrões e o comportamento global.


`` migrate = True`` define o comportamento de migração padrão para todas as tabelas


`` fake_migrate = False`` define o comportamento padrão de false_migrate para todas as tabelas


`` migrate_enabled = True`` Se definido como False, desativa TODAS as migrações


`` fake_migrate_all = False`` Se definido como True fake migra TODAS as tabelas


#### Experimente o shell py4web


Você pode experimentar a API do DAL usando o shell py4web, que está disponível usando a opção de linha de comando `` -S`` (leia mais no [Capítulo 4] (../04#CommandLineOptions)).
-------
Você precisa escolher um aplicativo para executar o shell, lembre-se de que as alterações no banco de dados podem ser persistentes. Portanto, tenha cuidado e NÃO saia para criar um novo aplicativo para teste em vez de adulterar um já existente.
-------


Comece criando uma conexão. Por uma questão de exemplo, você pode usar o SQLite. Nada nesta discussão muda quando você altera o mecanismo de backend.


Observe que a maioria dos trechos de código que contêm o prompt python `` >>> `` são diretamente executáveis ​​por meio de um shell simples, que você pode obter usando as opções de linha de comando `--PS``.


[[table_constructor]]
### Construtor de tabela
`` define_table``: inxx `` Tabela``: inxx As


tabelas são definidas no DAL via `` define_table``.


#### define_table assinatura
`` Field``: inxx


A assinatura para o método define_table é:
``
define_table (, * campos, ** kwargs)
``: python


nome da tabelaAceita um nome de tabela obrigatório e um número opcional de `` Instâncias de campo `` (mesmo nenhuma). Você também pode passar um objeto `` Tabela`` (ou subclasse) em vez de um objeto `` Campo``, isso clona e adiciona todos os campos (exceto o "id") à tabela de definição. Outras palavras-chave opcionais args são: `` rname``, `` redefine``, `` common_filter``, `` fake_migrate``, `` fields``, `` format``, `` migrate``, `` on_define``, `` plural``, `` polymodel``, `` primarykey``, `` sequence_name``, `` singular``, `` table_class`` e `` trigger_name``, que são discutidos abaixo.


Por exemplo:
``
>>> db.define_table ('person', Field ('name'))
<Pessoa da tabela (id, nome)>
``: python


Define, armazena e retorna um objeto `` Table`` chamado "pessoa" contendo um campo (coluna) "nome". Este objeto também pode ser acessado via `` db.person``, assim você não precisa capturar o valor retornado por define_tabela.


#### `` id``: anotações sobre a chave primária 


Não declare um campo chamado "id", pois ele é criado pelo py4web de qualquer maneira. Toda tabela possui um campo chamado "id" por padrão. É um campo inteiro de incremento automático (geralmente começando em 1) usado para referência cruzada e para tornar cada registro exclusivo, portanto "id" é uma chave primária. (Nota: o contador de id começando em 1 é específico do back-end. Por exemplo, isso não se aplica ao Google App Engine NoSQL.)


`` Named id field``: inxx
Opcionalmente, você pode definir um campo `` type = 'id' 'e py4web usarão esse campo como campo de identificação de incremento automático. Isso não é recomendado, exceto ao acessar tabelas de banco de dados herdadas que possuem uma chave primária com um nome diferente.
Com algumas limitações, você também pode usar chaves primárias diferentes usando o parâmetro `` primarykey``.


#### `` plural`` e `` singular``


Os objetos Smartgridpodem precisar conhecer o nome no singular e no plural da tabela. Os padrões são inteligentes, mas esses parâmetros permitem que você seja específico. O Smartgrid está descrito em [[Capítulo 7 ../07#SQLFORM-smartgrid]].


#### `` redefine`` As
tabelas podem ser definidas apenas uma vez, mas você pode forçar o py4web a redefinir uma tabela existente:


``
db.define_table ('person', Field ('name'))
db.define_table ('person' , Field ('name'), redefine = True)
``: python


A redefinição pode desencadear uma migração se a definição da tabela for alterada.


[[record_representation]]
#### `` format``: representação de registro


É opcional, mas recomendável especificar uma representação de formato para registros com o parâmetro `` format``.
``
db.define_table ('person', Field ('name'), format = '% (name) s')
``: python


ou
``
db.define_table ('person', Field ('name'), formato = '% (name) s% (id) s')
``: python


ou ainda mais complexos usando uma função:
``
db.define_table ('person', Field ('name'),
                format = lambda r: r .name ou 'anonymous')
``: python


O atributo format será usado para duas finalidades:
- Para representar registros referenciados nas caixas suspensas de seleção / opção.
- Para definir o atributo `` db.othertable.otherfield.represent`` para todos os campos que fazem referência a esta tabela. Isso significa que SQLTABLE não mostrará referências por ID, mas usará a representação preferida de formato.
  (Veja a seção [[Serializing Rows in views #sqltable]] neste capítulo para aprender mais sobre o SQLTABLE.)


#### `` rname``: O nome real


`` rname`` define um nome de back-end do banco de dados para a tabela. Isso torna o nome da tabela py4web um alias, e `` rname`` é o nome real usado na construção da consulta para o back-end.
Para ilustrar apenas um uso, `` rname`` pode ser usado para fornecer nomes de tabelas totalmente qualificados para MSSQL acessando tabelas pertencentes a outros bancos de dados no servidor: `` rname = 'db1.dbo.table1'``: python


[[primarykey] ]
#### `` primarykey``: suporte para tabelas herdadas


`` primarykey`` ajuda a suportar tabelas herdadas com chaves primárias existentes, mesmo com várias partes.
Consulte a seção [[Bancos de dados herdados e tabelas com chave #LegacyDatabases]] neste capítulo.


#### `` migrate``, `` fake_migrate``


`` migrate`` define opções de migração para a tabela. Consulte a seção [[Migrations #table_migrations]] neste capítulo para obter detalhes.


#### `` table_class``


Se você definir sua própria classe Table como uma subclasse de pydal.objects.Table, poderá fornecê-la aqui; isso permite estender e substituir métodos. Exemplo:
``
from pydal.objects importtabela MyTable


Classe de(Table):
    ...


db.define_table (..., table_class = MyTable)
``: python


#### `` sequence_name``


O nome de uma tabela personalizada sequência (se suportada pelo banco de dados). Pode criar uma SEQUENCE (iniciando em 1 e incrementando em 1) ou usar isso para tabelas herdadas com sequências personalizadas.
-------
Observe que, quando necessário, o py4web criará sequências automaticamente por padrão.
-------


#### `` trigger_name``


Relaciona-se a `` sequence_name``. Relevante para alguns back-end que não oferecem suporte a campos numéricos de incremento automático. 


#### `` polymodel``


Para o Google App Engine


#### `` on_define``


`` on_define`` é um retorno de chamada acionado quando uma tabela lenta é instanciada, embora seja chamada assim mesmo se a tabela não for preguiçosa. Isso permite alterações dinâmicas na tabela sem perder as vantagens da instanciação atrasada. 


Exemplo:
``
db = DAL (lazy_tables = True)
db.define_table ('person',
    Field ('name'),
    Field ('age', 'integer'),
    on_define = lambda table: [
        table.name.set_attributes ( requer = IS_NOT_EMPTY (), padrão = ''),
        table.age.set_attributes (requer = IS_INT_IN_RANGE (0, 120), padrão = 30)])
``: python
Observe este exemplo mostra como usar `` on_define`` mas não é realmente necessário. Os valores simples `` required`` podem ser adicionados às definições de Field e a tabela ainda é lenta. No entanto, `` require``, que recebe um objeto Set como o primeiro argumento, como IS_IN_DB, fará uma consulta como `` db.sometable.somefield == some_value``: python que faria com que `` sometable`` fosse definido cedo. Esta é a situação salva por `` on_define``.


[[lazy_tables]]
#### Lazy Tables, um grande aumento de desempenho
`` lazy tables``: osinxx


modelospy4web são executados antes dos controladores, portanto todas as tabelas são definidas a cada solicitação. Nem todas as tabelas são necessárias para lidar com cada solicitação, portanto, é possível que algum tempo gasto na definição de tabelas seja desperdiçado. Modelos condicionais (consulte [[Capítulo 4 ../04#conditional_models]]]) podem ajudar, mas o py4web oferece um grande aumento de desempenho via lazy_tables. Esse recurso significa que a criação da tabela é adiada até que a tabela seja realmente referenciada. A ativação de tabelas lentas é feita ao inicializar um banco de dados por meio do construtor DAL.
Requer a configuração do parâmetro lazy_tables: `` DAL (..., lazy_tables = True) ``: python
Este é um dos mais significativos aprimoramentos no desempenho do tempo de resposta no py4web.


#### Adicionando atributos aos campos e tabelas


Se você precisar adicionar atributos personalizados aos campos, basta fazer o seguinte:
`` db.table.field.extra = {} ``: python 


"extra" não é uma palavra-chave; é um atributo personalizado agora anexado ao objeto de campo. Você pode fazê-lo com mesas também, mas eles devem ser precedidos por um 
sublinhado para evitar conflitos de nomes com campos: 


`` db.table._extra = {} ``: python


### construtor Campo
`` constructor`` Campo: inxx


Estes são os valores padrão de um construtor de campo:
``
Campo (nome do campo, tipo = 'string', comprimento = Nenhum, padrão = DEFAULT,
      obrigatório = Falso, requer = DEFAULT,
      ondelete = 'CASCADE', notnull = False, unique = False ,
      uploadfield = True, widget = None, label = None, comment = None,
      gravável = True, legível = True, pesquisável = True, listável = True,
      atualização = None, autorize = None, autodelete = False, representa = None,
      uploadfolder = Nenhum, uploadseparate = Nenhum, uploadfs = Nenhum,
      computação = Nenhum, filter_in = Nenhum, filter_out = Nenhum,
      custom_qualifier = Nenhum, map_none = Nenhum, rname = Nenhum)
``: python em
que DEFAULT é um valor especial usado para permitir o valor Nenhum para um parâmetro.


Nem todos são relevantes para todos os campos. `` length`` é relevante apenas para os campos do tipo "string". `` uploadfield``, `` authorize`` e `` autodelete`` são relevantes apenas para os campos do tipo "upload". `` ondelete`` é relevante apenas para os campos do tipo "reference" e "upload".


- `` length`` define o tamanho máximo de um campo "string", "senha" ou "upload". Se `` length`` não for especificado, será usado um valor padrão, mas não é garantido que o valor padrão seja compatível com versões anteriores. '' Para evitar migrações indesejadas nas atualizações, recomendamos que você sempre especifique o tamanho dos campos de string, senha e upload. ''
- `` default`` define o valor padrão para o campo. O valor padrão é usado ao executar uma inserção se um valor não for especificado explicitamente. Também é usado para preencher previamente formulários criados a partir da tabela usando SQLFORM. Observe que, em vez de ser um valor fixo, o padrão pode ser uma função (incluindo uma função lambda) que retorna um valor do tipo apropriado para o campo. Nesse caso, a função é chamada uma vez para cada registro inserido, mesmo quando vários registros são inseridos em uma única transação.
- `` required`` informa ao DAL que nenhuma inserção deve ser permitida nesta tabela se um valor para esse campo não for especificado explicitamente.
- `` required`` é um validador ou uma lista de validadores. Isso não é usado pelo DAL, mas é usado pelo SQLFORM. Os validadores padrão para os tipos fornecidos são mostrados na próxima seção.
-------
Observe que `` require = ... `` é aplicado no nível dos formulários, `` required = True`` é aplicado no nível do DAL (insert), enquanto `` notnull` `,` `unique`` e` `ondelete`` são aplicados no nível do banco de dados. Embora possam parecer redundantes, é importante manter a distinção ao programar com o DAL.
-------
- `` rname`` fornece ao campo um "nome real", um nome para o campo conhecido pelo adaptador de banco de dados; quando o campo é usado, é o valor rname que é enviado ao banco de dados. O nome py4web para o campo é efetivamente um alias.
`` ondelete``: inxx
- `` ondelete`` se traduz na instrução SQL "ON DELETE". Por padrão, é definido como "CASCADE". Isso informa ao banco de dados que, ao excluir um registro, ele também deve excluir todos os registros que se referem a ele. Para desativar este recurso, defina `` ondelete`` para "NO ACTION" ou "SET NULL".
- `` notnull = True`` se traduz na instrução SQL "NOT NULL". Impede que o banco de dados insira valores nulos para o campo.
- `` unique = True`` se traduz na instrução SQL "UNIQUE" e garante que os valores desse campo sejam exclusivos na tabela. É aplicado no nível do banco de dados.
- `` uploadfield`` aplica-se apenas aos campos do tipo "upload". Um campo do tipo "upload" armazena o nome de um arquivo salvo em outro lugar, por padrão no sistema de arquivos na pasta "uploads /" do aplicativo. Se `` uploadfield`` estiver definido como True, o arquivo será armazenado em um campo de blob na mesma tabela e o valor de `` uploadfield`` é o nome do campo de blob. Isso será discutido em mais detalhes posteriormente na seção [[Mais sobre envios # Mais envios]] neste capítulo.
- `` uploadfolder`` define a pasta para os arquivos enviados. Por padrão, um arquivo carregado entra na pasta "uploads /" do aplicativo, que está em `` os.path.join (request.folder, 'uploads') `` (este não parece ser o caso do MongoAdapter atualmente).
  Por exemplo:
  `` Field (..., uploadfolder = os.path.join (request.folder, 'static / temp')) ``: python
  fará upload de arquivos para o "py4web / applications / myapp / static / temp" pasta.
- `` uploadseparate`` se definido como True, fará upload de arquivos em diferentes subpastas da pasta '' uploadfolder ''. Isso é otimizado para evitar muitos arquivos na mesma pasta / subpasta. ATENÇÃO: Você não pode alterar o valor de `` uploadseparate`` de True para False sem quebrar os links dos uploads existentes. O py4web usa as subpastas separadas ou não. Alterar o comportamento após o upload dos arquivos impedirá que o py4web consiga recuperar esses arquivos. Se isso acontecer, é possível mover arquivos e corrigir o problema, mas isso não é descrito aqui.
`` uploadfs``: inxx `` PyFileSystem``: inxx
- `` uploadfs`` permite especificar um sistema de arquivos diferente para o upload de arquivos, incluindo um armazenamento Amazon S3 ou um armazenamento SFTP remoto.
  -------
  Você precisa ter o PyFileSystem instalado para que isso funcione. `` uploadfs`` deve apontar para PyFileSystem.
  -------
- `` autodelete`` determina se o arquivo carregado correspondente deve ser excluído quando o registro referente ao arquivo for excluído. Apenas para os campos "upload". However, records deleted by the database itself due to a CASCADE operation will not trigger py4web's autodelete. The py4web Google group has workaround discussions.
- ``widget`` must be one of the available widget objects, including custom widgets, for example: ``SQLFORM.widgets.string.widget``. A list of available widgets will be discussed later. Each field type has a default widget.
- ``label`` is a string (or a helper or something that can be serialized to a string) that contains the label to be used for this field in auto-generated forms.
- ``comment`` is a string (or a helper or something that can be serialized to a string) that contains a comment associated with this field, and will be displayed to the right of the input field in the autogenerated forms.
- ``writable`` declares whether a field is writable in forms.
- ``readable`` declares whether a field is readable in forms. If a field is neither readable nor writable, it will not be displayed in create and update forms.
- ``searchable`` declares whether a field is searchable in grids (``SQLFORM.grid`` and ``SQLFORM.smartgrid`` are described in [[Chapter 7 ../07#SQLFORM-grid-and-SQLFORM-smartgrid]]). Notice that a field must also be readable to be searched.
- ``listable`` declares whether a field is visible in grids (when listing multiple records)
- ``update`` contains the default value for this field when the record is updated.
- ``compute`` is an optional function. If a record is inserted or updated, the compute function will be executed and the field will be populated with the function result. The record is passed to the compute function as a ``dict``, and the dict will not include the current value of that, or any other compute field.
- ``authorize`` can be used to require access control on the corresponding field, for "upload" fields only. It will be discussed more in detail in the context of Authentication and Authorization.
- ``represent`` can be None or can point to a function that takes a field value and returns an alternate representation for the field value. 
  Examples:
  ``
db.mytable.name.represent = lambda name, row: name.capitalize()
db.mytable.other_id.represent = lambda oid, row: row.myfield
db.mytable.some_uploadfield.represent = lambda val, row: A('get it', _href=URL('download', args=val))
``:python
- ``filter_in`` and ``filter_out`` can be set to callables for further processing of field's value. ``filter_in`` is passed the field's value to be written to the database before an insert or update while ``filter_out`` is passed the value retrieved from the database before field assignment. The value returned by the callable is then used. See [[filter_in and filter_out #filter_in-and-filter_out]] section in this chapter.
- ``custom_qualifier`` is a custom SQL qualifier for the field to be used at table creation time (cannot use for field of type "id", "reference", or "big-reference").




[[field_types]]
#### Field types
``field types``:inxx


==============
**field type** | **default field validators**
``string`` | ``IS_LENGTH(length)`` default length is 512
``text`` | ``IS_LENGTH(length)`` default length is 32768
``blob`` | ``None`` default length is 2**31 (2 GiB)
``boolean`` | ``None``
``integer`` | ``IS_INT_IN_RANGE(-2**31, 2**31)``
``double`` | ``IS_FLOAT_IN_RANGE(-1e100, 1e100)``
``decimal(n,m)`` | ``IS_DECIMAL_IN_RANGE(-10**10, 10**10)``
``date`` | ``IS_DATE()``
``time`` | ``IS_TIME()``
``datetime`` | ``IS_DATETIME()``
``password`` | ``IS_LENGTH(length)`` default length is 512
``upload`` | ``None`` default length is 512
``reference <table>`` | ``IS_IN_DB(db, table.field, format)``
``list:string`` | ``None``
``list:integer`` | ``None``
``list:reference <table>`` | ``IS_IN_DB(db, table._id, format, multiple=True)``
``json`` | ``IS_EMPTY_OR(IS_JSON())`` default length is 512
``bigint`` | ``IS_INT_IN_RANGE(-2**63, 2**63)``
``big-id`` | ``None``
``big-reference`` | ``None``
===================


Decimal requires and returns values as ``Decimal`` objects, as defined in the Python ``decimal`` module. SQLite does not handle the ``decimal`` type so internally we treat it as a ``double``. The (n,m) are the number of digits in total and the number of digits after the decimal point respectively.


The ``big-id`` and, ``big-reference`` are only supported by some of the database engines and are experimental. They are not normally used as field types unless for legacy tables, however, the DAL constructor has a ``bigint_id`` argument that when set to ``True`` makes the ``id`` fields and ``reference`` fields ``big-id`` and ``big-reference`` respectively.


The ``list:<type>`` fields are special because they are designed to take advantage of certain denormalization features on NoSQL (in the case of Google App Engine NoSQL, the field types ``ListProperty`` and ``StringListProperty``) and back-port them all the other supported relational databases. On relational databases lists are stored as a ``text`` field. The items are separated by a ``|`` and each ``|`` in string item is escaped as a ``||``. They are discussed in [[list:<type> and contains #list_types]] section in this chapter.


The ``json`` field type is pretty much explanatory. It can store any json serializable object. It is designed to work specifically for MongoDB and backported to the other database adapters for portability.


``blob``:inxx
``blob`` fields are also special. By default, binary data is encoded in base64 before being stored into the actual database field, and it is decoded when extracted. This has the negative effect of using 33% more storage space than necessary in blob fields, but has the advantageof making the communication independent of back-end-specific escaping conventions.


#### Run-time field and table modification


Most attributes of fields and tables can be modified after they are defined:


``
>>> db.define_table('person', Field('name', default=''), format='%(name)s')
<Table person (id, name)>
>>> db.person._format = '%(name)s/%(id)s'
>>> db.person.name.default = 'anonymous'
``:python
notice that attributes of tables are usually prefixed by an underscore to avoid conflict with possible field names.


You can list the tables that have been defined for a given database connection:


``tables``:inxx
``
>>> db.tables
['person']
``:python


You can query for the type of a table:


``Table``:inxx
``
>>> type(db.person)
<class 'pydal.objects.Table'>
``:python


You can access a table using different syntaxes:
``
>>> db.person is db['person']
True
``:python


You can also list the fields that have been defined for a given table:


``fields``:inxx
``
>>> db.person.fields
['id', 'name']
``:python


Similarly you can access fields from their name in multiple equivalent ways:
``
>>> type(db.person.name)
<class 'pydal.objects.Field'>
>>> db.person.name is db.person['name']
True
``:python


Given a field, you can access the attributes set in its definition:
``
>>> db.person.name.type
string
>>> db.person.name.unique
False
>>> db.person.name.notnull
False
>>> db.person.name.length
32
``:python


including its parent table, tablename, and parent connection:
``
>>> db.person.name._table == db.person
True
>>> db.pers on.name._tablename == 'person'
True
>>> db.person.name._db == db
True
``:python


A field also has methods. Some of them are used to build queries and we will see them later.
A special method of the field object is ``validate`` and it calls the validators for the field.


``
>>> db.person.name.validate('John')
('John', None)
``:python


which returns a tuple ``(value, error)``. ``error`` is ``None`` if the input passes validation.


[[table_migrations]]
### Migrations


``migrations``:inxx


``define_table`` checks whether or not the corresponding table exists. If it does not, it generates the SQL to create it and executes the SQL. If the table does exist but differs from the one being defined, it generates the SQL to alter the table and executes it. If a field has changed type but not name, it will try to convert the data (If you do not want this, you need to redefine the table twice, the first time, letting py4web drop the field by removing it, and the second time adding the newly defined field so that py4web can create it.). If the table exists and matches the current definition, it will leave it alone. In all cases it will create the ``db.person`` object that represents the table.


We refer to this behavior as a "migration". py4web logs all migrations and migration attempts in the file "sql.log".
-------
Notice that by default py4web uses the "app/databases" folder for the log file and all other migration files it needs. You can change this setting the ``folder`` argument to DAL. To set a different log file name, for example "migrate.log" you can do ``db = DAL(..., adapter_args=dict(logfile='migrate.log'))``:python
-------


The first argument of ``define_table`` is always the table name. The other unnamed arguments are the fields (Field). The function also takes an optional keyword argument called "migrate":
``
db.define_table('person', ..., migrate='person.table')
``:python


The value of migrate is the filename where py4web stores internal migration information for this table.
These files are very important and should never be removed while the corresponding tables exist. In cases where a table has been dropped and the corresponding file still exist, it can be removed manually. By default, migrate is set to True. This causes py4web to generate the filename from a hash of the connection string. If migrate is set to False, the migration is not performed, and py4web assumes that the table exists in the datastore and it contains (at least) the fields listed in ``define_table``.


There may not be two tables in the same application with the same migrate filename.


The DAL class also takes a "migrate" argument, which determines the default value of migrate for calls to ``define_table``. For example,
``
db = DAL('sqlite://storage.sqlite', migrate=False)
``:python


will set the default value of migrate to False whenever ``db.define_table`` is called without a migrate argument.


------
Notice that py4web only migrates new columns, removed columns, and changes in column type (except in SQLite). py4web does not migrate changes in attributes such as changes in the values of ``default``, ``unique``, ``notnull``, and ``ondelete``.
------


Migrations can be disabled for all tables at once:


``
db = DAL(..., migrate_enabled=False)
``:python


This is the recommended behavior when two apps share the same database. Only one of the two apps should perform migrations, the other should disabled them.


### Fixing broken migrations
``fake_migrate``:inxx


There are two common problems with migrations and there are ways to recover from them.


One problem is specific with SQLite. SQLite does not enforce column types and cannot drop columns. This means that if you have a column of type string and you remove it, it is not really removed. If you add the column again with a different type (for example datetime) you end up with a datetime column that contains strings (junk for practical purposes). py4web does not complain about this because it does not know what is in the database, until it tries to retrieve records and fails.


If py4web returns an error in some parse function when selecting records, most likely this is due to corrupted data in a column because of the above issue.


The solution consists in updating all records of the table and updating the values in the column in question with None.


The other problem is more generic but typical with MySQL. MySQL does not allow more than one ALTER TABLE in a transaction. This means that py4web must break complex transactions into smaller ones (one ALTER TABLE at the time) and commit one piece at the time. It is therefore possible that part of a complex transaction gets committed and one part fails, leaving py4web in a corrupted state. Why would part of a transaction fail? Because, for example, it involves altering a table and converting a string column into a datetime column, py4web tries to convert the data, but the data cannot be converted. What happens to py4web? It gets confused about what exactly is the table structure actually stored in the database.


The solution consists of enabling fake migrations:
``
db.define_table(...., migrate=True, fake_migrate=True)
``:python


This will rebuild py4web metadata about the table according to the table definition. Try multiple table definitions to see which one works (the one before the failed migration and the one after the failed migration). Once successful remove the ``fake_migrate=True`` parameter.


Before attempting to fix migration problems it is prudent to make a copy of "applications/yourapp/databases/*.table" files.


Migration problems can also be fixed for all tables at once:


``
db = DAL(..., fake_migrate_all=True)
``:python


This also fails if the model describes tables that do not exist in the database,
but it can help narrowing down the problem.


### Migration control summary


The logic of the various migration arguments are summarized in this pseudo-code:
``
if DAL.migrate_enabled and table.migrate:
   if DAL.fake_migrate_all or table.fake_migrate:
       perform fake migration
   else:
       perform migration
``:python


### ``insert``
``insert``:inxx


Given a table, you can insert records


``
>>> db.person.insert(name="Alex")
1
>>> db.person.insert(name="Bob")
2
``:python


Insert returns the unique "id" value of each record inserted.


You can truncate the table, ie, delete all records and reset the counter of the id.


``truncate``:inxx
``
>>> db.person.truncate()
``:python


Now, if you insert a record again, the counter starts again at 1 (this is back-end specific and does not apply to Google NoSQL):
``
>>> db.person.insert(name="Alex")
1
``:python


Notice you can pass a parameter to ``truncate``, for example you can tell SQLite to restart the id counter.


``
>>> db.person.truncate('RESTART IDENTITY CASCADE')
``:python


The argument is in raw SQL and therefore engine specific.


``bulk_insert``:inxx
py4web also provides a bulk_insert method
``
>>> db.person.bulk_insert([{'name': 'Alex'}, {'name': 'John'}, {'name': 'Tim'}])
[3, 4, 5]
``:python


It takes a list of dictionaries of fields to be inserted and performs multiple inserts at once. It returns the list of "id" values of the inserted records. On the supported relational databases there is no advantage in using this function as opposed to looping and performing individual inserts but on Google App Engine NoSQL, there is a major speed advantage.


### ``commit`` and ``rollback``
``commit``:inxx


The insert, truncate, delete, and update operations aren't actually committed until py4web issues the commit command. The create and drop operations may be executed immediately, depending on the database engine. Calls to py4web actions are automatically wrapped in transactions. If you executed commands via the shell, you are required to manually commit:


``
>>> db.commit()
``:python


To check it let's insert a new record:
``
>>> db.person.insert(name="Bob")
2
``:python


and roll back, ie, ignore all operations since the last commit:


``rollback``:inxx
``
>>> db.rollback()
``:python


If you now insert again, the counter will again be set to 2, since the previous insert was rolled back.
``
>>> db.person.insert(name="Bob")
2
``:python


Code in models, views and controllers is enclosed in py4web code that looks like this (pseudo code) :
``
try:
    execute models, controller function and view
except:
    rollback all connections
    log the traceback
    send a ticket to the visitor
else:
    commit all connections
    save cookies, sessions and return the page
``:python


So in models, views and controllers there is no need to ever call ``commit`` or ``rollback`` explicitly in py4web unless you need more granular control.
However, in modules you will need to use ``commit()``.


### Raw SQL


#### Timing queries


All queries are automatically timed by py4web. The variable ``db._timings`` is a list of tuples. Each tuple contains the raw SQL query as passed to the database driver and the time it took to execute in seconds. This variable can be displayed in views using the toolbar:


``
{{=response.toolbar()}}
``:python[lexer='jinja']


#### ``executesql``
``executesql``:inxx


The DAL allows you to explicitly issue SQL statements.


``
>>> db.executesql('SELECT * FROM person;')
[(1, u'Massimo'), (2, u'Massimo')]
``:python


In this case, the return values are not parsed or transformed by the DAL, and the format depends on the specific database driver. This usage with selects is normally not needed, but it is more common with indexes.


``executesql`` takes five optional arguments: ``placeholders``, ``as_dict``, ``fields``, ``colnames``, and ``as_ordered_dict``.


``placeholders`` is an optional
sequence of values to be substituted in
or, if supported by the DB driver, a dictionary with keys
matching named placeholders in your SQL.


If ``as_dict`` is set to True, the results cursor returned by the DB driver will be converted to a sequence of dictionaries keyed with the db field names. Results returned with ``as_dict = True`` are the same as those returned when applying **.as_list()** to a normal select:
``
[{'field1': val1_row1, 'field2': val2_row1}, {'field1': val1_row2, 'field2': val2_row2}]
``:python
``as_ordered_dict`` is pretty much like ``as_dict`` but the former ensures that the order of resulting fields (OrderedDict keys) reflect the order on which they are returned from DB driver:
``
[OrderedDict([('field1', val1_row1), ('field2', val2_row1)]),
 OrderedDict([('field1', val1_row2), ('field2', val2_row2)])]
``:python


The ``fields`` argument is a list of DAL Field objects that match the
fields returned from the DB. The Field objects should be part of one or
more Table objects defined on the DAL object. The ``fields`` list can
include one or more DAL Table objects in addition to or instead of
including Field objects, or it can be just a single table (not in a
list). In that case, the Field objects will be extracted from the
table(s).


Instead of specifying the ``fields`` argument, the ``colnames`` argument
can be specified as a list of field names in tablename.fieldname format.
Again, these should represent tables and fields defined on the DAL
object.


It is also possible to specify both ``fields`` and the associated
``colnames``. In that case, ``fields`` can also include DAL Expression
objects in addition to Field objects. For Field objects in "fields",
the associated ``colnames`` must still be in tablename.fieldname format.
For Expression objects in ``fields``, the associated ``colnames`` can
be any arbitrary labels.


Notice, the DAL Table objects referred to by ``fields`` or ``colnames`` can
be dummy tables and do not have to represent any real tables in the
database. Also, note that the ``fields`` and ``colnames`` must be in the
same order as the fields in the results cursor returned from the DB.


#### ``_lastsql``
``_lastsql``:inxx


Whether SQL was executed manually using executesql or was SQL generated by the DAL, you can always find the SQL code in ``db._lastsql``. This is useful for debugging purposes:


``
>>> rows = db().select(db.person.ALL)
>>> db._lastsql
SELECT person.id, person.name FROM person;
``:python


-------
py4web never generates queries using the "*" operator. py4web is always explicit when selecting fields.
-------


### ``drop``
``drop``:inxx


Finally, you can drop tables and all data will be lost:


``
db.person.drop()
``:python


### Indexes


Currently the DAL API does not provide a command to create indexes on tables, but this can be done using the ``executesql`` command. This is because the existence of indexes can make migrations complex, and it is better to deal with them explicitly. Indexes may be needed for those fields that are used in recurrent queries.


Here is an example of how to [[create an index using SQL in SQLite http://www.sqlite.org/lang_createindex.html]]:
``
db = DAL('sqlite://storage.sqlite')
db.define_table('person', Field('name'))
db.executesql('CREATE INDEX IF NOT EXISTS myidx ON person (name);')
``:python


Other database dialects have very similar syntaxes but may not support the optional "IF NOT EXISTS" directive.


[[LegacyDatabases]]
### Legacy databases and keyed tables


py4web can connect to legacy databases under some conditions.


The easiest way is when these conditions are met:
- Each table must have a unique auto-increment integer field called "id"
- Records must be referenced exclusively using the "id" field.


When accessing an existing table, ie, a table not created by py4web in the current application, always set ``migrate=False``.


If the legacy table has an auto-increment integer field but it is not called "id", py4web can still access it but the table definition must declare the auto-increment field with 'id' type (that is using ``FIeld('...', 'id')``).


``keyed table``:inxx


Finally if the legacy table uses a primary key that is not an auto-increment id field it is possible to use a "keyed table", for example:
``
db.define_table('account',
                Field('accnum', 'integer'),
                Field('acctype'),
                Field('accdesc'),
                primarykey=['accnum', 'acctype'],
                migrate=False)
``:python


- ``primarykey`` is a list of the field names that make up the primary key.
- All primarykey fields have a ``NOT NULL`` set even if not specified.
- Keyed tables can only reference other keyed tables.
- Referencing fields must use the ``reference tablename.fieldname`` format.
- The ``update_record`` function is not available for Rows of keyed tables.


-------
Currently keyed tables are only supported for DB2, MSSQL, Ingres and Informix, but others engines will be added.
-------


At the time of writing, we cannot guarantee that the ``primarykey`` attribute works with every existing legacy table and every supported database backend.
For simplicity, we recommend, if possible, creating a database view that has an auto-increment id field.


### Distributed transaction
``distributed transactions``:inxx


------
At the time of writing this feature is only supported
by PostgreSQL, MySQL and Firebird, since they expose API for two-phase commits.
------


Assuming you have two (or more) connections to distinct PostgreSQL databases, for example:
``
db_a = DAL('postgres://...')
db_b = DAL('postgres://...')
``:python


In your models or controllers, you can commit them concurrently with:
``
DAL.distributed_transaction_commit(db_a, db_b)
``:python


On failure, this function rolls back and raises an ``Exception``.


In controllers, when one action returns, if you have two distinct connections and you do not call the above function, py4web commits them separately. This means there is a possibility that one of the commits succeeds and one fails. The distributed transaction prevents this from happening.


### More on uploads


Consider the following model:
``
db.define_table('myfile',
                Field('image', 'upload', default='path/to/file'))
``:python


In the case of an "upload" field, the default value can optionally be set to a path (an absolute path or a path relative to the current app folder), the default value is then assigned to each new record that does not specify an image.


Notice that this way multiple records may end to reference the same default image file and this could be a problem on a Field having ``autodelete`` enabled.
When you do not want to allow duplicates for the image field (ie multiple records referencing the same file) but still want to set a default value for the "upload" then you need a way to copy the default file for each new record that does not specify an image.
This can be obtained using a file-like object referencing the default file as the ``default`` argument to Field, or even with:
``
Field('image', 'upload', default=dict(data='<file_content>', filename='<file_name>'))
``:python


Normally an insert is handled automatically via a SQLFORM or a crud form (which is a SQLFORM) but occasionally you already have the file on the filesystem and want to upload it programmatically. This can be done in this way:
``
with open(filename, 'rb') as stream:
    db.myfile.insert(image=db.myfile.image.store(stream, filename))
``:python


It is also possible to insert a file in a simpler way and have the insert method call ``store`` automatically:


``
with open(filename, 'rb') as stream:
    db.myfile.insert(image=stream)
``:python


In this case the filename is obtained from the stream object if available.


The ``store`` method of the upload field object takes a file stream and a filename. It uses the filename to determine the extension (type) of the file, creates a new temp name for the file (according to py4web upload mechanism) and loads the file content in this new temp file (under the uploads folder unless specified otherwise). It returns the new temp name, which is then stored in the ``image`` field of the ``db.myfile`` table.


Note, if the file is to be stored in an associated blob field rather than the file system, the ``store`` method will not insert the file in the blob field (because ``store`` is called before the insert), so the file must be explicitly inserted into the blob field:
``
db.define_table('myfile',
                Field('image', 'upload', uploadfield='image_file'),
                Field('image_file', 'blob'))
with open(filename, 'rb') as stream:
    db.myfile.insert(image=db.myfile.image.store(stream, filename),
                     image_file=stream.read())
``:python


The ``retrieve`` method does the opposite of ``store``.


When uploaded files are stored on filesystem (as in the case of a plain ``Field('image', 'upload')``) the code:
``
row = db(db.myfile).select().first()
(filename, fullname) = db.myfile.image.retrieve(row.image, nameonly=True)
``:python
retrieves the original file name (filename) as seen by the user at upload time and the name of stored file (fullname, with path relative to application folder).
While in general the call:
``
(filename, stream) = db.myfile.image.retrieve(row.image)
``:python
retrieves the original file name (filename) and a file-like object ready to access uploaded file data (stream).
-------
Notice that the stream returned by ``retrieve`` is a real file object in the case that uploaded files are stored on filesystem.
In that case remember to close the file when you have done calling ``stream.close()``.
-------


Here is an example of safe usage of ``retrieve``:
``
from contextlib import closing
import shutil
row = db(db.myfile).select().first()
(filename, stream) = db.myfile.image.retrieve(row.image)
with closing(stream) as src, closing(open(filename, 'wb')) as dest:
    shutil.copyfileobj(src, dest)
``:python


### ``Query``, ``Set``, ``Rows``
``Query``:inxx ``Set``:inxx


Let's consider again the table defined (and dropped) previously and insert three records:
``
>>> db.define_table('person', Field('name'))
<Table person (id, name)>
>>> db.person.insert(name="Alex")
1
>>> db.person.insert(name="Bob")
2
>>> db.person.insert(name="Carl")
3
``:python


You can store the table in a variable. For example, with variable ``person``, you could do:


``Table``:inxx
``
>>> person = db.person
``:python


You can also store a field in a variable such as ``name``. For example, you could also do:


``Field``:inxx
``
>>> name = person.name
``:python


You can even build a query (using operators like ==, !=, <, >, <=, >=, like, belongs) and store the query in a variable ``q`` such as in:


``
>>> q = name == 'Alex'
``:python


When you call ``db`` with a query, you define a set of records. You can store it in a variable ``s`` and write:


``
>>> s = db(q)
``:python


Notice that no database query has been performed so far. DAL + Query simply define a set of records in this db that match the query.
py4web determines from the query which table (or tables) are involved and, in fact, there is no need to specify that.


### ``select``
``select``:inxx


Given a Set, ``s``, you can fetch the records with the command ``select``:


``Rows``:inxx
``
>>> rows = s.select()
``:python


``Row``:inxx
It returns an iterable object of class ``pydal.objects.Rows`` whose elements are Row objects. ``pydal.objects.Row`` objects act like dictionaries, but their elements can also be accessed as attributes, like ``gluon.storage.Storage``.The former differ from the latter because its values are read-only.


The Rows object allows looping over the result of the select and printing the selected field values for each row:
``
>>> for row in rows:
... print row.id, row.name
... 
1 Alex
``:python


You can do all the steps in one statement:
``
>>> for row in db(db.person.name == 'Alex').select():
... print row.name
... 
Alex
``:python


``ALL``:inxx


The select command can take arguments. All unnamed arguments are interpreted as the names of the fields that you want to fetch. For example, you can be explicit on fetching field "id" and field "name":
``
>>> for row in db().select(db.person.id, db.person.name):
... print row.name
... 
Alex
Bob
Carl
``:python


The table attribute ALL allows you to specify all fields:
``
>>> for row in db().select(db.person.ALL):
... print row.id, row.name
... 
1 Alex
2 Bob
3 Carl
``:python


Notice that there is no query string passed to db. py4web understands that if you want all fields of the table person without additional information then you want all records of the table person.


An equivalent alternative syntax is the following:
``
>>> for row in db(db.person).select():
... print row.id, row.name
... 
1 Alex
2 Bob
3 Carl
``:python


and py4web understands that if you ask for all records of the table person without additional information, then you want all the fields of table person.


Given one row


``
>>> row = rows[0]
``:python


you can extract its values using multiple equivalent expressions:


``
>>> row.name
Alex
>>> row['name']
Alex
>>> row('person.name')
Alex
``:python


The latter syntax is particularly handy when selecting en expression instead of a column. We will show this later.


You can also do
``
rows.compact = False
``:python
to disable the notation
``
rows[i].name
``:python
and enable, instead, the less compact notation:
``
rows[i].person.name
``:python
Yes this is unusual and rarely needed.


Row objects also have two important methods:
``
row.delete_record()
``:python
and 
``
row.update_record(name="new value")
``:python


#### Using an iterator-based select for lower memory use


Python "iterators" are a type of "lazy-evaluation". They 'feed' data one step at time; traditional Python loops create the entire set of data in memory before looping. 


The traditional use of select is:
``
for row in db(db.table).select():
    ...
``:python


but for large numbers of rows, using an iterator-based alternative has dramatically lower memory use:
``
for row in db(db.table).iterselect():
    ...
``:python
Testing shows this is around 10% faster as well, even on machines with large RAM.


#### Rendering rows using represent


You may wish to rewrite rows returned by select to take advantage of formatting information contained in the represents setting of the fields. 


``
rows = db(query).select()  
repr_row = rows.render(0)
``:python


If you don't specify an index, you get a generator to iterate over all the rows:


``
for row in rows.render():
    print row.myfield
``:python


Can also be applied to slices:


``
for row in rows[0:10].render():
    print row.myfield
``:python


If you only want to transform selected fields via their "represent" attribute, you can list them in the "fields" argument:


``
repr_row = row.render(0, fields=[db.mytable.myfield])
``:python


Note, it returns a transformed copy of the original Row, so there's no update_record (which you wouldn't want anyway) or delete_record.




#### Shortcuts
``DAL shortcuts``:inxx


The DAL supports various code-simplifying shortcuts.
In particular:
``
myrecord = db.mytable[id]
``:python


returns the record with the given ``id`` if it exists. If the ``id`` does not exist, it returns ``None``. The above statement is equivalent to


``
myrecord = db(db.mytable.id == id).select().first()
``:python


You can delete records by id:


``
del db.mytable[id]
``:python


and this is equivalent to


``
db(db.mytable.id == id).delete()
``:python


and deletes the record with the given ``id``, if it exists.


Note: this delete shortcut syntax does not currently work if [[versioning #versioning]] is activated


You can insert records:


``
db.mytable[None] = dict(myfield='somevalue')
``:python


It is equivalent to


``
db.mytable.insert(myfield='somevalue')
``:python


and it creates a new record with field values specified by the dictionary on the right hand side.


Note: insert shortcut was previously ``db.table[0] = ...``. It has changed in PyDAL 19.02 to permit normal usage of id 0.


You can update records:


``
db.mytable[id] = dict(myfield='somevalue')
``:python


which is equivalent to


``
db(db.mytable.id == id).update(myfield='somevalue')
``:python


and it updates an existing record with field values specified by the dictionary on the right hand side.


#### Fetching a ``Row``


Yet another convenient syntax is the following:


``
record = db.mytable(id)
record = db.mytable(db.mytable.id == id)
record = db.mytable(id, myfield='somevalue')
``:python


Apparently similar to ``db.mytable[id]`` the above syntax is more flexible and safer. First of all it checks whether ``id`` is an int (or ``str(id)`` is an int) and returns ``None`` if not (it never raises an exception). It also allows to specify multiple conditions that the record must meet. If they are not met, it also returns ``None``.


#### Recursive ``select``s
``recursive selects``:inxx


Consider the previous table person and a new table "thing" referencing a "person":
``
db.define_table('thing',
                Field('name'),
                Field('owner_id', 'reference person'))
``:python


and a simple select from this table:
``
things = db(db.thing).select()
``:python


which is equivalent to


``
things = db(db.thing._id != None).select()
``:python


``_id``:inxx
where ``_id`` is a reference to the primary key of the table. Normally ``db.thing._id`` is the same as ``db.thing.id`` and we will assume that in most of this book.


For each Row of things it is possible to fetch not just fields from the selected table (thing) but also from linked tables (recursively):
``
for thing in things:
    print thing.name, thing.owner_id.name
``:python


Here ``thing.owner_id.name`` requires one database select for each thing in things and it is therefore inefficient. We suggest using joins whenever possible instead of recursive selects, nevertheless this is convenient and practical when accessing individual records.


You can also do it backwards, by selecting the things referenced by a person:


``
person = db.person(id)
for thing in person.thing.select(orderby=db.thing.name):
    print person.name, 'owns', thing.name
``:python


In this last expression ``person.thing`` is a shortcut for


``
db(db.thing.owner_id == person.id)
``:python


ie the Set of ``thing``s referenced by the current ``person``. This syntax breaks down if the referencing table has multiple references to the referenced table. In this case one needs to be more explicit and use a full Query.


[[sqltable]]
#### Serializing ``Rows`` in views


Given the following action containing a query
``SQLTABLE``:inxx


``
def index():
    return dict(rows = db(query).select())
``:python


The result of a select can be displayed in a view with the following syntax:
``
{{extend 'layout.html'}}
<h1>Records</h1>
{{=rows}}
``:python[lexer='html+jinja']


Which is equivalent to:
``
{{extend 'layout.html'}}
<h1>Records</h1>
{{=SQLTABLE(rows)}}
``:python[lexer='html+jinja']


``SQLTABLE`` converts the rows into an HTML table with a header containing the column names and one row per record. The rows are marked as alternating class "even" and class "odd". Under the hood, Rows is first converted into a SQLTABLE object (not to be confused with Table) and then serialized. The values extracted from the database are also formatted by the validators associated to the field and then escaped.


Yet it is possible and sometimes convenient to call SQLTABLE explicitly.


The SQLTABLE constructor takes the following optional arguments:


- ``linkto`` lambda function or an action to be used to link reference fields (default to None).
If you assign it a string with the name of an action, it will generate a link to that function passing it, as args, the name of the table and the id of each record (in this order). Example:
``
linkto = 'pointed_function' # generates something like <a href="pointed_function/table_name/id_value">
``:python
If you want a different link to be generated, you can specify a lambda, wich will receive as parameters, the value of the id, the type of the object (eg table), and the name of the object. For example, if you want to receive the args in reverse order:
``
linkto = lambda id, type, name: URL(f='pointed_function', args=[id, name])
``:python
- ``upload`` the URL or the download action to allow downloading of uploaded files (default to None)
- ``headers`` a dictionary mapping field names to their labels to be used as headers (default to ``{}``). It can also be an instruction. Currently we support ``headers='fieldname:capitalize'``.
- ``truncate`` the number of characters for truncating long values in the table (default is 16)
- ``columns`` the list of fieldnames to be shown as columns (in tablename.fieldname format).
   Those not listed are not displayed (defaults to all).
- ``**attributes`` generic helper attributes to be passed to the most external TABLE object.


Here is an example:
``
{{extend 'layout.html'}}
<h1>Records</h1>
{{=SQLTABLE(rows,
            headers='fieldname:capitalize',
            truncate=100,
            upload=URL('download'))
}}
``:python[lexer='html+jinja']


``SQLFORM.grid``:inxx ``SQLFORM.smartgrid``:inxx


------
``SQLTABLE`` is useful but there are times when one needs more. ``SQLFORM.grid`` is an extension of SQLTABLE that creates a table with search features and pagination, as well as ability to open detailed records, create, edit and delete records. ``SQLFORM.smartgrid`` is a further generalization that allows all of the above but also creates buttons to access referencing records.
------


Here is an example of usage of ``SQLFORM.grid``:


``
def index():
    return dict(grid=SQLFORM.grid(query))
``:python


and the corresponding view:


``
{{extend 'layout.html'}}
{{=grid}}
``:python[lexer='jinja']


For working with multiple rows, ``SQLFORM.grid`` and ``SQLFORM.smartgrid`` are preferred to ``SQLTABLE`` because they are more powerful. Please see [[Chapter 7 ../07#SQLFORM-grid-and-SQLFORM-smartgrid]].


[[orderby]] [[limitby]] [[distinct]]
#### ``orderby``, ``groupby``, ``limitby``, ``distinct``, ``having``, ``orderby_on_limitby``, ``join``, ``left``, ``cache``


The ``select`` command takes a number of optional arguments.


##### orderby
You can fetch the records sorted by name:


``orderby``:inxx ``groupby``:inxx ``having``:inxx
``
>>> for row in db().select(db.person.ALL, orderby=db.person.name):
... print row.name
... 
Alex
Bob
Carl
``:python


You can fetch the records sorted by name in reverse order (notice the tilde):
``
>>> for row in db().select(db.person.ALL, orderby=~db.person.name):
... print row.name
...
Carl
Bob
Alex
``:python


You can have the fetched records appear in random order:
``
>>> for row in db().select(db.person.ALL, orderby='<random>'):
... print row.name
... 
Carl
Alex
Bob
``:python


-----
The use of ``orderby='<random>'`` is not supported on Google NoSQL. However, to overcome this limit, sorting can be accomplished on selected rows:
``
import random
rows = db(...).select().sort(lambda row: random.random())
``:python
-----


You can sort the records according to multiple fields by concatenating them with a "|":
``
>>> for row in db().select(db.person.name, orderby=db.person.name|db.person.id):
... print row.name
... 
Alex
Bob
Carl
``:python


##### groupby, having
Using ``groupby`` together with ``orderby``, you can group records with the same value for the specified field (this is back-end specific, and is not on the Google NoSQL):
``
>>> for row in db().select(db.person.ALL,
... orderby=db.person.name,
... groupby=db.person.name):
... print row.name
... 
Alex
Bob
Carl
``:python


You can use ``having`` in conjunction with ``groupby`` to group conditionally (only those ``having`` the condition are grouped).


``
>>> print db(query1).select(db.person.ALL, groupby=db.person.name, having=query2)
``:python


Notice that query1 filters records to be displayed, query2 filters records to be grouped.


##### distinct
``distinct``:inxx


With the argument ``distinct=True``, you can specify that you only want to select distinct records. This has the same effect as grouping using all specified fields except that it does not require sorting. When using distinct it is important not to select ALL fields, and in particular not to select the "id" field, else all records will always be distinct.


Here is an example:
``
>>> for row in db().select(db.person.name, distinct=True):
... print row.name
... 
Alex
Bob
Carl
``:python


Notice that ``distinct`` can also be an expression, for example:
``
>>> for row in db().select(db.person.name, distinct=db.person.name):
... print row.name
... 
Alex
Bob
Carl
``:python


##### limitby
With ``limitby=(min, max)``, you can select a subset of the records from offset=min to but not including offset=max.
In the next example we select the first two records starting at zero:


``limitby``:inxx
``
>>> for row in db().select(db.person.ALL, limitby=(0, 2)):
... print row.name
... 
Alex
Bob
``:python


##### orderby_on_limitby
``orderby_on_limitby``:inxx
Note that the DAL defaults to implicitly adding an orderby when using a limitby.
This ensures the same query returns the same results each time, important for pagination.
But it can cause performance problems. 
use ``orderby_on_limitby = False`` to change this (this defaults to True). 


##### join, left
These are involved in managing [[one to many relations #One-to-many-relation]]. They are described in [[Inner join #Inner-join]] and [[Left outer join #Left-outer-join]] sections respectively.


##### cache, cacheable
An example use which gives much faster selects is:
``rows = db(query).select(cache=(cache.ram, 3600), cacheable=True)``:python
Look at [[Caching selects #Caching-selects]] section in this chapter, to understand what the trade-offs are.


#### Logical operators
``and``:inxx ``or``:inxx ``not``:inxx


Queries can be combined using the binary AND operator "``&``":


``
>>> rows = db((db.person.name=='Alex') & (db.person.id > 3)).select()
>>> for row in rows: print row.id, row.name
>>> len(rows)
0
``:python


and the binary OR operator "``|``":
``
>>> rows = db((db.person.name == 'Alex') | (db.person.id > 3)).select()
>>> for row in rows: print row.id, row.name
1 Alex
``:python


You can negate a sub-query inverting its operator:
``
>>> rows = db((db.person.name != 'Alex') | (db.person.id > 3)).select()
>>> for row in rows: print row.id, row.name
2 Bob
3 Carl
``:python


or by explicit negation with the "``~``" unary operator:
``
>>> rows = db(~(db.person.name == 'Alex') | (db.person.id > 3)).select()
>>> for row in rows: print row.id, row.name
2 Bob
3 Carl
``:python


------
Due to Python restrictions in overloading "``and``" and "``or``" operators, these cannot be used in forming queries. The binary operators "``&``" and "``|``" must be used instead. Note that these operators (unlike "``and``" and "``or``") have higher precedence than comparison operators, so the "extra" parentheses in the above examples are mandatory. Similarly, the unary operator "``~``" has higher precedence than comparison operators, so ``~``-negated comparisons must also be parenthesized.
------


It is also possible to build queries using in-place logical operators:


``
>>> query = db.person.name != 'Alex'
>>> query &= db.person.id > 3
>>> query |= db.person.name == 'John'
``:python


#### ``count``, ``isempty``, ``delete``, ``update``


You can count records in a set:


``count``:inxx ``isempty``:inxx


``
>>> db(db.person.name != 'William').count()
3
``:python


Notice that ``count`` takes an optional ``distinct`` argument which defaults to False, and it works very much like the same argument for ``select``. ``count`` has also a ``cache`` argument that works very much like the equivalent argument of the ``select`` method.


Sometimes you may need to check if a table is empty. A more efficient way than counting is using the ``isempty`` method:


``
>>> db(db.person).isempty()
False
``:python


You can delete records in a set:


``delete``:inxx
``
>>> db(db.person.id > 3).delete()
0
``:python


The ``delete`` method returns the number of records that were deleted.


And you can update all records in a set by passing named arguments corresponding to the fields that need to be updated:


``update``:inxx
``
>>> db(db.person.id > 2).update(name='Ken')
1
``:python


The ``update`` method returns the number of records that were updated.


#### Expressions


The value assigned an update statement can be an expression. For example consider this model
``
db.define_table('person',
                Field('name'),
                Field('visits', 'integer', default=0))


db(db.person.name == 'Massimo').update(visits = db.person.visits + 1)
``:python


The values used in queries can also be expressions
``
db.define_table('person',
                Field('name'),
                Field('visits', 'integer', default=0),
                Field('clicks', 'integer', default=0))


db(db.person.visits == db.person.clicks + 1).delete()
``:python


#### ``case``
``case``:inxx


An expression can contain a case clause for example:


``
>>> condition = db.person.name.startswith('B')
>>> yes_or_no = condition.case('Yes', 'No')
>>> for row in db().select(db.person.name, yes_or_no):
... print row.person.name, row[yes_or_no] # could be row(yes_or_no) too
... 
Alex No
Bob Yes
Ken No
``:python


#### ``update_record``
``update_record``:inxx


py4web also allows updating a single record that is already in memory using ``update_record``


``
>>> row = db(db.person.id == 2).select().first()
>>> row.update_record(name='Curt')
<R ow {'id': 2L, 'name': 'Curt'}>
``:python


``update_record`` should not be confused with


``
>>> row.update(name='Curt')
``:python


because for a single row, the method ``update`` updates the row object but not the database record, as in the case of ``update_record``.


It is also possible to change the attributes of a row (one at a time) and then call ``update_record()`` without arguments to save the changes:


``
>>> row = db(db.person.id > 2).select().first()
>>> row.name = 'Philip'
>>> row.update_record() # saves above change
<Row {'id': 3L, 'name': 'Philip'}>
``:python


-------
Note, you should avoid using ``row.update_record()`` with no arguments when the ``row`` object contains fields that have an ``update`` attribute (eg, ``Field('modified_on', update=request.now)``). Calling ``row.update_record()`` will retain ''all'' of the existing values in the ``row`` object, so any fields with ``update`` attributes will have no effect in this case. Be particularly mindful of this with tables that include ``auth.signature``.
-------


The ``update_record`` method is available only if the table's ``id`` field is included in the select, and ``cacheable`` is not set to ``True``.


#### Inserting and updating from a dictionary


A common issue consists of needing to insert or update records in a table where the name of the table, the field to be updated, and the value for the field are all stored in variables. For example: ``tablename``, ``fieldname``, and ``value``.


The insert can be done using the following syntax:


``
db[tablename].insert(**{fieldname:value})
``:python


The update of record with given id can be done with: ``_id``:inxx


``
db(db[tablename]._id == id).update(**{fieldname:value})
``:python


Notice we used ``table._id`` instead of ``table.id``. In this way the query works even for tables with a primary key field with type other than "id".


#### ``first`` and ``last``
``first``:inxx ``last``:inxx


Given a Rows object containing records:


``
rows = db(query).select()
first_row = rows.first()
last_row = rows.last()
``:python


are equivalent to
``
first_row = rows[0] if len(rows) else None
last_row = rows[-1] if len(rows) else None
``:python


Notice, ``first()`` and ``last()`` allow you to obtain obviously the first and last record present in your query, but this won't mean that these records are going to be the first or last inserted records. In case you want the first or last record inputted in a given table don't forget to use ``orderby=db.table_name.id``. If you forget you will only get the first and last record returned by your query which are often in a random order determined by the backend query optimiser.


#### ``as_dict`` and ``as_list``
``as_list``:inxx ``as_dict``:inxx


A Row object can be serialized into a regular dictionary using the ``as_dict()`` method and a Rows object can be serialized into a list of dictionaries using the ``as_list()`` method. Here are some examples:
``
rows = db(query).select()
rows_list = rows.as_list()
first_row_dict = rows.first().as_dict()
``:python


These methods are convenient for passing Rows to generic views and or to store Rows in sessions (since Rows objects themselves cannot be serialized since contain a reference to an open DB connection):
``
rows = db(query).select()
session.rows = rows # not allowed!
session.rows = rows.as_list() # allowed!
``:python


#### Combining rows


Rows objects can be combined at the Python level. Here we assume:


``
>>> print rows1
person.name
Max
Tim


>>> print rows2
person.name
John
Tim
``:python


You can do union of the records in two sets of rows:


``
>>> rows3 = rows1 + rows2
>>> print rows3
person.name
Max
Tim
John
Tim
``:python


You can do union of the records removing duplicates:


``
>>> rows3 = rows1 | rows2
>>> print rows3
person.name
Max
Tim
John
``:python


You can do intersection of the records in two sets of rows:


``
>>> rows3 = rows1 & rows2
>>> print rows3
person.name
Tim
``:python


#### ``find``, ``exclude``, ``sort``
``find``:inxx ``exclude``:inxx ``sort``:inxx


Some times you need to perform two selects and one contains a subset of a previous select. In this case it is pointless to access the database again. The ``find``, ``exclude`` and ``sort`` objects allow you to manipulate a Rows object and generate another one without accessing the database. More specifically:
- ``find`` returns a new set of Rows filtered by a condition and leaves the original unchanged.
- ``exclude`` returns a new set of Rows filtered by a condition and removes them from the original Rows.
- ``sort`` returns a new set of Rows sorted by a condition and leaves the original unchanged.


All these methods take a single argument, a function that acts on each individual row.


Here is an example of usage:
``
>>> db.define_table('person', Field('name'))
<Table person (id, name)>
>>> db.person.insert(name='John')
1
>>> db.person.insert(name='Max')
2
>>> db.person.insert(name='Alex')
3
>>> rows = db(db.person).select()
>>> for row in rows.find(lambda row: row.name[0]=='M'):
... print row.name
... 
Max
>>> len(rows)
3
>>> for row in rows.exclude(lambda row: row.name[0]=='M'):
... print row.name
... 
Max
>>> len(rows)
2
>>> for row in rows.sort(lambda row: row.name):
... print row.name
... 
Alex
John
``:python


They can be combined:
``
>>> rows = db(db.person).select()
>>> rows = rows.find(lambda row: 'x' in row.name).sort(lambda row: row.name)
>>> for row in rows:
... print row.name
... 
Alex
Max
``:python


Sort takes an optional argument ``reverse=True`` with the obvious meaning.


The ``find`` method has an optional ``limitby`` argument with the same syntax and functionality as the Set ``select`` method.


### Other methods


#### ``update_or_insert``
``update_or_insert``:inxx


Some times you need to perform an insert only if there is no record with the same values as those being inserted.
This can be done with


``
db.define_table('person',
                Field('name'),
                Field('birthplace'))


db.person.update_or_insert(name='John', birthplace='Chicago')
``:python


The record will be inserted only if there is no other user called John born in Chicago.


You can specify which values to use as a key to determine if the record exists. For example:
``
db.person.update_or_insert(db.person.name == 'John',
                           name='John',
                           birthplace='Chicago')
``:python


and if there is John his birthplace will be updated else a new record will be created.


The selection criteria in the example above is a single field. 
It can also be a query, such as 
``
db.person.update_or_insert((db.person.name == 'John') & (db.person.birthplace == 'Chicago'),
                           name='John',
                           birthplace='Chicago',
                           pet='Rover')
``:python


#### ``validate_and_insert``, ``validate_and_update``
``validate_and_insert``:inxx ``validate_and_update``:inxx


The function


``
ret = db.mytable.validate_and_insert(field='value')
``:python


works very much like


``
id = db.mytable.insert(field='value')
``:python


except that it calls the validators for the fields before performing the insert and bails out if the validation does not pass. If validation does not pass the errors can be found in ``ret.errors``. ``ret.errors`` holds a key-value mapping where each key is the field name whose validation failed, and the value of the key is the result from the validation error (much like ``form.errors``). If it passes, the id of the new record is in ``ret.id``. Mind that normally validation is done by the form processing logic so this function is rarely needed.


Similarly


``
ret = db(query).validate_and_update(field='value')
``:python


works very much the same as


``
num = db(query).update(field='value')
``:python


except that it calls the validators for the fields before performing the update. Notice that it only works if query involves a single table. The number of updated records can be found in ``ret.updated`` and errors will be in ``ret.errors``.


#### ``smart_query`` (experimental)


There are times when you need to parse a query using natural language such as


``
name contains m and age greater than 18
``:python[lexer=None]


The DAL provides a method to parse this type of queries:


``
search = 'name contains m and age greater than 18'
rows = db.smart_query([db.person], search).select()
``:python


The first argument must be a list of tables or fields that should be allowed in the search. It raises a ``RuntimeError`` if the search string is invalid. This functionality can be used to build RESTful interfaces (see chapter 10) and it is used internally by the ``SQLFORM.grid`` and ``SQLFORM.smartgrid``.


In the smart_query search string, a field can be identified by fieldname only and or by tablename.fieldname. Strings may be delimited by double quotes if they contain spaces.


### Computed fields
``compute``:inxx


DAL fields may have a ``compute`` attribute. This must be a function (or lambda) that takes a Row object and returns a value for the field. When a new record is modified, including both insertions and updates, if a value for the field is not provided, py4web tries to compute from the other field values using the ``compute`` function. Here is an example:
``
>>> db.define_table('item',
... Field('unit_price', 'double'),
... Field('quantity', 'integer'),
... Field('total_price',
... compute=lambda r: r['unit_price'] * r['quantity']))
<Table item (id, unit_price, quantity, total_price)>
>>> rid = db.item.insert(unit_price=1.99, quantity=5)
>>> db.item[rid]
<Row {'total_price': '9.95', 'unit_price': 1.99, 'id': 1L, 'quantity': 5L}>
``:python


Notice that the computed value is stored in the db and it is not computed on retrieval, as in the case of virtual fields, described next. Two typical applications of computed fields are:
- in wiki applications, to store the processed input wiki text as HTML, to avoid re-processing on every request
- for searching, to compute normalized values for a field, to be used for searching.


Computed fields are evaluated in the order in which they are defined in the table definition. A computed field can refer to previously defined computed fields (new after v 2.5.1)


### Virtual fields
``virtual fields``:inxx


Virtual fields are also computed fields (as in the previous subsection) but they differ from those because they are ''virtual'' in the sense that they are not stored in the db and they are computed each time records are extracted from the database. They can be used to simplify the user's code without using additional storage but they cannot be used for searching.


#### New style virtual fields (experimental)


py4web provides a new and easier way to define virtual fields and lazy virtual fields. This section is marked experimental because the APIs may still change a little from what is described here.


Here we will consider the same example as in the previous subsection. In particular we consider the following model:


``
db.define_table('item',
                Field('unit_price', 'double'),
                Field('quantity', 'integer'))
``:python


One can define a ``total_price`` virtual field as


``
db.item.total_price = Field.Virtual(lambda row: row.item.unit_price * row.item.quantity)
``:python


ie by simply defining a new field ``total_price`` to be a ``Field.Virtual``. The only argument of the constructor is a function that takes a row and returns the computed values.


A virtual field defined as the one above is automatically computed for all records when the records are selected:


``
for row in db(db.item).select():
    print row.total_price
``:python


It is also possible to define method fields which are calculated on-demand, when called.
For example:


``
db.item.discounted_total = \\
    Field.Method(lambda row, discount=0.0:
                 row.item.unit_price * row.item.quantity * (100.0 - discount / 100))
``:python


In this case ``row.discounted_total`` is not a value but a function. The function takes the same arguments as the function passed to the ``Method`` constructor except for ``row`` which is implicit (think of it as ``self`` for objects).


The lazy field in the example above allows one to compute the total price for each ``item``:


``
for row in db(db.item).select(): print row.discounted_total()
``:python


And it also allows to pass an optional ``discount`` percentage (say 15%):


``
for row in db(db.item).select(): print row.discounted_total(15)
``:python


Virtual and Method fields can also be defined in place when a table is defined:


``
db.define_table('item',
                Field('unit_price', 'double'),
                Field('quantity', 'integer'),
                Field.Virtual('total_price', lambda row: ...),
                Field.Method('discounted_total', lambda row, discount=0.0: ...))
``:python


------
Mind that virtual fields do not have the same attributes as regular fields (length, default, required, etc). They do not appear in the list of ``db.table.fields`` and in older versions of py4web they require a special approach to display in SQLFORM.grid and SQLFORM.smartgrid. See the discussion on grids and virtual fields in [[Chapter 7 ../07#Virtual-fields-in-SQLFORM-grid-and-smartgrid]].
------


#### Old style virtual fields


In order to define one or more virtual fields, you can also define a container class, instantiate it and link it to a table or to a select. For example, consider the following table:


``
db.define_table('item',
                Field('unit_price', 'double'),
                Field('quantity', 'integer'))
``:python


One can define a ``total_price`` virtual field as
``
class MyVirtualFields(object):
    def total_price(self):
        return self.item.unit_price * self.item.quantity


db.item.virtualfields.append(MyVirtualFields())
``:python


Notice that each method of the class that takes a single argument (self) is a new virtual field. ``self`` refers to each one row of the select. Field values are referred by full path as in ``self.item.unit_price``. The table is linked to the virtual fields by appending an instance of the class to the table's ``virtualfields`` attribute.


Virtual fields can also access recursive fields as in
``
db.define_table('item',
                Field('unit_price', 'double'))


db.define_table('order_item',
                Field('item', 'reference item'),
                Field('quantity', 'integer'))


class MyVirtualFields(object):
    def total_price(self):
        return self.order_item.item.unit_price * self.order_item.quantity


db.order_item.virtualfields.append(MyVirtualFields())
``:python


Notice the recursive field access ``self.order_item.item.unit_price`` where ``self`` is the looping record.


They can also act on the result of a JOIN
``
rows = db(db.order_item.item == db.item.id).select()


class MyVirtualFields(object):
    def total_price(self):
        return self.item.unit_price * self.order_item.quantity


rows.setvirtualfields(order_item=MyVirtualFields())


for row in rows:
    print row.order_item.total_price
``:python


Notice how in this case the syntax is different. The virtual field accesses both ``self.item.unit_price`` and ``self.order_item.quantity`` which belong to the join select. The virtual field is attached to the rows of the table using the ``setvirtualfields`` method of the rows object. This method takes an arbitrary number of named arguments and can be used to set multiple virtual fields, defined in multiple classes, and attach them to multiple tables:
``
class MyVirtualFields1(object):
    def discounted_unit_price(self):
        return self.item.unit_price * 0.90


class MyVirtualFields2(object):
    def total_price(self):
        return self.item.unit_price * self.order_item.quantity
    def discounted_total_price(self):
        return self.item.discounted_unit_price * self.order_item.quantity


rows.setvirtualfields(item=MyVirtualFields1(),
                      order_item=MyVirtualFields2())


for row in rows:
    print row.order_item.discounted_total_price
``:python


Virtual fields can be ''lazy''; all they need to do is return a function and access it by calling the function:
``
db.define_table('item',
                Field('unit_price', 'double'),
                Field('quantity', 'integer'))


class MyVirtualFields(object):
    def lazy_total_price(self):
        def lazy(self=self):
            return self.item.unit_price * self.item.quantity
        return lazy


db.item.virtualfields.append(MyVirtualFields())


for item in db(db.item).select():
    print item.lazy_total_price()
``:python


or shorter using a lambda function:
``
class MyVirtualFields(object):
    def lazy_total_price(self):
        return lambda self=self: self.item.unit_price * self.item.quantity
``:python


### One to many relation
``one to many``:inxx


To illustrate how to implement one to many relations with the DAL, define another table "thing" that refers to the table "person" which we redefine here:
``
>>> db.define_table('person',
... Field('name'))
<Table person (id, name)>
>>> db.person.insert(name='Alex')
1
>>> db.person.insert(name='Bob')
2
>>> db.person.insert(name='Carl')
3
>>> db.de fine_table('thing',
... Field('name'),
... Field('owner_id', 'reference person'))
<Table thing (id, name, owner_id)>
``:python


Table "thing" has two fields, the name of the thing and the owner of the thing. The "owner_id" field is a reference field, it is intended that the field reference the other table by its id.
A reference type can be specified in two equivalent ways, either:
``Field('owner_id', 'reference person')``:python
or:
``Field('owner_id', db.person)``:python


The latter is always converted to the former. They are equivalent except in the case of lazy tables, self references or other types of cyclic references where the former notation is the only allowed notation.


Now, insert three things, two owned by Alex and one by Bob:
``
>>> db.thing.insert(name='Boat', owner_id=1)
1
>>> db.thing.insert(name='Chair', owner_id=1)
2
>>> db.thing.insert(name='Shoes', owner_id=2)
3
``:python


You can select as you did for any other table:
``
>>> for row in db(db.thing.owner_id == 1).select():
... print row.name
... 
Boat
Chair
``:python


Because a thing has a reference to a person, a person can have many things, so a record of table person now acquires a new attribute thing, which is a Set, that defines the things of that person. This allows looping over all persons and fetching their things easily:


``referencing``:inxx
``
>>> for person in db().select(db.person.ALL):
... print person.name
... for thing in person.thing.select():
... print ' ', thing.name
...
Alex
     Boat
     Chair
Bob
     Shoes
Carl
``:python


#### Inner joins


Another way to achieve a similar result is by using a join, specifically an INNER JOIN. py4web performs joins automatically and transparently when the query links two or more tables as in the following example:


``Rows``:inxx ``inner join``:inxx ``join``:inxx
``
>>> rows = db(db.person.id == db.thing.owner_id).select()
>>> for row in rows:
... print row.person.name, 'has', row.thing.name
... 
Alex has Boat
Alex has Chair
Bob has Shoes
``:python


Observe that py4web did a join, so the rows now contain two records, one from each table, linked together. Because the two records may have fields with conflicting names, you need to specify the table when extracting a field value from a row. This means that while before you could do:
``
row.name
``:python


and it was obvious whether this was the name of a person or a thing, in the result of a join you have to be more explicit and say:
``
row.person.name
``:python


or:
``
row.thing.name
``:python


There is an alternative syntax for INNER JOINS:
``
>>> rows = db(db.person).select(join=db.thing.on(db.person.id == db.thing.owner_id))
>>> for row in rows:
... print row.person.name, 'has', row.thing.name
... 
Alex has Boat
Alex has Chair
Bob has Shoes
``:python


While the output is the same, the generated SQL in the two cases can be different. The latter syntax removes possible ambiguities when the same table is joined twice and aliased:


``
db.define_table('thing',
                Field('name'),
                Field('owner_id1', 'reference person'),
                Field('owner_id2', 'reference person'))


rows = db(db.person).select(
        join=[db.person.with_alias('owner_id1').on(db.person.id == db.thing.owner_id1),
              db.person.with_alias('owner_id2').on(db.person.id == db.thing.owner_id2)])
``:python


The value of ``join`` can be list of ``db.table.on(...)`` to join.


#### Left outer join
``Rows``:inxx ``left outer join``:inxx ``outer join``:inxx


Notice that Carl did not appear in the list above because he has no things. If you intend to select on persons (whether they have things or not) and their things (if they have any), then you need to perform a LEFT OUTER JOIN. This is done using the argument "left" of the select. Here is an example:


``
>>> rows = db().select(db.person.ALL, db.thing.ALL,
... left=db.thing.on(db.person.id == db.thing.owner_id))
>>> for row in rows:
... print row.person.name, 'has', row.thing.name
... 
Alex has Boat
Alex has Chair
Bob has Shoes
Carl has None
``:python


where:
``
left = db.thing.on(...)
``:python


does the left join query. Here the argument of ``db.thing.on`` is the condition required for the join (the same used above for the inner join). In the case of a left join, it is necessary to be explicit about which fields to select.


Multiple left joins can be combined by passing a list or tuple of ``db.mytable.on(...)`` to the ``left`` parameter.


#### Grouping and counting


When doing joins, sometimes you want to group rows according to certain criteria and count them. For example, count the number of things owned by every person. py4web allows this as well. First, you need a count operator. Second, you want to join the person table with the thing table by owner. Third, you want to select all rows (person + thing), group them by person, and count them while grouping:


``grouping``:inxx
``
>>> count = db.person.id.count()
>>> for row in db(db.person.id == db.thing.owner_id
... ).select(db.person.name, count, groupby=db.person.name):
... print row.person.name, row[count]
... 
Alex 2
Bob 1
``:python


Notice the ``count`` operator (which is built-in) is used as a field. The only issue here is in how to retrieve the information. Each row clearly contains a person and the count, but the count is not a field of a person nor is it a table. So where does it go? It goes into the storage object representing the record with a key equal to the query expression itself.


The ``count`` method of the Field object has an optional ``distinct`` argument. When set to ``True`` it specifies that only distinct values of the field in question are to be counted.


### Many to many
``many-to-many``:inxx
In the previous examples, we allowed a thing to have one owner but one person could have many things. What if Boat was owned by Alex and Curt? This requires a many-to-many relation, and it is realized via an intermediate table that links a person to a thing via an ownership relation.


Here is how to do it:
``
>>> db.define_table('person',
... Field('name'))
<Table person (id, name)>
>>> db.person.bulk_insert([dict(name='Alex'), dict(name='Bob'), dict(name='Carl')])
[1, 2, 3]
>>> db.define_table('thing',
... Field('name'))
<Table thing (id, name)>
>>> db.thing.bulk_insert([dict(name='Boat'), dict(name='Chair'), dict(name='Shoes')])
[1, 2, 3]
>>> db.define_table('ownership',
... Field('person', 'reference person'),
... Field('thing', 'reference thing'))
<Table ownership (id, person, thing)>
``:python


the existing ownership relationship can now be rewritten as:
``
>>> db.ownership.insert(person=1, thing=1) # Alex owns Boat
1
>>> db.ownership.insert(person=1, thing=2) # Alex owns Chair
2
>>> db.ownership.insert(person=2, thing=3) # Bob owns Shoes
3
``:python


Now you can add the new relation that Curt co-owns Boat:
``
>>> db.ownership.insert(person=3, thing=1) # Curt owns Boat too
4
``:python


Because you now have a three-way relation between tables, it may be convenient to define a new set on which to perform operations:
``
>>> persons_and_things = db((db.person.id == db.ownership.person) &
... (db.thing.id == db.ownership.thing))
``:python


Now it is easy to select all persons and their things from the new Set:
``
>>> for row in persons_and_things.select():
... print row.person.name, 'has', row.thing.name
... 
Alex has Boat
Alex has Chair
Bob has Shoes
Curt has Boat
``:python


Similarly, you can search for all things owned by Alex:
``
>>> for row in persons_and_things(db.person.name == 'Alex').select():
... print row.thing.name
... 
Boat
Chair
``:python


and all owners of Boat:
``
>>> for row in persons_and_things(db.thing.name == 'Boat').select():
... print row.person.name
... 
Alex
Curt
``:python


A lighter alternative to many-to-many relations is tagging, you can found an example of this in the next section. Tagging is also discussed in the context of the [[IS_IN_DB ../07#IS_IN_DB-and-Tagging]] and [[IS_IN_SET ../07#IS_IN_SET-and-Tagging]] validators on chapter 7. Tagging works even on database backends that do not support JOINs like the Google App Engine NoSQL.


[[list_types]]
### ``list:<type>`` and ``contains``
``list:string``:inxx ``list:integer``:inxx ``list:reference``:inxx
``contains``:inxx ``multiple``:inxx ``tags``:inxx


py4web provides the following special field types:


``
list:string
list:integer
list:reference <table>
``:python


They can contain lists of strings, of integers and of references respectively.


On Google App Engine NoSQL ``list:string`` is mapped into ``StringListProperty``, the other two are mapped into ``ListProperty(int)``. On relational databases they are mapped into text fields which contain the list of items separated by ``|``. For example ``[1, 2, 3]`` is mapped into ``|1|2|3|``.


For lists of string the items are escaped so that any ``|`` in the item is replaced by a ``||``. Anyway this is an internal representation and it is transparent to the user.


You can use ``list:string``, for example, in the following way:


``
>>> db.define_table('product',
... Field('name'),
... Field('colors', 'list:string'))
<Table product (id, name, colors)>
>>> db.product.colors.requires = IS_IN_SET(('red', 'blue', 'green'))
>>> db.product.insert(name='Toy Car', colors=['red', 'green'])
1
>>> products = db(db.product.colors.contains('red')).select()
>>> for item in products:
... print item.name, item.colors
... 
Toy Car ['red', 'green']
``:python


``list:integer`` works in the same way but the items must be integers.


As usual the requirements are enforced at the level of forms, not at the level of ``insert``.


------
For ``list:<type>`` fields the ``contains(value)`` operator maps into a non trivial query that checks for lists containing the ``value``. The ``contains`` operator also works for regular ``string`` and ``text`` fields and it maps into a ``LIKE '%value%'``.
------


The ``list:reference`` and the ``contains(value)`` operator are particularly useful to de-normalize many-to-many relations. Here is an example:


``
>>> db.define_table('tag',
... Field('name'),
... format='%(name)s')
<Table tag (id, name)>
>>> db.define_table('product',
... Field('name'),
... Field('tags', 'list:reference tag'))
<Table product (id, name, tags)>
>>> a = db.tag.insert(name='red')
>>> b = db.tag.insert(name='green')
>>> c = db.tag.insert(name='blue')
>>> db.product.insert(name='Toy Car', tags=[a, b, c])
1
>>> products = db(db.product.tags.contains(b)).select()
>>> for item in products:
... print item.name, item.tags
... 
Toy Car [1, 2, 3]
>>> for item in products:
... print item.name, db.product.tags.represent(item.tags)
... 
Toy Car red, green, blue
``:python


Notice that a ``list:reference tag`` field get a default constraint


``
requires = IS_IN_DB(db, db.tag._id, db.tag._format, multiple=True)
``:python


that produces a ``SELECT/OPTION`` multiple drop-box in forms.


Also notice that this field gets a default ``represent`` attribute which represents the list of references as a comma-separated list of formatted references. This is used in read forms and ``SQLTABLE``s.


-----
While ``list:reference`` has a default validator and a default representation, ``list:integer`` and ``list:string`` do not. So these two need an ``IS_IN_SET`` or an ``IS_IN_DB`` validator if you want to use them in forms.
-----


### Other operators


py4web has other operators that provide an API to access equivalent SQL operators.
Let's define another table "log" to store security events, their event_time and severity, where the severity is an integer number.


``date``:inxx ``datetime``:inxx ``time``:inxx
``
>>> db.define_table('log', Field('event'),
... Field('event_time', 'datetime'),
... Field('severity', 'integer'))
<Table log (id, event, event_time, severity)>
``:python


As before, insert a few events, a "port scan", an "xss injection" and an "unauthorized login".
For the sake of the example, you can log events with the same event_time but with different severities (1, 2, and 3 respectively).
``
>>> import datetime
>>> now = datetime.datetime.now()
>>> db.log.insert(event='port scan', event_time=now, severity=1)
1
>>> db.log.insert(event='xss injection', event_time=now, severity=2)
2
>>> db.log.insert(event='unauthorized login', event_time=now, severity=3)
3
``:python


#### ``like``, ``ilike``, ``regexp``, ``startswith``, ``endswith``, ``contains``, ``upper``, ``lower``
``like``:inxx ``ilike``:inxx ``startswith``:inxx ``endswith``:inxx ``regexp``:inxx
``contains``:inxx ``upper``:inxx ``lower``:inxx


Fields have a ``like`` operator that you can use to match strings:


``
>>> for row in db(db.log.event.like('port%')).select():
... print row.event
... 
port scan
``:python


Here "port%" indicates a string starting with "port". The percent sign character, "%", is a wild-card character that means "any sequence of characters".


The ``like`` operator maps to the LIKE word in ANSI-SQL. LIKE is case-sensitive in most databases, and depends on the collation of the database itself. The ``like`` method is hence case-sensitive but it can be made case-insensitive with


``
db.mytable.myfield.like('value', case_sensitive=False)
``:python


which is the same as using ``ilike``


``
db.mytable.myfield.ilike('value')
``:python


py4web also provides some shortcuts:


``
db.mytable.myfield.startswith('value')
db.mytable.myfield.endswith('value')
db.mytable.myfield.contains('value')
``:python


which are roughly equivalent respectively to


``
db.mytable.myfield.like('value%')
db.mytable.myfield.like('%value')
db.mytable.myfield.like('%value%')
``:python


Remember that ``contains`` has a special meaning for ``list:<type>`` fields, as discussed in previous [[list:<type> and contains #list-type-and-contains]] section.


The ``contains`` method can also be passed a list of values and an optional boolean argument ``all`` to search for records that contain all values:


``
db.mytable.myfield.contains(['value1', 'value2'], all=True)
``:python


or any value from the list
``
db.mytable.myfield.contains(['value1', 'value2'], all=False)
``:python


There is a also a ``regexp`` method that works like the ``like`` method but allows regular expression syntax for the look-up expression. It is only supported by MySQL, Oracle, PostgreSQL, SQLite, and MongoDB (with different degree of support).


The ``upper`` and ``lower`` methods allow you to convert the value of the field to upper or lower case, and you can also combine them with the like operator:


``
>>> for row in db(db.log.event.upper().like('PORT%')).select():
... print row.event
... 
port scan
``:python


#### ``year``, ``month``, ``day``, ``hour``, ``minutes``, ``seconds``
``hour``:inxx ``minutes``:inxx ``seconds``:inxx ``day``:inxx ``month``:inxx ``year``:inxx


The date and datetime fields have ``day``, ``month`` and ``year`` methods. The datetime and time fields have ``hour``, ``minutes`` and ``seconds`` methods. Here is an example:


``
>>> for row in db(db.log.event_time.year() > 2018).select():
... print row.event
... 
port scan
xss injection
unauthorized login
``:python


#### ``belongs``
``belongs``:inxx


The SQL IN operator is realized via the ``belongs`` method which returns true when the field value belongs to the specified set (list or tuples):


``
>>> for row in db(db.log.severity.belongs((1, 2))).select():
... print row.event
... 
port scan
xss injection
``:python


``nested select``:inxx
The DAL also allows a nested select as the argument of the belongs operator. The only caveat is that the nested select has to be a ``_select``, not a ``select``, and only one field has to be selected explicitly, the one that defines the set.


``
>>> bad_days = db(db.log.severity == 3)._select(db.log.event_time)
>>> for row in db(db.log.event_time.belongs(bad_days)).select():
... print row.severity, row.event
... 
1 port scan
2 xss injection
3 unauthorized login
``:python


In those cases where a nested select is required and the look-up field is a reference we can also use a query as argument. For example:


``
db.define_table('person', Field('name'))
db.define_table('thing',
                Field('name'),
                Field('owner_id', 'reference person'))


db(db.thing.owner_id.belongs(db.person.name == 'Jonathan')).select()
``:python


In this case it is obvious that the nested select only needs the field referenced by the ``db.thing.owner_id`` field so we do not need the more verbose ``_select`` notation.


``nested_select``:inxx
A nested select can also be used as insert/update value but in this case the syntax is different:


``
lazy = db(db.person.name == 'Jonathan').nested_select(db.person.id)


db(db.thing.id == 1).update(owner_id = lazy)
``:python


In this case ``lazy`` is a nested expression that computes the ``id`` of person "Jonathan". The two lines result in one single SQL query.


#### ``sum``, ``avg``, ``min``, ``max`` and ``len``
``sum``:inxx ``avg``:inxx ``min``:inxx ``max``:inxx


Previously, you have used the ``count`` operator to count records. Similarly, you can use the ``sum`` operator to add (sum) the values of a specific field from a group of records. As in the case of count, the result of a sum is retrieved via the storage object:


``
>>> sum = db.log.severity.sum()
>>> print db().select(sum).first()[sum]
6
``:python


You can also use ``avg``, ``min``, and ``max`` to the average, minimum, and maximum value respectively for the selected records. For example:


``
>>> max = db.log.severity.max()
>>> print db().select(max).first()[max]
3
``:python


``len`` computes the length of field's value. It is generally used on string or text fields but depending on the back-end it may still work for other types too (boolean, integer, etc).


``
>>> for row in db(db.log.event.len() > 13).select():
... print row.event
... 
unauthorized login
``:python


Expressions can be combined to form more complex expressions. For example here we are computing the sum of the length of the event strings in the logs plus one:


``
>>> exp = (db.log.event.len() + 1).sum()
>>> db().select(exp).first()[exp]
43
``:python


#### Substrings


One can build an expression to refer to a substring. For example, we can group things whose name starts with the same three characters and select only one from each group:


``
db(db.thing).select(distinct = db.thing.name[:3])
``:python




#### Default values with ``coalesce`` and ``coalesce_zero``


There are times when you need to pull a value from database but also need a default values if the value for a record is set to NULL. In SQL there is a function, ``COALESCE``, for this. py4web has an equivalent ``coalesce`` method:


``
>>> db.define_table('sysuser', Field('username'), Field('fullname'))
<Table sysuser (id, username, fullname)>
>>> db.sysuser.insert(username='max', fullname='Max Power')
1
>>> db.sysuser.insert(username='tim', fullname=None)
2
>>> coa = db.sysuser.fullname.coalesce(db.sysuser.username)
>>> for row in db().select(coa):
... print row[coa]
... 
Max Power
tim
``:python


Other times you need to compute a mathematical expression but some fields have a value set to None while it should be zero.
``coalesce_zero`` comes to the rescue by defaulting None to zero in the query:


``
>>> db.define_table('sysuser', Field('username'), Field('points'))
<Table sysuser (id, username, points)>
>>> db.sysuser.insert(username='max', points=10)
1
>>> db.sysuser.insert(username='tim', points=None)
2
>>> exp = db.sysuser.points.coalesce_zero().sum()
>>> db().select(exp).first()[exp]
10
>>> type(exp)
<class 'pydal.objects.Expression'>
>>> print exp
SUM(COALESCE("sysuser"."points",'0'))
``:python


### Generating raw sql
``raw SQL``:inxx


Sometimes you need to generate the SQL but not execute it. This is easy to do with py4web since every command that performs database IO has an equivalent command that does not, and simply returns the SQL that would have been executed. These commands have the same names and syntax as the functional ones, but they start with an underscore:


``_insert``:inxx
Here is ``_insert``
``
>>> print db.person._insert(name='Alex')
INSERT INTO "person"("name") VALUES ('Alex');
``:python


``_count``:inxx
Here is ``_count``
``
>>> print db(db.person.name == 'Alex')._count()
SELECT COUNT(*) FROM "person" WHERE ("person"."name" = 'Alex');
``:python


``_select``:inxx
Here is ``_select``
``
>>> print db(db.person.name == 'Alex')._select()
SELECT "person"."id", "person"."name" FROM "person" WHERE ("person"."name" = 'Alex');
``:python


``_delete``:inxx
Here is ``_delete``
``
>>> print db(db.person.name == 'Alex')._delete()
DELETE FROM "person" WHERE ("person"."name" = 'Alex');
``:python


``_update``:inxx
And finally, here is ``_update``
``
>>> print db(db.person.name == 'Alex')._update(name='Susan')
UPDATE "person" SET "name"='Susan' WHERE ("person"."name" = 'Alex');
``:python


-----
Moreover you can always use ``db._lastsql`` to return the most recent
SQL code, whether it was executed manually using executesql or was SQL
generated by the DAL.
-----


### Exporting and importing data
``export``:inxx ``import``:inxx


#### CSV (one Table at a time)
``csv``:inxx


When a Rows object is converted to a string it is automatically
serialized in CSV:


``
>>> rows = db(db.person.id == db.thing.owner_id).select()
>>> print rows
person.id,person.name,thing.id,thing.name,thing.owner_id
1,Alex,1,Boat,1
1,Alex,2,Chair,1
2,Bob,3,Shoes,2


``:python


You can serialize a single table in CSV and store it in a file "test.csv":
``
with open('test.csv', 'wb') as dumpfile:
    dumpfile.write(str(db(db.person).select()))
``:python


-------
Notice that converting a ``Rows`` object into a string using Python 2 produces an utf8 encoded binary string. To obtain a different encoding you have to ask for it explicitly, for example with:
``unicode(str(db(db.person).select()), 'utf8').encode(...)``:python
-------


Or in Python 3:
``
with open('test.csv', 'w', encoding='utf-8', newline='') as dumpfile:
    dumpfile.write(str(db(db.person).select()))
``:python


This is equivalent to


``
rows = db(db.person).select()
with open('test.csv', 'wb') as dumpfile:
    rows.export_to_csv_file(dumpfile)
``:python


You can read the CSV file back with:
``
with open('test.csv', 'rb') as dumpfile:
    db.person.import_from_csv_file(dumpfile)
``:python


Again, when using Python 3, you can be explict about the encoding for the exporting file:
``
rows = db(db.person).select()
with open('test.csv', 'w', encoding='utf-8', newline='') as dumpfile:
    rows.export_to_csv_file(dumpfile)
``:python


and the importing one:
``
with open('test.csv', 'r', encoding='utf-8', newline='') as dumpfile:
    db.person.import_from_csv_file(dumpfile)
``:python


When importing, py4web looks for the fiel d names in the CSV header. In this example, it finds two columns: "person.id" and "person.name". It ignores the "person." prefix, and it ignores the "id" fields. Then all records are appended and assigned new ids. Both of these operations can be performed via the appadmin web interface.


#### CSV (all tables at once)


In py4web, you can backup/restore an entire database with two commands:


To export:
``
with open('somefile.csv', 'wb') as dumpfile:
    db.export_to_csv_file(dumpfile)
``:python


To import:
``
with open('somefile.csv', 'rb') as dumpfile:
    db.import_from_csv_file(dumpfile)
``:python


Or in Python 3:


To export:
``
with open('somefile.csv', 'w', encoding='utf-8', newline='') as dumpfile:
    db.export_to_csv_file(dumpfile)
``:python


To import:
``
with open('somefile.csv', 'r', encoding='utf-8', newline='') as dumpfile:
    db.import_from_csv_file(dumpfile)
``:python


This mechanism can be used even if the importing database is of a different type than the exporting database.


The data is stored in "somefile.csv" as a CSV file where each table starts with one line that indicates the tablename, and another line with the fieldnames:
``
TABLE tablename
field1,field2,field3,...
``:python[lexer=None]


Two tables are separated by ``\r\n\r\n`` (that is two empty lines). The file ends with the line
``
END
``:python[lexer=None]


The file does not include uploaded files if these are not stored in the database. The upload files stored on filesystem must be dumped separately, a zip of the "uploads" folder may suffice in most cases.


When importing, the new records will be appended to the database if it is not empty. In general the new imported records will not have the same record id as the original (saved) records but py4web will restore references so they are not broken, even if the id values may change.


If a table contains a field called ``uuid``, this field will be used to identify duplicates. Also, if an imported record has the same ``uuid`` as an existing record, the previous record will be updated.


#### CSV and remote database synchronization


Consider once again the following model:
``
db.define_table('person',
                Field('name'))


db.define_table('thing',
                Field('name'),
                Field('owner_id', 'reference person'))


# usage example
if db(db.person).isempty():
    nid = db.person.insert(name='Massimo')
    db.thing.insert(name='Chair', owner_id=nid)
``:python


Each record is identified by an identifier and referenced by that id. If you have two copies of the database used by distinct py4web installations, the id is unique only within each database and not across the databases. This is a problem when merging records from different databases.


In order to make records uniquely identifiable across databases, they must:
- have a unique id (UUID),
- have a last modification time to track the most recent among multiple copies,
- reference the UUID instead of the id.


This can be achieved changing the above model into:


``
import uuid


db.define_table('person',
                Field('uuid', length=64),
                Field('modified_on', 'datetime', default=request.now, update=request.now),
                Field('name'))


db.define_table('thing',
                Field('uuid', length=64),
                Field('modified_on', 'datetime', default=request.now, update=request.now),
                Field('name'),
                Field('owner_id', length=64))


db.person.uuid.default = db.thing.uuid.default = lambda:str(uuid.uuid4())


db.thing.owner_id.requires = IS_IN_DB(db, 'person.uuid', '%(name)s')


# usage example
if db(db.person).isempty():
    nid = str(uuid.uuid4())
    db.person.insert(uuid=nid, name='Massimo')
    db.thing.insert(name='Chair', owner_id=nid)
``:python


-------
Notice that in the above table definitions, the default value for the two ``uuid`` fields is set to a lambda function, which returns a UUID (converted to a string). The lambda function is called once for each record inserted, ensuring that each record gets a unique UUID, even if multiple records are inserted in a single transaction.
-------


Create a controller action to export the database:


``
def export():
    s = StringIO.StringIO()
    db.export_to_csv_file(s)
    response.headers['Content-Type'] = 'text/csv'
    return s.getvalue()
``:python


Create a controller action to import a saved copy of the other database and sync records:


``
def import_and_sync():
    form = FORM(INPUT(_type='file', _name='data'), INPUT(_type='submit'))
    if form.process().accepted:
        db.import_from_csv_file(form.vars.data.file, unique=False)
        # for every table
        for tablename in db.tables:
            table = db[tablename]
            # for every uuid, delete all but the latest
            items = db(table).select(table.id, table.uuid,
                                     orderby=~table.modified_on,
                                     groupby=table.uuid)
            for item in items:
                db((table.uuid == item.uuid) & (table.id != item.id)).delete()
    return dict(form=form)
``:python


Optionally you should create an index manually to make the search by uuid faster.




``XML-RPC``:inxx
Alternatively, you can use XML-RPC to export/import the file.


If the records reference uploaded files, you also need to export/import the content of the uploads folder. Notice that files therein are already labeled by UUIDs so you do not need to worry about naming conflicts and references.


#### HTML and XML (one Table at a time)
``Rows objects``:inxx


``HTML``:inxx
Rows objects also have an ``xml`` method (like helpers) that serializes it to XML/HTML:


``
>>> rows = db(db.person.id == db.thing.owner_id).select()
>>> print rows.xml()
``:python
``
<table>
<thead>
<tr><th>person.id</th><th>person.name</th><th>thing.id</th><th>thing.name</th><th>thing.owner_id</th></tr>
</thead>
<tbody>
<tr class="w2p_odd odd"><td>1</td><td>Alex</td><td>1</td><td>Boat</td><td>1</td></tr>
<tr class="w2p_even even"><td>1</td><td>Alex</td><td>2</td><td>Chair</td><td>1</td></tr>
<tr class="w2p_odd odd"><td>2</td><td>Bob</td><td>3</td><td>Shoes</td><td>2</td></tr>
</tbody>
</table>
``:python[lexer='html']


``XML``:inxx ``Rows custom tags``:inxx
If you need to serialize the Rows in any other XML format with custom tags, you can easily do that using the universal ``TAG`` helper (described in [[Chapter 5 ../05#TAG]]) and the Python syntax ``*<iterable>`` allowed in function calls:


``
>>> rows = db(db.p erson).select()
>>> print TAG.result(*[TAG.row(*[TAG.field(r[f], _name=f) for f in db.person.fields]) for r in rows])
``:python
``
<result>
<row><field name="id">1</field><field name="name">Alex</field></row>
<row><field name="id">2</field><field name="name">Bob</field></row>
<row><field name="id">3</field><field name="name">Carl</field></row>
</result>
``:python[lexer='xml']


#### Data representation


``export_to_csv_file``:inxx
The ``Rows.export_to_csv_file`` method accepts a keyword argument named ``represent``. When ``True`` it will use the columns ``represent`` function while exporting the data instead of the raw data.


``colnames``:inxx
The function also accepts a keyword argument named ``colnames`` that should contain a list of column names one wish to export. It defaults to all columns.


Both ``export_to_csv_file`` and ``import_from_csv_file`` accept keyword arguments that tell the csv parser the format to save/load the files:
- ``delimiter``: delimiter to separate values (default ',')
- ``quotechar``: character to use to quote string values (default to double quotes)
- ``quoting``: quote system (default ``csv.QUOTE_MINIMAL``)


Here is some example usage:
``
import csv
rows = db(query).select()
with open('/tmp/test.txt', 'wb') as oufile:
    rows.export_to_csv_file(oufile,
                            delimiter='|',
                            quotechar='"',
                            quoting=csv.QUOTE_NONNUMERIC)
``:python


Which would render something similar to
``
"hello"|35|"this is the text description"|"2013-03-03"
``:python[lexer=None]


For more information consult the official Python documentation ``quoteall``:cite


### Caching selects


The select method also takes a ``cache`` argument, which defaults to None. For caching purposes, it should be set to a tuple where the first element is the cache model (``cache.ram``, ``cache.disk``, etc.), and the seco nd element is the expiration time in seconds.


``cache select``:inxx
In the following example, you see a controller that caches a select on the previously defined db.log table. The actual select fetches data from the back-end database no more frequently than once every 60 seconds and stores the result in memory. If the next call to this controller occurs in less than 60 seconds since the last database IO, it simply fetches the previous data from memory.


``
def cache_db_select():
    logs = db().select(db.log.ALL, cache=(cache.ram, 60))
    return dict(logs=logs)
``:python


``cacheable``:inxx
The ``select`` method has an optional ``cacheable`` argument, normally set to False. When ``cacheable=True`` the resulting ``Rows`` is serializable but The ``Row``s lack ``update_record`` and ``delete_record`` methods.


If you do not need these methods you can speed up selects a lot by setting the ``cacheable`` attribute:


``
rows = db(query).select(cacheable=True)
``:python


When the ``cache`` argument is set but ``cacheable=False`` (default) only the database results are cached, not the actual Rows object. When the ``cache`` argument is used in conjunction with ``cacheable=True`` the entire Rows object is cached and this results in much faster caching:


``
rows = db(query).select(cache=(cache.ram, 3600), cacheable=True)
``:python


### Self-Reference and aliases


``self reference``:inxx ``alias``:inxx
It is possible to define tables with fields that refer to themselves, here is an example:


``reference table``:inxx
``
db.define_table('person',
                Field('name'),
                Field('father_id', 'reference person'),
                Field('mother_id', 'reference person'))
``:python


Notice that the alternative notation of using a table object as field type will fail in this case, because it uses a table before it is defined:
``
db.define_table('person',
                Field('name'),
                Field('father_id', db.person), # wrong!
                Field('mother_id', db['person'])) # wrong!
``:python


In general ``db.tablename`` and ``'reference tablename'`` are equivalent field types, but the latter is the only one allowed for self-references.


``with_alias``:inxx
When a table has a self-reference and you have to do join, for example to select a person and its father, you need an alias for the table.
In SQL an alias is a temporary alternate name you can use to reference a table/column into a query (or other SQL statement).


With py4web you can make an alias for a table using the ``with_alias`` method. This works also for expressions, which means also for fields since ``Field`` is derived from ``Expression``.


Here is an example:
``
>>> fid, mid = db.person.bulk_insert([dict(name='Massimo'), dict(name='Claudia')])
>>> db.person.insert(name='Marco', father_id=fid, mother_id=mid)
3
>>> Father = db.person.with_alias('father')
>>> Mother = db.person.with_alias('mother')
>>> type(Father)
<class 'pydal.objects.Table'>
>>> str(Father)
'person AS father'
>>> rows = db().select(db.person.name, Father.name, Mother.name,
... left=(Father.on(Father.id == db.person.father_id),
... Mother.on(Mother.id == db.person.mother_id)))
>>> for row in rows:
... print row.person.name, row.father.name, row.mother.name
... 
Massimo None None
Claudia None None
Marco Massimo Claudia
``:python


Notice that we have chosen to make a distinction between:
- "father_id": the field name used in the table "person";
- "father": the alias we want to use for the table referenced by the above field; this is communicated to the database;
- "Father": the variable used by py4web to refer to that alias.


The difference is subtle, and there is nothing wrong in using the same name for the three of them:
``
>>> db.define_table('person',
... Field('name'),
... Field('father', 'reference person'),
... Field('mother', 'reference person'))
<Table person (id, name, father, mother)>
>>> fid, mid = db.person.bulk_insert([dict(name='Massimo'), dict(name='Claudia')])
>>> db.person.insert(name='Marco', father=fid, mother=mid)
3
>>> father = db.person.with_alias('father')
>>> mother = db.person.with_alias('mother')
>>> rows = db().select(db.person.name, father.name, mother.name,
... left=(father.on(father.id==db.person.father),
... mother.on(mother.id==db.person.mother)))
>>> for row in rows:
... print row.person.name, row.father.name, row.mother.name
... 
Massimo None None
Claudia None None
Marco Massimo Claudia
``:python


But it is important to have the distinction clear in order to build correct queries.


### Advanced features


#### Table inheritance
``inheritance``:inxx


It is possible to create a table that contains all the fields from another table. It is sufficient to pass the other table in place of a field to ``define_table``. For example
``
>>> db.define_table('person', Field('name'), Field('gender'))
<Table person (id, name, gender)>
>>> db.define_table('doctor', db.person, Field('specialization'))
<Table doctor (id, name, gender, specialization)>
``:python


``dummy table``:inxx
It is also possible to define a dummy table that is not stored in a database in order to reuse it in multiple other places. For example:


``
signature = db.Table(db, 'signature',
                     Field('is_active', 'boolean', default=True),
                     Field('created_on', 'datetime', default=request.now),
                     Field('created_by', db.auth_user, default=auth.user_id),
                     Field('modified_on', 'datetime', update=request.now),
                     Field('modified_by', db.auth_user, update=auth.user_id))


db.define_table('payment', Field('amount', 'double'), signature)
``:python


This example assumes that standard py4web authentication is enabled.


Notice that if you use ``Auth`` py4web already creates one such table for you:


``
auth = Auth(db)
db.define_table('payment', Field('amount', 'double'), auth.signature)
``:python


When using table inheritance, if you want the inheriting table to inherit validators, be sure to define the validators of the parent table before defining the inheriting table.


#### ``filter_in`` and ``filter_out``
``filter_in``:inxx ``filter_out``:inxx


It is possible to define a filter for each field to be called before a value is inserted into the database for that field and after a value is retrieved from the database.


Imagine for example that you want to store a serializable Python data structure in a field in the json format. Here is how it could be accomplished:


``
>>> import json
>>> db.define_table('anyobj',
... Field('name'),
... Field('data', 'text'))
<Table anyobj (id, name, data)>
>>> db.anyobj.data.filter_in = lambda obj: json.dumps(obj)
>>> db.anyobj.data.filter_out = lambda txt: json.loads(txt)
>>> myobj = ['hello', 'world', 1, {2: 3}]
>>> aid = db.anyobj.insert(name='myobjname', data=myobj)
>>> row = db.anyobj[aid]
>>> row.data
['hello', 'world', 1, {'2': 3}]
``:python


Another way to accomplish the same is by using a Field of type ``SQLCustomType``, as discussed in next [[Custom ``Field`` types #Custom-Field-types]] section.


#### callbacks on record insert, delete and update


``_before_insert``:inxx ``_after_insert``:inxx
``_before_update``:inxx ``_after_update``:inxx
``_before_delete``:inxx ``_after_delete``:inxx


PY4WEB provides a mechanism to register callbacks to be called before and/or after insert, update and delete of records.


Each table stores six lists of callbacks:


``
db.mytable._before_insert
db.mytable._after_insert
db.mytable._before_update
db.mytable._after_update
db.mytable._before_delete
db.mytable._after_delete
``:python[lexer=None]


You can register a callback function by appending it to the corresponding list. The caveat is that depending on the functionality, the callback has different signature.


This is best explained via some examples.


``
>>> db.define_table('person', Field('name'))
<Table person (id, name)>
>>> def pprint(callback, *args):
... print "%s%s" % (callback, args)
... 
>>> db.person._before_insert.append(lambda f: pprint('before_insert', f))
>>> db.person._after_insert.append(lambda f, i: pprint('after_insert', f, i))
>>> db.person.insert(name='John')
before_insert(<OpRow {'name': 'John'}>,)
after_insert(<OpRow {'name': 'John'}>, 1L)
1L
>>> db.person._before_update.append(lambda s, f: pprint('before_update', s, f))
>>> db.person._after_update.append(lambda s, f: pprint('after_update', s, f))
>>> db(db.person.id == 1).update(name='Tim')
before_update(<Set ("person"."id" = 1)>, <OpRow {'name': 'Tim'}>)
after_update(<Set ("person"."id" = 1)>, <OpRow {'name': 'Tim'}>)
1
>>> db.person._before_delete.append(lambda s: pprint('before_delete', s))
>>> db.person._after_delete.append(lambda s: pprint('after_delete', s))
>>> db(db.person.id == 1).delete()
before_delete(<Set ("person"."id" = 1)>,)
after_delete(<Set ("p erson"."id" = 1)>,)
1
``:python


As you can see:
- ``f`` gets passed the ``OpRow`` object with data for insert or update.
- ``i`` gets passed the id of the newly inserted record.
- ``s`` gets passed the ``Set`` object used for update or delete.
``OpRow`` is an helper object specialized in storing (field, value) pairs, you can think of it as a normal dictionary that you can use even with the syntax of attribute notation (that is ``f.name`` and ``f['name']`` are equivalent).


The return values of these callback should be ``None`` or ``False``. If any of the ``_before_*`` callback returns a ``True`` value it will abort the actual insert/update/delete operation.


``update_naive``:inxx


Some times a callback may need to perform an update in the same or a different table and one wants to avoid firing other callbacks, which could cause an infinite loop.


For this purpose there the ``Set`` objects have an ``update_naive`` method that works like ``update`` but ignores before and after callbacks.


##### Database cascades
Database schema can define relationships which trigger deletions of related records, known as cascading. The DAL is not informed when a record is deleted due to a cascade. So no *_delete callaback will ever be called as conseguence of a cascade-deletion.


[[versioning]]
#### Record versioning
``_enable_record_versioning``:inxx


It is possible to ask py4web to save every copy of a record when the record is individually modified. There are different ways to do it and it can be done for all tables at once using the syntax:


``
auth.enable_record_versioning(db)
``:python


this requires ``Auth`` and it is discussed in [[Chapter 9 ../09#Record-versioning]].
It can also be done for each individual table as discussed below.


Consider the following table:


``
db.define_table('stored_item',
                Field('name'),
                Field('quantity', 'integer'),
                Field('is_active', 'boolean',
                      writable=False, readable=False, default=True))
``:python


Notice the hidden boolean field called ``is_active`` and defaulting to True.


We can tell py4web to create a new table (in the same or a different database) and store all previous versions of each record in the table, when modified.


This is done in the following way:
``
db.stored_item._enable_record_versioning()
``:python


or in a more verbose syntax:


``
db.stored_item._enable_record_versioning(archive_db=db,
                                         archive_name='stored_item_archive',
                                         current_record='current_record',
                                         is_active='is_active')
``:python


The ``archive_db=db`` tells py4web to store the archive table in the same database as the ``stored_item`` table. The ``archive_name`` sets the name for the archive table. The archive table has the same fields as the original table ``stored_item`` except that unique fields are no longer unique (because it needs to store multiple versions) and has an extra field which name is specified by ``current_record`` and which is a reference to the current record in the ``stored_item`` table.


When records are deleted, they are not really deleted. A deleted record is copied in the ``stored_item_archive`` table (like when it is modified) and the ``is_active`` field is set to False. By enabling record versioning py4web sets a ``common_filter`` on this table that hides all records in table ``stored_item`` where the ``is_active`` field is set to False. The ``is_active`` parameter in the ``_enable_record_versioning`` method allows to specify the name of the field used by the ``common_filter`` to determine if the field was deleted or not.


``common_filter``s will be discussed in next [[Common filters #Common-filters]] section..


#### Common fields and multi-tenancy
``common fields``:inxx ``multi tenancy``:inxx


``db._common_fields`` is a list of fields that should belong to all the tables. This list can also contain tables and it is understood as all fields from the table.


For example occasionally you find yourself in need to add a signature to all your tables but the ``Auth`` tables. In this case, after you ``auth.define_tables()`` but before defining any other table, insert:


``
db._common_fields.append(auth.signature)
``:python


One field is special: ``request_tenant``, you can set a different name in ``db._request_tenant``.
This field does not exist but you can create it and add it to any of your tables (or all of them):


``
db._common_fields.append(Field('request_tenant',
                               default=request.env.http_host,
                               writable=False))
``:python


For every table with such a field, all records for all queries are always automatically filtered by:


``
db.table.request_tenant == db.table.request_tenant.default
``:python


and for every record inserted, this field is set to the default value.
In the example above we have chosen:
``
default = request.env.http_host
``:python
this means we have chosen to ask our app to filter all tables in all queries with:
``
db.table.request_tenant == request.env.http_host
``:python


This simple trick allow us to turn any application into a multi-tenant application.
Even though we run one instance of the application and we use one single database, when the application is accessed under two or more domains the visitors will see different data depending on the domain (in the example the domain name is retrieved from ``request.env.http_host``).


``ignore_common_filters``:inxx
You can turn off multi tenancy filters using ``ignore_common_filters=True`` at ``Set`` creation time:
``
db(query, ignore_common_filters=True)
``:python


#### Common filters


A common filter is a generalization of the above multi-tenancy idea.
It provides an easy way to prevent repeating of the same query.
Consider for example the following table:


``
db.define_table('blog_post',
                Field('subject'),
                Field('post_text', 'text'),
                Field('is_public', 'boolean'),
                common_filter = lambda query: db.blog_post.is_public == True)
``:python


Any select, delete or update in this table, will include only public blog posts. The attribute can also be modified at runtime:


``
db.blog_post._common_filter = lambda query: ...
``:python


It serves both as a way to avoid repeating the "db.blog_post.is_public==True" phrase in each blog post search, and also as a security enhancement, that prevents you from forgetting to disallow viewing of non-public posts.


In case you actually do want items left out by the common filter (for example, allowing the admin to see non-public posts), you can either remove the filter:
``
db.blog_post._common_filter = None
``:python


or ignore it:
``
db(query, ignore_common_filters=True)
``:python


-------
Note that common_filters are ignored by the appadmin interface.
-------


#### Custom ``Field`` types
``SQLCustomType``:inxx


Aside for using ``filter_in`` and ``filter_out``, it is possible to define new/custom field types.
For example, suppose that you want to define a custom type to store an IP address:


``
>>> def ip2int(sv):
... "Convert an IPV4 to an integer."
... sp = sv.split('.'); assert len(sp) == 4 # IPV4 only
... iip = 0
... for i in map(int, sp): iip = (iip<<8) + i
... return iip
... 
>>> def int2ip(iv):
... "Convert an integer to an IPV4."
... assert iv > 0
... iv = (iv,); ov = []
... for i in range(3):
... iv = divmod(iv[0], 256)
... ov.insert(0, iv[1])
... ov.insert(0, iv[0])
... return '.'.join(map(str, ov))
... 
>>> from gluon.dal import SQLCustomType
>>> ipv4 = SQLCustomType(type='string', native='integer',
... encoder=lambda x : str(ip2int(x)), decoder=int2ip)
>>> db.define_table('website',
... Field('name'),
... Field('ipaddr', type=ipv4))
<Table website (id, name, ipaddr)>
>>> db.website.insert(name='wikipedia', ipaddr='91.198.174.192')
1
>>> db.website.insert(name='google', ipaddr='172.217.11.174')
2
>>> db.website.insert(name='youtube', ipaddr='74.125.65.91')
3
>>> db.website.insert(name='github', ipaddr='207.97.227.239')
4
>>> rows = db(db.website.ipaddr > '100.0.0.0').select(orderby=~db.website.ipaddr)
>>> for row in rows:
... print row.name, row.ipaddr
... 
github 207.97.227.239
google 172.217.11.174
``:python


``SQLCustomType`` is a field type factory. Its ``type`` argument must be one of the standard py4web types. It tells py4web how to treat the field values at the py4web level. ``native`` is the type of the field as far as the database is concerned. Allowed names depend on the database engine. ``encoder`` is an optional transformation function applied when the data is stored and ``decoder`` is the optional reverse transformation function.


-------
This feature is marked as experimental. In practice it has been in py4web for a long time and it works but it can make the code not portable, for example when the native type is database specific.


It does not work on Google App Engine NoSQL.
-------


#### Using DAL without define tables


The DAL can be used from any Python program simply by doing this:


``
from gluon import DAL
db = DAL('sqlite://storage.sqlite', folder='path/to/app/databases')
``:python


ie import the DAL, connect and specify the folder which contains the .table files (the app/databases folder).


To access the data and its attributes we still have to define all the tables we are going to access with ``db.define_table``.


If we just need access to the data but not to the py4web table attributes, we get away without re-defining the tables but simply asking py4web to read the necessary info from the metadata in the .table files:


``
from gluon import DAL
db = DAL('sqlite://storage.sqlite', folder='path/to/app/databases', auto_import=True)
``:python


This allows us to access any db.table without need to re-define it.


#### PostGIS, SpatiaLite, and MS Geo (experimental)
``PostGIS``:inxx ``StatiaLite``:inxx ``Geo Extensions``:inxx
``geometry``:inxx ``geoPoint``:inxx ``geoLine``:inxx ``geoPolygon``:inxx


The DAL supports geographical APIs using PostGIS (for PostgreSQL), SpatiaLite (for SQLite), and MSSQL and Spatial Extensions. This is a feature that was sponsored by the Sahana project and implemented by Denes Lengyel.


DAL provides geometry and geography fields types and the following functions:


``st_asgeojson``:inxx ``st_astext``:inxx ``st_contains``:inxx
``st_distance``:inxx ``st_equals``:inxx ``st_intersects``:inxx ``st_overlaps``:inxx
``st_simplify``:inxx ``st_touches``:inxx ``st_within``:inxx


``
st_asgeojson (PostGIS only)
st_astext
st_contains
st_distance
st_equals
st_intersects
st_overlaps
st_simplify (PostGIS only)
st_touches
st_within
st_x
st_y
``:python[lexer=None]


Here are some examples:


``
>>> from gluon.dal import DAL, Field, geoPoint, geoLine, geoPolygon
>>> db = DAL("mssql://user:pass@host/db")
>>> sp = db.define_table('spatial', Field('loc', 'geometry()'))
``:python


Below we insert a point, a line, and a polygon:
``
>>> sp.insert(loc=geoPoint(1, 1))
1
>>> sp.insert(loc=geoLine((100, 100), (20, 180), (180, 180)))
2
>>> sp.insert(loc=geoPolygon((0, 0), (150, 0), (150, 150), (0, 150), (0, 0)))
3
``:python


Notice that
``
rows = db(sp).select()
``:python


Always returns the geometry data se rialized as text.
You can also do the same more explicitly using ``st_astext()``:


``
>>> print db(sp).select(sp.id, sp.loc.st_astext())
spatial.id,spatial.loc.STAsText()
1,"POINT (1 2)"
2,"LINESTRING (100 100, 20 180, 180 180)"
3,"POLYGON ((0 0, 150 0, 150 150, 0 150, 0 0))"
``:python


You can ask for the native representation by using ``st_asgeojson()`` (in PostGIS only):


``
>>> print db(sp).select(sp.id, sp.loc.st_asgeojson().with_alias('loc'))
spatial.id,loc
1,[1, 2]
2,[[100, 100], [20 180], [180, 180]]
3,[[[0, 0], [150, 0], [150, 150], [0, 150], [0, 0]]]
``:python


(notice an array is a point, an array of arrays is a line, and an array of array of arrays is a polygon).


Here are example of how to use geographical functions:


``
>>> query = sp.loc.st_intersects(geoLine((20, 120), (60, 160)))
>>> query = sp.loc.st_overlaps(geoPolygon((1, 1), (11, 1), (11, 11), (11, 1), (1, 1)))
>>> query = sp.loc.st_contains(geoPoint(1, 1))
>>> print db(query).select(sp.id, sp.loc)
spatial.id,spatial.loc
3,"POLYGON ((0 0, 150 0, 150 150, 0 150, 0 0))"
``:python


Computed distances can also be retrieved as floating point numbers:


``
>>> dist = sp.loc.st_distance(geoPoint(-1,2)).with_alias('dist')
>>> print db(sp).select(sp.id, dist)
spatial.id,dist
1,2.0
2,140.714249456
3,1.0
``:python


#### Copy data from one db into another


Consider the situation in which you have been using the following database:


``
db = DAL('sqlite://storage.sqlite')
``:python


and you wish to move to another database using a different connection string:


``
db = DAL('postgres://username:password@localhost/mydb')
``:python


Before you switch, you want to move the data and rebuild all the metadata for the new database. We assume the new database to exist but we also assume it is empty.


PY4WEB provides a script that does this work for you:


``
cd py4web
python scripts/cpdb.py \\
   -f applications/app/databases \\
   -y 'sqlite://storage.sqlite' \\
   -Y 'postgres://username:password@localhost/mydb' \\
   -d ../gluon
``:python[lexer='sh']


After running the script you can simply switch the connection string in the model and everything should work out of the box. The new data should be there.


This script provides various command line options that allows you to move data from one application to another, move all tables or only some tables, clear the data in the tables. For more info try:


``
python scripts/cpdb.py -h
``:python[lexer='sh']


#### Note on new DAL and adapters


The source code of the Database Abstraction Layer was completely rewritten in 2010. While it stays backward compatible, the rewrite made it more modular and easier to extend. Here we explain the main logic.


The file "gluon/dal.py" defines, among other, the following classes.


``
ConnectionPool
BaseAdapter extends ConnectionPool
Row
DAL
Reference
Table
Expression
Field
Query
Set
Rows
``:python[lexer=None]


Their use has been explained in the previous sections, except for ``BaseAdapter``. When the methods of a ``Table`` or ``Set`` object need to communicate with the database they delegate to methods of the adapter the task to generate the SQL and or the function call.


For example:


``
db.mytable.insert(myfield='myvalue')
``:python


calls


``
Table.insert(myfield='myvalue')
``:python


which delegates the adapter by returning:


``
db._adapter.insert(db.mytable, db.mytable._listify(dict(myfield='myvalue')))
``:python


Here ``db.mytable._listify`` converts the dict of arguments into a list of ``(field,value)`` and calls the ``insert`` method of the ``adapter``. ``db._adapter`` does more or less the following:


``
query = db._adapter._insert(db.mytable, list_of_fields)
db._adapter.execute(query)
``:python


where the first line builds the query and the second executes it.


``BaseAdapter`` defines the interface for all adapters.


"gluon/dal.py" at the moment of writing this book, contains the following adapters:


``
SQLiteAdapter extends BaseAdapter
JDBCSQLiteAdapter extends SQLiteAdapter
MySQLAdapter extends BaseAdapter
PostgreSQLAdapter extends BaseAdapter
JDBCPostgreSQLAdapter extends PostgreSQLAdapter
OracleAdapter extends BaseAdapter
MSSQLAdapter extends BaseAdapter
MSSQL2Adapter extends MSSQLAdapter
MSSQL3Adapter extends MSSQLAdapter
MSSQL4Adapter extends MSSQLAdapter
FireBirdAdapter extends BaseAdapter
FireBirdEmbeddedAdapter extends FireBirdAdapter
InformixAdapter extends BaseAdapter
DB2Adapter extends BaseAdapter
IngresAdapter extends BaseAdapter
IngresUnicodeAdapter extends IngresAdapter
GoogleSQLAdapter extends MySQLAdapter
NoSQLAdapter extends BaseAdapter
GoogleDatastoreAdapter extends NoSQLAdapter
CubridAdapter extends MySQLAdapter (experimental)
TeradataAdapter extends DB2Adapter (experimental)
SAPDBAdapter extends BaseAdapter (experimental)
CouchDBAdapter extends NoSQLAdapter (experimental)
IMAPAd apter extends NoSQLAdapter (experimental)
MongoDBAdapter extends NoSQLAdapter (experimental)
VerticaAdapter extends MSSQLAdapter (experimental)
SybaseAdapter extends MSSQLAdapter (experimental)
``:python[lexer=None]


which override the behavior of the ``BaseAdapter``.


Each adapter has more or less this structure:


``
class MySQLAdapter(BaseAdapter):


    # specify a driver to use
    driver = globals().get('pymysql', None)


    # map py4web types into database types
    types = {
        'boolean': 'CHAR(1)',
        'string': 'VARCHAR(%(length)s)',
        'text': 'LONGTEXT',
        ...
        }


    # connect to the database using driver
    def __init__(self, db, uri, pool_size=0, folder=None, db_codec ='UTF-8',
                 credential_decoder=lambda x:x, driver_args={},
                 adapter_args={}):
        # parse uri string and store parameters in driver_args
        ...
        # define a connection function
        def connect(driver_args=driver_args):
            return self.driver.connect(**driver_args)
        # place it in the pool
        self.pool_connection(connect)
        # set optional parameters (after connection)
        self.execute('SET FOREIGN_KEY_CHECKS=1;')
        self.execute("SET sql_mode='NO_BACKSLASH_ESCAPES';")


   # override BaseAdapter methods as needed
   def lastrowid(self, table):
        self.execute('select last_insert_id();')
        return int(self.cursor.fetchone()[0])


``:python


Looking at the various a dapters as example should be easy to write new ones.


When ``db`` instance is created:


``
db = DAL('mysql://...')
``:python


the prefix in the uri string defines the adapter. The mapping is defined in the following dictionary also in "gluon/dal.py":


``
ADAPTERS = {
    'sqlite': SQLiteAdapter,
    'spatialite': SpatiaLiteAdapter,
    'sqlite:memory': SQLiteAdapter,
    'spatialite:memory': SpatiaLiteAdapter,
    'mysql': MySQLAdapter,
    'postgres': PostgreSQLAdapter,
    'postgres:psycopg2': PostgreSQLAdapter,
    'postgres2:psycopg2': NewPostgreSQLAdapter,
    'oracle': OracleAdapter,
    'mssql': MSSQLAdapter,
    'mssql2': MSSQL2Adapter,
    'mssql3': MSSQL3Adapter,
    'mssql4' : MSSQL4Adapter,
    'vertica': VerticaAdapter,
    'sybase': SybaseAdapter,
    'db2': DB2Adapter,
    'teradata': TeradataAdapter,
    'informix': InformixAdapter,
    'informix-se': InformixSEAdapter,
    'firebird': FireBirdAdapter,
    'firebird_embedded': FireBirdAdapter,
    'ingres': IngresAdapter,
    'ingresu': IngresUnicodeAdapter,
    'sapdb': SAPDBAdapter,
    'cubrid': CubridAdapter,
    'jdbc:sqlite': JDBCSQLiteAdapter,
    'jdbc:sqlite:memory': JDBCSQLiteAdapter,
    'jdbc:postgres': JDBCPostgreSQLAdapter,
    'gae': GoogleDatastoreAdapter, # discouraged, for backward compati bility
    'google:datastore': GoogleDatastoreAdapter,
    'google:datastore+ndb': GoogleDatastoreAdapter,
    'google:sql': GoogleSQLAdapter,
    'couchdb': CouchDBAdapter,
    'mongodb': MongoDBAdapter,
    'imap': IMAPAdapter
}
``:python


the uri string is then parsed in more detail by the adapter itself.


For any adapter you can replace the driver with a different one:


``
import MySQLdb as mysqldb
from gluon.dal import MySQLAdapter
MySQLAdapter.driver = mysqldb
``:python


ie ``mysqldb`` has to be ''that module'' with a .connect() method.
You can specify optional driver arguments and adapter arguments:


``
db =DAL(..., driver_args={}, adapter_args={})
``:python




### Gotchas


#### SQLite


SQLite does not support dropping and altering columns. That means that py4web migrations will work up to a point. If you delete a field from a table, the column will remain in the database but will be invisible to py4web. If you decide to reinstate the column, py4web will try re-create it and fail. In this case you must set ``fake_migrate=True`` so that metadata is rebuilt without attempting to add the column again. Also, for the same reason, **SQLite** is not aware of any change of column type. If you insert a number in a string field, it will be stored as string. If you later change the model and replace the type "string" with type "integer", SQLite will continue to keep the number as a string and this may cause problem when you try to extract the data.


SQLite doesn't have a boolean type. py4web internally maps booleans to a 1 character string, with 'T' and 'F' representing True and False. The DAL handles this completely; the abstraction of a true boolean value works well.
But if you are updating the SQLite table with SQL directly, be aware of the py4web implementation, and avoid using 0 and 1 values.


#### MySQL


MySQL does not support multiple ALTER TABLE within a single transaction. This means that any migration process is broken into multiple commits. If something happens that causes a failure it is possible to break a migration (the py4web metadata are no longer in sync with the actual table structure in the database). This is unfortunate but it can be prevented (migrate one table at the time) or it can be fixed a posteriori (revert the py4web model to what corresponds to the table structure in database, set ``fake_migrate=True`` and after the metadata has been rebuilt, set ``fake_migrate=False`` and migrate the table again).


#### Google SQL


Google SQL has the same problems as MySQL and more. In particular table metadata itself must be stored in the database in a table that is not migrated by py4web. This is because Google App Engine has a read-only file system. PY4WEB migrations in Google SQL combined with the MySQL issue described above can result in metadata corruption. Again, this can be prevented (by migrating the table at once and then setting migrate=False so that the metadata table is not accessed any more) or it can fixed a posteriori (by accessing the database using the Google dashboard and deleting any corrupted entry from the table called ``py4web_filesystem``.


#### MSSQL (Microsoft SQL Server)
``limitby``:inxx


MSSQL < 2012 does not support the SQL OFFSET keyword. Therefore the database cannot do pagination. When doing a ``limitby=(a, b)`` py4web will fetch the first ``a + b`` rows and discard the first ``a``. This may result in a considerable overhead when compared with other database engines.
If you're using MSSQL >= 2005, the recommended prefix to use is ``mssql3://`` which provides a method to avoid the issue of fetching the entire non-paginated resultset. If you're on MSSQL >= 2012, use ``mssql4://`` that uses the ``OFFSET ... ROWS ... FETCH NEXT ... ROWS ONLY`` construct to support natively pagination without performance hits like other backends.
The ``mssql://`` uri also enforces (for historical reasons) the use of ``text`` columns, that are superseeded in more recent versions (from 2005 onwards) by ``varchar(max)``. ``mssql3://`` and ``mssql4://`` should be used if you don't want to face some limitations of the - officially deprecated - ``text`` columns.


MSSQL has problems with circular references in tables that have ONDELETE CASCADE. This is an MSSQL bug and you work around it by setting the ondelete attribute for all reference fields to "NO ACTION". 
You can also do it once and for all before you define tables:


``
db = DAL('mssql://....')
for key in db._adapter.types:
    if ' ON DELETE %(on_delete_action)s' in db._adapter.types[key]:
        db._adapter.types[key] = db._adapter.types[key].replace('%(on_delete_action)s', 'NO ACTION')
``:python


MSSQL also has problems with arguments passed to the DISTINCT keyword and therefore
 while this works,


``
db(query).select(distinct=True)
``:python


this does not


``
db(query).select(distinct=db.mytable.myfield)
``:python


#### Oracle


Oracle also does not support pagination. It does not support neither the OFFSET nor the LIMIT keywords. PY4WEB achieves pagination by translating a ``db(...).select(limitby=(a, b))`` into a complex three-way nested select (as suggested by official Oracle documentation).
This works for simple select but may break for complex selects involving aliased fields and or joins.


#### Google NoSQL (Datastore)


Google NoSQL (Datastore) does not allow joins, left joins, aggregates, expression, OR involving more than one table, the 'like' operator searches in "text" fields. 


Transactions are limited and not provided automatically by py4web (you need to use the Google API ``run_in_transaction`` which you can look up in the Google App Engine documentation online). 


Google also limits the number of records you can retrieve in each one query (1000 at the time of writing). On the Google datastore record IDs are integer but they are not sequential. 
While on SQL the "list:string" type is mapped into a "text" type, on the Google Datastore it is mapped into a ``ListStringProperty``. Similarly "list:integer" and "list:reference" are mapped into ``ListProperty``. This makes searches for content inside these fields types more efficient on Google NoSQL than on SQL databases.