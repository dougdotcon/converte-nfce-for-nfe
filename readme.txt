Conversor de NFC-e para NF-e
Este aplicativo é uma ferramenta simples para converter arquivos XML de Notas Fiscais de Consumidor Eletrônicas (NFC-e) em arquivos XML de Notas Fiscais Eletrônicas (NF-e).

Requisitos

Python 3.7 ou superior
Bibliotecas Python: Flask, lxml e requests

Instalação

Clone o repositório ou baixe os arquivos para seu computador.
Navegue até a pasta do projeto usando o terminal ou prompt de comando.

Execute o seguinte comando para instalar as bibliotecas necessárias:

pip install -r requirements.txt

Uso

Execute o arquivo app.py:

python app.py

A interface gráfica do aplicativo será aberta.
Clique no botão "Procurar" e selecione o arquivo XML da NFC-e que deseja converter.
O aplicativo enviará a requisição para converter o arquivo e, em seguida, salvará o arquivo XML convertido como nfe_convertida.xml na mesma pasta do projeto.

Observações
Este aplicativo foi desenvolvido para fins educacionais e demonstrativos, e pode não ser adequado para uso em produção. Verifique se o arquivo XML convertido atende aos requisitos e especificações exigidos antes de usá-lo para fins oficiais.