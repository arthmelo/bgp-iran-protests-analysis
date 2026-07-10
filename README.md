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

## Fontes, Metodologia e Coleta de Dados

Para comprovar as diferentes táticas de censura, o projeto cruzou dados do plano de controle com o plano de dados através de três fontes distintas. Devido à disponibilidade histórica e limitações de protocolo, a metodologia foi adaptada para cada evento:

### 1. IODA (Internet Outage Detection and Analysis)
* **2019 (Apagão Nacional):** Utilizamos a métrica nacional de tráfego do **Google (Search)**, que ilustra a queda abrupta da conectividade do país a níveis próximos a zero (0.06%) durante os dias de bloqueio de força bruta.
* **2022 (Censura Cirúrgica):** Utilizamos uma abordagem multidimensional cruzando *BGP Reachability*, *Active Probing* e *Network Telescope*, tanto a nível de operadoras (ASNs) quanto a nível regional (Província de Kordestan). Isso comprovou a tática de filtragem de pacotes, onde o BGP permaneceu estável enquanto o tráfego real (Probing/Telescope) caiu.

### 2. RIPE RIS (via API RIPEstat)
* **O que medimos:** Instabilidade das rotas e atividade anômala no plano de controle BGP.
* **Nota Metodológica:** Constatamos que pacotes de retirada de rota (*withdrawals*) no BGP não carregam o atributo *AS_PATH*. Portanto, coletores globais não conseguem associar *withdrawals* à origem em tempo real. Para contornar isso, mensuramos a instabilidade através do volume anômalo de **Announcements** (*route flapping*).
* **Como foi coletado:** Extração automatizada via API consumindo o endpoint `bgp-update-activity`, salvos em formato `.json`.

### 3. Cloudflare Radar (Apenas 2022)
* **Nota Metodológica:** Utilizado exclusivamente para 2022, pois a plataforma iniciou sua telemetria pública após o evento de 2019.
* **O que medimos:** Impacto real na camada de aplicação via séries temporais de *Netflows*. 
* **Evidência de Autoria:** Os arquivos extraídos contêm metadados e anotações técnicas oficiais do Cloudflare que classificam os eventos explicitamente como disrupções governamentais (*"cause: government directed"*).

