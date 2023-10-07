# trab_inf1407
Objetivo: Criar um website que satisfaça as operações básicas de desenvolvimento de uma aplicação (CRUD). Um usuário pode se cadastrar no site e criar uma lista de jogos de sua coleção, sendo um conceito similar a sites como "MyAnimeList" e outros, servindo apenas como forma de anotação e consulta de um ou mais usuários sobre um "produto" já consumido.

Erros: 
1-Após o usuário editar seu perfil, a url não será "inicio/pk", assim operações como adicionar e retirar jogos a sua biblioteca e  deletar jogos da existência(caso for administrador) não irão funcionar.
2-Senhas não tem as restrições de tipo de carácter necessário. Característica comum em maioria das aplicações web.
3-No código ainda há código legado referente a um modelo/classe "Adm" que deverá ser retirado.
4-O tratamento de login não está perfeito, pois ele apenas confere se existe um usuário com o nome e senha fornecido, não exatamente se são o mesmo usuário.
5- No cadastro de jogos falta retratar a realidade que mesmo que usem "caixa alta" nomes e senhas ainda podem ser basicamente as mesmas. exemplo: "P5" e "p5" são tratados como diferentes, mesmo que no contexto de jogos sejam basicamente o mesmo.


Observação: Se um usuário não "administrador" tentar deletar um jogo, irá retornar uma tela branca informando sobre a realidade da operação, é um resultado planejado.
