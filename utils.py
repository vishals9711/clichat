from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
import os

from models import CodeHelper

# Avoid hardcoding API keys in the code
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

def get_chat_response(message) -> str:
    try:
        if not OPENAI_API_KEY:
            raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY in your environment.")

        model = ChatOpenAI(temperature=0, api_key=OPENAI_API_KEY)
        parser = PydanticOutputParser(pydantic_object=CodeHelper)

        prompt = PromptTemplate(
            template="You are a coding assistant your objective is to help user with their command line queries. And provide useful description for the given code. \n{format_instructions}\n{query}\n",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        chain = prompt | model | parser
        output = chain.invoke({"query": message})
        return output.json()
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e
