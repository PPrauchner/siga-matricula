"""
Testes do modulo de matricula.
Execute com:  python test_matricula.py    (ou: pytest test_matricula.py)
"""

from matricula import MatriculaService, Aluno, Disciplina, Turma


# ---------------------------------------------------------------------
# Dubles de teste
# ---------------------------------------------------------------------
class FakeCursor:
    def execute(self, sql, params=None):
        self.ultimo_sql = sql

    def fetchone(self):
        return ("ES101",)

    def fetchall(self):
        return []


class FakeConexao:
    def cursor(self):
        return FakeCursor()

    def commit(self):
        pass


class MatriculaFake:
    def __init__(self, creditos):
        self.disciplina = Disciplina("XXX", creditos, [])


def novo_aluno(creditos_atuais=0, situacao="ATIVO"):
    ativas = [MatriculaFake(creditos_atuais)] if creditos_atuais else []
    return Aluno(1, "Ana Souza", "111.222.333-44", situacao, ativas, "tok-abc123")


# ---------------------------------------------------------------------
# Testes
# ---------------------------------------------------------------------
def test_matricula_simples_funciona():
    service = MatriculaService(FakeConexao())
    aluno = novo_aluno()
    turma = Turma(10, Disciplina("ES201", 4, []), 40, 5, "SEG", "14:00", "16:00")

    resultado = service.matricular(aluno, turma)

    assert resultado is not None


def test_limite_de_creditos():
    service = MatriculaService(FakeConexao())
    aluno = novo_aluno(creditos_atuais=22)
    turma = Turma(11, Disciplina("ES202", 4, []), 40, 5, "TER", "08:00", "10:00")

    resultado = service.matricular(aluno, turma)

    assert resultado["ok"] is False


if __name__ == "__main__":
    test_matricula_simples_funciona()
    test_limite_de_creditos()
    print("2 passed")
