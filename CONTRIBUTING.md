# Padrão de codificação — equipe SIGA

Todo código submetido a este repositório deve seguir os padrões abaixo.
Revisões verificam conformidade com este documento.

## Banco de dados

- **Toda** consulta ao banco deve usar **parâmetros vinculados** (`?`).
  Concatenação ou interpolação de valores em SQL é proibida, sem exceção,
  inclusive para valores que "vêm de dentro do sistema".
- Operações que dependem de um estado lido previamente devem ocorrer dentro de
  uma **transação**. O período de matrícula tem alta concorrência.

## Log e dados pessoais

- Registros de log, mensagens de erro e telemetria **não podem conter dados
  pessoais nem credenciais**: CPF, RG, e-mail, senha, token de sessão.
- Identifique entidades por **id**, nunca por dado pessoal.
- Log é replicado para ferramentas de observabilidade com controle de acesso
  mais permissivo que o do banco. Trate log como público.

## Tratamento de erro

- Exceção capturada deve ser **tratada ou registrada**. `except: pass` e
  `except Exception: pass` são proibidos.
- Não capture `Exception` genérica quando souber qual exceção espera.

## Contratos de método

- Um método público retorna **sempre o mesmo tipo**. Não misture `bool`, `dict`
  e `None` como retornos do mesmo método.
- Estados de resultado distintos precisam ser **distinguíveis pelo chamador**.

## Constantes e regras de negócio

- Valor de regra de negócio é definido **em um único lugar**, com nome.
- Números mágicos no meio da lógica são proibidos.
- Quando a regra vem de um documento de requisito, cite o identificador da regra
  em comentário.

## Testes

- Todo requisito implementado precisa de teste derivado dos **critérios de
  aceitação** do documento de requisito — não do código escrito.
- Teste deve verificar **comportamento**, não ausência de exceção.
  `assert x is not None` não é asserção de comportamento.
- Caminhos de falha e recusa são obrigatórios, não opcionais.
