Backup Automático de Arquivos

Este script em Python realiza backups automáticos de uma pasta de origem para um diretório de destino, criando cópias com data e hora para organização e segurança.

Funcionalidades

Copia todo o conteúdo de uma pasta de origem para um diretório de destino.

Nomeia os backups com a data e hora da execução.

Exclui pastas de backup preexistentes antes de copiar novos arquivos.

Pode ser agendado para execução automática a cada 30 dias às 02:00.

Mantém o script rodando em loop, verificando quando executar o próximo backup.

Requisitos

Python 3 instalado.

Biblioteca schedule instalada (se for utilizar o agendamento).

Como Usar

Edite os caminhos no script para indicar a pasta de origem e a pasta de destino:

Execute o script:

O backup será criado imediatamente e salvo na pasta de destino com a data e hora no nome.

Para ativar o agendamento automático, descomente a seguinte linha no código:

O script rodará continuamente verificando se é hora de executar um novo backup.

Agendando o Script no Windows

O Agendador de Tarefas do Windows permite que você execute scripts automaticamente em horários específicos. Para agendar o seu script Python para rodar automaticamente, siga estas etapas:

Passo 1: Criar um arquivo .bat

Crie um arquivo de lote (batch file) para executar o script Python. Isso pode ser feito criando um arquivo .bat com o seguinte conteúdo:

Abra o Bloco de Notas (Notepad) e cole o seguinte código:

Importante: Substitua C:\caminho\para\seu\script pelo caminho onde o seu script backup.py está localizado.

Salve o arquivo como backup.bat.

Exemplo de Saída

Observação

Certifique-se de que o script tem permissão para acessar as pastas especificadas.

Se desejar interromper a execução do script, use Ctrl + C no terminal.

