# Projeto de Automação do WhatsApp Web

## Descrição
Este projeto é uma aplicação de automação do WhatsApp Web que utiliza o Selenium e o WebDriver do Microsoft Edge para interagir com o WhatsApp Web. O código automatiza várias tarefas, como enviar mensagens e anexos, ler mensagens não lidas e interagir com os contatos.

## Progresso Atual
- **Dia 2 de Desenvolvimento**
  - O código agora suporta a inicialização do driver do Edge com um perfil de usuário especificado, permitindo a persistência de sessões entre os lançamentos do navegador.
  - Implementação da funcionalidade de login via QR Code, com a captura e exibição do QR para autenticação manual.
  - Funções para enviar mensagens de texto e anexos para contatos específicos estão operacionais.
  - Capacidade de buscar e exibir mensagens não lidas, bem como recuperar o histórico de mensagens de conversas específicas.

## Tecnologias Utilizadas
- Python 3.8+
- Selenium 4
- WebDriver Manager
- Microsoft Edge WebDriver
- Matplotlib para visualização do QR Code
- Biblioteca `dotenv` para gerenciamento de variáveis de ambiente

## Configuração
1. Clone este repositório.
2. Instale as dependências necessárias usando `pip install -r requirements.txt` (assumindo que um arquivo de requisitos esteja presente).
3. Defina as variáveis de ambiente `PATH_TO_YOUR_EDGE_DRIVER` e `PATH_TO_YOUR_BROWSER_PROFILE_DIRECTORY` para configurar o caminho do driver e o diretório de perfil do usuário, respectivamente.

## Utilização
- Execute o script principal para iniciar a automação. A interface do usuário do WhatsApp Web será aberta, e o script aguardará que você escaneie o QR Code quando necessário.
- Use as funções disponíveis na classe `WhatsApp` para realizar várias operações, como enviar mensagens ou anexos.

## Contribuições
Contribuições são bem-vindas! Por favor, crie um pull request para propor melhorias ou adicionar novas funcionalidades.

## Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
