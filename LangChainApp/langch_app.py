from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def nombre_empresa(empresa):
    llm = OpenAI(temperature=0.6)
    prompt_template_name = PromptTemplate(
        input_variable = ["empresa"],
        template = "Me gustaría iniciar un emprendimineto en {empresa}. Devuelveme una lista de cinco nombres adecuados a mi negocio."
    )
    name = LLMChain(llm = llm, prompt = prompt_template_name)
    response = name({"empresa": nombre_empresa})
    
    return response

if __name__ == "_main_":
    print(nombre_empresa("empresa"))