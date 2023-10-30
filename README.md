# MatchJobs

MatchJobs é uma ferramenta desenvolvida para facilitar os profissionais da área de tecnologia a encontrar a vaga que mais combina com eles. O projeto foi criado com a intenção de ser facilmente reaproveitado e editado, permitindo a inserção de mais áreas, perguntas e respostas. Além disso, o projeto agora inclui uma interface gráfica do usuário para facilitar a interação.

## Estrutura do Projeto

O projeto é organizado nas seguintes pastas:

- `src`: Contém todos os scripts Python do projeto.
- `data`: Armazena o arquivo CSV com as respostas.

Os scripts Python incluem:

- `areas.py`: Define a classe Areas.
- `data.py`: Contém a classe Data para exportar os resultados.
- `interview.py`: Define a classe Interview para realizar a entrevista.
- `questions.py`: Define a classe Questions para lidar com as perguntas.
- `utils_interview.py`: Define a classe Utils para verificar as respostas e calcular os resultados.
- `main.py`: É o script principal que executa o programa e cria a interface gráfica do usuário.

## Como Usar

1. Clone o repositório.
2. Navegue até o diretório do projeto.
3. Execute o script principal com o comando: `python main.py`.
4. Uma janela será aberta. Insira seu nome na caixa de texto e clique em "OK".
5. Responda às perguntas selecionando uma das opções disponíveis e clique em "Próximo" para ir para a próxima pergunta.
6. Quando todas as perguntas forem respondidas, os resultados serão exportados para um arquivo CSV na pasta 'data'.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob os termos da licença MIT.
