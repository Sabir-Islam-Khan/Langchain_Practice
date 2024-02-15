from langchain.llms import OpenAI 
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent 
from langchain.agents import AgentType 


load_dotenv()


def detectEmotion(text):
    llm = OpenAI(temperature=0.5)
    promtTemplate = PromptTemplate( 
        input_variables=["emotion"],
        template="""You are an expert in understanding student sentiments about their classes. Your task is to categorize the
        emotion conveyed in the provided text. Imagine you're assessing feedback from university students about their 
        recent class experience. The categories you'll use are: Good, Average, and Bad. Consider all aspects of the 
        feedback, including praise, criticism, and nuances in expression. Here is the text you need to evaluate: "{text}"
        Please respond with one of the following categories: Good, Average, Bad."""
        )
    
    emotion_chain = LLMChain(llm=llm, prompt=promtTemplate)
    
    response = emotion_chain({"text": text})
    
    return response



if __name__ == "__main__":
    type = input("Enter preferred car type:\n")
    budget = input("Enter your budget range:\n")
    print("\n")
    print(suggest_cars(type,budget))