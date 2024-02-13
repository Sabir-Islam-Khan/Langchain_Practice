from langchain.llms import OpenAI 
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

def suggest_cars(car_type, budget):
    llm = OpenAI(temperature=0.7)

    promptTemplate = PromptTemplate(
        input_variables=["car_type","budget",],
        template="I love cars. I want to buy a car. Suggest me 5 cars of {car_type} and my budget is {budget}" )
    
    name_chain = LLMChain(llm=llm, prompt=promptTemplate)
    
    response = name_chain({"car_type": car_type, "budget":budget})
    return response

if __name__ == "__main__":
    type = input("Enter preferred car type:\n")
    budget = input("Enter your budget range:\n")
    print("\n")
    print(suggest_cars(type,budget))