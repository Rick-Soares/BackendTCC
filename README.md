# 🚨 Sistema de Detecção de Quedas com IoT

Este projeto tem como objetivo desenvolver um sistema de **detecção de quedas em tempo real**, voltado para auxiliar pessoas em situações de risco, enviando alertas automáticos para contatos cadastrados.

O sistema é baseado no conceito de **Internet of Things (IoT)**, onde um dispositivo físico se comunica com um backend na nuvem para disparo de notificações críticas.

---

# 🧠 Motivação

Quedas são uma das principais causas de acidentes domésticos graves, especialmente entre idosos ou pessoas com mobilidade reduzida.

Este projeto busca aplicar tecnologia IoT para:

- Detectar eventos de queda em tempo real (via dispositivo físico futuro)
- Automatizar o envio de alertas
- Reduzir o tempo de resposta em situações de emergência
- Tornar a solução acessível e de fácil configuração por usuários leigos

---

# ⚙️ Arquitetura do Sistema

O sistema é dividido em três partes principais:

### 📱 Interface Web (Frontend)
- Responsável pelo cadastro de usuários
- Configuração de telefone e dispositivos
- Hospedado futuramente na Vercel

### 🧠 Backend (API)
- Desenvolvido em Python
- Responsável pela lógica de negócio
- Autenticação e gerenciamento de usuários/dispositivos
- Recebimento de eventos do dispositivo IoT
- Disparo de notificações

### 📡 Dispositivo IoT (futuro)
- Baseado em ESP32
- Responsável por detectar quedas
- Envia eventos para o backend via internet

---

# 🧰 Tecnologias Utilizadas

### Backend
- Python
- FastAPI
- JSON (armazenamento inicial)
- Estrutura baseada em Services + Repositories

### Integração e Comunicação
- API REST
- Webhooks (IoT → Backend)
- Telegram (fase de testes)
- Twilio (futuro para chamadas reais)

### Infraestrutura
- Vercel (frontend e possíveis funções serverless)
- GitHub (versionamento do código)

---

# 🚀 Funcionalidades (em desenvolvimento)

- [x] Cadastro de usuários
- [x] Login simples (email e senha)
- [x] Associação de telefone ao usuário
- [x] Registro de dispositivos
- [x] Sistema de alerta simulado
- [ ] Integração com dispositivo IoT real
- [ ] Chamadas automáticas via Twilio
- [ ] Dashboard web completo

---

# 🔁 Fluxo do Sistema

1. Usuário cria conta na plataforma
2. Cadastra telefone de emergência
3. Associa um dispositivo IoT
4. Dispositivo detecta uma queda
5. Backend recebe o evento
6. Sistema envia notificação (Telegram ou ligação futura)

---

# 📌 Observação sobre o projeto

Este projeto está em fase de desenvolvimento e tem como objetivo principal a integração entre:

- Backend moderno
- Dispositivos IoT (ESP32)
- Serviços de comunicação em nuvem

---

# 📈 Futuro do projeto

- Integração completa com ESP32
- Sistema de chamadas automáticas via Twilio
- Aplicação mobile
- Melhorias de segurança (JWT e criptografia de senhas)
- Migração de JSON para banco de dados relacional

---

# 👨‍💻 Autor


Projeto desenvolvido por Ricardo Soares como base para TCC na área de tecnologia, com foco em **IoT, backend e automação de emergências médicas**.