from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_criar_empresa():
    empresa_data = {
        "nome": "Empresa Teste",
        "cnpj": "12345678000199",
        "endereco": "Rua Exemplo, 123",
        "email": "empresa@teste.com",
        "telefone": "11999999999"
    }

    response = client.post("/empresas/", json=empresa_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == empresa_data["nome"]
    assert data["cnpj"] == empresa_data["cnpj"]
    assert data["email"] == empresa_data["email"]
    assert "id" in data

def test_listar_empresas():
    response = client.get("/empresas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_obter_empresa():
    empresa_data = {
        "nome": "Empresa Teste 2",
        "cnpj": "12345678000188",
        "endereco": "Rua Nova, 456",
        "email": "empresa2@teste.com",
        "telefone": "11988888888"
    }
    post_response = client.post("/empresas/", json=empresa_data)
    empresa_id = post_response.json()["id"]

    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == empresa_id
    assert data["nome"] == empresa_data["nome"]


def test_atualizar_empresa():
    empresa_data = {
        "nome": "Empresa Atualizar",
        "cnpj": "12345678000177",
        "endereco": "Rua Atualizar, 789",
        "email": "empresa3@teste.com",
        "telefone": "11977777777"
    }
    post_response = client.post("/empresas/", json=empresa_data)
    empresa_id = post_response.json()["id"]

    novos_dados = {
        "nome": "Empresa Atualizada",
        "cnpj": "12345678000177",
        "endereco": "Rua Atualizada, 789",
        "email": "empresa_atualizada@teste.com",
        "telefone": "11966666666"
    }

    response = client.put(f"/empresas/{empresa_id}", json=novos_dados)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == novos_dados["nome"]
    assert data["email"] == novos_dados["email"]


def test_apagar_empresa():
    empresa_data = {
        "nome": "Empresa Excluir",
        "cnpj": "12345678000166",
        "endereco": "Rua Excluir, 101",
        "email": "empresa4@teste.com",
        "telefone": "11955555555"
    }
    post_response = client.post("/empresas/", json=empresa_data)
    empresa_id = post_response.json()["id"]


    response = client.delete(f"/empresas/{empresa_id}")
    assert response.status_code == 204


    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == 404



def test_criar_obrigacao():
    empresa_data = {
        "nome": "Empresa Obrigação",
        "cnpj": "12345678000155",
        "endereco": "Rua Principal, 202",
        "email": "empresa5@teste.com",
        "telefone": "11944444444"
    }
    post_response = client.post("/empresas/", json=empresa_data)
    empresa_id = post_response.json()["id"]

    obrigacao_data = {
        "nome": "Declaração Anual de Impostos",
        "periodicidade": "anual"
    }
    response = client.post(f"/empresas/{empresa_id}/obrigacoes/", json=obrigacao_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == obrigacao_data["nome"]
    assert data["periodicidade"] == obrigacao_data["periodicidade"]
    assert "id" in data


def test_listar_obrigacoes():
    response = client.get("/obrigacoes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # O retorno deve ser uma lista
