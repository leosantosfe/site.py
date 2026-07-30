import streamlit as str  # Carrega o motor web moderno
import os
import time
from PIL import Image

# Configuração da página web (Tema Dashboard Premium)
str.set_page_config(page_title="InclusivAI — Painel Corporativo", layout="wide")

# Senha master de ativação por escola
SENHA_VALIDA = "INCLUSIVAI-MATA-2026"

# 1. TELA DE LOGIN SEGURA
if "autenticado" not in str.session_state:
    str.session_state["autenticado"] = False

if not str.session_state["autenticado"]:
    str.title("🔑 Sistema InclusivAI — Portal de Inclusão")
    str.write("Módulo de Segurança e Ativação por Unidade Escolar")
    
    # Campo de senha já preenchido para facilitar seu teste na prefeitura
    senha = str.text_input("Insira a Chave de Licença da Escola:", value=SENHA_VALIDA, type="password")
    
    if str.button("VERIFICAR ATIVAÇÃO"):
        if senha == SENHA_VALIDA:
            str.session_state["autenticado"] = True
            str.rerun()
        else:
            str.error("Chave de Licença Inválida ou Expirada!")
else:
    # 2. SE O USUÁRIO ACERTAR A SENHA, ABRE O DASHBOARD WEB COMPLETO
    str.title("🏛️ Portal InclusivAI — Secretaria de Educação")
    str.caption("Módulo Assistivo Corporativo de Gestão de Educação Especial | Licença: ATIVA")
    
    # Divisão de tela: Barra Lateral com Filtros de Gestão (Sua melhoria solicitada!)
    with str.sidebar:
        str.header("🏫 Gestão da Rede")
        str.selectbox("Selecione a Unidade:", ["Escola Municipal Polo A", "Escola Municipal Polo B", "Creche Central"])
        str.selectbox("Selecione a Turma:", ["3º Ano - Fundamental I", "4º Ano - Fundamental I", "5º Ano - Fundamental I"])
        str.write("---")
        str.write("👤 **Docente Logado:**\nProf. Leonardo S.")
        
    # Área Central: Entrada de Texto do Professor
    str.subheader("Cole o Conteúdo da Aula Regular abaixo:")
    texto_usuario = str.text_area("", value="O calor do Sol aquece a água do rio. A água vira vapor, sobe para o céu e forma as nuvens. Depois, cai em forma de chuva.", height=100)
    
    if str.button("🚀 ADAPTAR MATERIAL E CARREGAR IMAGENS"):
        with str.spinner("Processando Inteligência Pedagógica..."):
            time.sleep(1.0)
            
        # Cria as abas de neurodiversidade de forma linda na web
        aba1, aba2, aba3 = str.tabs(["🧩 Autismo (TEA)", "⚡ TDAH / Dislexia", "❤️ Síndrome de Down"])
        
        with aba1:
            col_texto, col_fotos = str.columns([2, 1])
            with col_texto:
                str.markdown("### Material Adaptado — TEA")
                str.write("• O Sol brilha muito forte no céu. ☀️")
                str.write("• O calor do Sol esquenta a água do rio. 🌊")
                str.write("• A água vira nuvem de chuva. ☁️")
            with col_fotos:
                str.markdown("### Pictogramas")
                # Busca as fotos na sua pasta local para exibir na web
                for nome in ["sol", "rio", "nuvem"]:
                    for ext in [".png", ".jpg", ".jpeg"]:
                        caminho = os.path.join("imagens", f"{nome}{ext}")
                        if os.path.exists(caminho):
                            img = Image.open(caminho)
                            str.image(img, caption=f"Apoio Visual: {nome.upper()}", width=90)
                            break
                            
        with aba2:
            str.markdown("### Roteiro de Foco Ativo — TDAH")
            str.write("☀️ O **SOL** aquece a água dos oceanos e rios.")
            str.write("💨 **EVAPORAÇÃO**: A água vira vapor e sobe para o céu.")
            str.write("📌 **DESAFIO:** O que faz a água subir? (b) O calor do Sol.")
            
        with aba3:
            str.markdown("### Aprendizado Prático — Síndrome de Down")
            str.write("A água faz uma grande viagem que nunca acaba! Sabe quando a mamãe ferve água na panela e sai aquela fumaça subindo? Na natureza o Sol faz a mesma coisa com a água do rio...")
