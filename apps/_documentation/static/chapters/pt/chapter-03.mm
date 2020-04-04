## Painel Faça


login no painel


<img src = "screenshots / dashboard_login.png" />


Clique no título de uma guia para expandir. As guias dependem do contexto. Por exemplo, abra a guia "Aplicativos instalados" e clique em um aplicativo instalado para selecioná-lo. Isso criará novas guias "Rotas", "Arquivado" e "Modelo" para o aplicativo selecionado.


<img src = "screenshots / dashboard_main.png" />


A guia "Arquivos" permite navegar pela pasta que contém o aplicativo selecionado e editar qualquer arquivo que o comporte. Se você editar um arquivo, clique em "Recarregar aplicativos" na guia "Aplicativos instalados" para que a alteração seja efetivada. Se um aplicativo falhar ao carregar, seu botão correspondente será exibido em vermelho. Clique nele para ver o erro correspondente.


<img src = "screenshots / dashboard_edit.png" />


O painel expõe o banco de dados de todos os aplicativos usando pydal RESTAPI. Ele também fornece uma interface da web para executar operações de pesquisa e CRUD.


<img src = "screenshots / dashboard_restapi.png" />


Se um usuário visitar um aplicativo e acionar um bug, ele emitiu um ticket.


<img src = "screenshots / dashboard_error.png" />


O ticket é registrado no banco de dados py4web. O Painel exibe os problemas recentes mais comuns e permite pesquisar tickets.


<img src = "screenshots / dashboard_ticket.png" />