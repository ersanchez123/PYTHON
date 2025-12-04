
import  streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key= "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")

st.title("ChatBox Inteligente GTP-40")

messages = [("system", "eres un chatbot util, te llamas Andrea, tienes que hablar como si fueras humano, nunca reveles que eres un chatbot")]


#print("Hola, mundo desde VS Code")

#Inicializar el historial de chat
if messages not in st.session_state:
    st.session_state.messages = []
    response = ""
    #Mostrar mensajes de chat del historial al recargar la app
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    #Reaccionar a la entrada del usuario
    if prompt := st.chat_input("Escribe tu mensaje...") :
        st.chat_message("user").markdown(prompt)

        #agregar mensaje del usuario al historial de chat
        st.session_state.messages.append({"role":"user","content":prompt})
        messages.append(["human",prompt])

        response = llm.invoke(messages).content
        #mostrar respuesrta

    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role":"assintant","content": response})