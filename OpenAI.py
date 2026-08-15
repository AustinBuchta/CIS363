from openai import OpenAI


client = OpenAI(
  api_key=("OPENAI_API_KEY")
)

message = ""
messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("\nYour new assistant is ready!")
print("Start by typing a message and pressing enter. To quit, type STOP\n")

while message != "STOP":
    message = input("Austin:   ")
    if message != "STOP":
        messages.append({"role": "user", "content": message})
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            reply = response.choices[0].message.content
            print("\nLight: " + reply + "\n")
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"Error occurred: {e}")
            break

print("Session Murdered.")
