from typing import Dict


def generate_response(query: str, docs: Dict[str, str], model, tokenizer) -> str:
    context = ''.join(docs.values())
    prompt = (f'Answer the query according to provided context.\n'
              f'Query: {query}'
              f'Context: {context}')
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
