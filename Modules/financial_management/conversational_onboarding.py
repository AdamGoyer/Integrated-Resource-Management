import openai
import json
from datetime import datetime

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

def save_to_markdown(client_responses, session_id, client_name=None):
    """
    Save questions and answers to a markdown file with session ID and optional client name.
    """
    if client_name:
        filename = f"responses_{client_name.replace(' ', '_')}_{session_id}.md"
    else:
        filename = f"responses_{session_id}.md"

    with open(filename, "w") as file:
        file.write(f"# Financial Planning Responses\n\n")
        file.write(f"**Session ID:** {session_id}\n\n")
        for question, response in client_responses.items():
            file.write(f"## Question\n{question}\n\n")
            file.write(f"### Answer\n{response}\n\n")
    print(f"Responses saved to {filename}")

def main():
    openai.api_key = "your-api-key"  # Replace with your OpenAI API key

    print("Welcome to the Financial Planning Assistant!")
    print("Let's gather some information to help with your financial planning.")

    # Initialize session
    session_id = datetime.now().strftime("%Y%m%d%H%M%S")
    conversation_log = [
        {"role": "system", "content": "You are a helpful financial advisor."}
    ]

    client_responses = {}
    client_name = None

    # Questions based on the conversational AI script
    questions = [
        # Personal Information
        "Can you tell me your full name and date of birth?",
        "Do you live in the U.S.? If so, what’s your home address?",
        "Are you currently employed? What’s your job title and how long have you been there?",
        "Do you have a spouse or partner you’d like included in this plan? If yes, what’s their name and date of birth?",
        "Do you have any children or dependents? If yes, what are their names and ages?",

        # Financial Overview
        "What’s your annual salary or income? Do you receive any bonuses or other sources of income?",
        "Do you currently receive Social Security or pension income? If not, do you have any projections for when you might?",
        "What about your expenses—how much do you spend monthly on essentials like housing, utilities, and groceries?",
        "Do you own any property, like a home or rental property? If so, can you tell me about its current value?",
        "What investments do you currently have? These could be retirement accounts like a 401(k) or brokerage accounts.",
        "Do you have any debts we should consider, such as a mortgage, auto loan, or credit card balances?",

        # Protection and Insurance
        "Do you currently have life insurance or disability coverage? If yes, what are the coverage amounts?",
        "Do you use tobacco, or are you taking any medication?",
        "How much of your income would need to be replaced in case of premature death?",
        "Would you want to pay off existing liabilities in case of death or disability?",
        "Do you expect additional expenses in such events, like childcare or medical costs?",

        # Goals and Risk Tolerance
        "What are your short-term financial goals? For example, are you saving for a big purchase or paying down debt?",
        "What about long-term goals? Do you have a specific retirement age in mind or plans to support your children’s education?",
        "How would you describe your comfort level with financial risk: conservative, moderate, or aggressive?",

        # Estate Planning
        "Do you have a will or trust in place? If yes, when was it last updated?",
        "Do you have guardianship provisions for your children?",
        "Are you considering any estate distribution strategies like gifting or charitable giving?",

        # Retirement and Education Goals
        "When would you like to retire, and how much do you anticipate needing annually in retirement (in today’s dollars)?",
        "Are you currently saving for college expenses or other education goals? If yes, how much would you like to contribute?",

        # Investments
        "Are any of your current investments not meeting your expectations?",
        "How do you currently make investment decisions?",
        "What are your expectations for annual returns on investments?",

        # Long-Term Care
        "Have you considered plans for long-term care if you become functionally disabled in the future?",
        "Would you prefer to stay in your home or enter a long-term care facility if necessary?"
    ]

    for question in questions:
        print(f"\n{question}")
        response = ask_question(question, conversation_log)
        print(f"{response}")

        # Capture client name from the first question
        if "full name" in question.lower() and not client_name:
            try:
                client_name = "_".join(response.split()[:2])  # Use first two words as name
            except IndexError:
                client_name = "Unknown_Client"

        client_responses[question] = response

    print("\nThank you for sharing this information. Here is a summary of your responses:")
    print(json.dumps(client_responses, indent=2))

    # Save responses to a markdown file
    save_to_markdown(client_responses, session_id, client_name)

if __name__ == "__main__":
    main()
