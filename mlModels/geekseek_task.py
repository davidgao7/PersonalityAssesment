# new_task.py
from openai import OpenAI
from dotenv import load_dotenv
import os
# import pandas as pd

load_dotenv()

# Initialize the client
client = OpenAI(
    api_key=os.environ["DEEPSEEK_API"],
    base_url="https://api.deepseek.com"
)

system_role = """
1. You are a psychology expert;
2. I hope you can perform a Big Five personality prediction;
3. I will input a string of text, and you need to return the personality type. The Big Five personalities include: 'Extroversion', 'Neuroticism', 'Agreeableness', 'Conscientiousness', 'Openness';
4. You need to provide the percentage for each personality trait, ranging from 0% to 100%, and you can keep one decimal place.
5. Then give the top 3 job recommendations based on the Big Five personalities result.
"""

#TaskInput = """
#I am Neuroticism.
#"""

# # Read the CSV file
# file_path = "Personality_Test.csv"  # Ensure the path is correct
# df = pd.read_csv(file_path)
#
# # Process the first 4 samples
# num_samples = 4  # Only process the first 4 samples
# for i in range(num_samples):
#     # Get the first 25 columns of data and merge them into a string
#     sample_text = " ".join(df.iloc[i, :25].astype(str))  # Get the first 25 columns and merge
#
#     # Build TaskInput
#     TaskInput = f"""
#     Here is the user's psychological test data:
#     {sample_text}
#     Please predict the user's Big Five personality based on this data.
#     """
#
#     # Call the API
#     response = client.chat.completions.create(
#         model="deepseek-chat",
#         messages=[
#             {"role": "system", "content": system_role},  # System role
#             {"role": "user", "content": TaskInput},  # User input
#         ],
#         stream=False
#     )
#
#     # Print the response content
#     print(f"\n=== Sample {i+1} ===")
#     print(response.choices[0].message.content)

def ask_question():
    responses = {}

    # Openness to Experience
    print("\nOpenness to Experience:")
    responses['openness_q1'] = int(input("On a scale from 1 to 10, how comfortable are you with trying new or unfamiliar activities? "))
    responses['openness_q2'] = int(input("On a scale from 1 to 10, how often do you seek out creative or unconventional solutions to problems? "))
    responses['openness_q3'] = input("Can you describe a time when you stepped outside of your comfort zone and what you learned from the experience? ")

    # Conscientiousness
    print("\nConscientiousness:")
    responses['conscientiousness_q1'] = int(input("On a scale from 1 to 10, how organized do you feel you are when managing multiple tasks or deadlines? "))
    responses['conscientiousness_q2'] = int(input("On a scale from 1 to 10, how important is attention to detail in your work or personal life? "))
    responses['conscientiousness_q3'] = input("What strategies do you use to ensure you meet deadlines and follow through on commitments? ")

    # Extraversion
    print("\nExtraversion:")
    responses['extraversion_q1'] = int(input("On a scale from 1 to 10, how energized do you feel when working in a team environment? "))
    responses['extraversion_q2'] = int(input("On a scale from 1 to 10, how comfortable are you with initiating conversations or meeting new people? "))
    responses['extraversion_q3'] = input("Can you recall a time when you led or contributed significantly to a group discussion or meeting? What was your role? ")

    # Agreeableness
    print("\nAgreeableness:")
    responses['agreeableness_q1'] = int(input("On a scale from 1 to 10, how important is it to you that others feel heard and valued in a team setting? "))
    responses['agreeableness_q2'] = int(input("On a scale from 1 to 10, how often do you find yourself going out of your way to help others? "))
    responses['agreeableness_q3'] = input("How do you typically handle disagreements or conflicts with colleagues or teammates? ")

    # Neuroticism
    print("\nNeuroticism:")
    responses['neuroticism_q1'] = int(input("On a scale from 1 to 10, how well do you feel you handle stress or pressure in challenging situations? "))
    responses['neuroticism_q2'] = int(input("On a scale from 1 to 10, how often do you experience feelings of worry or self-doubt in your work or personal life? "))
    responses['neuroticism_q3'] = input("Can you share a time when you overcame a stressful or anxiety-inducing situation? How did you manage it? ")

    print("\nThank you for completing the questionnaire!")
    return responses

# Gather user responses
user_responses = ask_question()

# Prepare the responses for the API
user_responses_str = "\n".join([f"{key}: {value}" for key, value in user_responses.items()])

# Call the API
response = client.chat.completions.create(
    model="deepseek-chat",  # Name of the model to use
    messages=[
        {"role": "system", "content": system_role},  # System role
        {"role": "user", "content": user_responses_str}  # User input
    ],
    stream=False  # Whether to stream the output
)

# Print the response content
print(response.choices[0].message.content)



