# Análise de BGP e Geopolítica: Apagões de Internet no Irã (2019 vs. 2022)

Este repositório contém os dados, scripts e análises do trabalho final sobre **BGP, Internet e Geopolítica**. O objetivo central deste estudo é investigar, utilizando dados públicos de telemetria e roteamento da Internet, como o governo iraniano implementou apagões de conectividade durante duas de suas maiores crises políticas recentes.

## Sobre o Projeto

A pesquisa analisa a **Dimensão A6 (Protestos, eleições e crises internas)** em relação à **Questão B3 (Conflitos no Oriente Médio)**, contrastando os mecanismos técnicos utilizados pelo Estado iraniano em dois eventos distintos:

* **Novembro de 2019 ("Bloody November"):** Protestos motivados pelo aumento do preço dos combustíveis. Caracterizado por um apagão de "força bruta", com corte contínuo, a nível nacional, de redes fixas e móveis por cerca de 5 a 6 dias.
* **Setembro de 2022 ("Women, Life, Freedom"):** Protestos desencadeados pela morte de Mahsa (Zhina) Amini. Caracterizado por uma tática de censura cirúrgica e regionalizada, focada em redes móveis através de apagões intermitentes noturnos (*curfews* digitais) e limitação severa na camada de pacotes, mantendo o plano de controle aparentemente estável.

O estudo foca nos 5 principais Sistemas Autônomos (ASes) do Irã:
* **AS58224** (Iran Telecom Co / TCI)
* **AS44244** (IranCell)
* **AS57218** (Rightel)
* **AS16322** (ParsOnline)
* **AS197207** (MCCI)

---

## Fontes e Coleta de Dados

Para comprovar a tática de censura e contornar a "cegueira" técnica do protocolo BGP (onde pacotes de retirada de rota não carregam a origem do AS), o projeto cruzou dados do plano de controle com o plano de dados através de três fontes distintas:

### 1. IODA (Internet Outage Detection and Analysis)
* **O que medimos:** O contraste entre a visibilidade do BGP e o acesso real à rede.
* **Sinais extraídos:** * *BGP Reachability:* Visibilidade das rotas no mapa global.
    * *Active Probing:* Pacotes (pings) enviados de fora do Irã para dentro.
    * *Network Telescope:* Ruído de fundo não solicitado (tráfego saindo do Irã).
* **Como foi coletado:** Exportação manual de dados históricos em formato `.csv` (intervalos de 15 minutos) diretamente do [Dashboard oficial do IODA](https://ioda.inetintel.cc.gatech.edu/), filtrando tanto a nível nacional (por ASN) quanto a nível regional (ex: província de Kordestan).

### 2. RIPE RIS (via API RIPEstat)
* **O que medimos:** Instabilidade das rotas (Route Flapping) e atividade anômala no plano de controle.
* **Sinais extraídos:** Volume de atualizações BGP, com foco específico nos picos de *Announcements*.
* **Como foi coletado:** Extração automatizada via scripts em Python consumindo o endpoint `bgp-update-activity` da API pública do RIPEstat. Os dados foram salvos em formato `.json`.

### 3. Cloudflare Radar
* **O que medimos:** O impacto real na camada de aplicação e a confirmação de autoria.
* **Sinais extraídos:** Séries temporais de *Netflows* (volume de bytes processados pela CDN).
* **Como foi coletado:** Arquivos `.json` contendo não apenas as métricas de tráfego, mas metadados e anotações técnicas oficiais do Cloudflare que classificam os eventos explicitamente como disrupções direcionadas pelo governo (*"cause: government directed"*).

