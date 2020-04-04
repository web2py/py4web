### Ajudantes do YATL
`` helpers``: inxx


Considere o seguinte código em uma exibição:
``
[[= DIV ('this', 'is', 'a', 'test', _id = '123', _class = 'myclass')]]
``: html


é renderizado como:
``
<div id = "123" class = "myclass"> thisisatest </div>
``: html
`` DIV`` é uma classe auxiliar, ou seja, algo que pode ser usado para criar HTML programaticamente. Corresponde à tag HTML `` <div> ``.


Argumentos posicionais são interpretados como objetos contidos entre as tags abrir e fechar. Os argumentos nomeados que começam com um sublinhado são interpretados como atributos da tag HTML (sem o sublinhado). Alguns auxiliares também nomearam argumentos que não começam com sublinhado; esses argumentos são específicos da marca.


Em vez de um conjunto de argumentos não nomeados, um auxiliar também pode usar uma única lista ou tupla como seu conjunto de componentes usando a notação `` * `` e pode usar um único dicionário como seu conjunto de atributos usando a `` ** ` `, por exemplo:
` `
[[
contents = ['this', 'is', 'a', 'test']
atributos = {'_id': '123', '_class': 'myclass'}
= DIV ( * conteúdos, atributos
**)]]
``: HTML
(produz a mesma saída que antes).


O seguinte conjunto de ajudantes:


`` A``, `` BEAUTIFY``, `` BODY``, `` CAT``, `` CODE``, `` DIV``, `` EM``, `` FORM``, `` H1``, `` H2``, `` H3``, `` H4``, `` H5``, `` H6``, `` HEAD``, `` HTML` `` I '', `` IMG``, `` INPUT``, `` LABEL``, `` LI``, `` LINK``, `` META``, `` METATAG``, `` OL``, `` OPTION``, `` PRE``, `` SELECT``, `` SPAN``, `` STRONG``, `` TABLE``, `` TAG``, `` TBODY``, `` TD``, `` TEXTAREA``, `` TH``, `` THAED``, `` TR``, `` UL``, `` XML``, `` higienizar` `,` `xmlescape``


pode ser usado para criar expressões complexas que podem ser serializadas para XML``xml-w``: cite` `xml-o``: cite. Por exemplo:
``
[[= DIV (B (I ("olá", "<world>")), _class = "myclass")]
`` `: o html


é renderizado:
` `
<div class =" myclass " > <b> <i> olá & lt; world & gt; </i> </b> </div>
``: html Os


auxiliares também podem ser serializados em seqüências de caracteres, de forma equivalente, com o `` __str__`` e o `` xml `` métodos:


``
>>> print str (DIV ("olá mundo"))
<div> olá mundo </div>
>>> print DIV ("olá mundo"). xml ()
<div> olá mundo < / div>
``: python


`` Document Object Model (DOM) ``: inxx
O mecanismo auxiliar no py4web é mais do que um sistema para gerar HTML sem concatenar seqüências de caracteres. Ele fornece uma representação do servidor do DOM (Document Object Model).


Os componentes dos auxiliares podem ser referenciados por meio de sua posição, e os auxiliares agem como listas em relação aos seus componentes:
``
>>> a = DIV (SPAN ('a', 'b'), 'c')
>>> imprima um
<div> <span> ab </span> c </div>
>>> del [1]
>>> a.append (B ('x'))
>>> a [0] [0] = ' y'
>>> imprimir um
<div> <span> YB </ span> <b> x </ b> </ div>
``: python


Atributos de ajudantes podem ser referenciados pelo nome, e ajudantes agir como dicionários com respeito para seus atributos:
``
>>> a = DIV (SPAN ('a', 'b'), 'c')
>>> a ['_ class'] = 's'
>>> a [0] [' _class '] =' t '
>>> imprima um
<div class = "s"> <span class = "t"> ab </span> c </div>
``: python


Nota: o conjunto completo de componentes pode seja acessado através de uma lista chamada `` a.components``, e o conjunto completo de atributos pode ser acessado através de um dicionário chamado `` a.attributes``. Portanto, `` a [i] `` é equivalente a `` a.components [i] `` quando `` i`` é um número inteiro e `` a [s] `` é equivalente a `` a.attributes [s] `` quando `` s`` é uma string.


Observe que os atributos auxiliares são passados ​​como argumentos de palavra-chave para o auxiliar. Em alguns casos, no entanto, os nomes de atributos incluem caracteres especiais que não são permitidos nos identificadores Python (por exemplo, hífens) e, portanto, não podem ser usados ​​como nomes de argumentos de palavras-chave. Por exemplo:


``
DIV ('text', _data-role = 'collapsible')
``: python


não funcionará porque "_data-role" inclui um hífen, o que produzirá um erro de sintaxe do Python.


Nesses casos, você tem algumas opções.
Você pode usar o argumento `` data`` (desta vez sem sublinhado à esquerda) para passar um dicionário de atributos relacionados sem o hífen à esquerda, e a saída terá as combinações desejadas, por exemplo,


``
>>> print DIV ('text' , data = {'role': 'collapsible'})
<div data-role = "collapsible"> texto </div>
``: python


ou você pode passar os atributos como um dicionário e usar o `` * do Python * `` notação de argumentos de função, que mapeia um dicionário de pares (chave: valor) em um conjunto de argumentos de palavras-chave:


``
>>> imprime DIV ('texto', ** {'_ data-role': 'recolhível'} )
<div data-role = "collapsible"> texto </div>
``: python


Observe que entradas mais elaboradas introduzirão entidades de caracteres HTML, mas funcionarão, por exemplo,


``
>>> print DIV ('text', data = {'options': '{"mode": "calbox", "useNewStyle": true}'})
<div data-options = "{& quot; mode & quot;: & quot; calbox & quot ;, & quot; useNewStyle & quot;: true} "> text </div>
` `: python


Você também pode criar dinamicamente TAGs especiais:


` `
>>> print TAG ['soap: Body'] ('qualquer', ** {'_ xmlns: m ':' http: //www.example.org '})
<soap: Body xmlns: m = "http://www.example.org"> qualquer que seja </ soap: Body>
``: python


# ### `` XML``
`` XML``: inxx
`` XML`` é um objeto usado para encapsular o texto que não deve ser escapado. O texto pode ou não conter XML válido. Por exemplo, ele pode conter JavaScript.


O texto neste exemplo é escapado:
``
>>> print DIV ("<b> olá </b>")
<div> & lt; b & gt; olá & lt; / b & gt; </div>
``: python


usando ` `XML``, você pode evitar escapar:
` `
>>> print DIV (XML (" <b> hello </b> "))
<div><b> hello</b> </div>
` `: python


Às vezes, você deseja renderizar HTML armazenado em uma variável, mas o HTML pode conter tags não seguras, como scripts:
``
>>> print XML ('<script> alert ("inseguro!") </script>')
<script> alert ("inseguro!") </script>
``: python A


entrada executável não escapada como esta (por exemplo, inserida no corpo de um comentário em um blog) é insegura, porque pode ser usada para gerar Cross Site Ataques de script (XSS) contra outros visitantes da página.


