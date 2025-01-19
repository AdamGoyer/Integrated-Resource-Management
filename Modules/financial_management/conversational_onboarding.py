import openai
import json

def ask_question(prompt, conversation_log):
    """
    Send a prompt to the OpenAI model and return the response.
    """
    conversation_log.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation_log
    )
    answer = response['choices'][0]['message']['content']
    conversation_log.append({"role": "assistant", "content": answer})
    return answer

def main():
    openai.api_key = "your-api-key"  # Replace with your OpenAI API key

    print("Welcome to the Financial Planning Assistant!")
    print("Let's gather some information to help with your financial planning.")

    # Initialize conversation log
    conversation_log = [
        {"role": "system", "content": "You are a helpful financial advisor."}
    ]

    # Questions based on the conversational AI script
    questions = [
        "Can you tell me your full name and date of birth?",
        "Do you live in the U.S.? If so, what’s your home address?",
        "Are you currently employed? What’s your job title and how long have you been there?",
        "Do you have a spouse or partner you’d like included in this plan? If yes, what’s their name and date of birth?",
        "Do you have any children or dependents? If yes, what are their names and ages?",
        "What’s your annual salary or income? Do you receive any bonuses or other sources of income?",
        "Do you currently receive Social Security or pension income? If not, do you have any projections for when you might?",
        "Do you own any property, like a home or rental property? If so, can you tell me about its current value?",
        "What investments do you currently have? These could be retirement accounts like a 401(k) or brokerage accounts.",
        "Do you have any debts we should consider, such as a mortgage, auto loan, or credit card balances?",
        "Do you currently have life insurance or disability coverage? If yes, what are the coverage amounts?",
        "What are your short-term financial goals? For example, are you saving for a big purchase or paying down debt?",
        "What about long-term goals? Do you have a specific retirement age in mind or plans to support your children’s education?",
        "Do you have a will or trust in place?",
        "Are there any charitable organizations you’d like to include in your plans?"
    ]

    client_responses = {}

    for question in questions:
        print(f"\n{question}")
        response = ask_question(question, conversation_log)
        print(f"{response}")
        client_responses[question] = response

    print("\nThank you for sharing this information. Here is a summary of your responses:")
    print(json.dumps(client_responses, indent=2))

if __name__ == "__main__":
    main()
