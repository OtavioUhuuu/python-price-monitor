1. Preparação do Ambiente
Certifique-se de ter o Python instalado e instale as bibliotecas necessárias via terminal:

Bash

pip install requests beautifulsoup4
2. Configuração das Variáveis
No topo do código, você deve editar as seguintes informações:

URL_PRODUTO: Cole o link completo do produto do Mercado Livre entre aspas.

PRECO_DESEJADO: Insira o valor máximo que você aceita pagar (use ponto para decimais, ex: 145.50).

3. Execução
Salve o arquivo com a extensão .py (exemplo: monitor.py).

Abra o terminal ou prompt de comando na pasta do arquivo.

Execute o comando:

Bash

python monitor.py
4. Funcionamento
Monitoramento Silencioso: O script rodará em segundo plano.

Frequência: Ele checa o preço a cada 30 minutos (1800 segundos) para evitar que seu IP seja bloqueado pelo site.

Ação: Assim que o preço for igual ou menor que o desejado, o script abrirá automaticamente o link no seu navegador padrão e encerrará a execução.
