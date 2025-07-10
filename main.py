import openai

from dotenv import load_dotenv, find_dotenv

load_dotenv()

client = openai.OpenAI()

model = "gpt-4.1-nano"

# Create Personal Trainer Assistant
personal_trainer_assistant = client.beta.assistants.create(
    name="Personal Trainer",
    instructions="""You are the best personal trainer and nutritionist who knows how to get clients to \n
    build lean muscles. You've trained high-caliber athletes and movie stars""",
    model= model
)

assistant_id = personal_trainer_assistant.id
print(assistant_id)

# Create Thread
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "How do I get started working out to lose fat and build muscles?",
        }
    ]
)

thread_id = thread.id
print(thread_id)
































