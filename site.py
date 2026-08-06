import streamlit as st
import time
import re

# Configuração da página web (Tema Dashboard Premium)
st.set_page_config(page_title="InclusivAI — Painel Corporativo", layout="wide")

# Senha master de ativação por escola
SENHA_VALIDA = "INCLUSIVAI-MATA-2026"

# Função estável que gera a página oficial de impressão da prefeitura
def gerar_pagina_impressao(titulo_segmento, conteudo_texto, nome_aluno, laudo_aluno, idade_aluno):
    texto_formatado = conteudo_texto.replace("\n", "<br>")
    data_atual = time.strftime('%d/%m/%Y')
    
    html_oficial = f"""
    <html>
    <head>
        <title>InclusivAI - Prontuário Escolar</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; color: #1e293b; }}
            .cabecalho {{ border-bottom: 3px solid #1e3a8a; padding-bottom: 15px; margin-bottom: 20px; text-align: center; }}
            .titulo {{ color: #1e3a8a; font-size: 24px; font-weight: bold; margin: 0; }}
            .sub {{ color: #64748b; font-size: 12px; font-weight: bold; text-transform: uppercase; margin-top: 5px; }}
            .ficha-aluno {{ background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; justify-content: space-between; font-size: 13px; }}
            .tag {{ background: #f1f5f9; padding: 10px; border-left: 5px solid #10b981; font-weight: bold; margin-bottom: 25px; }}
            .texto {{ font-size: 14px; line-height: 1.8; white-space: pre-wrap; }}
        </style>
    </head>
    <body>
        <div class='cabecalho'>
            <div class='titulo'>PORTAL INCLUSIVAI — TECNOLOGIA ASSISTIVA</div>
            <div class='sub'>Secretaria Municipal de Educação e Ensino Inclusivo</div>
        </div>
        <div class='ficha-aluno'>
            <div><strong>ALUNO(A):</strong> {nome_aluno.upper()}</div>
            <div><strong>IDADE:</strong> {idade_aluno} ANOS</div>
            <div><strong>LAUDO MÉDICO:</strong> {laudo_aluno.upper()}</div>
            <div><strong>DATA DE EMISSÃO:</strong> {data_atual}</div>
        </div>
        <div class='tag'>MATERIAL DIDÁTICO ADAPTADO — PÚBLICO: {titulo_segmento.upper()}</div>
        <div class='texto'>{texto_formatado}</div>
        <script>
            window.print();
        </script>
    </body>
    </html>
    """
    return html_oficial

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
        st.write("Módulo Ativo: **Visualização Integrada Total**")
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
            
            # --- BANCO DE TRADUÇÃO EXPANDIDO ---
            traduzido_simples = texto_limpo
            substituicoes = {
                "bombeia": "empurra e joga", "órgãos": "partes do corpo", "veias": "caminhos do sangue",
                "saudável": "forte e cheio de saúde", "principal": "mais importante", "músculo": "motor de carne",
                "descobrimento": "chegada dos navios", "savana": "campo aberto de terra", "ruge": "faz um som muito alto"
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

            # --- RENDERIZAÇÃO EM SEQUÊNCIA INQUEBRÁVEL NO STREAMLIT ---
            st.write("---")
            st.success("✨ Inteligência Assistiva: Materiais Traduzidos e Diagramados para os Laudos da Rede!")
            
            # EXIBIÇÃO TEXTUAL CONCATENADA (Sem travar abas ou botões internos)
            st.markdown("## 🧩 Segmento 1: Autismo (TEA)")
            col_t1, col_f1 = st.columns(2)
            with col_t1:
                st.info(txt_autismo)
            with col_f1:
                st.markdown("#### 🖼️ Figuras Demonstrativas")
                txt_m = texto_limpo.lower()
                if "sol" in txt_m: st.markdown("<h1>☀️ SOL</h1>", unsafe_allow_html=True)
                if "rio" in txt_m or "água" in txt_m: st.markdown("<h1>🌊 RIO / ÁGUA</h1>", unsafe_allow_html=True)
                if "nuvem" in txt_m or "chuva" in txt_m: st.markdown("<h1>☁️ NUVEM</h1>", unsafe_allow_html=True)
                if "leão" in txt_m or "leao" in txt_m: st.markdown("<h1>🦁 LEÃO</h1>", unsafe_allow_html=True)
                if "elefante" in txt_m: st.markdown("<h1>🐘 ELEFANTE</h1>", unsafe_allow_html=True)
                if "árvore" in txt_m or "arvore" in txt_m: st.markdown("<h1>🌳 ÁRVORE</h1>", unsafe_allow_html=True)
                if "navio" in txt_m or "barco" in txt_m: st.markdown("<h1>🚢 NAVIO</h1>", unsafe_allow_html=True)
                if "coração" in txt_m or "coracao" in txt_m: st.markdown("<h1>❤️ CORAÇÃO</h1>", unsafe_allow_html=True)

            st.write("---")
            
            # CORREÇÃO: O Segmento 2 agora é exibido obrigatoriamente logo abaixo
            st.markdown("## ⚡ Segmento 2: TDAH / Dislexia")
            st.warning(txt_tdah)

            st.write("---")
            
            # CORREÇÃO: O Segmento 3 agora é exibido obrigatoriamente no fim do fluxo
            st.markdown("## ❤️ Segmento 3: Síndrome de Down / Dificuldades Cognitivas")
            st.error(txt_down)
            
            st.write("---")
            
            # 🖨️ PAINEL DE IMPRESSÃO CENTRALIZADO (Isolado no fim da página para não quebrar a tela)
            st.markdown("### 🖨️ Central de Emissão de Prontuários Oficiais")
            st.write("Selecione qual documento timbrado você deseja enviar para a impressora escolar:")
            
            col_p1, col_p2, col_p3 = st.columns(3)
            with col_p1:
                html_tea = gerar_pagina_impressao("Autismo (TEA)", txt_autismo, nome_aluno, laudo_aluno, idade_aluno)
                st.download_button(label="Imprimir Material TEA", data=html_tea, file_name="Prontuario_TEA.html", key="print_key_tea")
            with col_p2:
                html_tdah = gerar_pagina_impressao("TDAH / Dislexia", txt_tdah, nome_aluno, laudo_aluno, idade_aluno)
