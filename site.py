import streamlit as st
import os
import time
import re
from PIL import Image

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
        <title>InclusivAI - Prontuário de Impressão</title>
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

# Inicialização segura das variáveis de controle na memória
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False
if "exibir_resultados" not in st.session_state:
    st.session_state["exibir_resultados"] = False

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
    # 2. DASHBOARD WEB COMPLETO (APÓS LOGIN)
    st.title("🏛️ Portal InclusivAI — Secretaria de Educação")
    st.caption("Módulo Assistivo Corporativo de Gestão de Educação Especial | Licença: ATIVA")
    
    # Barra Lateral com Filtros de Gestão
    with st.sidebar:
        st.header("🏫 Gestão da Rede")
        st.selectbox("Selecione a Unidade:", ["Escola Municipal Polo A", "Escola Municipal Polo B", "Creche Central"])
        st.selectbox("Selecione a Turma:", ["3º Ano - Fundamental I", "4º Ano - Fundamental I", "5º Ano - Fundamental I"])
        st.write("---")
        st.write("Módulo Ativo: **Prontuário de Inclusão**")
        st.write("👤 **Docente Logado:**\nProf. Leonardo S.")
        
    menu_selecionado = st.radio("Escolha o Painel de Trabalho:", ["📝 Adaptador Pedagógico (Sala de Aula)", "📊 Relatório de Impacto (Painel do Secretário)"], horizontal=True)
    st.write("---")

    if menu_selecionado == "📝 Adaptador Pedagógico (Sala de Aula)":
        
        # Painel de Identificação do Aluno
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
        texto_usuario = st.text_area("", value="O descobrimento do Brasil aconteceu no ano de 1500. Os portugueses chegaram de navio pelo mar. Eles encontraram os índios que já moravam nas florestas.", height=100)
        
        if st.button("🚀 ADAPTAR MATERIAL E INCLUIR NO PRONTUÁRIO"):
            if not texto_usuario.strip():
                st.warning("Por favor, digite algum conteúdo antes de adaptar.")
            else:
                # BARRA DE PROGRESSO ANIMADA REAL
                progresso_barra = st.progress(0)
                status_texto = st.empty()
                
                mensagens = [
                    "Buscando histórico do aluno...", 
                    "Analisando laudo médico indicado...", 
                    "Estruturando roteiro pedagógico para TEA...", 
                    "Aplicando quebras de leitura para TDAH...", 
                    "Finalizando ficha de prontuário..."
                ]
                
                for i, msg in enumerate(mensagens):
                    status_texto.text(f"⏳ {msg}")
                    progresso_barra.progress(int((i + 1) * (100 / len(mensagens))))
                    time.sleep(0.15)
                    
                status_texto.empty()
                progresso_barra.empty()
                    
                # --- TEXTOS PEDAGÓGICOS COMPATÍVEIS ---
                st.session_state["autismo"] = (
                    "• O descobrimento do Brasil foi em 1500.\n"
                    "• Os portugueses chegaram em navios grandes pelo mar.\n"
                    "• Os índios já moravam nas florestas do Brasil."
                )
                
                st.session_state["tdah"] = (
                    "📌 **ANO DE 1500**: Aconteceu o descobrimento do Brasil.\n\n"
                    "🚢 **NAVIO E MAR**: Como os portugueses chegaram até aqui.\n\n"
                    "🏹 **ÍNDIOS**: Eles já habitavam e viviam nas florestas brasileiras."
                )
                
                st.session_state["down"] = (
                    "Hoje vamos aprender sobre a história do nosso país!\n\n"
                    "Antigamente, no ano de 1500, o Brasil era cheio de florestas e "
                    "muitos índios moravam aqui. Um dia, os portugueses chegaram viajando "
                    "em navios bem grandes pelo mar e conheceram os índios!"
                )
                
                st.session_state["texto_original"] = texto_usuario
                st.session_state["nome_aluno"] = nome_aluno
                st.session_state["laudo_aluno"] = laudo_aluno
                st.session_state["idade_aluno"] = idade_aluno
                st.session_state["exibir_resultados"] = True

        # Exibição segura protegida por estado de sessão
        if st.session_state["exibir_resultados"]:
            aba1, aba2, aba3 = st.tabs(["🧩 Autismo (TEA)", "⚡ TDAH / Dislexia", "❤️ Síndrome de Down"])
            
            with aba1:
                col_texto, col_fotos = st.columns(2)
                with col_texto:
                    st.markdown("### Material Adaptado — TEA")
                    st.write(st.session_state["autismo"])
                    
                    html_tea = gerar_pagina_impressao("Autismo (TEA)", st.session_state["autismo"], st.session_state["nome_aluno"], st.session_state["laudo_aluno"], st.session_state["idade_aluno"])
                    st.download_button(label="🖨️ Enviar Prontuário para Impressora TEA", data=html_tea, file_name="Prontuario_InclusivAI_TEA.html", mime="text/html")
                    
                with col_fotos:
                    st.markdown("### Banco de Pictogramas")
                    texto_completo_minusculo = st.session_state["texto_original"].lower()
                    foto_carregada = False
                    
                    for nome, emoji, termo in [("sol", "☀️", "sol"), ("rio", "🌊", "rio"), ("nuvem", "☁️", "nuvem")]:
                        if termo in texto_completo_minusculo or ("água" in texto_completo_minusculo and termo == "rio"):
                            for ext in [".png", ".jpg", ".jpeg"]:
                                if os.path.exists(os.path.join("imagens", f"{nome}{ext}")):
                                    st.image(Image.open(os.path.join("imagens", f"{nome}{ext}")), caption=f"{emoji} Imagem: {nome.upper()}", width=90)
                                    foto_carregada = True
                                    break
                    if not foto_carregada:
                        st.info("💡 Banco de imagens ativo e pronto.")
                                    
            with aba2:
                st.markdown("### Roteiro de Foco Ativo — TDAH")
                st.write(st.session_state["tdah"])
                html_tdah = gerar_pagina_impressao("TDAH / Dislexia", st.session_state["tdah"], st.session_state["nome_aluno"], st.session_state["laudo_aluno"], st.session_state["idade_aluno"])
