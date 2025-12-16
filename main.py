from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

prompt = ChatPromptTemplate.from_template("You are a joker. Crack a joke on following {topic} using this style: {style}")

class JokeOutputParser(BaseModel):
    topic: str = Field(description="Topic of a joke")
    style: str = Field(description="Style of a joke")
    joke: str = Field(description="Joke of topic following of given style")


llm_structure_parser = llm.with_structured_output(JokeOutputParser)

chain = prompt | llm_structure_parser

result = chain.invoke({"topic": "AI", "style": "Sarcasm poetry"})
print(result)