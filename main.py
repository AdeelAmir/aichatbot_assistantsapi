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
# def analyze_customer_feedback(feedback_text):
#     print("Analyze customer feedback in real time: \n")
#
#     stream = client.responses.create(
#         model=model,
#         instructions="",
#         input=feedback_text,
#         stream=True,
#         temperature=0.3,
#         max_output_tokens=150
#     )
#
#     full_response = ""
#
#     for event in stream:
#         if event.type == "response.output_text.delta":
#             print(event.delta, end="")
#             full_response += event.delta
#         elif event.type == "response.error":
#             print(f"\nError occurred: {event.error}")
#
#     return full_response
#
# # Example with a complex customer review
# feedback = """
# I've been using the SmartHome Hub for about 3 months now. The voice recognition is fantastic
# and the integration with my existing devices was mostly seamless. However, the app crashes
# at least once a day, and the night mode feature often gets stuck until I restart the system.
# Customer support was helpful but couldn't fully resolve the app stability issues.
# """
#
# analysis_result = analyze_customer_feedback(feedback)

def customer_support_agent(customer_feedback):
    stream = client.responses.create(
        model=model,
        instructions="",
        input="",
        stream=True,
        temperature=0.3,
        
    )