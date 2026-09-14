# SIGA — Sistema Integrado de Gestão Acadêmica

Módulo de **Matrícula**. Repositório de referência da disciplina.

## Estrutura

```
matricula.py         módulo de matrícula (serviço + modelos de domínio)
test_matricula.py    testes do módulo
docs/RF-014.md       especificação do requisito de matrícula
CONTRIBUTING.md      padrão de codificação da equipe
```

## Como executar os testes

```bash
python test_matricula.py     # ou: pytest test_matricula.py
```

Sem dependências externas. Python 3.8+.

---

# 📚 Atividade de aula — Revisão de Software

> Esta seção é para a turma. Se você caiu aqui por acaso, é um repositório didático:
> o código contém defeitos plantados de propósito. **Não use como referência.**

## O que fazer

O desenvolvedor **@dev.junior** abriu o **[Pull Request #1](../../pull/1)**,
que implementa o requisito **RF-014 — Matrícula de aluno em turma de disciplina**.

Ele escreveu na descrição do PR:

> *"Implementei o RF-014 conforme combinado na daily. Testes passando localmente
> (2/2 verdes). Acho que dá pra fazer o merge hoje."*

O pipeline está verde. A pessoa que revisaria o PR está de férias.
**Vocês são a revisão.**

## Por onde começar

1. Abra o **[PR #1 → aba *Files changed*](../../pull/1/files)** — é o diff que vocês vão revisar
2. Leia **[`docs/RF-014.md`](docs/RF-014.md)** — a especificação é a **fonte da verdade**
3. Leia **[`CONTRIBUTING.md`](CONTRIBUTING.md)** — o padrão de codificação da equipe
4. Aplique **o modo de revisão do cartão que o seu grupo recebeu**, exatamente como está escrito
5. Preencha a **ata de revisão** (em papel) — é a entrega do grupo

## Regras

- **Cada grupo tem um modo de revisão diferente.** Não troque de modo e não olhe o
  que o grupo do lado está fazendo.
- **Não comente aqui no GitHub.** Os achados vão para a ata em papel — se os grupos
  comentarem no PR, todo mundo vê os achados de todo mundo e a comparação final morre.
- **Ferramentas automáticas estão proibidas:** sem linter, sem análise estática
  (`ruff`, `bandit`, `pylint`), sem Copilot, sem assistente de IA.
  *Exceção:* os grupos que receberam o cartão de **Revisão assistida por IA** usam
  apenas o prompt que lhes foi entregue.
- **Revisa-se o artefato, não a pessoa.**
- **Registrar o defeito, não debater a correção.** Anote e siga.
- **Achado sem localização não conta** — todo defeito precisa de arquivo + linha.
- **Falso positivo custa.** Cada grupo também reporta quantos achados não se confirmaram.

## Pontuação do "campeonato"

| Métrica | Como medir |
|---|---|
| Defeitos reais encontrados | Quantos dos achados batem com o gabarito |
| Falsos positivos | Achados que não são defeitos reais |
| Defeitos críticos | Quantos dos de severidade Alta o grupo pegou |
| Achado exclusivo | Algum defeito que **só o seu grupo** encontrou |

Não existe grupo vencedor por acaso: **cada modo de revisão é bom em achar uma classe
diferente de defeito.** Descobrir *qual* é a lição da aula.

⏱ **20 minutos de revisão.** Boa sorte.
