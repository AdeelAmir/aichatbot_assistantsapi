import json
from email.policy import strict
from fileinput import close

import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv()
client = openai.OpenAI()
model = "gpt-4.1-nano"

# First Example - automatically generate compelling product descriptions based on basic product details
# def generate_product_description(product_name, product_features, target_audience, product_price):
#     response = client.responses.create(
#         model=model,
#         instructions="You are a professional copywriter to write compelling, concise product descriptions. Focus on product benefits rather than its features.",
#         input=f"""
#         Create product description for product name given inside three character delimiter
#
#         Product Name: '''{product_name}'''
#         Product Features:
#         - {product_features[0]}
#         - {product_features[1]}
#         - {product_features[2]}
#
#         Target Audience: {target_audience}
#         Product Price: {product_price}
#
#         OUTPUT_FORMAT:
#         The output must be in valid JSON format, without any special characters, markdown, or quotation formatting (e.g., no triple quotes or backticks).
#
#         json_format: {{
#             'short_description': '<short product description of 20 words>',
#             'product_benefits': '<array of product benefits upto 3>',
#             'product_features': '<array of product features upto 3>',
#             'target_audience': '<target audience>',
#             'product_price': '<product price>',
#         }}
#
#          Keep it under 150 words.
#         """,
#         temperature=0.7,
#         max_output_tokens=150
#     )
#
#     return response.output_text
#
# product_description = generate_product_description("HP Pavilion 15", ["11th Gen Intel Core i5 Processor", "15.6 inch Full HD Display", "512GB SSD + 8GB RAM"], "Students, remote workers", "$649 USD")
#
# print(product_description)

# Second Example - e-commerce platforms need to analyze product photos
# def analyze_product_image(image_url):
#     response = client.responses.create(
#         model=model,
#         instructions="You are a product photography expert and ecommerce consultant",
#         input=[
#             {
#                 "role": "user",
#                 "content": f"""
#                 Analyze this product image and provide the following details: \n
#
#                 1. Product Category
#                 2. Product Color
#                 3. Product Brand
#                 4. Product Make
#                 5. Product Model
#
#                 Output Format (No special characters or formatting):
#                 Product Category: <category>
#                 Product Color: <color>
#                 Product Brand: <brand>
#                 Product Model: <model>
#                 """
#             },
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "input_image",
#                         "image_url": image_url
#                     }
#                 ]
#             }
#         ],
#         temperature=0.2
#     )
#
#     return response.output_text
#
# analysis = analyze_product_image("https://storage.googleapis.com/sogauto-522d4.firebasestorage.app/files/listings/File-20250714-095807-58033937.webp")
# print(analysis)

# Third Example - Response Streaming
# def customer_support_agent(customer_feedback):
#     print("Customer support agent: \n\n")
#
#     stream = client.responses.create(
#         model=model,
#         instructions="You are a customer support agent, Do the sentimental analysis of customer feedback, provide key issues of customer in feedback and actionable insights, Respond customer in a friendly way",
#         input=customer_feedback,
#         stream=True,
#         temperature=0.3,
#         max_output_tokens=300
#     )
#
#     full_response = ""
#
#     for event in stream:
#         if event.type == "response.output_text.delta":
#             print(event.delta, end="")
#             full_response += event.delta
#
#         elif event.type == "response.error":
#             print(f"\n\nError: {event.error}")
#
#     return full_response
#
# feedback = f"""
#         I was using postman software for last three years and its working good for me \n
#         but one thing i saw incase I dont have API collection of software but have code, \n
#         its very difficult to manually create an API collection. To create AI based solution \n
#         which review code and auto create api collection with all the apis required in postman, \n
#         i am looking for postman developer API but postman is not providing it.
#
#         OUTPUT_FORMAT:
#         The output must be in valid JSON format, without any special characters, markdown, or quotation formatting (e.g., no triple quotes or backticks).
#
#         json_format: {{
#             "sentimental_analysis": <sentimental analysis of customer feedback>,
#             "key_issues": <highlight key issues of customer>,
#             "actionable_insights": <actionable insights of customer feedback>,
#             "respond_to_customer": <your response to customer>
#         }}"""
#
# response = customer_support_agent(feedback)

# Example 4 - Internet based searching to answer customer queries
# def ai_web_agent(query):
#     stream = client.responses.create(
#         model="gpt-4o",
#         tools=[{ "type": "web_search_preview" }],
#         stream=True,
#         input=query,
#         max_output_tokens=200
#     )
#
#     full_response = ""
#
#     for event in stream:
#         if event.type == "response.output_text.delta":
#             print(event.delta, end="")
#             full_response += event.delta
#         elif event.type == "response.error":
#             print(f"\nError Occured: {event.error}")
#
#
#     return full_response
#
# customer_query = "What are LLMs? How OPEN AI is better than Claude? In which domain Claude is best? Response should be under 200 words"
# agent_response = ai_web_agent(customer_query)

