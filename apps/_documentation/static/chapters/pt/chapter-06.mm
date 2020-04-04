## O RESTAPI


Desde a versão 19.5.10, o PyDAL inclui uma API repousante chamada RestAPI. Ele é inspirado no GraphQL, mas não é o mesmo porque é menos poderoso, mas, no espírito do web2py, é mais prático e mais fácil de usar.
Como o GraphSQL, o RestAPI permite que um cliente consulte informações usando o método GET e permite especificar alguns detalhes sobre o formato da resposta (que referências a serem seguidas e como desnormalizar os dados). Diferentemente do GraphSQL, ele permite ao servidor especificar uma política e restringir quais consultas são permitidas e quais não. Eles podem ser avaliados dinamicamente por solicitação, com base no usuário e no estado do servidor.
Como o nome implícito, RestAPI permite todos os métodos stardard GET, POST, PUT e DELETE. Cada um deles pode ser ativado ou desativado com base na política, para tabelas e campos individuais.


Nos exemplos abaixo, assumimos um aplicativo chamado "super-heróis" e o seguinte modelo:


``
db.define_table (
    'person',
    Field ('name'),name'),
    Field ('Field ('job'))


db.define_table (
    'superhero',
    Field ('name'),
    Field ('real_identity', 'reference person'))


db.define_table (
    'superpower',
    Field ('description'))


db.define_table (
    'tag',
    Field ('superhero', 'reference superhero '),
    Field (' superpower ',' reference superpower '),
    Field (' Strength ',' integer '))
``


Também assumimos o seguinte controlador `` rest.py``:


``
from pydal.dbapi import RestAPI , Policy


policy = Policy ()
policy.set ('super-herói', 'GET', autorize = True, allowed_patterns = ['*'])
policy.set ('*', 'GET', autorize = True, allowed_patterns = [ '*'])
policy.set ('*', 'PUT', autorize = False)
policy.set ('*', 'POST', autorize = False)
policy.set ('*', 'DELETE', autorize = False)


@action ('api / <tablename> /')
@action ('api / <tablename> / <rec_id>')
def api (tablename, rec_id = None):
    retorna RestAPI (db, policy) (request. método, 
                               tablename, 
                               rec_id,
                               request.GET, 
                               request.POST
                               )
``


O pol gelado é por tabela (ou * para todas as tabelas e por método. authorize pode ser True (permitir), False (negar) ou uma função com a assinatura (método, nome da tabela, record_id, get_vars, post_vars) que retorna True / False. Para a política GET, pode-se especificar uma lista de padrões de consulta permitidos (* para todos). Um padrão de consulta será comparado com as chaves na string de consulta.


A ação acima é exposta como:


``
/ superheroes / rest / api / {tablename}
`` `    


Em nossa política de exemplo, desabilitamos todos os métodos, exceto GET.


#### RestAPI GET




A consulta geral tem o formato `` {something} .eq = value`` onde `` eq = `` significa "equal", `` gt = `` significa "maior que", etc A expressão pode ser anexada com `` não ''. 


`` {something} `` pode ser o nome de um campo na tabela que foi consultado como em:


** Todos os super-heróis chamados "Super-Homem" **
``
/superheroes/rest/api/superhero?name.eq=Superman
``


Pode ser o nome de um campo de uma tabela referida pela tabela e consultado como:


** Todos os super-heróis com identidade real "Clark Kent" **
``
/superheroes/rest/api/superhero?real_identity.name.eq = Clark Kent
``


Pode ser o nome de um campo de uma tabela que se refere à tabela consultada como em:


** Todos os super-heróis com qualquer tag superpower com força> 90 **
``
/ superheroes / rest / api / superhero ? superhero.tag.strength.gt = 90
``


(aqui tag é o nome da tabela de links, o `` superhero`` anterior é o nome do campo que se refere à tabela selecionada e `` força`` é o nome do campo usado para filtrar)


Também pode ser um campo da tabela referenciada por uma tabela vinculada muitos-para-muitos como em:


** Todos os super-heróis com poder de vôo **
``
/ superheroes / rest / api / superhero ? superhero.tag.superpower.description.eq = Vôo
``


A chave t o entender que a sintaxe acima é quebrá-la da seguinte forma:


``
superhero? superhero.tag.superpower.description.eq = Flight
''


e leia-a como:


--------
selecione registros da tabela ** superhero * * referido pelo campo ** superhero ** da tabela ** tag ** quando o campo ** superpower ** da referida tabela aponta para um registro com ** description ** ** eq ** ual para "Flight".
---------


A consulta permite modificadores adicionais, por exemplo,
``
@ offest = 10
@ limit = 10
@ order = name
@ model = true
@ lookup = real_identity
``


Os três primeiros são óbvios. @model retorna uma descrição JSON do modelo de banco de dados.
A pesquisa desnormaliza o campo vinculado.


Aqui estão alguns exemplos práticos:


URL:
`` / superheroes / rest / api / superhero``


SAÍDA:
``
{
    "count": 3,
    "status": "success",
    "code": 200,
    "items": [
        {
            "real_identity": 1,
            "nome": "Super-homem",
            "id": 1
        },
        {
            "real_identity": 2,
            "nome": "Homem-Aranha",
            "id": 2
        },
        {
            "real_identity": 3 ,
            "name": "Batman",
            "id": 3
        }
    ],
    "timestamp": "2019-05-19T05: 38: 00.132635",
    "api_version": "0.1"
}
``


URL:
``
/ superheroes / rest / api / superhero? @ model = true
``


SAÍDA:
``
{
    "count": 3,
    "status": "success",
    "code": 200,
    "items": [
        {
            "real_identity": 1,
            " nome ":" Super-homem ",
            " id ": 1
        },
        {
            " real_identity ": 2,
            " nome ":" Homem-Aranha ",
            " id ": 2
        },
        {
            " real_identity ": 3,
            " nome ":" Batman " ,
            "id": 3
        }
    ],
    "timestamp": "2019-05-19T05: 38: 00.098292",
    "model": [
        {
            "regex": "[1-9] \\ d *",
            "name" : "id",
            "padrão": nulo,
            "obrigatório": false,
            "label": "Id",
            "post_writable": true,
            "referenced_by": [],
            "exclusivo": false,
            "type": "id ",
            " options ": null,
            " put_writable ": true
        },
        {
            " regex ": null,
            " name ":" name ",
            " default ": null,
            " required ": false,
            " label ":" Nam e ",
            " post_writable ": true,
            " unique ": false,
            " type ":" string ",
            " options ": null,
            " put_writable ": true
        },
        {
            " regex ": null,
            " name ":" real_identity " ,
            "padrão": nulo,
            "obrigatório": falso,
            "rótulo": "Identidade real",
            "post_writable": true,
            "referências": "pessoa",
            "exclusivo": falso,
            "tipo": "referência",
            "opções": null,
            "put_writable": true
        }
    ],
    "api_version": "0.1"
}
``


URL:
``
/ superheroes / rest / api / superhero? @ lookup = real_identity
``


SAÍDA:
``
{
    "count ": 3,
    " status ":" success ",
    " code ": 200,
    " items ": [
        {
            " real_identity ": {
                " name ":" Clark Kent ",
                " job ":" Journalist ",
                " id ": 1
            },
            "nome": "Super-homem",
            "id": 1
        },
        {
            "real_identity": {
                "nome": "Peter Park",
                "trabalho": "Fotógrafo",
                "id": 2
            },
            "nome ":" Homem-Aranha ",
            " id ": 2
        },
        {
            " real_identity ": {
                " name ":" Bruce Wayne ",
                " job ":" CEO ",
                " id ": 3
            },
            " name ":" Batman " ,
            "id": 3
        }
    ],
    "timestamp": "2019-05-19T05: 38: 00.178974",
    "api_version": "0.1"
}
``


URL:
``
/ superheroes / rest / api / superhero? @lookup = identity: real_identity
``


(desnormalize a real_identity e renomeie-a i dentidade)


SAÍDA:
``
{
    "contar": 3,
    "status": "sucesso",
    "code": 200,
    "itens":
        [{
            "real_identity": 1,
            "nome": "Superman",
            "id" : 1,
            "identity": {
                "name": "Clark Kent",
                "job": "Journalist",
                "id": 1
            }
        },
        {
            "real_identity": 2,
            "name": "Spiderman",
            "id ": 2,
            " identity ": {
                " name ":" Peter Park ",
                " job ":" Photographer ",
                " id ": 2
            }
        },
        {
            " real_identity ": 3,
            " name ":" Batman ",
            " id ": 3,
            " identity ": {
                " name ":" Bruce Wayne ",
                " job ":" CEO ",
                " id ": 3
            }
        }
    ],
    " timestamp ":" 2019-05-19T05: 38: 00.123218 ",
    " api_version ":" 0.1 "
}
` `


URL:
` `
/ superheroes / rest / api / superhero? @ lookup = identity!: real_identity [nome, trabalho]
` `


(desnormalize a real_identity [mas apenas campos nome e trabalho ], reduza o prefixo de identidade)


SAÍDA:
``
{
    "count": 3,
    "status": "success",
    "code": 200,
    "items": [
        {
            "name": "Superman",
            "identity_job ":" Jornalista ",
            " identity_name ":" Clark Kent ",
            " id ": 1
        },
        {
            " name ":" Homem-Aranha ",
            " identity_job ":" Fotógrafo ",
            " identity_name ":" Peter Park ",
            " id ": 2
        },
        {
            " name ":" Batman ",
            " identity_job ":" CEO ",
            " identity_name ":" Bruce Wayne ",
            " id ": 3
        }
    ],
    " timestamp ":" 2019-05-19T05: 38: 00.192180 ",
    " api_version ":" 0.1 "
}
` `


URL:
` `
/ superheroes / rest /api/superhero?@lookup=superhero.tag
``


SAÍDA:
``
{
    "count": 3,
    "status": "success",
    "code": 200,
    "items": [
        {
            "real_identity": 1,
            "nome": "Super-homem",
            "super-herói.tag": [
                {
                    "força": 100,
                    "super-herói": 1,
                    "id": 1,
                    "super-poder": 1
                },
                {
                    "força": 100,
                    "super-herói ": 1,
                    " id ": 2,
                    " superpotência ": 2
                },
                {
                    " força ": 100,
                    " super-herói ": 1,
                    " id ": 3,
                    " superpotência ": 3
                },
                {
                    " força ": 100,
                    "super-herói": 1,
                    "id": 4,
                    "superpotência": 4
                }
            ],
            "id": 1
        },
        {
            "real_identity": 2,
            "nome": "Homem-Aranha",
            "superhero.tag": [
                {
                    "força": 50,
                    "super-herói": 2,
                    "id": 5,
                    "superpotência": 2
                },
                {
                    "força": 75,
                    "super-herói": 2,
                    "id": 6,
                    "superpotência": 3
                } ,
                {
                    "força": 10,
                    "super-herói": 2,
                    "id": 7,
                    "superpotência": 4
                }
            ],
            "id": 2
        },
        {
            "real_identity": 3,
            "nome": "Batman",
            "superhero.tag": [
                {
                    "força": 80,
                    "super-herói": 3,
                    "id": 8,
                    "superpotência": 2
                },
                {
                    "força": 20,
                    "super-herói": 3,
                    "id": 9
                    " superpotência ": 3
                },
                {
                    " força ": 70,
                    " super-herói ": 3,
                    " id ": 10,
                    " superpotência ": 4
                }
            ],
            " id ": 3
        }
    ],
    " timestamp ":" 2019-05- 19T05: 38: 00.201988 ",
    " api_version ":" 0.1 "
}
` `


URL:
` `/
superheroes/rest/api/superhero?@lookup=superhero.tag.superpower`
`


SAÍDA:
` `
{
    " count ": 3 ,
    "status": "success",
    "code": 200,
    "items": [
        {
            "real_identity": 1,
            "name": "Superman",
            "superhero.tag.superpower": [
                {
                    "Strength": 100 ,
                    "superhero": 1,
                    "id": 1,
                    "superpower": {
                        "id": 1,
                        "description": "Flight"
                    }
                },
                {
                    "Strength": 100,
                    "superhero": 1,
                    "id" : 2,
                    "superpotência": {
                        "id": 2,
                        "descrição": "Força"
                    }
                },
                {
                    "força": 100,
                    "super-herói": 1,
                    "id": 3,
                    "superpotência": {
                        "id ": 3,
                        " descrição ":" Velocidade "
                    }
                },
                {
                    " força ": 100,
                    " super-herói ": 1,
                    " id ": 4,
                    " superpotência ": {
                        " id ": 4,
                        " descrição ":" Durabilidade "
                    }
                }
            ],
            " id ": 1
        },
        {
            " real_identity ": 2,
            " name ":" Spiderman ",
            " superhero.tag.superpower ": [
                {
                    " Strength ": 50,
                    " superhero ": 2,
                    " id ": 5,
                    " superpotência ": {
                        " id ": 2,
                        " descrição ":" Força "
                    }
                },
                {
                    " força ": 75,
                    " super-herói ": 2,
                    " id ": 6,
                    " superpotência ": {
                        " id ": 3,
                        " descrição ":" Velocidade "
                    }
                },
                {
                    " força ": 10,
                    " super-herói ": 2,
                    " id ": 7,
                    " superpotência ": {
                        "id": 4,
                        "descrição": "Durabilidade"
                    }
                }
            ],
            "id": 2
        },
        {
            "real_identity": 3,
            "name": "Batman",
            "superhero.tag.superpower": [
                {
                    " força ": 80,
                    " super-herói ": 3,
                    " id ": 8,
                    " superpotência ": {
                        " id ": 2,
                        " descrição ":" Força "
                    }
                },
                {
                    " força ": 20,
                    " super-herói ": 3 ,
                    "id": 9,
                    "superpotência": {
                        "id": 3,
                        "descrição": "Velocidade"
                    }
                },
                {
                    "força": 70,
                    "super-herói": 3,
                    "id": 10,
                    "superpotência" : {
                        "id": 4,
                        "description": "Durability"
                    }
                }
            ],
            "id": 3
        }
    ],
    "timestamp": "2019-05-19T05: 38: 00.322494",
    "api_version": "0.1"
}
``


URL:
``
/superheroes/rest/api/superhero?@lookup=powers:superhero.tag[strength}.superpower[description]
``


SAÍDA:
``
{
    "count": 3,
    "status": " success ",
    " code ": 200,
    " items ": [
        {
            " real_identity ": 1,
            " name ":" Superman ",
            " powers ": [
                {
                    " Strength ": 100,
                    " superpower ": {
                        " description ": "Vôo"
                    }
                },
                {
                    "força": 100,
                    "superpotência": {
                        "descrição": "Força"
                    }
                },
                {
                    "força": 100,
                    "superpotência": {
                        "descrição": "Velocidade"
                    }
                },
                {
                    "força": 100,
                    "superpotência": {
                        "descrição": "Durabilidade"
                    }
                }
            ],
            "id": 1
        },
        {
            "real_identity ": 2,
            " name ":" Homem-Aranha ",
            " poderes ": [
                {
                    " força ": 50,
                    " superpotência ": {
                        " descrição ":" Força "
                    }
                },
                {
                    " força ": 75,
                    " superpotência ": {
                        "description": "Speed"
                    }
                },
                {
                    "Strength": 10,
                    "Superpower": {
                        "description": "Durability"
                    }
                }
            ],
            "id": 2
        },
        {
            "real_identity": 3,
            "name ":" Batman ",
            " poderes ": [
                {
                    " força ": 80,
                    " superpotência ": {
                        " descrição ":" Força "
                    }
                },
                {
                    " força ": 20,
                    " superpotência ": {
                        " descrição ":" Velocidade "
                    }
                },
                {
                    " força ": 70,
                    " superpotência ": {
                        " descrição ":" Durabilidade "
                    }
                }
            ],
            " id ": 3
        }
    ],
    " registro de data e hora ":" 2019-05-19T05: 38: 00.309903 ",
    " api_version ":" 0.1 "
}
` `


URL:
` `
/superheroes/rest/api/superhero?@lookup=powers!:superhero.tag[strength.superpower[description]
` `


SAÍDA:
` `
{{
    " contagem ": 3,
    " status ":" sucesso ",
    " código ": 200,
    " itens ": [
        {
            " real_identity ": 1,
            " nome ":" Super-homem ",
            " poderes ": [
                {
                    " força ": 100 ,
                    "description": "Flight"
                },
                {
                    "força": 100,
                    "descrição": "Força"
                },
                {
                    "força": 100,
                    "descrição": "Velocidade"
                },
                {
                    "força": 100,
                    "descrição": "Durabilidade"
                }
            ],
            "id ": 1
        },
        {
            " real_identity ": 2,
            " name ":" Spiderman ",
            " powers ": [
                {
                    " força ": 50,
                    " descrição ":" Força "
                },
                {
                    " força ": 75,
                    " descrição ":" Velocidade "
                },
                {
                    " força ": 10,
                    " descrição ":" Durabilidade "
                }
            ],
            " id ": 2
        },
        {
            " real_identity ": 3,
            " nome ":" Batman ",
            " poderes ": [
                {
                    "força": 80,
                    "descrição": "Força"
                },
                {
                    "força": 20,
                    "descrição": "Velocidade"
                },
                {
                    "força": 70,
                    "descrição": "Durabilidade"
                }
            ],
            "id": 3
        }
    ],
    "timestamp": "2019-05-19T05: 38: 00.355181",
    "api_version": "0.1"
}
``


URL:
``
/ superheroes / rest / api / superhero? @ lookup = poderes!: superhero.tag [força] .superpotência [descrição], identidade!: real_identity [nome]
``


SAÍDA:
``
{
    "count": 3,
    "status": "success",
    "code": 200,
    " items ": [
        {
            " name ":" Superman ",
            " identity_name ":" Clark Kent ",
            " powers ": [
                {
                    " Strength ": 100,
                    " description ":" Flight "
                },
                {
                    " Strength ": 100,
                    "description": "Força "
                },
                {
                    " força ": 100,
                    " descrição ":" Velocidade "
                },
                {
                    " força ": 100,
                    " descrição ":" Durabilidade "
                }
            ],
            " id ": 1
        },
        {
            " nome ":" Homem-Aranha ",
            " identity_name ":" Peter Park ",
            " poderes ": [
                {
                    " força ": 50,
                    " descrição ":" Força "
                },
                {
                    " força ": 75,
                    " descrição ":" Velocidade "
                },
                {
                    " força ": 10,
                    " descrição ":" Durabilidade "
                }
            ],
            " id ": 2
        },
        {
            " name ":" Batman ",
            " identity_name ":" Bruce Wayne ",
            " poderes ": [
                {
                    " força ": 80,
                    "descrição": "Força"
                },
                {
                    "força": 20,
                    "descrição": "Velocidade"
                },
                {
                    "força": 70,
                    "descrição": "Durabilidade"
                }
            ],
            "id": 3
        }
    ],
    "timestamp": "2019-05-19T05: 38: 00.396583",
    "api_version": "0.1"
}
``


URL:
``
/superheroes/rest/api/superhero?name.eq=Superman
``


SAÍDA:
``
{
    "count": 1,
    "status": "success",
    "code": 200,
    "items": [
        {
            "real_identity": 1,
            "name": "Superman",
            "id": 1
        }
    ] ,
    "timestamp": "2019-05-19T05: 38: 00.405515",
    "api_version": "0.1"
}
``


URL:
``
/superheroes/rest/api/superhero?real_identity.name.eq=Clark Kent
``


SAÍDA:
``
{
    "count": 1,
    "status": "success",
    "cod e ": 200,
    " items ": [
        {
            " real_identity ": 1,
            " name ":" Superman ",
            " id ": 1
        }
    ],
    " timestamp ":" 2019-05-19T05: 38: 00.366288 ",
    " api_version ":" 0.1 "
}
` `


URL:
` `
/superheroes/rest/api/superhero?not.real_identity.name.eq=Clark Kent`
`


SAÍDA:
` `
{
    " count ": 2,
    " status ":" success ",
    " code ": 200,
    " items ": [
        {
            " real_identity ": 2,
            " name ":" Spiderman ",
            " id ": 2
        },
        {
            " real_identity ": 3,
            " name ":" Batman " ,
            "id": 3
        }
    ],
    "timestamp": "2019-05-19T05: 38: 00.451907",
    "api_version": "0.1"
}
``


URL:
``
/ superheroes / rest / api / superhero? superhero. tag.superpower.description = Voo
``


SAÍDA:
``
{
    "count": 1,
    "status": "success",
    "code": 200,
    "items": [
        {
            "real_identity": 1,
            "name": "Superman",
            "id": 1
        }
    ],
    "timestamp": "2019-05-19T05: 38: 00.453020",
    "api_version": "0.1"
}
``


Observe todas as respostas RestAPI com os campos


``
{
    "api_version ": ...
    " timestamp ": ...
    " status ": ...    
    " code ": ...
}
` `


e alguns campos opcionais:


` `
{
    " count ": ... (correspondência total, não total retornado, para GET)
    "itens": ... (em resposta a um GET)
    "erros ": ... (geralmente erro de validação0
    " modelos ": ... (geralmente se status! = sucesso)
    " message ": ... (is if error)
}
` `


As especificações exatas estão sujeitas a alterações, pois esta é uma novo recurso.