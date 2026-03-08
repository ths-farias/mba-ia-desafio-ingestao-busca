from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

from search import search_prompt
from langchain.agents import create_agent
from langchain.messages import AIMessage, HumanMessage

load_dotenv()


def main():
    model = None

    if os.getenv("OPENAI_API_KEY"):
        model = ChatOpenAI(model="gpt-5-nano", temperature=0.7)
    elif os.getenv("GOOGLE_API_KEY"):
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    else:
        raise ValueError("API_KEY environment variable is not set")

    print("Faça sua pergunta:")
    pergunta = input("PERGUNTA: ")
    prompt = search_prompt(pergunta)

    agent = create_agent(
        model=model,
        system_prompt=prompt,
    )

    human_msg = HumanMessage(pergunta)

    response = agent.invoke({"messages": [human_msg]})
    message: AIMessage = response["messages"][1]
    print("RESPOSTA: ", message.content)


if __name__ == "__main__":
    main()
