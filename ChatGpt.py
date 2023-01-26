import openai

# Set the API key
openai.api_key = "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"

# Define the prompt
print("scrie o intrebare")
prompt = input()

# Generate text
completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7
)

# Print the generated text
generated_text = completions.choices[0].text
print(generated_text)