"""
SIGA - Sistema Integrado de Gestao Academica
Modulo: matricula

Estrutura de dominio do modulo de matricula. A regra de negocio de
RF-014 ainda nao foi implementada.
"""


class MatriculaService:
    """Regras de matricula de aluno em turma de disciplina."""

    def __init__(self, conexao):
        self.conexao = conexao

    def matricular(self, aluno, turma):
        raise NotImplementedError("RF-014 ainda nao implementado")

    def listar_turmas_do_aluno(self, aluno):
        cursor = self.conexao.cursor()
        cursor.execute(
            "SELECT turma_id FROM matricula WHERE aluno_id = ?", (aluno.id,)
        )
        return [linha[0] for linha in cursor.fetchall()]

    def cancelar_matricula(self, aluno, turma):
        cursor = self.conexao.cursor()
        cursor.execute(
            "DELETE FROM matricula WHERE aluno_id = ? AND turma_id = ?",
            (aluno.id, turma.id),
        )
        self.conexao.commit()
        turma.vagas_ocupadas = turma.vagas_ocupadas - 1
        return True


# ---------------------------------------------------------------------
# Modelos simplificados usados pelo servico
# ---------------------------------------------------------------------
class Aluno:
    def __init__(self, id, nome, cpf, situacao, matriculas_ativas,
                 token_sessao="", formando=False):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.situacao = situacao
        self.matriculas_ativas = matriculas_ativas
        self.token_sessao = token_sessao
        self.formando = formando


class Disciplina:
    def __init__(self, codigo, creditos, prerequisitos):
        self.codigo = codigo
        self.creditos = creditos
        self.prerequisitos = prerequisitos


class Turma:
    def __init__(self, id, disciplina, vagas_total, vagas_ocupadas,
                 dia_semana, hora_inicio, hora_fim):
        self.id = id
        self.disciplina = disciplina
        self.vagas_total = vagas_total
        self.vagas_ocupadas = vagas_ocupadas
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.lista_espera = []
