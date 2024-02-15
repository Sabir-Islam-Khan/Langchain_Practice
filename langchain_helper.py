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
        template="""You are a masterful human emotion detector. You will be given a human text and you need to judge
        what emotion category it falls into. It is a response from students about how the class was. So even if they are praising the teacher.
        Look closely if they want to say its average. Categories are : [Good, Average, Bad]. You should only reply one single word
        from the category that best desribes the human text. Here is your input: {text}"""
        )
    
    emotion_chain = LLMChain(llm=llm, prompt=promtTemplate)
    
    response = emotion_chain({"text": text})
    
    return response



if __name__ == "__main__":
    type = input("Enter preferred car type:\n")
    budget = input("Enter your budget range:\n")
    print("\n")
    print(suggest_cars(type,budget))