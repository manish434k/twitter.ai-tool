"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

# [todo] Configure API key from environment variable
#genai.configure(api_key=os.environ["GEMINI_API_KEY"])
genai.configure(api_key='')

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[  ]
)


"""
Sends a tweet prompt to the chat session and generates a tweet.

Args:
    tweetPrompt (str): The prompt for the tweet generation.

Returns:
    str: The generated tweet text.
"""
def generate_tweet(tweetPrompt):
    print("Generating tweet: " + tweetPrompt)
    response = chat_session.send_message(tweetPrompt)
    return response.text


# response = chat_session.send_message("An overview on Germany's economy.")

# print(response.text)