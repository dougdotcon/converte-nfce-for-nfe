import requests
from flask import Flask, request, send_file
from lxml import etree
import tkinter as tk
from tkinter import filedialog
import threading

app = Flask(__name__)

# Funções e rotas existentes ...

def run_flask_app():
    app.run(debug=True, use_reloader=False, threaded=True)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos XML", "*.xml")])
    if file_path:
        send_request(file_path)

def create_gui():
    root = tk.Tk()
    root.title("Conversor NFC-e para NF-e")

    label = tk.Label(root, text="Selecione o arquivo NFC-e para converter:")
    label.pack(pady=10)

    browse_button = tk.Button(root, text="Procurar", command=browse_file)
    browse_button.pack()

    root.mainloop()

if __name__ == '__main__':
    # Iniciar o servidor Flask em segundo plano
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    # Iniciar a interface gráfica de usuário no processo principal
    create_gui()

def converter_nfce_para_nfe(xml_nfce):
    # Carregar o arquivo XML da NFC-e
    nfce = etree.fromstring(xml_nfce)

    # Localizar a tag <infNFe>
    inf_nfe = nfce.find(".//{*}infNFe")
    
    # Alterar o atributo Id da tag <infNFe>
    inf_nfe.attrib['Id'] = inf_nfe.attrib['Id'].replace('NFC', 'NFE')

    # Alterar o atributo versao da tag <infNFe>
    inf_nfe.attrib['versao'] = '4.00'

    # Alterar a tag <tpEmis> dentro da tag <ide>
    tp_emis = nfce.find(".//{*}ide/{*}tpEmis")
    tp_emis.text = '1'

    # Remover ou alterar outras tags específicas da NFC-e
    tags_para_remover = ['tpImp', 'tpAmb', 'finNFe', 'indFinal']
    for tag in tags_para_remover:
        elemento = nfce.find(f".//{{*}}{tag}")
        if elemento is not None:
            elemento.getparent().remove(elemento)

    # Converter o XML alterado de volta para string
    xml_nfe = etree.tostring(nfce, encoding="utf-8", xml_declaration=True).decode("utf-8")

    return xml_nfe

@app.route('/converter', methods=['POST'])
def converter():
    arquivo_xml = request.files['xml']
    conteudo_xml = arquivo_xml.read()
    
    xml_convertido = converter_nfce_para_nfe(conteudo_xml)
    
    return send_file(xml_convertido, mimetype='application/xml', as_attachment=True, attachment_filename='nfe_convertida.xml')

def send_request(file_path):
    url = 'http://localhost:5000/converter'
    files = {'xml': open(file_path, 'rb')}

    response = requests.post(url, files=files)

    with open('nfe_convertida.xml', 'wb') as f:
        f.write(response.content)

    print('Arquivo XML convertido salvo como nfe_convertida.xml')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

    # Altere 'caminho/para/arquivo_nfce.xml' pelo caminho do arquivo XML da NFC-e que você deseja converter
    send_request('caminho/para/arquivo_nfce.xml')
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos XML", "*.xml")])
    if file_path:
        send_request(file_path)

def create_gui():
    root = tk.Tk()
    root.title("Conversor NFC-e para NF-e")

    label = tk.Label(root, text="Selecione o arquivo NFC-e para converter:")
    label.pack(pady=10)

    browse_button = tk.Button(root, text="Procurar", command=browse_file)
    browse_button.pack()

    root.mainloop()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=True)

    # Inicia a interface gráfica de usuário
    create_gui()