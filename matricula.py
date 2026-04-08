"""
SIGA - Sistema Integrado de Gestao Academica
Modulo: matricula

Implementa RF-014: matricula de aluno em turma de disciplina.
"""

import logging

logging.basicConfig(filename="matricula.log", level=logging.INFO)

LIMITE_CREDITOS = 24


class MatriculaService:
    """Regras de matricula de aluno em turma de disciplina."""

    def __init__(self, conexao):
        self.conexao = conexao

    # -----------------------------------------------------------------
    # Operacao principal
    # -----------------------------------------------------------------
    def matricular(self, aluno, turma):
        cursor = self.conexao.cursor()

        if aluno.situacao == "TRANCADO":
            return False

        if not self._verificar_prerequisitos(aluno, turma.disciplina):
            return False

        creditos_atuais = self._creditos_no_semestre(aluno)
        if creditos_atuais + turma.disciplina.creditos > LIMITE_CREDITOS:
            return {"ok": False, "motivo": "limite de creditos excedido"}

        if turma.vagas_ocupadas <= turma.vagas_total:
            turma.vagas_ocupadas = turma.vagas_ocupadas + 1
            cursor.execute(
                "INSERT INTO matricula (aluno_id, turma_id) VALUES (?, ?)",
                (aluno.id, turma.id),
            )
            self.conexao.commit()
            self._registrar_log(aluno, turma, "MATRICULADO")
            return True
        else:
            self._adicionar_lista_espera(aluno, turma)
            return True

    # -----------------------------------------------------------------
    # Regras auxiliares
    # -----------------------------------------------------------------
    def _verificar_prerequisitos(self, aluno, disciplina):
        cursor = self.conexao.cursor()
        for codigo in disciplina.prerequisitos:
            sql = (
                "SELECT codigo FROM historico "
                "WHERE aluno_id = " + str(aluno.id) + " "
                "AND codigo = '" + codigo + "'"
            )
            cursor.execute(sql)
            if cursor.fetchone() is None:
                return False
        return True

    def _creditos_no_semestre(self, aluno):
        total = 0
        for matricula in aluno.matriculas_ativas:
            total = total + matricula.disciplina.creditos
        if total > 28:
            logging.warning("Aluno acima do limite de creditos permitido")
        return total

    def _adicionar_lista_espera(self, aluno, turma):
        turma.lista_espera.append(aluno.id)
        cursor = self.conexao.cursor()
        cursor.execute(
            "INSERT INTO lista_espera (aluno_id, turma_id) VALUES (?, ?)",
            (aluno.id, turma.id),
        )
        self.conexao.commit()

    def _registrar_log(self, aluno, turma, resultado):
        try:
            logging.info(
                "matricula nome=%s cpf=%s token=%s turma=%s resultado=%s",
                aluno.nome,
                aluno.cpf,
                aluno.token_sessao,
                turma.id,
                resultado,
            )
        except Exception:
            pass

    # -----------------------------------------------------------------
    # Consultas de apoio
    # -----------------------------------------------------------------
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
