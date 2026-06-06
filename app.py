print("Hello Ronak!")

import google.generativeai as genai

# Paste your Gemini API key here
genai.configure(api_key="AQ.Ab8RN6I_2WAqU_7KaTo4rhQ8clkEOvkyYTvYHhUdKf7LLrKUgw")

model = genai.GenerativeModel("gemini-2.5-flash")

print("=== AI Career Assistant ===")
print("Type 'exit' to stop")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = model.generate_content(question)

    print("\nAI:", response.text)