#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar o `powershell` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `powershell` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `powershell` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `powershell`
# 
# O `PowerShell` é uma poderosa linguagem de script e ambiente de automação desenvolvida pela Microsoft, projetada para simplificar a administração e a automação de tarefas em sistemas Windows e ambientes de rede. Ele fornece uma interface de linha de comando interativa que permite aos usuários executar comandos e escrever scripts para realizar uma ampla gama de tarefas, desde gerenciamento de arquivos e configuração de sistema até administração de servidores. O `PowerShell` se destaca pela ênfase na manipulação de objetos, permitindo que os resultados dos comandos sejam tratados como objetos que podem ser facilmente processados e encadeados. Além disso, ele oferece acesso a uma vasta biblioteca de módulos e cmdlets (comandos) que facilitam a automação de tarefas específicas. O `PowerShell` é uma ferramenta essencial para administradores de sistemas e profissionais de TI que desejam simplificar e agilizar suas operações de gerenciamento de sistemas Windows.
# 

# ## 1. Como configurar/instalar o `powershell` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar o `powershell` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. Para instalar o `PowerShell` no `Linux Ubuntu`, você pode usar os seguintes comandos:
# 
# 4. **Digite o comando de instalação do `PowerShell` usando o `Snap`:** `sudo snap install powershell --classic`
# 
#     Este comando solicitará a sua senha de usuário do `Linux Ubuntu` para conceder permissões de administrador (root) necessárias para instalar software.
# 
# 3. O parâmetro `--classic` permite a instalação de um pacote `snap` que requer acesso completo ao sistema, sem as restrições habituais aplicadas aos snaps. Isso é necessário para o `PowerShell` devido à sua natureza de ferramenta de administração.
# 
# 4. O sistema irá baixar e instalar o `PowerShell`. Esse processo pode levar alguns minutos, dependendo da sua conexão com a internet.
# 
# 5. Uma vez concluída a instalação, você pode iniciar o `PowerShell` digitando no seu terminal: `pwsh` 
# 
#     Isso abrirá o shell do `PowerShell`, onde você pode começar a executar comandos do `PowerShell`.
# 
# É assim que você instala o `PowerShell` no Ubuntu usando o `Snap`. A vantagem de usar o `Snap` é que ele mantém o _software_ instalado automaticamente atualizado para a última versão estável.
# 

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `PowerShell` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo snap install powershell --classic
#     pwsh
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar o powershell no linux ubuntu.*** Disponível em: <https://chat.openai.com/c/27d692b7-1d9e-4884-b9cb-d66639f1520c> (texto adaptado). ChatGPT. Acessado em: 14/12/2023 08:51.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 14/12/2023 08:51.
# 
# [3] OPENAI. ***Comandos de manutenção do ubuntu.*** Disponível em: <https://chat.openai.com/c/4a8cfaa2-30d6-474d-821f-7047a6a39830> (texto adaptado). ChatGPT. Acessado em: 15/12/2023 08:25.
# 
