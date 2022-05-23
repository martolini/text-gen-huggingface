from transformers import pipeline

def predict(input: str):
    generator = pipeline(task='text-generation')
    return generator(input, max_length=250)