# Example 5 - File based searching

# Example 6 - Function Calling

# Dictionary of exchange rates (relative to USD)
# exchange_rates = {
#     "USD": 1.0,
#     "EUR": 0.93,
#     "GBP": 0.79,
#     "JPY": 153.2,
#     "CAD": 1.37,
#     "AUD": 1.52
# }
#
# def convert_currency(amount, from_currency, to_currency):
#     """Convert an amount from one currency to another."""
#     # Normalize currency codes to uppercase
#     from_currency = from_currency.upper()
#     to_currency = to_currency.upper()
#
#     # Check if currencies are supported
#     if from_currency not in exchange_rates:
#         return {"error": f"Currency not supported: {from_currency}"}
#     if to_currency not in exchange_rates:
#         return {"error": f"Currency not supported: {to_currency}"}
#
#     # Convert to USD first, then to target currency
#     amount_in_usd = amount / exchange_rates[from_currency]
#     converted_amount = amount_in_usd * exchange_rates[to_currency]
#
#     return {
#         "original_amount": amount,
#         "from_currency": from_currency,
#         "to_currency": to_currency,
#         "converted_amount": round(converted_amount, 2)
#     }
#
# tools = [
#    {
#        "type": "function",
#        "name": "convert_currency",
#        "description": "Convert an amount from one currency to another using current exchange rates",
#        "parameters": {
#            "type": "object",
#            "properties": {
#                "amount": {
#                    "type": "number",
#                    "description": "The amount of money to convert"
#                },
#                "from_currency": {
#                    "type": "string",
#                    "description": "The currency code to convert from (e.g., USD, EUR, GBP)"
#                },
#                "to_currency": {
#                    "type": "string",
#                    "description": "The currency code to convert to (e.g., USD, EUR, GBP)"
#                }
#            },
#            "required": ["amount", "from_currency", "to_currency"],
#            "additionalProperties": False
#        },
#        "strict": True
#    }
# ]
#
# input_messages = [
#    {"role": "user", "content": "How much is 100 euros in Japanese yen?"}
# ]
#
# response = client.responses.create(
#    model="gpt-4o",
#    input=input_messages,
#    tools=tools,
# )
#
# tool_call = response.output[0]
# print(f"Function called: {tool_call.name}")
# print(f"Arguments: {tool_call.arguments}")
#
# args = json.loads(tool_call.arguments)
#
# # Execute the function with the parameters determined by the model
# conversion_result = convert_currency(**args)
# print(f"Function results: {conversion_result}")

# List of exchange rates
# exchange_rates = {
#     "USD": 1.0,
#     "EUR": 0.93,
#     "GBP": 0.79,
#     "JPY": 153.2,
#     "CAD": 1.37,
#     "AUD": 1.52,
#     "PKR": 284.5
# }
#
# def convert_currency(amount, from_currency, to_currency):
#     """Convert an amount from one currency to another."""
#     # Normalize currency codes to uppercase
#     from_currency = from_currency.upper()
#     to_currency = to_currency.upper()
#
#     # Check if currencies are supported
#     if from_currency not in exchange_rates:
#         return {"error": f"Currency not supported: {from_currency}"}
#     if to_currency not in exchange_rates:
#         return {"error": f"Currency not supported: {to_currency}"}
#
#     # Convert to USD first, then to target currency
#     amount_in_usd = amount / exchange_rates[from_currency]
#     converted_amount = amount_in_usd * exchange_rates[to_currency]
#
#     return {
#         "original_amount": amount,
#         "from_currency": from_currency,
#         "to_currency": to_currency,
#         "converted_amount": round(converted_amount, 2)
#     }

# tools = [
#     {
#         "type": "function",
#         "name": "convert_currency",
#         "description": "Function to convert amount from one currency to another currency based on live currency rates",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "amount": {
#                     "type": "number",
#                     "description": "The amount to be converted from one currency to another."
#                 },
#                 "from_currency": {
#                     "type": "string",
#                     "description": "The currency code to convert from (e.g., USD, PKR, GBP)."
#                 },
#                 "to_currency": {
#                     "type": "string",
#                     "description": "The currency code to convert to (e.g., USD, PKR, GBP)."
#                 }
#             },
#             "required": ["amount", "from_currency", "to_currency"],
#             "additionalProperties": False
#         }
#     }
# ]
#
# response = client.responses.create(
#     model= model,
#     input= [
#         {
#             "role": "user",
#             "content": "I want to convert 100 pounds into pakistani rupees"
#         }
#     ],
#     tools= tools
# )
#
# tools_call = response.output[0]
# print(f"Function called: {tools_call.name}")
# print(f"Function arguments: {tools_call.arguments}")
#
# if tools_call.name == "convert_currency":
#
#     arguments = json.loads(tools_call.arguments)
#
#     conversion_response = convert_currency(**arguments)
#
#     print(conversion_response)
#
# else:
#     print("Cannot handle this query")

