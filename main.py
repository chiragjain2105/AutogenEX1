from autogen import ConversableAgent
from autogen import UserProxyAgent
from dotenv import load_dotenv


load_dotenv()

llm_config = {
    "config_list" : [
        {
            "model": "llama3-8b-8192",
            "api_type": "groq",
        }
    ]
} 


user_proxy_agent = UserProxyAgent(name="User Agent", system_message="User proxy agent")


assistant_agent = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful travel assistant. Provide detailed and accurate information about travel destinations, activities, and best times to visit. Offer personalized recommendations based on the user's preferences.",
    llm_config=llm_config,
)

def main():
    while True:
        user_input = input("User: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Assistant: Goodbye! Have a great day!!")
            break

        user_proxy_agent.initiate_chat(assistant_agent, message=user_input)

if __name__ == "__main__":
    main()