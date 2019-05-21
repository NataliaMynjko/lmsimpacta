# lmsimpacta

Nesta Tarefa vocês farão modificações no Modelo Curso do projeto LMS apresentado em sala. seguem instruçoes de como proceder pra realização da AC.

- Clone o o código do respositório do Projeto (link em anexo)

- instale as depencias do projeto com o aplicativo pip (como realizado em aula)

- dentro da pasta referente ao app curriculo, substitua os arquivos:
-- models/cursos.py
-- admin.py
-- templates/curriculo/curso.html
-- views.py
pelos arquivos fornecidos em anexo com o mesmo nome.

- Faça as migrações necessárias, e em seguida aplique as migrações para criar todas as tabelas no banco de dados.

- Crie um usuário administrador com o comando: manage.py createsuperuser

- acesse o sistema através do navegador no endereço: localhost:8000

- clique ementrar no canto superior direito e entre com o login e senha cadastrados no passo anterior

- use a ferramenta do administrador para criar algumas disciplinas

-use a ferrmenta do adminstrado para criar alguns cursos

- Após criar os cursos, visite a página de cada um deles em: localhost:8000/cursos/<sigla-curso>, onde <sigla-curso> é a sigla de cada curso que você criou

- Você irá notar que a página do curso será exibida com vários campos em branco. Sua tarefa é criar no modelo Curso os campos necessário para a vizualização correta das páginas.

- Você deverá criar os campos:
-- semestres: Um campo de número inteiro, com valor default de 4
-- descricao: Um campo de texto (Não um campo CharField, um campo de Texto), com blank=True

- Criem as migrações para as alterações

- Vejam o resultado nas páginas das disciplinas ( Se quiserem ver os resultados, podem atualizar os cursos já criados para terem valores novos nos campos: "semestres" e "descricao", utilizem a ferramenta do administrador para isso)

- Vocês notarão que a matriz curricular dos cursos ainda não está sendo exibida. Para que ela seja exibida, vá no arquivo views.py do app curriculos e altere o valor de 'matriz' dentro de context, para ser o resultado do método monta matriz. Entre nas páginas das disciplinas e veja o resultado

- Entregue no Classroom somente seu arquivo cursos.py modificado, não esqueça de colocar os emails da dupla na variável __alunos__ (como feito em todas as AC's anteriores)

Bom Trabalho

