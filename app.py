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
if "melhor_casal" not in st.session_state:
    st.session_state.melhor_casal = False

if st.button("Já dei play abre o livro logo garoto! 📖"):
    st.session_state.livro_aberto = True

if st.session_state.livro_aberto:
    # Capítulo 1
    st.header("Capítulo 1: Feitos um para o outro? ❤️")
    st.write("""
    Sophia, fiz esse pequeno livro digital só para você, bem pequeno mesmo kk.
    
    Mesmo sendo tão opostos em tantas coisas, estar com você é a melhor parte 
    dos meus dias. Obrigado por cada momento, cada conversa e por ser essa 
    pessoa incrível que você é. Espero que eu também possa fazer você feliz 
    e que se sinta especial também assim como você me faz eu me sentir,
    porque você é especial para mim, eu sinto como se tivesse realmente encontrado a pessoa certa, 
    e esse sentimento que não consigo transformar em palavras, espero que possa sentir também, estou sentindo nesse exato momento.
    como a gente se conheceu foi algo tão aleatório, em um jogo, e não acho que seremos assim para sempre
    por isso fiz isso, para saber que mesmo que nós separemos, saberá que teve alguém que amou você muito
    mesmo, eu só desejo o melhor pra você, mesmo que no futuro não estejamos mais juntos, porque acho que isso é o amor
    é bom, mas também machuca, e acho que não tem como amar sem se machucar um poquinho não é? Se eu tivesse que contar todos os motivos 
    pelos quais eu te amo, o resultado seria como o número Pi π infinito e impossível de terminar.
    
    
    Esse livro ainda tem muitas páginas em branco, e eu quero escrever todas 
    elas ao seu lado enquanto der.
    """)
    
    st.write("")
    
    # Capítulo 2
    st.header("Capítulo 2: Sobre Você ✨")
    st.write("""
    Se eu tivesse que escrever um livro inteiro só sobre você, ainda faltariam páginas. 
    Eu amo o seu jeito, o seu sorriso, o jeito como você enxerga as coisas e até os 
    pequenos detalhes que você acha que ninguém repara.
    
    Você tem uma luz própria que deixa tudo mais leve quando está por perto, eu acho que sou viciado em você, é inteligente, engraçada
    e fala bastante também, mas essa parte é a que eu mais gosto, você é linda, muito mesmo, queria que você pudesse ver com os meus olhos
    nem que fosse por um segudo, então ai você enxergaria, o quão incrível você é, exatamente do jeito que é, se tivesse uma música nossa
    acho que seria a Pixelated Kisses, porque a pior parte de amar você é ter que estar tão longe de você. 
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
        else:
            # Quando terminar a última estrofe, aparece a pergunta final do casal + DBD!
            st.write("---")
            st.subheader("Melhor casal? 👀")
            
            col_final1, col_final2 = st.columns(2)
            with col_final1:
                if st.button("Sim ❤️"):
                    st.session_state.melhor_casal = True
            with col_final2:
                if st.button("Claro 😎"):
                    st.session_state.melhor_casal = True
                    
            if st.session_state.melhor_casal:
                st.success("Eu amo você Sophia, agora me da sua conta do DBD por favor? ❤️")

# Créditos engraçados bem no cantinho lá embaixo
st.write("")
st.write("")
st.write("---")
st.caption("🛠️ *Agradecimentos especiais ao ChatGPT por me ajudar a programar isso do zero só pra fazer essa surpresa kkk, não tem nada de darkmoon aqui, fique tranquila.*")
