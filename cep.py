import requests
from PyQt5 import uic, QtWidgets

def main():
    try:
        r = requests.get(f"https://viacep.com.br/ws/{cep.lineEdit.text().replace('-', '')}/json/").json()
        cep.label_3.setText("")
        cep.label_2.setText(f"CEP: {r['cep']}\nLogradouro: {r['logradouro']}\nBairro: {r['bairro']}\nLocalidade: {r['localidade']}\nUF: {r['uf']}\nIBGE: {r['ibge']}\nDDD: {r['ddd']}\nComplemento: {r['complemento']}\n")
    except:
        cep.label_3.setText("Cep inválido")
        cep.label_2.setText("")


app = QtWidgets.QApplication([])
cep = uic.loadUi("cep.ui")
cep.pushButton.clicked.connect(main)

cep.show()
app.exec()