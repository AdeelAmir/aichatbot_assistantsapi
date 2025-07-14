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