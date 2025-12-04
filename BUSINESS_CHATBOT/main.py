
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from business_info import info

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



def chat():

    print("Bienvenido al chat! Type 'exit' to quit.")
    context =""
    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            break
        result = chain.invoke({"business_organization": info,"context": context, "question": question})
        print("Elena:", result)
        context += f"\nElena: {result}\nYou: {question}\n"

if __name__ == "__main__":  
    chat()