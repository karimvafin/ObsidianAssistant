from VaultParser import read_obsidian_notes
from Assistant import generate_response
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

login(token='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')

# Parse obsidian notes
vault_path = '/Users/karimvafin/Library/Mobile Documents/iCloud~md~obsidian/Documents/Work'
notes = read_obsidian_notes(vault_path)
print(notes)

# Initialize tokenizer and model
model_checkpoint = 'mistralai/Mistral-7B-v0.1'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForCausalLM.from_pretrained(model_checkpoint)

# Process query
query = 'What tasks do I have in my TODO list?'
response = generate_response(query, notes, tokenizer=tokenizer, model=model)
print(response)
