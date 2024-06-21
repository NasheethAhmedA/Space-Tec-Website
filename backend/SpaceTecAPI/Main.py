import sys
from fastapi import FastAPI
sys.path.append("..")
from AI_ChatBot.AI_Gen import Reply, Client

app = FastAPI()
my_client = Client()


@app.get("/chatbot/{message}")
async def root(message: str):
    """
    This endpoint is used to get the response from the chatbot.
    """
    return {"Reply": Reply(my_client, message)}



# while True:
#     user_input = input("You: ")
#     print("Bot:", Reply(my_client, user_input))
#     if user_input.lower() == "exit":
#         break





