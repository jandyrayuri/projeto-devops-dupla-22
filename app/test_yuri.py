from app import app


def test_aluno_tem_dupla_e_mensagem():
    dados = app.test_client().get("/aluno").get_json()
    assert "dupla" in dados
    assert "mensagem" in dados
