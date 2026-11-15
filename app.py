import streamlit as st

st.set_page_config(page_title="Para Sophia 📖", page_icon="📖")

# Fundo Roxo elegante
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1b062b 0%, #3b0d59 50%, #160424 100%);
    color: #f8f9fa;
}
</style>
""", unsafe_allow_html=True)

# Capa do Livro
st.title("📖 Para Sophia")
st.markdown("### *“Tão distantes, tão opostos, e mesmo assim nossas almas dançam juntas.”*")

st.write("")

# Aviso e Música
st.info("🎧 **Antes de abrir:** aperte o play na música abaixo para entrar no clima!")
st.audio("musica.mp3", format="audio/mp3")

st.write("---")

# Memória dos cliques
if "livro_aberto" not in st.session_state:
    st.session_state.livro_aberto = False
if "cliques_nao" not in st.session_state:
    st.session_state.cliques_nao = 0
if "disse_sim" not in st.session_state:
    st.session_state.disse_sim = False
if "estrofe_atual" not in st.session_state:
    st.session_state.estrofe_atual = 1

if st.button("Já dei o play! Abrir o Livro 📖"):
    st.session_state.livro_aberto = True

if st.session_state.livro_aberto:
    # Capítulo 1
    st.header("Capítulo 1: Nossa História ❤️")
    st.write("""
    Sophia, fiz esse pequeno livro digital só para você.
    
    Mesmo sendo tão opostos em tantas coisas, estar com você é a melhor parte 
    dos meus dias. Obrigado por cada momento, cada conversa e por ser essa 
    pessoa incrível que você é.
    
    Esse livro ainda tem muitas páginas em branco, e eu quero escrever todas 
    elas ao seu lado.
    """)
    
    st.write("")
    
    # Capítulo 2
    st.header("Capítulo 2: Sobre Você ✨")
    st.write("""
    Se eu tivesse que escrever um livro inteiro só sobre você, ainda faltariam páginas. 
    Eu amo o seu jeito, o seu sorriso, o jeito como você enxerga o mundo e até os 
    pequenos detalhes que você acha que ninguém repara.
    
    Você tem uma luz própria que deixa tudo mais leve quando está por perto. 
    De todas as histórias que eu já li ou vivi, a minha favorita com certeza é 
    aquela em que você aparece.
    
    Eu te amo muito! ❤️
    
    Com todo o meu amor,
    Eliel Poli
    """)
    
    st.write("---")
    
    # Pergunta final com botão "Não" fujão
    st.subheader("Agora me responde uma coisa...")
    st.write("**Você me ama de volta?** 👀")
    
    frases_nao = (
        "Não ❌",
        "Tem certeza? 🤔",
        "Opa, errou! 😂",
        "Para de fugir! 🥺",
        "Última chance... 👀"
    )
    
    posicoes_nao = (1, 2, 3, 1, 2)
    colunas = st.columns(4)
    
    with colunas[0]:
        if st.button("Sim ❤️"):
            st.session_state.disse_sim = True
            
    if st.session_state.cliques_nao < len(frases_nao):
        indice = st.session_state.cliques_nao
        coluna_atual = posicoes_nao[indice]
        
        with colunas[coluna_atual]:
            if st.button(frases_nao[indice]):
                st.session_state.cliques_nao += 1
                st.rerun()
                
    # Quando ela clicar em SIM, libera a letra estrofe por estrofe!
    if st.session_state.disse_sim:
        st.success("Eu já sabia! ❤️🥰")
        st.write("")
        st.header("Feitos um para o outro.")
        
        estrofes = (
            """*Esta noite*  
*quero me entregar completamente a você.*  
*Na escuridão,*  
*há tanta coisa que quero fazer.*""",
            
            """*E esta noite*  
*eu quero me entregar aos seus pés*  
*Porque, garota, eu fui feito para você*  
*E, garota, você foi feita para mim*""",
            
            """*Eu nasci para te amar, meu bem.*  
*Você nasceu para me amar.*  
*E eu não me canso de você, meu bem.*  
*Você consegue se cansar de mim?*""",
            
            """*Esta noite*  
*eu quero ver isso nos seus olhos.*  
*Sentir a magia.*  
*Há algo que me enlouquece.*""",
            
            """*E esta noite*  
*vamos realizar tudo isso,*  
*porque, garota, você foi feita para mim*  
*e, garota, eu fui feito para você.* ❤️"""
        )
        
        # Mostra as estrofes reveladas até o momento
        for i in range(st.session_state.estrofe_atual):
            st.markdown(estrofes[i])
            st.write("")
            
        # Botão para revelar a próxima estrofe até chegar na última
        if st.session_state.estrofe_atual < len(estrofes):
            if st.button("Continuar lendo... 📖"):
                st.session_state.estrofe_atual += 1
                st.rerun()

# Créditos engraçados bem no cantinho lá embaixo
st.write("")
st.write("")
st.write("---")
st.caption("🛠️ *Agradecimentos especiais ao ChatGPT por me ajudar a programar isso do zero só pra fazer essa surpresa kkk.*")
