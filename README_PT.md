# Conversor de NFC-e para NF-e

Uma aplicação web leve projetada para converter arquivos XML de **NFC-e (Nota Fiscal de Consumidor Eletrônica)** para o formato XML de **NF-e (Nota Fiscal Eletrônica)**. Construída com Python e Flask, esta ferramenta oferece uma interface direta para transformação de dados e demonstrações educacionais.

## ⚠️ Aviso Importante

Este software é fornecido apenas para **fins educacionais e demonstrativos**. Os arquivos XML convertidos não devem ser utilizados para envios fiscais oficiais sem as devidas validações e conformidade com as normas da Receita Federal. Utilize por sua própria conta e risco.

## Pré-requisitos

- **Python 3.7** ou superior
- **pip** (instalador de pacotes do Python)

## Instalação e Configuração

Siga estes passos para configurar o projeto localmente:

1. **Clonar o Repositório**
   bash
   git clone https://github.com/dougdotcon/converte-nfce-for-nfe.git
   cd converte-nfce-for-nfe
   

2. **Instalar Dependências**
   Instale as bibliotecas Python necessárias utilizando o arquivo `requirements.txt`:
   bash
   pip install -r requirements.txt
   

## Uso

1. **Iniciar a Aplicação**
   Inicie o servidor Flask executando o script principal:
   bash
   python app.py
   
   O terminal exibirá uma URL local (geralmente `http://127.0.0.1:5000`).

2. **Abrir no Navegador**
   Acesse a URL fornecida no seu navegador web.

3. **Converter Arquivos**
   - Clique no botão **"Procurar"**.
   - Selecione o arquivo `.xml` de origem contendo os dados da NFC-e.
   - Clique em **Enviar/Converter**.

4. **Obter Resultado**
   A aplicação processará o arquivo e baixará o arquivo convertido com o nome **`nfe_convertida.xml`** para sua máquina local.

## Estrutura do Projeto

- `app.py`: Lógica principal da aplicação Flask e rotas.
- `templates/`: Contém os arquivos HTML para a interface do usuário.
- `requirements.txt`: Lista de dependências Python (Flask, lxml, requests).

## Contribuição

Contribuições são bem-vindas! Siga este processo:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/melhoria`).
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Envie para a branch (`git push origin feature/melhoria`).
5. Abra um Pull Request.

## Contato

**Autor:** Douglas H. Machado  
**Email:** [dougdotcon@gmail.com](mailto:dougdotcon@gmail.com)  
**LinkedIn:** [dougdoton](https://www.linkedin.com/in/dougdoton/)  
**GitHub:** [dougdotcon](https://github.com/dougdotcon)