# def currency_assistant(user_message, conversation_history = None):
#
#     # create conversion history if not exists
#     if conversation_history is None:
#         conversation_history = []
#
#     # add user message into conversation history array
#     conversation_history.append({
#         "role": "user",
#         "content": user_message
#     })
#
#     # define available tools
#     tools = [
#         {
#             "type": "function",
#             "name": "currency_convertor",
#             "description": "Function to convert amount from one currency to another currency",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "amount": {
#                         "type": "number",
#                         "description": "The amount to be converted from one currency to another"
#                     },
#                     "from_currency": {
#                         "type": "string",
#                         "description": "The currency code of currency to convert from (e.g., USD, PKR)"
#                     },
#                     "to_currency": {
#                         "type": "string",
#                         "description": "The currency code of currency to convert to (e.g., USD, PKR)"
#                     }
#                 },
#                 "required": ["amount", "from_currency", "to_currency"],
#                 "additionalProperties": False
#             }
#         }
#     ]
#
#     response = client.responses.create(
#         model=model,
#         input=conversation_history,
#         tools=tools
#     )
#
#     if response.output and isinstance(response.output, list) and response.output[0].type == "function_call":
#
#         tool_calls = response.output[0]
#
#         # Process the function call
#         arguments  = json.loads(tool_calls.arguments)
#         result = convert_currency(**arguments)
#
#         # Add the function call and its results to conversation history
#         conversation_history.append(tool_calls)
#         conversation_history.append(
#             {
#                 "type": "function_call_output",
#                 "call_id": tool_calls.call_id,
#                 "output": json.dumps(result)
#             }
#         )
#
#         # Get the final response from agent
#         final_response = client.responses.create(
#             model=model,
#             input=conversation_history,
#             tools=tools
#         )
#
#         return final_response.output_text, conversation_history
#
#     else:
#         return response.output_text, conversation_history
#
# # Call Agent with user message 1
# user_message = "I want to convert 150 dollars into pakistani rupees"
# assistant_response, conversation = currency_assistant(user_message)
#
# print(f"User Message: {user_message}")
# print(f"Assistant Response: {assistant_response}")
#
# # Call Agent with user message 2
# user_message = "How much pounds for 200 euros"
# assistant_response, conversation = currency_assistant("How much pounds for 200 euros", conversation_history=conversation)
#
# print(f"User Message: {user_message}")
# print(f"Assistant Response: {assistant_response}")

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.93,
    "GBP": 0.79,
    "JPY": 153.2,
    "CAD": 1.37,
    "AUD": 1.52,
    "PKR": 284.5
}

def convert_currency(amount, from_currency, to_currency):
    """Convert an amount from one currency to another."""
    # Normalize currency codes to uppercase
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # Check if currencies are supported
    if from_currency not in exchange_rates:
        return {"error": f"Currency not supported: {from_currency}"}
    if to_currency not in exchange_rates:
        return {"error": f"Currency not supported: {to_currency}"}

    # Convert to USD first, then to target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]

    return {
        "original_amount": amount,
        "from_currency": from_currency,
        "to_currency": to_currency,
        "converted_amount": round(converted_amount, 2)
    }

# create currency conversion website ai-agent

def currency_conversion_agent(user_message, conversation_history = None):
    if conversation_history is None:
        conversation_history = []

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    tools = [
        {
            "type": "function",
            "name": "convert_currency",
            "description": "Function to convert amount from one currency to another currency",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "number",
                        "description": "The amount to be converted from one currency to another"
                    },
                    "from_currency": {
                        "type": "string",
                        "description": "The currency code of currency to convert from (e.g. USD, JYP, GBP)"
                    },
                    "to_currency": {
                        "type": "string",
                        "description": "The currency code of currency to convert to (e.g. USD, JYP, GBP)"
                    }
                },
                "required": ["amount", "from_currency", "to_currency"],
                "optionalProperties": False
            }
        }
    ]

    response = client.responses.create(
        model=model,
        input=conversation_history,
        tools=tools
    )


    if response.output and isinstance(response.output, list) and response.output[0].type == "function_call":
        tool_calls = response.output[0]

        arguments = json.loads(tool_calls.arguments)
        result = convert_currency(**arguments)

        # Add tool calls and its output into the conversion history
        conversation_history.append(tool_calls)
        conversation_history.append(
            {
                "type": "function_call_output",
                "call_id": tool_calls.call_id,
                "output": json.dumps(result)
            }
        )

        # generate final output
        final_output = client.responses.create(
            model=model,
            
        )









