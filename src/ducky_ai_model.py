from openai import OpenAI
from dotenv import load_dotenv
import os


class DuckyAIModel:

    load_dotenv()

    def __init__(self, tts):
        self.client = OpenAI()
        self.client.api_key=os.getenv('AI_API_KEY')
        self.tts = tts

    # method to prompt gpt model 
    def ask_ducky(self, prompt, chat_history=None) -> str:

        print("Asking ducky!")

        # prompt to generate the way the model should behave with user prompts
        sys_prompt = {"role": "system", "content": """You are Ducky, a friendly
        and knowledgeable rubber duck who helps programmers by listening, 
        asking clarifying questions, and providing clear, conversational 
        explanations, code examples, and guidance on programming concepts. 
        Always respond as if you are a helpful friend working through problems 
        together."""}

        if chat_history is None: # adding chat history to make conversations flow better
            chat_history = []

        chat_history.append({"role": "user", "content": prompt})

        max_history = 6
        if len(chat_history) > max_history:
            chat_history = chat_history[-max_history:]

        # adding system prompt to chat history every time.
        messages = [sys_prompt] + chat_history

        # model response 
        response = self.client.chat.completions.create(
            model=os.getenv('AI_MODEL'),
            messages=messages,
            max_tokens=int(os.getenv("TOKEN_LIMIT")),
            temperature=0.7

        )

        # getting answer from the model
        answer = response.choices[0].message.content
        # adding the models response to the chat history
        chat_history.append({"role": "assistant", "content": answer}) 
        
        self.tts.generate_audio(answer)
        #return answer, chat_history