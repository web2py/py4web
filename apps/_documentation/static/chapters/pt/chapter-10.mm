TRABALHO EM ANDAMENTO


Apenas saiba que `` py4web.utils.form.Form`` é praticamente equivalente ao `` SQLFORM`` do web2py.


O construtor `Form` aceita os seguintes argumentos:


` `
Form (self,
     table,
     record = None,
     readonly = False,
     deletable = True,
     formstyle = FormStyleDefault,
     dbio = True,
     keep_values ​​= False,
     form_name = False,
     hidden = None,
     before_validate = None):
``: python


Onde:


- `table`: uma tabela DAL ou uma lista de campos (equivalente ao antigo SQLFORM.factory) -` record`
: um registro DAL ou ID de registro
- `readonly`: set to Fiel ao fazer um formulário readonly
- `deletable`: definida como falsa a eliminação disallow de registro
-` formstyle`: uma função que torna o formulário usando ajudantes (FormStyleDefault)
- `dbio`: definido como falso para evitar qualquer DB escreve
-` keep_values`: se configurado como true, ele lembra os valores do formulário enviado anteriormente
- `form_name`: o nome opcional deste formulário
-` hidden`: um dicionário de campos ocultos que é adicionado ao formulário
- `before_validate`: validador opcional.


## Exemplo


Aqui está um exemplo simples de um formulário personalizado que não usa acesso ao banco de dados.
Declaramos um ponto de extremidade `/ form_example`, que será usado para o GET e para o POST do formulário:


` `
@action ('form_example', method = ['GET', 'POST'])
@ action.uses ('form_example.html', sessão)
def form_example ():
    form = Form ([
        Field ('product_name'),
        Field ('product_quantity', 'integer')],
        formstyle = FormStyleBulma)
    se form.accepted:
        # Faça algo com form.vars ['product_name'] e form.vars ['product_quantity']
        redirecione (URL ('index'))
    return dict (form = form)
``: python


O formulário pode ser exibido no modelo simplesmente usando `[ [= formulário]] `.


## Validação de formulário


A validação da entrada de formulário pode ser feita de duas maneiras. Pode-se definir atributos `requer` de` Campo`, ou pode-se definir explicitamente uma função de validação. Para fazer isso, passamos para `validar 'uma função que assume o formato e retorna um dicionário, mapeando nomes de campos para erros. Se o dicionário não estiver vazio, os erros serão exibidos para o usuário e nenhuma E / S do banco de dados ocorrerá.


Aqui está um exemplo:


``
from py4web import Field
from py4web.utils.form import Form, FormStyleBulma
from pydal.validators import IS_INT_IN_RANGE


def check_nonnegative_quantity (formulário):
    se não form.errors e form.vars ['product_quantity']% 2:
        form.errors ['product_quantity'] = T ('A quantidade do produto deve ser par')


@action ('form_example', método = ['GET', 'POST'])
@ action.uses ('form_example.html', sessão)
def form_example ():
    form = Form ([
        Field ('product_name'),
        Field ('product_quantity', 'integer', requer = IS_INT_IN_RANGE (0,100))],
        validação = check_nonnegative_quantity,
        formstyle = FormStyleBulma)
    se form.accepted :
        # Faça algo com o form.vars ['product_name'] e o form.vars ['product_quantity']
        redirecionar (URL ('index'))
    return dict (form = form)
``: python