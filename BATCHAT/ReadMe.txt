BATCHAT

Descrição:

A aplicação desenvolvida em Python é uma plataforma de agenda online que oferece recursos como 
criação de salas para conversação entre usuários, adição e remoção de contatos, listagem da lista de
 contatos e interação com as salas criadas. A arquitetura cliente/servidor é adotada no sistema, 
 permitindo que múltiplos clientes se conectem ao servidor e interajam simultaneamente.

Abordagens de cada disciplina:

PIRC: Está envolvida na interação e comunicação entre o cliente e o servidor.O protocolo de transporte 
TCP/IP foi utilizado para garantir a confiabilidade na transmissão dos dados.Além disso, foi implementado
um protocolo de aplicação chamado BATCHAT,onde comandos enviados pelo cliente ao servidor recebem uma
resposta correspondente.

Estrutura de Dados: A disciplina de Estrutura de Dados é aplicada na lógica do código, incluindo 
tratamento de exceções, encapsulamento, criação de classes e o uso de estruturas de dados. Na aplicação,
são utilizadas duas Hashtable Encadeadas, uma Fila Encadeada, uma Árvore AVL e um list de Python.

Hashtable A: Armazena as conexões dos clientes, utilizando o IP/PORTA como chave e o socket associado 
como valor, permitindo a comunicação entre os usuários.
Hashtable B: Armazena as salas criadas pelos usuários, utilizando um código único como chave e o objeto 
Sala como valor.
Árvore AVL: Utilizada para verificar se um código de sala já existe, evitando duplicatas ao criar novas
salas e armazenar nela.
List de Python: Cada objeto Sala possui uma lista para armazenar os participantes.
Fila Encadeada: Armazena as ações dos clientes e exibe-as na tela do servidor, mantendo uma ordem de 
ações do mais antigo ao mais recente.


Sistemas Operacionais: A disciplina de Sistemas Operacionais é aplicada na funcionalidade do código, 
incluindo o uso de Threads para lidar com múltiplos clientes conectados simultaneamente, o uso de 
semáforos para controlar regiões críticas e o uso de sockets para estabelecer a comunicação entre 
cliente e servidor.

Threads: Utilizadas para permitir que vários clientes se conectem ao servidor simultaneamente, 
paralelizar métodos de recebimento de ações dos clientes e receber mensagens de várias pessoas ao mesmo
tempo em salas.
Semáforos: Utilizados para proteger regiões críticas, como o processo de cadastro de usuários, evitando
conflitos e garantindo a consistência dos dados.
Sockets: Responsáveis pela conexão entre cliente e servidor, permitindo a comunicação através do 
estabelecimento de IPs e portas para cada conexão.




