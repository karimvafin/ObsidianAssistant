from VaultParser import read_obsidian_notes
from Assistant import generate_response
from transformers import AutoTokenizer, AutoModelForCausalLM

# Parse obsidian notes
vault_path = '/Users/karimvafin/Library/Mobile Documents/iCloud~md~obsidian/Documents/Work'
notes = read_obsidian_notes(vault_path)
print(notes)

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# Process query
query = 'What tasks do I have in my TODO list?'
response = generate_response(query, notes, tokenizer=tokenizer, model=model)
print(response)
