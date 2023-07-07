# Projeto_final_Redes_I
Projeto do terceiro crédito da disciplina de Redes I do curso de Ciência da Computação da Universidade Estadual de Santa Cruz (UESC).

## "Pedra, Papel, Tesoura, Lagarto, Spock"

### Descrição do Software
O software implementa o jogo "Pedra, Papel, Tesoura, Lagarto, Spock" no modelo cliente-servidor. É composto de duas partes: um programa cliente e um programa servidor. O cliente e o servidor se comunicam através de um socket UDP para trocar mensagens e jogar o jogo.

### Documentação do Protocolo da Camada de Aplicação

#### Eventos
- O cliente envia sua escolha para o servidor.
- O servidor recebe a escolha do cliente.
- O servidor gera sua própria escolha aleatoriamente.
- O servidor compara as escolhas do cliente e do servidor e determina o resultado.
- O servidor envia o resultado para o cliente.
- O cliente recebe o resultado do servidor.

#### Estados (Cliente)
- Estado Inicial: O cliente está pronto para fazer sua escolha.
- Estado Final: O resultado do jogo foi recebido pelo cliente.

#### Estados (Servidor)
- Estado Inicial: O servidor está esperando por conexões.
- Estado de Jogo: As escolhas do cliente e do servidor estão sendo comparadas para determinar o resultado.
- Estado Final: O resultado do jogo foi enviado para o cliente.

#### Mensagens
- Cliente para Servidor: O cliente envia sua escolha (representada por uma letra) para o servidor.
- Servidor para Cliente: O servidor envia o resultado do jogo para o cliente.

## Funcionamento do Software
Este é o funcionamento do software detalhado em passos:
1. O servidor é iniciado e fica aguardando por conexões.
2. O cliente se conecta ao servidor.
3. O cliente faz sua escolha entre as opções disponíveis: "Pedra (R)", "Papel (P)", "Tesoura (T)", "Lagarto (L)", "Spock (S)" ou "Q" para sair do jogo. 
4. O cliente envia sua escolha para o servidor.
5. O servidor recebe a escolha do cliente.
6. O servidor gera sua própria escolha aleatoriamente.
7. O servidor exibe a sua escolha e a do cliente.
8. O servidor compara as escolhas do cliente e do servidor para determinar o resultado do jogo.
9. O servidor envia o resultado para o cliente.
10. O cliente recebe o resultado e exibe-o na tela.
11. O jogo continua a partir do passo 3 até que o cliente digite Q.
12. Após o término do jogo, a pontuação do cliente e do servidor é exibida.


### Propósito do software
O propósito deste software é implementar o jogo "Pedra, Papel, Tesoura, Lagarto Spock" em uma arquitetura cliente-servidor. O jogo é baseado em algumas regras, onde o cliente escolhe entre as opções disponíveis (pedra-papel-tesoura, lagarto, Spock), e o servidor gera aleatoriamente suas próprias escolhas. O servidor compara as escolhas do cliente e do servidor para determinar o resultado do jogo. O objetivo é fornecer um jogo interativo que demonstre o uso da comunicação em rede e a implementação de um protocolo simples para troca de mensagens entre clientes e servidores.

### Motivação da Escolha do Protocolo de Transporte
Para este software, o protocolo de transporte escolhido foi o UDP porque o jogo não requer uma comunicação confiável, então a perda ocasional de pacotes não afetará significativamente a experiência do usuário. Além disso, o UDP é mais adequado para jogos em tempo real, pois oferece menor latência e overhead em comparação com o TCP, e a simplicidade desse protocolo permite que o jogo seja implementado de uma forma mais direta, sem precisar estabelecer e manter uma conexão persistente.

### Requisitos Mínimos de Funcionamento
- Conexão de rede entre o cliente e o servidor.
- A porta de rede utilizada pelo software (neste caso, a porta 12345) deve estar aberta e sem bloqueio por firewalls ou outros mecanismos de segurança.
- Python 3.x instalado.
- Entrada válida.