`` sanitize``: inxx
O auxiliar py4web `` XML`` pode higienizar nosso texto para evitar injeções e escapar de todas as tags, exceto aquelas que você permitir explicitamente. Aqui está um exemplo:
``
>>> print XML ('<script> alert ("inseguro!") </script>', sanitize = True)
& lt; script & gt; alert ("inseguro!") & Lt; / script & gt;
``: python


Os construtores `` XML``, por padrão, consideram seguro o conteúdo de algumas tags e alguns de seus atributos. Você pode substituir os padrões usando os argumentos opcionais `` allowed_tags`` e `` allowed_attributes``. Aqui estão os valores padrão dos argumentos opcionais do auxiliar `` XML``.
``
XML (text, sanitize = False,
    allowed_tags = ['a', 'b', 'blockquote', 'br /', 'i', 'li',
       'ol', 'ul', 'p', 'citar', 'código', 'pre', 'img /'],
    allowed_attributes = { 'a': [ 'href', 'título'],
       'img': [ 'src', 'alt'], ' blockquote ': [' type ']})
``: python


### Ajudantes


internos #### `` A``
`` A``: inxx


Este auxiliar é usado para criar links.


``
>>> print A ('<click>', XML ('<b> me </b>')),
            _href = 'http: //www.py4web.com')
<a href = 'http: / /www.py4web.com'>&lt;click&gt;<b>me </b> </a>
``: python


#### `` BODY``
`` BODY``: inxxcria
Esse ajudanteo corpo de uma página.
``
>>> print BODY ('<hello>', XML ('<b> mundo </b>'), _bgcolor = 'vermelho')
<body bgcolor = "red"> & lt; olá & gt; <b> mundo </b> </body>
``: python


#### `` CAT``:
`` CAT``: inxx


