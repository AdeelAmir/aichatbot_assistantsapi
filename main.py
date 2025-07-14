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
def analyze_product_image(product_image_url):
    response = client.responses.create(
        model=model,
        instructions="",
        input=f"""
        
        """,
        temperature=0.2
    )

    return response.output_text

# Example with a sports team image
analysis = analyze_product_image(
    "https://upload.wikimedia.org/wikipedia/commons/a/a5/Barcelona_fc_lamina_elgrafico.jpg")
print(analysis)





