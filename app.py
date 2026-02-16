#==================================================================#

from flask import Flask, jsonify, request
import json

#==================================================================#

app = Flask(__name__)

ARQUIVO = "dados.json"

# CARREGAR OS DADOS DE ACORDO COM AS MODIFICAÇÕES DO ENDPOINT
def carregar_dados():
    with open(ARQUIVO, "r") as f:
        return json.load(f)
    

# SALVAR OS DADOS DE ACORDO COM AS MODIFICAÇÕES DO ENDPOINT
def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)    

#==================================================================#


# CONSULTA GERAL IMÓVEIS

@app.route("/imoveis", methods=["GET"])
def consulta_imoveis():
    imoveis = carregar_dados()
    return jsonify(imoveis)




# CONSULTA IMÓVEIS POR ID

@app.route("/imoveis/<int:id>", methods=["GET"])
def consulta_imoveis_id(id):
    imoveis = carregar_dados()
    for imovel in imoveis:
        if imovel ["id"] == id:
         return jsonify(imovel)
    return jsonify({"erro": "Imóvel não encontrado"}), 404



# CADASTRAR IMÓVEIS

@app.route("/imoveis/cadastro", methods=["POST"])
def cadastrar_imoveis():
    imoveis = carregar_dados()
    novo_imovel = request.get_json()
    imoveis.append(novo_imovel)
    salvar_dados(imoveis)
    return jsonify(imoveis)



# EDITAR IMÓVEIS

@app.route("/imoveis/<int:id>", methods=["PUT"])
def editar_imovel(id):
    imoveis = carregar_dados()
    dados = request.get_json()

    for imovel in imoveis:
        if imovel["id"] == id:   
            # atualiza só o que vier no JSON
            if "titulo" in dados:
                imovel["titulo"] = dados["titulo"]

            if "preco" in dados:
                imovel["preco"] = dados["preco"]

            if "quartos" in dados:
                imovel["quartos"] = dados["quartos"]

            if "banheiro" in dados:
                imovel["banheiro"] = dados["banheiro"]

            if "metro2" in dados:
                imovel["metro2"] = dados["metro2"]

            salvar_dados(imoveis)
            return jsonify(imovel)
    return jsonify({"erro": "Imóvel não encontrado"}), 404



# DELETAR IMÓVEIS

@app.route("/imoveis/<int:id>", methods=["DELETE"])
def deletar_imoveis(id):
   imoveis = carregar_dados()
   for indice, imovel in enumerate(imoveis):
      if imovel.get("id") == id:
         del imoveis[indice]
         salvar_dados(imoveis)
   return jsonify(imoveis)
 
#==================================================================#


app.run(port=6000,host="localhost",debug=True)


#==================================================================#


