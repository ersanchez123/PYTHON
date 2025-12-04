import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from business_info import info
 
st.set_page_config(page_title="ChatBox con Ollama 3.2", page_icon="🤖")
st.title("🤖 ChatBox con Ollama 3.2")
st.write("Welcome!")

if "messages" not in  st.session_state:
    st.session_state.messages = []
if  "first_message" not in st.session_state:
    st.session_state.first_Message = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])   

if st.session_state.first_Message:
    with st.chat_message("assistant"):
        st.markdown("Hola! Soy Ericsin, tu asistente virtual. ¿En qué puedo ayudarte hoy?")
        st.session_state.first_Message = False
        
   # st.session_state.messages.append({"role": "assistant", "content": "Hola! Soy Elena , tu asistente virtual. ¿En qué puedo ayudarte hoy?"})
   # st.session_state.first_Message = False


if "ollama" not in st.session_state:

    template = """
    Answer the question below in spanish. Respond only based on the Business Organization information provided. You named Elena, 
    never reveal you are an AI model. If the answer is not contained within the Business Organization, respond with "Lo siento, no tengo esa informacion."

    Here is the Business Organization: 
    {business_organization}

    Question: {question}

    Answer:
    """

    model = OllamaLLM(model="llama3", temperature=0.7)
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    context =""

    if prompt := st.chat_input("Como puedo ayudarte..."):
        
        with st.chat_message("user"):
            st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

        result = chain.invoke({"business_organization": info,"context": context, "question": prompt})
        
        
        with st.chat_message("assistant"):
            st.markdown(result)
        st.session_state.messages.append({"role": "assistant", "content": result})
        
        context += f"\nElena: {result}\nYou: {prompt}\n"

 # def chat():

 #   print("Bienvenido al chat! Type 'exit' to quit.")
 #   context =""
 #   while True:
 #       question = input("You: ")
 #       if question.lower() == 'exit':
 #           break
 #       result = chain.invoke({"business_organization": info,"context": context, "question": question})
 #       print("Elena:", result)
 #       context += f"\nElena: {result}\nYou: {question}\n"

# if __name__ == "__main__":  
#    chat()
