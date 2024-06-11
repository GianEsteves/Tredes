# Projeto: Implementação de Controles TCP sobre UDP

## Objetivo

Este projeto tem como objetivo aprofundar o conhecimento sobre os controles implementados pelo protocolo TCP ao replicar funcionalidades similares em uma aplicação que utiliza o protocolo UDP. O foco será na implementação de controles de confiabilidade e ordenação de mensagens, além de realizar uma comparação de desempenho entre TCP, UDP e a nova versão do UDP desenvolvida.

## Descrição

Desenvolvemos uma aplicação que modifica o protocolo UDP para incluir funcionalidades presentes no TCP. Os controles implementados incluem:

- **Controle de Fluxo**: Garantir que o receptor possa controlar o fluxo de dados recebidos.
- **Controle de Congestionamento**: Implementar mecanismos para evitar a saturação da rede.
- **Garantia de Entrega**: Assegurar que todas as mensagens sejam entregues, utilizando técnicas de retransmissão.
- **Ordenação de Mensagens**: Garantir que as mensagens sejam entregues na ordem correta.

Para simular situações de congestionamento e perda de pacotes, utilizamos métodos simples que imitam esses comportamentos.

## Estrutura do Projeto

O projeto está organizado nos seguintes arquivos:

- **cliente_udp_modificado.py**: Implementação do cliente que utiliza a nova versão do UDP com controles TCP.
- **servidor_udp_modificado.py**: Implementação do servidor que utiliza a nova versão do UDP com controles TCP.
- **servidor_udp.py**: Implementação do servidor UDP padrão.
- **servidor_tcp.py**: Implementação do servidor TCP padrão.
- **teste_desempenho.py**: Script para testar o desempenho dos três protocolos (TCP, UDP, e UDP modificado).

## Como Executar

1. **Servidor TCP**:
   ```bash
   python servidor_tcp.py
   ```

2. **Servidor UDP**:
   ```bash
   python servidor_udp.py
   ```

3. **Servidor UDP Modificado**:
   ```bash
   python servidor_udp_modificado.py
   ```

4. **Cliente UDP Modificado**:
   ```bash
   python cliente_udp_modificado.py
   ```

5. **Teste de Desempenho**:
   ```bash
   python teste_desempenho.py
   ```

## Contribuidores

- [Gian Esteves Oliveira](giann.esteves@gmail.com)
- [Tamires Antunes Nunes](tamiresantunesnunes@gmail.com)

---

Este projeto nos permitiu compreender melhor os mecanismos de controle do TCP e como eles podem ser aplicados no UDP para melhorar a confiabilidade e a eficiência da comunicação em rede. Esperamos que este trabalho possa servir de base para futuras melhorias e estudos na área de protocolos de comunicação.
