from transformers import pipeline

# Load AI Model
generator = pipeline("text-generation", model="Salesforce/codegen-350M-mono")

def generate_code(prompt):
    response = generator(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']
