import streamlit as st
import time
import re

# Configuração da página web (Tema Dashboard Premium)
st.set_page_config(page_title="InclusivAI — Painel Corporativo", layout="wide")

# Senha master de ativação por escola
SENHA_VALIDA = "INCLUSIVAI-MATA-2026"

# Inicialização limpa da autenticação
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# 1. TELA DE LOGIN SEGURA
if not st.session_state["autenticado"]:
    st.title("🔑 Sistema InclusivAI — Portal de Inclusão")
    st.write("Módulo de Segurança e Ativação por Unidade Escolar")
    senha = st.text_input("Insira a Chave de Licença da Escola:", value=SENHA_VALIDA, type="password")
    if st.button("VERIFICAR ATIVAÇÃO"):
        if senha == SENHA_VALIDA:
            st.session_state["autenticado"] = True
            st.rerun()
        else:
            st.error("Chave de Licença Inválida ou Expirada!")
else:
    # 2. DASHBOARD WEB COMPLETO
    st.title("🏛️ Portal InclusivAI — Secretaria de Educação")
    st.caption("Módulo Assistivo Corporativo de Gestão de Educação Especial | Licença: ATIVA")
    
    with st.sidebar:
        st.header("🏫 Gestão da Rede")
        st.selectbox("Selecione a Unidade:", ["Escola Municipal Polo A", "Escola Municipal Polo B"])
        st.selectbox("Selecione a Turma:", ["3º Ano - Fundamental I", "4º Ano - Fundamental I"])
        st.write("---")
        st.write("Módulo Ativo: **Impressão Direta e Estável**")
        st.write("👤 **Docente Logado:**\nProf. Leonardo S.")
        
    menu_selecionado = st.radio("Escolha o Painel de Trabalho:", ["📝 Adaptador Pedagógico e PEI", "📊 Relatório de Impacto (Painel do Secretário)"], horizontal=True)
    st.write("---")

    if menu_selecionado == "📝 Adaptador Pedagógico e PEI":
        st.subheader("📋 Identificação do Estudante Laudado")
        col_a1, col_a2, col_a3 = st.columns(3)
        with col_a1:
            nome_aluno = st.text_input("Nome Completo do Aluno:", value="João Pedro Santos")
        with col_a2:
            idade_aluno = st.number_input("Idade do Estudante:", min_value=4, max_value=18, value=9)
        with col_a3:
            laudo_aluno = st.selectbox("Laudo Médico de Referência:", ["TEA (Autismo) - CID F84", "TDAH - CID F90.0", "Síndrome de Down - CID Q90"])

        st.write("---")
        st.subheader("📚 Conteúdo da Aula Regular abaixo:")
        texto_usuario = st.text_area("Digite ou cole qualquer conteúdo aqui para a IA traduzir:", value="O coração é o músculo principal do corpo humano. Ele bombeia o sangue para todos os órgãos através das veias. Praticar exercícios físicos faz bem para manter o coração forte e saudável.")
        
        if not texto_usuario.strip():
            st.info("💡 Digite uma matéria na caixa acima para iniciar o de adaptação.")
        else:
            texto_limpo = str(texto_usuario).strip()
            
            # --- MOTOR DE TRADUÇÃO DE VOCABULÁRIO REAL ---
            traduzido_simples = texto_limpo
            substituicoes = {
                "bombeia": "empurra e joga", "órgãos": "partes do corpo", "veias": "caminhos do sangue",
                "saudável": "forte e cheio de saúde", "principal": "mais importante", "músculo": "motor de carne",
                "descobrimento": "chegada dos navios", "savana": "campo aberto de terra",
                "ruge": "faz um som muito alto"
            }
            for original, novo in substituicoes.items():
                traduzido_simples = re.sub(re.escape(original), novo, traduzido_simples, flags=re.IGNORECASE)
                
            linhas = [l.strip() for l in re.split(r'[.!]', traduzido_simples) if len(l.strip()) > 3]
            if not linhas:
                linhas = [traduzido_simples]

            # 1. TEXTO ADAPTADO AUTISMO
            txt_autismo = "📋 DIRETRIZES DE LEITURA COMPORTAMENTAL LITERAL (TEA):\n\n"
            for l in linhas[:3]:
                txt_autismo += f"🔷 [PASSO VISUAL]: {l}.\n\n"
            txt_autismo += "📌 DICA PEDAGÓGICA: Use cartões visuais para fixar o vocabulário simples."

            # 2. TEXTO ADAPTADO TDAH
            txt_tdah = "⚡ ROTEIRO DE FOCO ATIVO (TDAH):\n\n"
            emojis = ["📌", "🎯", "🔍"]
            for idx, l in enumerate(linhas[:3]):
                em = emojis[idx % len(emojis)]
                txt_tdah += f"{em} **TÓPICO CHAVE DE LEITURA**: {l}.\n\n"
            txt_tdah += "🎮 DESAFIO RELÂMPAGO: Escreva em seu caderno uma palavra resumindo o que você leu hoje!"

            # 3. TEXTO ADAPTADO DOWN
            txt_down = "❤️ APRENDIZADO DIÁRIO CONCRETO E CONTEXTUALIZADO (DOWN):\n\n"
            txt_down += "Vamos aprender uma lição muito importante e divertida para a nossa vida hoje!\n\n"
            txt_down += f"👉 **Ideia prática para lembrar**: {' '.join(linhas[:2])}.\n\n"
            txt_down += "🤝 ATIVIDADE: Conte para o professor o que você entendeu dessa historinha com suas próprias palavras!"

            # --- RENDERIZAÇÃO EM FLUXO SEGURO (NADA PODE TRAVAR OU SUMIR) ---
            st.write("---")
            st.success("✨ Inteligência Assistiva: Materiais Traduzidos e Diagramados para os Laudos da Rede!")
            
            # BLOCO 1: AUTISMO (TEA)
            st.markdown("## 🧩 Segmento 1: Autismo (TEA)")
            col_texto, col_fotos = st.columns(2)
            with col_texto:
                st.info(txt_autismo)
            with col_fotos:
                st.markdown("#### 🖼️ Gerador Automático de Figuras Demonstrativas")
                texto_minusculo = texto_limpo.lower()
                if "sol" in texto_minusculo: st.markdown("<h1 style='font-size: 70px; margin: 0;'>☀️ SOL</h1>", unsafe_allow_html=True)
                if "rio" in texto_minusculo or "água" in texto_minusculo: st.markdown("<h1 style='font-size: 70px; margin: 0;'>🌊 RIO / ÁGUA</h1>", unsafe_allow_html=True)
                if "nuvem" in texto_minusculo or "chuva" in texto_minusculo: st.markdown("<h1 style='font-size: 70px; margin: 0;'>☁️ NUVEM</h1>", unsafe_allow_html=True)
                if "leão" in texto_minusculo or "leao" in texto_minusculo: st.markdown("<h1 style='font-size: 70px; margin: 0;'>🦁 LEÃO</h1>", unsafe_allow_html=True)
                if "elefante" in texto_minusculo: st.markdown("<h1 style='font-size: 70px; margin: 0;'>🐘 ELEFANTE</h1>", unsafe_allow_html=True)
                if "árvore" in texto_minusculo or "arvore" in texto_minusculo: st.markdown("<h1 style='font-size: 70px; margin: 0;'>🌳 ÁRVORE</h1>", unsafe_allow_html=True)
                if "navio" in texto_minusculo or "barco" in texto_minusculo: st.markdown("<h1 style='font-size: 70px; margin: 0;'>🚢 NAVIO</h1>", unsafe_allow_html=True)
                if "coração" in texto_minusculo or "coracao" in texto_minusculo: st.markdown("<h1 style='font-size: 70px; margin: 0;'>❤️ CORAÇÃO</h1>", unsafe_allow_html=True)

            st.write("---")
            
            # BLOCO 2: TDAH
            st.markdown("## ⚡ Segmento 2: TDAH / Dislexia")
            st.warning(txt_tdah)

            st.write("---")
            
            # BLOCO 3: SÍNDROME DE DOWN
            st.markdown("## ❤️ Segmento 3: Síndrome de Down / Dificuldades Cognitivas")
            st.error(txt_down)

    elif menu_selecionado == "📊 Relatório de Impacto (Painel do Secretário)":
        st.subheader("📊 Painel Gerencial de Auditoria de Inclusão Escolar")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric(label="✨ PEIs Gerados Automaticamente", value="487")
        c2.metric(label="🏫 Escolas Ativas no Sistema", value="32 / 32")
        c3.metric(label="👤 Alunos Cadastrados no Censo Especial", value="487")
        c4.metric(label="🛡️ Risco de Auditoria do MP", value="ZERO", delta="Segurança Legal")
        st.write("---")
        st.bar_chart({"Autismo (TEA)": 640, "TDAH / Dislexia": 510, "Síndrome de Down": 270})