Esse assistente concatena outros auxiliares, o mesmo que TAG [\ '\'].


``
>>> print CAT ('Aqui está um', A ('link', _href = URL ()), 'e aqui estão alguns', B ('negrito'), '.')
Aqui está um <a href="/app/default/index"> link </a>, e aqui estão alguns <b> texto em negrito </b>.
``: python


#### `` CODE``
`` CODE``: inxx


Este assistente executa realce de sintaxe para códigos Python, C, C ++, HTML e py4web, e é preferível a `` PRE`` para listagens de código. O `` CODE`` também tem a capacidade de criar links para a documentação da API py4web.


Aqui está um exemplo de destaque de seções do código Python.
``
>>> print CODE ('print "hello"', language = 'python'). xml ()
``: python
``
<table> <tr style = "vertical-align: top;">
  <estilo td = "largura mínima: 40px; alinhamento de texto: direita;"> <pre style = "
        tamanho da fonte: 11px;
        família de fontes: Bitstream Vera Sans Mono, monoespaço;
        cor de fundo: transparente;
        margem: 0;
        preenchimento: 5px;
        border: none;
        color: # A0A0A0;
    "> 1 </ pre> </ td> <td> <pre style =."
        font-size: 11px;
        font-family: Bitstream Vera Sans Mono, monospace;
        background- cor: transparente;
        margem: 0;
        preenchimento: 5px;
        borda: nenhuma;
        excesso: automático;
        espaço em branco: pre! important;
"> <span style =" color: # 185369; peso da fonte: negrito "> print </ span>
  <span style = "color: # FF9966"> "olá" </span> </pre> </td> </tr> </table>
``: html


Aqui está um exemplo semelhante para HTML
``
> >> print CODE ('<html> <body> [[= request.env.remote_add]] </body> </html>',
... idioma = 'html')
``: python
``
<table> ... <code> ...
<html><body>[[=request.env.remote_addorgeous ♡<<body> </html>
... </code> ... </table>
``: python


Estes são os argumentos padrão para o auxiliar `` CODE``:
``
CODE ("print ' olá mundo '", language =' python ', link = None, counter = 1, styles = {})
` `: python


Os valores suportados para o argumento` `language`` são" python "," html_plain "," c " , "cpp", "py4web" e "html". A linguagem "html" interpreta as tags [[and]] como código "py4web", enquanto "html_plain" não.


Se um valor `` link`` for especificado, por exemplo "/ examples / global / vars /", as referências da API py4web no código serão vinculadas à documentação no URL do link. Por exemplo, "request" seria vinculado a "/ examples / global / vars / request". No exemplo acima, o URL do link é tratado pela ação "vars" no controlador "global.py" que é distribuído como parte do aplicativo "examples" do py4web.


O argumento `` counter`` é usado para numeração de linha. Pode ser definido com qualquer um dos três valores diferentes. Pode ser `` None`` para nenhum número de linha, um valor numérico especificando o número inicial ou uma string. Se o contador estiver definido como uma sequência, ele será interpretado como um prompt e não haverá números de linha.


O argumento `` styles`` é um pouco complicado. Se você observar o HTML gerado acima, ele conterá uma tabela com duas colunas e cada coluna terá seu próprio estilo declarado embutido usando CSS. Os atributos `` styles`` permitem substituir esses dois estilos CSS. Por exemplo:


``
CODE (..., styles = {'CODE': 'margin: 0; padding: 5px; border: none;'})
``: python


O atributo `` styles`` deve ser um dicionário, e permite duas chaves possíveis: `` CODE`` para o estilo do código real e `` LINENUMBERS`` para o estilo da coluna esquerda, que contém os números das linhas. Lembre-se de que esses estilos substituem completamente os estilos padrão e não são simplesmente adicionados a eles.


#### `` COL``
`` COL``: inxx


``
>>> print COL ('a', 'b')
<col> ab </col>
``: python


#### `` DIV``
`` DIV``: inxx


Todos os auxiliares, além de `` XML``, são derivados de `` DIV`` e herdam seus métodos básicos.


``
>>> DIV print ( '<Olá>', XML ( '<b> mundo </ b>'), _class = 'test', _id = 0)
<div id = "0" class = "teste" > & lt; hello & gt; <b> mundo </b> </div>
``: python


#### `` EM``
`` EM``: inxx


Enfatiza seu conteúdo.


``
>>> imprima EM ('<ello>', XML ('<b> mundo </b>')), _class = 'teste', _id = 0)
<em id = "0" class = "test" > & lt; hello & gt; <b> mundo </b> </em>
``: python


#### `` FIELDSET``
`` FIELDSET``: inxx


Isso é usado para criar um campo de entrada junto com seu rótulo.
``
>>> print FIELDSET ('Height:', INPUT (_name = 'height'), _class = 'test')
<fieldset class = "test"> Altura: <nome da entrada = "height" /> </ fieldset >
``: python


#### `` FORM``
`` FORM``: inxx


Este é um dos ajudantes mais importantes. Em sua forma simples, ele cria uma tag `` <form> ... </form> ``, mas como os auxiliares são objetos e têm conhecimento do que eles contêm, eles podem processar os formulários enviados (por exemplo, executar a validação de os campos). Isso será discutido em detalhes no Capítulo 7.
``
>>> print FORM (INPUT (_type = 'submit'), _action = '', _method = 'post')
<form enctype = ação "multipart / form-data" = "" method = "post">
<input type = "submit" /> </form>
``: python


O "enctype" é "multipart / form-data" por padrão.


`` hidden``: inxx
O construtor de um `` FORM`` e de `` SQLFORM`` também pode usar um argumento especial chamado `` hidden``. Quando um dicionário é passado como `` oculto``, seus itens são traduzidos para os campos "ocultos" INPUT. Por exemplo:
``
>>> print FORM (hidden = dict (a = 'b'))
<form enctype = "multipart / form-data" action = "" method = "post">
<input value = "b" type = "hidden" name = "a" /> </form>
``: python


#### `` H1``, `` H2``, `` H3``, `` H4``, `` H5``, `` H6``
`` H1``: inxx


Esses auxiliares são para cabeçalhos e subtítulos de parágrafos:
``
>>> print H1 ('<hello>', XML ('<b> world </b> '', _class = 'test', _id = 0)
<h1 id = "0" class = "test"> & lt; olá & gt; <b> mundo </b> </h1>
``: python


#### `` HEAD``
`` HEAD``: inxx


Para marcar o HEAD de uma página HTML.


``
>>> print HEAD (TITLE ('<hello>', XML ('<b> mundo </b>')))
<head> <title> & lt; hello & gt; <b> mundo </b> < / title> </ head>
``: python


#### `` HTML``
`` HTML``: inxx `` XHTML``: inxx


Este ajudante é um pouco diferente. Além de criar as tags `` <html> ``,
ela precede a tag com uma string doctype``xhtml-w, xhtml-o, xhtml-school``: cite.
``
>>> print HTML (BODY ('<hello>', XML ('<b> mundo </b>')))
<! DOCTYPE HTML PUBLIC "- // W3C // DTD HTML 4.01 Transitório // PT "" http://www.w3.org/TR/html4/loose.dtd ">
<html><body>&lt;hello&gt;<b>world</b></body> </html>
` `: python


O auxiliar HTML também aceita alguns argumentos opcionais adicionais que possuem o seguinte padrão:
``
HTML (..., lang = 'en', doctype = 'transitional')
``: python


onde doctype pode ser 'estrito', 'transicional ',' frameset ',' html5 'ou uma string de tipo de documento completa.


#### ``I``
``I``: inxx


Este assistente torna o seu conteúdo em itálico.
``
>>> imprima I ('<hello>', XML ('<b> mundo </b>'), _class = 'teste', _id = 0)
<i id = "0" class = "test" > & lt; hello & gt; <b> mundo </b> </i>
``: python


#### `` IMG``
`` IMG``: inxx


Pode ser usado para incorporar imagens no HTML:


``
> >> imprimir IMG (_src = 'http: //example.com/image.png', _alt = 'teste')
<img src = "http://example.com/image.ong" alt = "rest" >
``: python


Aqui está uma combinação de auxiliares A, IMG e URL para incluir uma imagem estática com um link:


``
>>> print A (IMG (_src = URL ('estático', 'logo.png')) , _alt = "Meu logotipo"),
... _href = URL ('padrão', 'índice'))
... 
<a href="/myapp/default/index">
  <img src = "/ myapp / static /logo.png "alt =" Meu logotipo "/>
</a>
` `: python


####` `INPUT```
`INPUT``: inxxum`


Cria`<input ... />` ` tag. Uma tag de entrada pode não conter outras tags e é fechada por `` /> `` em vez de ``> ``. A tag de entrada possui um atributo opcional `` _type`` que pode ser definido como "text" (o padrão), "submit", "checkbox" ou "radio".
``
>>> print INPUT (_name = 'test', _value = 'a')
<input value = "a" name = "test" />
``: python


Também é necessário um argumento especial opcional chamado "value", distinto de "_value". O último define o valor padrão para o campo de entrada; o primeiro define seu valor atual. Para uma entrada do tipo "text", a primeira substitui a última:
``
>>> print INPUT (_name = 'test', _value = 'a', valor = 'b')
<input value = "b" name = "test" />
``: python


Para botões de opção, `` INPUT`` define seletivamente o atributo "marcado":


`` radio``: inxx
``
>>> para v em ['a', 'b', 'c']:
... print INPUT (_tipo = 'radio', _name = 'test', _value = v, valor = 'b'), v
... 
<input value = "a" type = "radio" nome = "teste" /> a
<valor da entrada = "b" tipo = "rádio" verificado = "verificado" nome = "teste" /> b
<valor da entrada = "c" tipo = "rádio" nome = "teste" /> c
``: python


e da mesma forma para caixas de seleção:


`` checkbox``: inxx
``
>>> print INPUT (_type = 'checkbox', _name = 'test', _value = 'a', value = True)
< valor de entrada = "a" tipo = "caixa de seleção" marcado = "nome" marcado = "teste" />
>>> imprimir INPUT (_tipo = 'caixa de seleção', _nome = 'teste', _valor = 'a', valor = Falso )
<input value = "a" type = "checkbox" name = "test" />
``: python


#### `` LABEL``
`` LABEL``: inxx


É usado para criar uma tag LABEL para um Campo de entrada.


``
>>> imprima LABEL ('<hello>', XML ('<b> mundo </b>'), _class = 'test', _id = 0)
<label id = "0" class = "test" > & lt; hello & gt; <b> mundo </b> </label>
``: python


#### `` LEGEND``
`` LEGEND``: inxx


É usado para criar uma tag de legenda para um campo em um Formato.


``
>>> print LEGEND ('Name', _for = 'myfield')
<legend for = "myfield"> Name </legend>
``: python


#### `` LI``
`` LI``: inxx


faz um item da lista e deve estar contido em um `` UL`` ou `` tag OL``.


``
>>> imprima LI ('<hello>', XML ('<b> mundo </b>')), _class = 'teste', _id = 0)
<li id ​​= "0" class = "test" > & lt; hello & gt; <b> mundo </b> </li>
``: python


#### `` OL``
`` OL``: inxx


Significa Lista ordenada. A lista deve conter tags LI. Os argumentos `` OL`` que não são objetos `` LI`` são automaticamente colocados em tags `` <li> ... </li> ``.


``
>>> imprima OL ('<hello>', XML ('<b> mundo </b>'), _class = 'teste', _id = 0)
<ol id = "0" class = "test" > <li> & hello & gt; </li> <li> <b> mundo </b> </li> </ol>
``: python




#### `` OPTION``
`` OPTION``: inxx


Isso só deve ser usado como parte de um `` / `` combinação OPTION`` SELECT``.


``
>>> print OPTION ('<hello>', XML ('<b> mundo </b>'), _value = 'a')
<option value = "a"> & lt; olá & gt; <b> mundo </b> </option>
``: python


Como no caso de `` INPUT``, o py4web faz uma distinção entre "_value" (o valor da OPTION) e "value" (o valor atual do anexo) selecione). Se forem iguais, a opção é "selecionada".


`` selected``: inxx
``
>>> print SELECT ('a', 'b', value = 'b'):
<select>
<opção valor = "a"> a </option>
<opção valor = "b" selected = "selected"> b </option>
</select>
``: python


#### `` P``
`` P``: inxx


Isto é para marcar um parágrafo.
``
>>> imprima P ('<hello>' ', XML (' <b> mundo </b> '), _class =' ​​test ', _id = 0)
<p id = "0" class = "test" > & lt; hello & gt; <b> mundo </b> </p>
``: python


#### `` PRE``
`` PRE``: inxx


Gera um `` <pre> ... </ pre > `` tag para exibir texto pré-formatado. O auxiliar `` CODE`` é geralmente preferível para listagens de código.
``
>>> imprima PRE ('<hello>', XML ('<b> mundo </b>')), _class = 'teste', _id = 0)
<pre id = "0" class = "test" > & lt; hello & gt; <b> mundo </b> </pre>
``: python


#### `` SCRIPT``
`` SCRIPT``: inxx


Isso inclui ou vincula um script, como JavaScript. O conteúdo entre as tags é renderizado como um comentário HTML, para o benefício de navegadores realmente antigos.
``
>>> print SCRIPT ('alert ("olá mundo");', _type = 'text / javascript')
<tipo de script = "text / javascript"> <! -
alert ("olá mundo");
// -> </script>
``: python


#### `` SELECT``
`` SELECT``: inxxtag


Faz uma`` <select> ... </select> ``. Isso é usado com o auxiliar `` OPTION``. Esses argumentos `` SELECT`` que não são objetos `` OPTION`` são automaticamente convertidos em opções.
``
>>> print SELECT ('<hello>', XML ('<b> world </b>'), _class = 'test', _id = 0)
<selecione id = "0" class = "test" >
<opção value = "& lt; hello & gt;"> & lt; hello & gt; </option>
<option value = "& lt; b & gt; mundo & lt; / b & gt;"> <b> mundo </b> </option>
</ selecione>
``: python


#### `` SPAN``
`` SPAN``: inxx


Semelhante ao `` DIV``, mas usado para marcar o conteúdo embutido (em vez de bloquear).
``
>>> imprima SPAN ('<hello>', XML ('<b> mundo </b>'), _class = 'test', _id = 0)
<span id = "0" class = "test" > & lt; hello & gt; <b> world </b> </span>
``: python


#### `` STYLE``
`` STYLE``: inxx


Semelhante ao script, mas usado para incluir ou vincular o código CSS .
Aqui o CSS está incluído:
``
>>> print STYLE (XML ('body {color: white}'))
<style> <! -
body {color: white}
// -> </style>
`` : python


e aqui está o link:
``
>>> print STYLE (_src = 'style.css')
<style src = "style.css"> <! -
// -> </style>
``: python


#### `` TABLE``, `` TR``, `` TD``
`` TABLE``: inxx `` TR``: inxx `` TD``: inxx


Essas tags (junto com o opcional Os auxiliares `` THEAD`` e `` TBODY``) são usados ​​para criar tabelas HTML.
``
>>> print TABLE (TR (TD ('a'), TD ('b')), TR (TD ('c'), TD ('d')))
<table> <tr> <td > a </td> <td> b </td> </tr> <tr> <td> c </td> <td> d </td> </tr> </table>
``: python
` `TR`` espera conteúdo` `TD``; argumentos que não são objetos `` TD`` são convertidos automaticamente.
``
>>> print TABLE (TR ('a', 'b'), TR ('c', 'd'))
<table><tr><td>a</td> <td> b </ td> </ tr> <tr> <td> c </ td> <td> d </ td> </ tr> </ table>
``: python


é fácil converter uma matriz de Python em uma tabela HTML usando A notação de argumentos da função `` * `` do Python, que mapeia elementos da lista para argumentos da função posicional.


Aqui, faremos linha por linha:
``
>>> table = [['a', 'b'], ['c', 'd']]
>>> print TABLE (TR (* table [0 ]), TR (* tabela [1]))
<table><tr><td>a</td><td>b</td></tr><tr> <td> c </td> < td> d </td> </tr> </table>
``: python


Aqui fazemos todas as linhas ao mesmo tempo:
``
>>> table = [['a', 'b'], ['c', 'd']]
>>> imprima TABLE (* [TR (* linhas) para linhas na tabela])
<table><tr><td>a</td><td>b</td> </tr> <tr><td>c</td><td>d</td></tr> </table>
``: python


#### `` TBODY``
`` TBODY``: inxx


Isso é usado para marcar linhas contidas no corpo da tabela, em oposição às linhas de cabeçalho ou rodapé. É opcional
``
>>> imprima TBODY (TR ('<ello>'), _classe = 'teste', _id = 0)
<tbody id = "0" class = "test"> <tr> <td> & lt; hello & gt; </td></tr> </tbody>
``: python


#### `` TEXTAREA``
`` TEXTAREA``: inxxcria


Esse auxiliarum `` <textarea> ... </textarea> `` tag.
``
>>> imprima TEXTAREA ('<hello>', XML ('<b> mundo </b>'), _class = 'test')
<textarea class = "test" cols = "40" linhas = "10 "> & lt; hello & gt; <b> mundo </b> </textarea>
` `: python


A única ressalva é que seu" valor "opcional substitui seu conteúdo (HTML interno)
` `
>>> print TEXTAREA (value =" <Olá mundo>", _class = "teste")
<classe área de texto = "teste" cols = "40" linhas = "10"> & lt; Olá mundo & gt; </ área de
texto>``: pitão


####` `TH ``
`` TH``: inxx


É usado em vez de `` TD`` nos cabeçalhos das tabelas.
``
>>> imprima TH ('<hello>' ', XML (' <b> mundo </b> '), _class =' ​​teste ', _id = 0)
<th id = "0" class = "test" > & lt; hello & gt; <b> mundo </b> </th>
``: python


#### `` THEAD``
`` THEAD``: inxx


Isso é usado para marcar linhas de cabeçalho de tabela.
``
>>> imprima THEAD (TR (TH ('<ello>')), _classe = 'teste', _id = 0)
<thead id = "0" class = "test"> <tr> <th> & lt ; hello & gt; </th> </tr> </thead>
``: python


#### `` TITLE``
`` TITLE``: inxx


Isso é usado para marcar o título de uma página em um cabeçalho HTML.
``
>>> print TITLE ('<hello>', XML ('<b> mundo </b>'))
<title>&lt;hello&gt;<b>world</b> </title>
``: python


#### `` TR``
`` TR``: inxx Marca


uma linha da tabela. Ele deve ser renderizado dentro de uma tabela e conter as tags `` <td> ... </td> ``. Os argumentos `` TR`` que não são objetos `` TD`` serão convertidos automaticamente.
``
>>> imprima TR ('<hello>', XML ('<b> mundo </b>'), _class = 'teste', _id = 0)
<tr id = "0" class = "test" > <td> & lt; hello & gt; </td> <td> <b> mundo </b> </td> </tr>
``: python


#### `` TT``
`` TT``: inxx Marca o


texto como texto da máquina de escrever (monoespaçado).
``
>>> imprime TT ('<ello>', XML ('<b> mundo </b>')), _class = 'teste', _id = 0)
<tt id = "0" class = "test" > & lt; hello & gt; <b> world </b> </tt>
``: python


#### `` UL``
`` UL``: UL``: inxx


Significa uma lista não ordenada e deve conter itens `` LI`` . Se o conteúdo não estiver marcado como `` LI``, `` UL`` o fará automaticamente.
``
>>> imprima UL ('<hello>', XML ('<b> mundo </b>')), _class = 'teste', _id = 0)
<ul id = "0" class = "test" > <li> & hello & gt; </li> <li> <b> mundo </b> </li> </ul>
``: python


#### `` URL``


O auxiliar de URL está documentado em [[Capítulo 4 URL ../04#URL]]Auxiliares


###personalizados


#### `` TAG``
`` TAG``: inxx


Às vezes você precisa gerar tags XML personalizadas. O py4web fornece o `` TAG``, um gerador de tags universal.
``
[[= TAG.name ('a', 'b', _c = 'd')]]
``: html


gera o seguinte XML
``
<name c = "d"> ab </name>
`` : pitão [léxico = 'xml']


Argumentos "a", "b" e "d" são automaticamente escapou; use o auxiliar `` XML`` para suprimir esse comportamento. Usando `` TAG``, você pode gerar tags HTML / XML ainda não fornecidas pela API. Os TAGs podem ser aninhados e serializados com `` str (). ``
Uma sintaxe equivalente é:
``
[[= TAG ['name'] ('a', 'b', c = 'd')]]
``: html


Se o objeto TAG for criado com um nome vazio, ele poderá ser usado para concatenar várias seqüências de caracteres e auxiliares de HTML juntos sem inseri-los em uma tag circundante, mas esse uso será descontinuado. Use o auxiliar `` CAT`` em vez disso.


Tags de fechamento automático podem ser geradas com o auxiliar TAG. O nome da tag deve terminar com um "/".
``
[[= = TAG ['link /'] (_href = 'http: //py4web.com')]
``: html
gera o seguinte XML:
``
<link ref = "http://py4web.com "/>
` `: python [lexer = 'xml']
Observe que` `TAG`` é um objeto e` `TAG.name`` ou` `TAG ['name']` `é uma função que retorna um classe auxiliar temporária.


#### `` MENU``
`` MENU``: inxx


O auxiliar MENU pega uma lista de listas ou de tuplas na forma de `` response.menu`` (como descrito no Capítulo 4) e gera uma árvore - como estrutura usando listas não ordenadas representando o menu. Por exemplo:
``
>>> print MENU ([['One', False, 'link1'], ['Two', False, 'link2']])
<ul class = "py4web-menu py4web-menu py4web-menu-vertical ">
<li> <a href="link1"> Um </a> </li>
<li> <a href="link2"> Dois </a> </li>
</ul>
` `: python


------
O primeiro item de cada lista / tupla é o texto a ser exibido para o item de menu especificado.


O segundo item em cada lista / tupla é um booleano indicando se esse item de menu específico está ativo
(ou seja, o item atualmente selecionado). Quando definido como verdadeiro, o `` MENU`` helper irá adicionar uma"-py4web-menu ativo"
classepara o `` <li> `` para esse item (você pode alterar o nome dessa classe, através do argumento "li_active" para `` MENU``).
Outra maneira de especificar o URL ativo é transmiti-lo diretamente para `` MENU`` através do seu argumento "active_url".


O terceiro item em cada lista / tupla pode ser um auxiliar de HTML (que pode incluir auxiliares aninhados), e o auxiliar `` MENU`` simplesmente renderiza esse auxiliar em vez de criar sua própria tag `` <a> ``.
------


Cada item de menu pode ter um quarto argumento que é um submenu aninhado (e assim por diante):
``
>>> print MENU ([['One', False, 'link1', [['Two ', False,' link2 ']]]])
<ul class = "py4web-menu py4web-menu-vertical">
<li class = "py4web-menu-expand">
<a href="link1"> Um </ a>
<ul class = "py4web-menu-vertical">
<li> <a href="link2"> Dois </a> </li>
</ul>ul>
</</li>
</ul>
``: python


Um item de menu também pode ter um quinto elemento opcional, que é um booleano. Quando falso, o item de menu é ignorado pelo auxiliar de MENU.


O auxiliar `` MENU`` aceita os seguintes argumentos opcionais:
- `` _class``: o padrão é "py4web-menu py4web-menu py4web-menu-vertical" e define a classe dos elementos UL externos.
- `` ul_class``: o padrão é "py4web-menu-vertical" e define a classe dos elementos UL internos.
- `` li_class``: o padrão é "py4web-menu-expand" e define a classe dos elementos LI internos.
- `` li_first``: permite adicionar uma classe ao primeiro elemento da lista.
- `` li_last``: permite adicionar uma classe ao último elemento da lista.


`` mobile``: inxx


`` MENU`` aceita um argumento opcional `` mobile``. Quando definido como `` True``, em vez de criar uma estrutura de menu recursiva `` UL``, ele retorna um menu suspenso `` SELECT`` com todas as opções de menu e um atributo `` onchange`` que redireciona para a página correspondente ao opção selecionada. Isso foi projetado como uma representação alternativa de menu que aumenta a usabilidade em pequenos dispositivos móveis, como telefones.


Normalmente, o menu é usado em um layout com a seguinte sintaxe:


``
[[= MENU (response.menu, mobile = request.user_agent (). Is_mobile)]]
``: html


Dessa maneira, um dispositivo móvel é automaticamente detectado e o menu é renderizado de acordo.


### `` BEAUTIFY``:
`` BEAUTIFY``: inxx


`` BEAUTIFY`` é usado para criar representações HTML de objetos compostos, incluindo listas, tuplas e dicionários:
``
[[= BEAUTIFY ({"a": [ "hello", XML ("world")], "b": (1, 2)})]]
``: html
`` BEAUTIFY`` retorna um objeto semelhante a XML serializável em XML, com uma boa aparência de seu argumento construtor. Nesse caso, a representação XML de:
``
{"a": ["olá", XML ("world")], "b": (1, 2)}
``: python


será renderizada como:
``
< tabela>
<tr><td>a</td><td>:</td> <td> olá <br /> mundo </td> </tr>
<tr> <td> b </td> < td>: </td> <td> 1 <br /> 2 </td> </tr>
</table>
``: html


### DOM '' do servidor '' e analisando


#### ` `elements```
`element``: inxx` `elements``: inxxelement`` e`


O assistente de DIV e todos os auxiliares derivados fornecem os métodos de pesquisa` ``elements``.


`` element`` retorna o primeiro elemento filho que corresponde a uma condição especificada (ou Nenhum se não houver correspondência).


`` elements`` retorna uma lista de todos os filhos correspondentes.


** elemento ** e ** elementos ** usam a mesma sintaxe para especificar a condição de correspondência, o que permite três possibilidades que podem ser misturadas e correspondidas: expressões semelhantes a jQuery, correspondendo pelo valor exato do atributo, correspondendo usando expressões regulares.


Aqui está um exemplo simples:
``
>>> a = DIV (DIV (DIV ('a', _id = 'target', _class = 'abc'))))
>>> d = a.elements ('div # target ')
>>> d [0] [0] =' alterado '
>>> imprima uma
<div> <div> <div id = "target" class = "abc"> alterada </div> </div> < / div>
``: python


O argumento sem nome de `` elements`` é uma string que pode conter: o nome de uma tag, o ID de uma tag precedida por um símbolo de libra, a classe precedida por um ponto, o valor explícito de um atributo entre colchetes.


Aqui estão 4 maneiras equivalentes para pesquisar a tag anterior id:
``
d = a.elements ( '# alvo')
d = a.elements ( 'div # alvo')
d = a.elements ( 'div [id = alvo ] ')
d = a.elements (' div ', _id =' target ')
``: python


Aqui estão quatro maneiras equivalentes de pesquisar a tag anterior por classe:
``
d = a.elements ('. abc ')
d = a.elements ('div.abc')
d = a.elements ('div [class = abc]')
d = a.elements ('div', _class = 'abc')
``: python


Qualquer atributo pode ser usado para localizar um elemento (não apenas `` id`` e `` class``), incluindo vários atributos (o elemento de função pode receber vários argumentos nomeados), mas apenas o primeiro elemento correspondente será retornado.


Usando a sintaxe jQuery "div # target", é possível especificar vários critérios de pesquisa separados por vírgula:
``
a = DIV (SPAN ('a', _id = 't1'), DIV ('b', _class = ' c2 '))
d = a.elements (' span # t1, div.c2 ')
``: python


ou equivalente
``
a = DIV (SPAN (' a ', _id =' t1 ')), DIV (' b ' , _class = 'c2'))
d = a.elements ('span # t1', 'div.c2')
``: python


Se o valor de um atributo for especificado usando um argumento de nome, ele poderá ser uma string ou um expressão regular:
``
a = DIV (SPAN ('a', _id = 'test123'), DIV ('b', _class = 'c2'))
d = a.elements ('span', _id = re.compile ('test \ d {3}')
``: python


Um argumento especial nomeado dos auxiliares do DIV (e derivados) é `` find``. Ele pode ser usado para especificar um valor de pesquisa ou uma expressão regular de pesquisa no texto Por exemplo:
``
>>> a = DIV (SPAN ('abcde'), DIV ('fghij'))
>>> d = a.elements (find = 'bcd')
>>> print d [0]
<span> abcde </span>
``: python


ou
``
>>> a = DIV (SPAN ('abcde'), DIV ('fghij'))
>>> d = a.elements (find = re.compile ('fg \ w {3}'))
>>> print d [0]
<div> fghij </div>
``: python


# ### `` components`` 
`` components``: inxx


Aqui está um exemplo de lista de todos os elementos em uma string html:
``
>>> html = TAG ('<a> xxx </a> <b> aaaa < / b> ')
>>> para o item em html.components:
... print item
... 
<a> xxx </a>
<b> aaaa </b>
``: python


#### `` parent `` and `` siblings``
`` parent``: inxx `` sibling``: inxx


`` parent`` retorna o pai do elemento atual.
``
>>> a = DIV (SPAN ('a'), DIV ('b'))
>>> s = a.element ('span')
>>> d = s.parent
>>> d [' _class '] =' abc '
>>> imprima uma
<div class = "abc"> <span> a </span> <div> b </div> </div>
>>> para e em s.siblings ( ): print e
<div> b </div>
``: python


#### Substituindo elementos Os


elementos correspondentes também podem ser substituídos ou removidos especificando
o argumento `` replace``. Observe que uma
lista dos elementos correspondentes originais ainda é retornada como de costume.


``
>>>a = DIV (SPAN ( 'x'), DIV (SPAN ( 'y'))
b = >>> a.elements ( 'extensão', substituir = P ( 'z')
>>> impressão a
<div><p>z</p><div><p>z</p> </div>
``: python


`` replace`` pode ser exigível.Neste caso, será passado
o original elemento e espera-se retornar o elemento de substituição:


``
>>> a = DIV (SPAN ('x')), DIV (SPAN ('y'))
>>> b = a.elements ('span', replace = lambda t: P (t [0])
>>> imprime um
<div><p>x</p><div><p>y</p> </div>
``: python


If `` replace = None``, os elementos correspondentes serão removidos completamente.


``
>>> a = DIV (SPAN ('x'), DIV (SPAN ('y'))
>>> b = a.elements ('span', replace = None)
>>> imprima um
<div> </div>
``: python


#### `` flatten`` 
`` flatten``: inxx


O método flatten serializa recursivamente o conteúdo dos filhos de um determinado elemento em texto normal (sem tags):
``
>>> a = DIV (SPAN ('this', DIV ('is', B ('a'))), SPAN ('test'))
>>> imprima um .flatten ()
thisisatest
``: python


Flatten pode receber um argumento opcional, `` render``, ou seja, uma função que renderiza / nivela o conteúdo usando um protocolo diferente . Aqui está um exemplo para serializar algumas tags na sintaxe wiki do Markmin:
``
>>> a = DIV (H1 ('title'), P ('exemplo de a', A ('link', _href = '# test') ))
>>> from gluon.html import markmin_serializer
>>> print a.flatten(render=markmin_serializer)
# titles


example of [[a link #test]]


``:python


At the time of writing we provide ``markmin_serializer` ` and ``markdown_serializer``.


#### Parsing


The TAG object is also an XML/HTML parser. It can read text and convert into a tree structure of helpers. This allows manipulation using the API above:
``
>>> html = '<h1>Title</h1><p>this is a <span>test</span></p>'
>>> parsed_html = TAG(html)
>>> parsed_html.element('span')[0]='TEST'
>>> print parsed_html
<h1>Title</h1><p>this is a <span>TEST</span></p>
``:python




### Page layout
``page layout``:inxx ``layout.html``:inxx ``extent``:inxx ``include``:inxx


Views can extend and include other views in a tree-like structure.


For example, we can think of a view "index.html" that extends "layout.html" and includes "body.html".
At the same time, "layout.html" may include "header.html" and "footer.html".


The root of the tree is what we call a layout view. Just like any other HTML template file, you can edit it using the py4web administrative interface. The file name "layout.html" is just a convention.


Here is a minimalist page that extends the "layout.html" view and includes the "page.html" view:


``
[[extend 'layout.html']]
<h1>Hello World</h1>
[[include 'page.html']]
``:python


The extended layout file must contain an ``[[include]]`` directive, something like:
``
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    [[include]]
  </body>
</html>
``:python


When the view is called, the extended (layout) view is loaded, and the calling view replaces the ``[[include]]`` directive inside the layout. Processing continues recursively until all ``extend`` and ``include`` directives have been processed. The resulting template is then translated into Python code. Note, when an application is bytecode compiled, it is this Python code that is compiled, not the original view files themselves. So, the bytecode compiled version of a given view is a single .pyc file that includes the Python code not just for the original view file, but for its entire tree of extended and included views.


-------
``extend``, ``include``, ``block`` and ``super`` are special template directives,
not Python commands.
-------


Any content or code that precedes the ``[[extend ...]]`` directive will be inserted (and therefore executed) before the beginning of the extended view's content/code. Although this is not typically used to insert actual HTML content before the extended view's content, it can be useful as a means to define variables or functions that you want to make available to the extended view. For example, consider a view "index.html":
``
[[sidebar_enabled=True]]
[[extend 'layout.html']]
<h1>Home Page</h1>
``:python


and an excerpt from "layout.html":
``
[[if sidebar_enabled:]]
    <div id="sidebar">
        Sidebar Content
    </div>
[[pass]]
``:python


Because the ``sidebar_enabled`` assignment in "index.html" comes before the ``extend``, that line gets inserted before the beginning of "layout.html", making ``sidebar_enabled`` available anywhere within the "layout.html" code (a somewhat more sophisticated version of this is used in the **welcome** app).


It is also worth pointing out that the variables returned by the controller function are available not only in the function's main view, but in all of its extended and included views as well.


The argument of an ``extend`` or ``include`` (ie, the extended or included view name) can be a Python variable (though not a Python expression). However, this imposes a limitation -- views that use variables in ``extend`` or ``include`` statements cannot be bytecode compiled. As noted above, bytecode-compiled views include the entire tree of extended and included views, so the specific extended and included views must be known at compile time, which is not possible if the view names are variables (whose values are not determined until run time). Because bytecode compiling views can provide a significant speed boost, using variables in ``extend`` and ``include`` should generally be avoided if possible.


In some cases, an alternative to using a variable in an ``include`` is simply to place regular ``[[include ...]]`` directives inside an ``if...else`` block.


``
[[if some_condition:]]
[[include 'this_view.html']]
[[else:]]
[[include 'that_view.html']]
[[pass]]
``:html


The above code does not present any problem for bytecode compilation because no variables are involved. Note, however, that the bytecode compiled view will actually include the Python code for both "this_view.html" and "that_view.html", though only the code for one of those views will be executed, depending on the value of ``some_condition``.


Keep in mind, this only works for ``include`` -- you cannot place ``[[extend ...]]`` directives inside ``if...else`` blocks.


``response.menu``:inxx ``menu``:inxx ``response.meta``:inxx ``meta``:inxx


Layouts are used to encapsulate page commonality (headers, footers, menus), and though they are not mandatory, they will make your application easier to write and maintain. In particular, we suggest writing layouts that take advantage of the following variables that can be set in the controller. Using these well known variables will help make your layouts interchangeable:
``
response.title
response.subtitle
response.meta.author
response.meta.keywords
response.meta.description
response.flash
response.menu
response.files
``:python[lexer=None]


Except for ``menu`` and ``files``, these are all strings and their meaning should be obvious.


``response.menu`` menu is a list of 3-tuples or 4-tuples. The three elements are: the link name, a boolean representing whether the link is active (is the current link), and the URL of the linked page. For example:
``
response.menu = [('Google', False, 'http://www.google.com', []),
                 ('Index', True, URL('index'), [])]
``:python


``sub-menu``:inxx
The fourth tuple element is an optional sub-menu.


``response.files`` is a list of CSS and JS files that are needed by your page.


We also recommend that you use:


``
[[include 'py4web_ajax.html']]
``:html


in the HTML head, since this will include the jQuery libraries and define some backward-compatible JavaScript functions for special effects and Ajax. "py4web_ajax.html" includes the ``response.meta`` tags in the view, jQuery base, the calendar datepicker, and all required CSS and JS ``response.files``.


#### Default page layout


``Twitter Bootstrap``:inxx


The "views/layout.html" that ships with the py4web scaffolding application **welcome** (stripped down of some optional parts) is quite complex but it has the following structure:


``
<!DOCTYPE html>
<head>
  <meta charset="utf-8" />
  <title>[[=response.title or request.application]]</title>
  ...
  <script src="[[=URL('static', 'js/modernizr.custom.js')]]"></script>


  [[
  response.files.append(URL('static', 'css/py4web.css'))
  response.files.append(URL('static', 'css/bootstrap.min.css'))
  response.files.append(URL('static', 'css/bootstrap-responsive.min.css'))
  response.files.append(URL('static', 'css/py4web_bootstrap.css'))
  ]]


  [[include 'py4web_ajax.html']]


  [[
  # using sidebars need to know what sidebar you want to use
  left_sidebar_enabled = globals().get('left_sidebar_enabled', False)
  right_sidebar_enabled = globals().get('right_sidebar_enabled', False)
  middle_columns = {0:'span12', 1:'span9', 2:'span6'}[
    (left_sidebar_enabled and 1 or 0)+(right_s idebar_enabled and 1 or 0)]
  ]]


  [[block head]][[end]]
</head>


<body>
  <!-- Navbar ================================================== -->
  <div class="navbar navbar-inverse navbar-fixed-top">
    <div class="flash">[[=response.flash or '']]</div>
    <div class="navbar-inner">
      <div class="container">
        [[=response.logo or '']]
        <ul id="navbar" class="nav pull-right">
          [[='auth' in globals() and auth.navbar(mode="dropdown") or '']]
        </ul>
        <div class="nav-collapse">
          [[if response.menu:]]
          [[=MENU(response.menu)]]
          [[pass]]
        </div><!--/.nav-collapse -->
      </div>
    </div>
  </div><!--/top navbar -->


  <div class="container">
    <!-- Masthead ================================================== -->
    <header class="mastheader row" id="header">
        <div class="span12">
            <div class="page-header">
                <h1>
                    [[=response.title or request.application]]
                    <small>[[=response.subtitle or '']]</small>
                </h1>
            </div>
        </div>
    </header>


    <section id="main" class="main row">
        [[if left_sidebar_enabled:]]
        <div class="span3 left-sidebar">
            [[block left_sideb ar]]
            <h3>Left Sidebar</h3>
            <p></p>
            [[end]]
        </div>
        [[pass]]


        <div class="[[=middle_columns]]">
            [[block center]]
            [[include]]
            [[end]]
        </div>


        [[if right_sidebar_enabled:]]
        <div class="span3">
            [[block right_sidebar]]
            <h3>Right Sidebar</h3>
            <p></p>
            [[end]]
        </div>
        [[pass]]
    </section><!--/main-->


    <!-- Footer ================================================== -->
    <div class="row">
        <footer class="footer span12" id="footer">
            <div class="footer-content">
                [[block footer]] <!-- this is default footer -->
                ...
                [[end]]
            </div>
        </footer>
    </div>


  </div> <!-- /container -->


  <!-- The javascript =============================================
       (Placed at the end of the document so the pages load faster) -->
  <script src="[[=URL('static', 'js/bootstrap.min.js')]]"></script>
  <script src="[[=URL('static', 'js/py4web_bootstrap.js')]]"></script>
  [[if response.google_analytics_id:]]
    <script src="[[=URL('static', 'js/analytics.js')]]"></script>
    <script type="text/javascript">
    analytics.initialize({
      'Google Analytics':{tr ackingId:'[[=response.google_analytics_id]]'}
    });</script>
  [[pass]]
</body>
</html>
``:python


There are a few features of this default layout that make it very easy to use and customize:


- It is written in HTML5 and uses the "modernizr" ``modernizr``:cite library for backward compatibility. The actual layout includes some extra conditional statements required by IE and they are omitted for brevity.
- It displays both ``response.title`` and ``response.subtitle`` which can be set in a model or a controller. If they are not set, it adopts the application name as title.
- It includes the ``py4web_ajax.html`` file in the header which generated all the link and script import statements.
- It uses a modified version of Twitter Bootstrap for flexible layouts which works on mobile devices and re-arranges columns to fit small screens.
- It uses "analytics.js" to connect to Google Analytics.
- The ``[[=auth.navbar(...)]]`` displays a welcome to the current user and links to the auth functions like login, logout, register, change password, etc. depending on context. ``auth.navbar`` is a helper factory and its output can be manipulated as any other helper. It is placed in an expression to check for auth definition, the expression evaluates to '' in case auth is undefined.
- The ``[[=MENU(response.menu)]]`` displays the menu structure as ``<ul>...</ul>``.
- ``[[include]]`` is replaced by the content of the extending view when the page is rendered.
- By default it uses a conditional three column (the left and right sidebars can be turned off by the extending views)
- It uses the following classes: page-header, main, footer.
- It contains the following blocks: head, left_sidebar, center, right_sidebar, footer.


In views, you can turn on and customize sidebars as follows:


``
[[left_sidebar_enabled=True]]
[[extend 'layout.html']]


This text goes in center


[[block left_sidebar]]
This text goes in sidebar
[[end]]
``:html


#### Customizing the default layout
``CSS``:inxx


Customizing the default layout without editing is easy because the welcome application is based on Twitter Bootstrap which is well documented and supports themes. In py4web four static files which are relevant to style:


- "css/py4web.css" contains py4web specific styles
- "css/bootstrap.min.css" contains the Twitter Bootstrap CSS style ``bootstrap``:cite ``Bootstrap``:inxx
- "css/py4web_bootstrap.css" which overrides some Bootstrap styles to conform to py4web needs.
- "js/bootstrap.min.js" which includes the libraries for menu effects, modals, panels.


To change colors and background images,
try append the following code to layout.html header:


``
<style>
body { background: url('images/background.png') repeat-x #3A3A3A; }
a { color: #349C01; }
.page-header h1 { color: #349C01; }
.page-header h2 { color: white; font-style: italic; font-size: 14px;}
.statusbar { background: #333333; border-bottom: 5px #349C01 solid; }
.statusbar a { color: white; }
.footer { border-top: 5px #349C01 solid; }
</style>
``:python[lexer='css']


Of course you can also completely replace the "layout.html" and "py4web.css" files with your own.


#### Mobile development


Although the default layout.html is designed to be mobile-friendly, one may sometimes need to use different views when a page is visited by a mobile device.


To make developing for desktop and mobile devices easier, py4web includes the ``@mobilize`` decorator. This decorator is applied to actions that should have a normal view and a mobile view. This is demonstrated here:


``
from gluon.contrib.user_agent_parser import mobilize
@mobilize
def index():
    return dict()
``:python


Notice that the decorator must be imported before using it in a controller.
When the "index" function is called from a regular browser (desktop computer), py4web will render the returned dictionary using the view "[controller]/index.html". However, when it is called by a mobile device, the dictionary will be rendered by "[controller]/index.mobile.html". Notice that mobile views have the "mobile.html" extension.


Alternatively you can apply the following logic to make all views mobile friendly:


``
if request.user_agent().is_mobile:
    response.view.replace('.html', '.mobile.html')
``:python


The task of creating the "*.mobile.html" views is left to the developer but we strongly suggest using the "jQuery Mobile" plugin which makes the task very easy.


### Functions in views


Consider this "layout.html":


``
<html>
  <body>
    [[include]]
    <div class="sidebar">
      [[if 'mysidebar' in globals():]][[mysidebar()]][[else:]]
        my default sidebar
      [[pass]]
    </div>
  </body>
</html>
``:python


and this extending view


``
[[def mysidebar():]]
my new sidebar!!!
[[return]]
[[extend 'layout.html']]
Hello World!!!
``:html


Notice the function is defined before the ``[[extend...]]`` statement -- this results in the function being created before the "layout.html" code is executed, so the function can be called anywhere within "layout.html", even before the ``[[include]]``. Also notice the function is included in the extended view without the ``=`` prefix.


The code generates the following output:


``
<html>
  <body>
    Hello World!!!
    <div class="sidebar">
      my new sidebar!!!
    </div>
  </body>
</html>
``:html


Notice that the function is defined in HTML (although it could also contain Python code) so that ``response.write`` is used to write its content (the function does not return the content). This is why the layout calls the view function using ``[[mysidebar()]]`` rather than ``[[=mysidebar()]]``. Functions defined in this way can take arguments.


### Blocks in views
``block``:inxx


The main way to make a view more modular is by using ``[[block ...]]``s and this mechanism is an alternative to the mechanism discussed in the previous section.


To understand how this works, consider apps based on the scaffolding app welcome, which has a view layout.html. This view is extended by the view ``default/index.html`` via ``[[extend 'layout.html']]``. The contents of layout.html predefine certain blocks with certain default content, and these are therefore included into default/index.html.


You can override these default content blocks by enclosing your new content inside the same block name. The location of the block in the layout.html is not changed, but the contents is. 


Here is a simplifed version. Imagine this is "layout.html":


``
<html>
  <body>
    [[include]]
    <div class="sidebar">
      [[block mysidebar]]
        my default sidebar (this content to be replaced)
      [[end]]
    </div>
  </body>
</html>
``:python


and this is a simple extending view ``default/index.html``:


``
[[extend 'layout.html']]
Hello World!!!
[[block mysidebar]]
my new sidebar!!!
[[end]]
``:html


It generates the following output, where the content is provided by the over-riding block in the extending view, yet the enclosing DIV and class comes from layout.html. This allows consistency across views:


``
<html>
  <body>
    Hello World!!!
    <div class="sidebar">
        my new sidebar!!!
    </div>
  </body>
</html>
``:html


The real layout.html defines a number of useful blocks, and you can easily add more to match the layout your desire. 


You can have many blocks, and if a block is present in the extended view but not in the extending view, the content of the extended view is used. Also, notice that unlike with functions, it is not necessary to define blocks before the ``[[extend ...]]`` -- even if defined after the ``extend``, they can be used to make substitutions anywhere in the extended view.


``super``:inxx


Inside a block, you can use the expression ``[[super]]`` to include the content of the parent. For example, if we replace the above extending view with:


``
[[extend 'layout.html']]
Hello World!!!
[[block mysidebar]]
[[super]]
my new sidebar!!!
[[end]]
``:html


we get:


``
<html>
  <body>
    Hello World!!!
    <div class="sidebar">
        my default sidebar
        my new sidebar!
    </div>
  </body>
</html>
``:html