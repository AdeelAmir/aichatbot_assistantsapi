import time

import openai

from dotenv import load_dotenv, find_dotenv
from pyexpat.errors import messages

load_dotenv()

client = openai.OpenAI()

model = "gpt-4.1-nano"

# Create Personal Trainer Assistant
# personal_trainer_assistant = client.beta.assistants.create(
#     name="Personal Trainer",
#     instructions="""You are the best personal trainer and nutritionist who knows how to get clients to \n
#     build lean muscles. You've trained high-caliber athletes and movie stars""",
#     model= model
# )
#
# assistant_id = personal_trainer_assistant.id
# print(assistant_id)
#
# # Create Thread
# thread = client.beta.threads.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "How do I get started working out to lose fat and build muscles?",
#         }
#     ]
# )
#
# thread_id = thread.id
# print(thread_id)

# Assistant & Thread Ids
# assistant_id = "asst_AnXVe0bRWgux0klwfqLQa7Mw"
# thread_id = "thread_ZomFgbScfuBXIdxxNRzyuRer"
#
# message = "How many reps do I need to do to build lean muscles?"
# message = client.beta.threads.messages.create(
#     thread_id=thread_id,
#     role="user",
#     content=message
# )
#
# # Run the thread
# run = client.beta.threads.runs.create(
#     thread_id=thread_id,
#     assistant_id=assistant_id,
#     instructions="Please address the user as James Bond"
# )
#
# def wait_for_run_completion(client, thread_id, run_id, sleep_interval = 5):
#     while True:
#         try:
#             run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
#             if run.completed_at:
#                 print("Thread run completed")
#                 messages = client.beta.threads.messages.list(thread_id=thread_id)
#                 last_message = messages.data[0]
#                 response = last_message.content[0].text.value
#                 print(f"Assistants Response: {response}")
#                 break
#         except Exception as e:
#             print(f"An error occurred while retrieving the run: {e}")
#             break
#         time.sleep(sleep_interval)
#
# # Run
# wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id, sleep_interval=5)


# PRACTICE CODE

# Create Assistant
# fitness_training_assistant = client.beta.assistants.create(
#     name = "Personal Trainer",
#     instructions="""You are the best personal trainer and nutritionist who knows how to get clients to build lean muscles.\n
#         You've trained high-caliber athletes and movie stars""",
#     model=model
# )
# assistant_id = fitness_training_assistant.id
# print(assistant_id)

# Create Thread
# thread = client.beta.threads.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "How do I get started working out to lose fat and build muscles?",
#         }
#     ]
# )
# thread_id = thread.id
# print(thread_id)

assistant_id = "asst_dEOjoWSKv7kvYMW82POJLn3K"
thread_id = "thread_4Ft444Mihe1pEPtCs2xvGeZg"

# Create Run
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content= "How many reps do I need to do to build lean muscles?"
)

run = client.beta.threads.runs.create(
    assistant_id=assistant_id,
    thread_id=thread_id,
    instructions="Treat user as James Bond"
)

def wait_for_run_completion(client, thread_id, run_id, sleep_interval):














































