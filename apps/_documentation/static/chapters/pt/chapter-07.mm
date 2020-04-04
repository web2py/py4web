## YATL Template Language


`` views``: inxx `` template language``: inxx `` HTML``: inxx


py4web usa Python para seus modelos, controladores e visualizações, embora use uma sintaxe Python ligeiramente modificada nas visualizações para permitir código mais legível sem impor restrições ao uso adequado do Python.


py4web usa `` [[...]] `` para escapar do código Python incorporado no HTML. A vantagem de usar colchetes em vez de colchetes é que é transparente para todos os editores de HTML comuns. Isso permite que o desenvolvedor use esses editores para criar visualizações py4web.


Como o desenvolvedor está incorporando o código Python no HTML, o documento deve ser recuado de acordo com as regras HTML, e não as regras do Python. Portanto, permitimos Python sem recuo dentro das tags `` [[...]] ``. Como o Python normalmente usa indentação para delimitar blocos de código, precisamos de uma maneira diferente de delimitá-los; é por isso que a linguagem de modelo py4web usa a palavra-chave Python `` pass``.


-------
Um bloco de código começa com uma linha que termina com dois pontos e termina com uma linha que começa com `` pass``. A palavra-chave `` pass`` não é necessária quando o final do bloco é óbvio a partir do contexto.
-------


Aqui está um exemplo:


``
[[
se i == 0:
response.write ('i is 0')
else:
response.write ('i is not 0')
pass
]]
'' : html


Observe que `` pass`` é uma palavra-chave Python, não uma palavra-chave py4web. Alguns editores de Python, como o Emacs, usam a palavra-chave `` pass`` para significar a divisão de blocos e a re-indentam o código automaticamente.


A linguagem do modelo py4web faz exatamente o mesmo. Quando encontra algo como:


``
<html> <body>
[[para x no intervalo (10):]] [[= x]] olá <br /> [[pass]]
</body> </html>
``: html


o converte em um programa:
``
response.write ("" "<html> <body>" "", escape = False)
para x no intervalo (10):
    response.write (x)
    response. write ("" "olá <br />" "", escape = False)
response.write ("" "</body> </html>" "", escape = False)
``: python
`` response.write `` escreve no `` response.body``.


Quando há um erro em uma exibição py4web, o relatório de erros mostra o código de exibição gerado, não a exibição real, conforme escrita pelo desenvolvedor. Isso ajuda o desenvolvedor a depurar o código, destacando o código real que é executado (que é algo que pode ser depurado com um editor de HTML ou o inspetor DOM do navegador).


Observe também que:
``
[[= x]]
``: html


gera
`` response.write``: inxx `` escape``: inxx
``
response.write (x)
``: python


Variáveis ​​injetadas no HTML dessa maneira, são escapados por padrão.
A saída é ignorada se `` x`` for um objeto `` XML``, mesmo se a saída estiver definida como `` True``.


Aqui está um exemplo que apresenta o auxiliar `` H1``:
``
[[= H1 (i)]]
``: html


que é traduzido para:
``
response.write (H1 (i))
``: python


upon Na avaliação, o objeto `` H1`` e seus componentes são serializados recursivamente, escapados e gravados no corpo da resposta. As tags geradas por `` H1`` e HTML interno não são escapadas. Esse mecanismo garante que todo o texto --- e somente texto --- exibido na página da web seja sempre escapado, evitando assim as vulnerabilidades do XSS. Ao mesmo tempo, o código é simples e fácil de depurar.


O método `` response.write (obj, escape = True) `` usa dois argumentos, o objeto a ser gravado e se ele precisa ser escapado (definido como `` True`` por padrão). Se `` obj`` tiver um método `` .xml () ``, ele será chamado e o resultado gravado no corpo da resposta (o argumento `` escape`` é ignorado). Caso contrário, ele usa o método `` __str__`` do objeto para serializá-lo e, se o argumento de escape for `` True``, o escapa. Todos os objetos auxiliares internos (`` H1`` no exemplo) são objetos que sabem como serializar-se por meio do método `` .xml () ``.


Tudo isso é feito de forma transparente. Você nunca precisa (e nunca deve) chamar o método `` response.write`` explicitamente.


### Sintaxe básica


A linguagem de modelo py4web suporta todas as estruturas de controle Python. Aqui nós fornecemos alguns exemplos de cada um deles. Eles podem ser aninhados de acordo com a prática de programação usual.


