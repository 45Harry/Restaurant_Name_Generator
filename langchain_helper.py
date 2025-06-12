import os
from secret_key import grok_key
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import SequentialChain


def generate_restaurant_name_and_fooditems(cuisine):
    # For Restaurant Name
    llm = ChatGroq(
        temperature=0.6,
        model_name="llama-3.3-70b-versatile",
        api_key=grok_key
    )

    # Create prompt template
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant for {cuisine} food. Suggest a single fancy name for this. No presemble'
    )

    # Create chain
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')
    # For Food Items
    llm = ChatGroq(temperature=0.7, model_name="llama-3.3-70b-versatile", api_key=grok_key)

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template='Suggest some menu items for {restaurant_name}. Return it as a comma seperated list. No Presemble'
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')


    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items'])

    response = chain.invoke({'cuisine': cuisine})

    return  response


if __name__ == '__main__':
    print(generate_restaurant_name_and_fooditems('Indian'))


