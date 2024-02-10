import openai

openai.api_key = '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'


# Initialize the conversation history with a system message
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
]

def ask_chatbot(user_input):
    # user_input = input("You: ")
    conversation_history.append({"role": "user", "content": user_input})

    # Generate response from GPT-3.5 using the chat completions endpoint
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate model name
        messages=conversation_history
    )

    # Extract and print the model's reply
    reply = response['choices'][0]['message']['content']
    # print(f"Chatbot: {reply}")

    # Append the AI's reply to the conversation history
    conversation_history.append({"role": "assistant", "content": reply})
    return reply

# while True:
#     ask_chatbot(input("Ask : "))

































# import json
# import requests

# def fetch_from_google(query):
#     api_key = "AIzaSyBVTNW1Z2VEkLcgSjW9q71hvFgu81Tlpyk"
#     engine_id = "4157e0d91e4b64fd5"
#     search_url = "https://www.googleapis.com/customsearch/v1"
#     params = {
#         "key": api_key,
#         "cx": engine_id,
#         "q": query
#     }
#     response = requests.get(search_url, params=params)
#     data = response.json()

#     if "items" in data:
#         # Extract and return the first search result
#         return data["items"][0]["snippet"]
#         # return data
#     else:
#         return "Sorry, I couldn't find any relevant information."

# def search_online(user_input):
#     # Implement code to search the user input online (e.g., using a search engine API)
#     # For example, we can use the DuckDuckGo Instant Answer API
#     search_url = f"https://api.duckduckgo.com/?q={user_input}&format=json"
#     response = requests.get(search_url)
#     if response.status_code == 200:
#         data = response.json()
#         if 'AbstractText' in data:
#             return data['AbstractText']
#     return None



# def chat_bot(user_input):
#     # Load the JSON data
#     with open('responses.json', 'r') as json_file:
#         data = json.load(json_file)

#     # Check if the user input is in the JSON data
#     if user_input in data:
#         return data[user_input]

#     # If the user input is not in the JSON data, search for the response online
#     else:
#         # Implement code to search for the response online (e.g., using a search engine API)
#         response = search_online(user_input)

#         if response!=None:
#             # Add the response to the JSON data
#             data[user_input] = response

#             # Save the updated JSON data back to the file
#             with open('responses.json', 'w') as json_file:
#                 json.dump(data, json_file, indent=4)

            
#         else:
#             response=fetch_from_google(user_input)
#             data[user_input] = response

#             # Save the updated JSON data back to the file
#             with open('responses.json', 'w') as json_file:
#                 json.dump(data, json_file, indent=4)
#     return response



