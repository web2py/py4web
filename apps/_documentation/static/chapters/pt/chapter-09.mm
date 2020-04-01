Pluralize


Pluralize é uma biblioteca Python para Internacionalização (i18n) e Pluralização (p10n).


A biblioteca assume uma pasta (por exemplo "traduções") que contém arquivos como:


``
it.json
it-IT.json
fr.json
fr-FR.json
(etc)
``


Cada arquivo tem a seguinte estrutura, por exemplo, para Italiano (it.json):


``
{"dog": {"0": "no cane", "1": "un cane", "2": "{n} cani", "10": "tantissimi cani "}}
` `


As chaves de nível superior são as expressões a serem traduzidas e o valor / dicionário associado mapeia um número para uma tradução.
Traduções diferentes correspondem a diferentes formas plurais da expressão.


Aqui está outro exemplo da palavra "bed" em checo


``
{"bed": {"0": "no postel", "1": "postel", "2 ":" postele "," 5 ":" postelí "}}
` `


Para traduzir e pluralizar uma string" dog ", basta entortar a string no operador T da seguinte maneira:


` `
>>> from pluralize import Translator
>>> T = Tradutor ('traduções')
>>> cachorro = T ("cachorro")
>>> imprimir (cachorro)
cachorro
>>> T.select ('it')
>>> imprimir (cachorro) uma
bengala
>>> print (dog.format (n = 0))
sem cana
>>> print (dog.format (n = 1)) com
cana
>>> print (dog.format (n = 5))
5 cani
>>> print ( dog.format (n = 20))
tantissimi cani
``


A cadeia pode conter vários espaços reservados, mas o espaço reservado {n} é especial porque
a variável chamada "n" é usada para determinar a pluralização pela melhor correspondência (chave máxima de ditado <= n )


Objetos T (...) podem ser adicionados entre si e com uma sequência, como seqüências regulares.


T.select (s) pode analisar uma string s seguindo o formato do idioma de aceitação HTTP.


### Atualize os arquivos de tradução


Encontre todas as strings envolvidas em T (...) nos arquivos .py, .html e .js:
``
correspondências = T.find_matches ('caminho / para / app / pasta')
``


Adicione entradas recém-descobertas em todos os idiomas suportados
``
T.update_languages ​​(correspondências)
``


Adicione um novo idioma suportado (por exemplo, alemão, "de")


``
T.languages ​​['de'] = {}
``


Verifique se todos idiomas contêm as mesmas expressões de origem
``
expressões_conhecidas = set ()
para idioma em T.languages.values ​​():
    para expressão em idioma:
        expressões_expressivas.add (expressão) expressões_update_languages ​​(expressões_expressões
))
``


Por fim, salve as alterações:


` `
T.save ('traduções')
` `