#### `` for ... in``
`` for``: inxx


Nos modelos, você pode fazer um loop sobre qualquer objeto iterável:
``
[[items = ['a', 'b', 'c']] ]
<ul>
[[para produto nos itens:]] <li> [[= item]] </ li> [[passar]]
</ ul>
``: HTML


que produz:
``
<UL>
<li> a </li>
<li> b </li>
<li> c </li>
</ul>
``: html


Aqui `` items`` é qualquer objeto iterável, como uma lista Python, tupla do Python ou Linhas objeto ou qualquer objeto implementado como um iterador. Os elementos exibidos são primeiro serializados e escapados.


#### `` while``
`` while``: inxx


Você pode criar um loop usando a palavra-chave while:
``
[[k = 3]]
<ul>
[[while k> 0:]] <li> [[= k]] [[k = k - 1]] </li> [[pass]]
</ul>
``: html


que produz:
``
<ul>
<li> 3 </li>
<li > 2 </li>
<li> 1 </li>
</ul>
``: html


#### `` if ... elif ... else``
`` if``: inxx `` elif` `: inxx` `else``: inxx


Você pode usar cláusulas condicionais:
` `
[[
import aleatório
k = random.randint (0, 100)
]]
<h2>
[[= k]]
[[se k% 2: ]] é ímpar [[else:]] é par [[pass]]
</h2>
``: html


que produz:
``
<h2>
45 é ímpar
</h2>
``: html


Como é óbvio que ` `else`` fecha o primeiro bloco` `if``, não há necessidade de uma declaração` `pass`` e o uso de uma estaria incorreto. No entanto, você deve fechar explicitamente o bloco `` else`` com um `` pass``.


Lembre-se de que no Python "else if" está escrito `` elif`` como no exemplo a seguir:
``
[[
import aleatório
k = random.randint (0, 100)
]]
<h2>
[[= k]]
[[ se k% 4 == 0:]] é divisível por 4
[[elif k% 2 == 0:]] é par
[[else:]] é ímpar
[[pass]]
</h2>
``: html


It produz:
``
<h2>
64 é divisível por 4
</h2>
``: html


#### `` tente ... exceto ... mais ... finalmente ...
`` tente`: ​​inxx `` except``: inxx `` else``: inxx `` finalmente``: inxx


Também é possível usar as instruções `` try ... except`` nas visualizações com uma ressalva. Considere o seguinte exemplo:
``
[[try:]]
Hello [[= 1/0]]
[[exceto:]]
divisão por zero
[[else:]]
nenhuma divisão por zero
[[finalmente:]]
<br / >
[[pass]]
``: html


Ele produzirá a seguinte saída:
``
Olá divisão por zero
<br />
``: html


Este exemplo ilustra que toda a saída gerada antes que uma exceção ocorra é renderizada (incluindo a saída que precedeu o exceção) dentro do bloco try. "Hello" é escrito porque precede a exceção.


#### `` def ... return``:
`` def``: inxx `` return``: inxx


A linguagem do modelo py4web permite ao desenvolvedor definir e implementar funções que podem retornar qualquer objeto Python ou um text / html corda. Aqui consideramos dois exemplos:
``
[[def itemize1 (link): retorna LI (A (link, _href = "http: //" + link))]]
<ul>
[[= itemize1 ('www.google. com ')]]
</ul>
``: html


produz a seguinte saída:
``
<ul>
<li> <a href="http:/www.google.com"> www.google.com </a> </li>
</ul>
``: html


A função `` itemize1`` retorna um objeto auxiliar que é inserido no local em que a função é chamada.


Agora, considere o seguinte código:
``
[[def itemize2 (link):]][[= link]]
<li> <a href="http://[[=link{""</a> </ li>
[[return]]
<ul>
[[itemize2 ('www.google.com')]]
</ul>
``: html


Produz exatamente a mesma saída que acima. Nesse caso, a função `` itemize2`` representa um pedaço de HTML que substituirá a tag py4web na qual a função é chamada. Observe que não há '=' na frente da chamada para `` itemize2``, pois a função não retorna o texto, mas a grava diretamente na resposta.


Há uma ressalva: as funções definidas em uma visualização devem terminar com uma declaração `` return``, ou a indentação automática falhará.