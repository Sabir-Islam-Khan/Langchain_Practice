from langchain.llms import OpenAI 
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent 
from langchain.agents import AgentType 


load_dotenv()

def suggest_cars(car_type, budget):
    llm = OpenAI(temperature=0.7)

    promptTemplate = PromptTemplate(
        input_variables=["car_type","budget",],
        template="I love cars. I want to buy a car. Suggest me 5 cars of {car_type} and my budget is {budget}" )
    
    name_chain = LLMChain(llm=llm, prompt=promptTemplate)
    
    response = name_chain({"car_type": car_type, "budget":budget})
    return response

def calculateAverage(origin, budget): 
    llm = OpenAI(temperature = 0.7)
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    
    agent = initialize_agent(
        tools = tools, llm=llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True,
    )
    
    result = agent.run("I love loud and noisy cars. I love drift and muscle cars more. My favourite origin country is {origin} and budget is {budget}. Suggest me some cars. Also tell me the average price of cars or my favourite origin.")
    
    return result 


if __name__ == "__main__":
    type = input("Enter preferred car type:\n")
    budget = input("Enter your budget range:\n")
    print("\n")
    print(suggest_cars(type,budget))