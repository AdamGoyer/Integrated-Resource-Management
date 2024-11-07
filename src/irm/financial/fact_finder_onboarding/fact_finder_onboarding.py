"""
MassMutual Financial Planning Fact Finder
----------------------------------------
This module implements an interactive fact finder questionnaire using ChatGPT
to collect and validate client financial information.

Implementation Strategy:
1. Collect basic client information
2. Validate responses in real-time
3. Store responses in structured JSON format
4. Support progressive disclosure of questions
"""

import openai
import json
import re
from datetime import datetime

# Configuration
openai.api_key = 'your-api-key-here'  # TODO: Move to environment variable or config file

def ask_chatgpt(question):
    """
    Sends a question to ChatGPT and returns the response.
    
    Args:
        question (str): The question to ask ChatGPT
        
    Returns:
        str: ChatGPT's response
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",  # TODO: Make model configurable
        messages=[
            {"role": "system", "content": "You are a helpful assistant collecting financial planning information."},
            {"role": "user", "content": question}
        ],
        temperature=0  # Using 0 for consistent, deterministic responses
    )
    return response['choices'][0]['message']['content'].strip()

# Validation Functions
def validate_date(date_text):
    """
    Validates if the provided date string matches YYYY-MM-DD format.
    
    Args:
        date_text (str): Date string to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_yes_no(answer):
    """
    Validates if the answer is either 'yes' or 'no' (case-insensitive).
    
    Args:
        answer (str): Response to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    return answer.lower() in ['yes', 'no']

def collect_responses(questionnaire):
    """
    Iterates through the questionnaire sections, collecting and validating responses.
    
    Implementation follows the progressive disclosure principle:
    1. Present questions by section
    2. Validate responses immediately
    3. Allow for correction of invalid responses
    
    Args:
        questionnaire (dict): Structured questionnaire with sections and questions
        
    Returns:
        dict: Collected responses organized by section
    """
    responses = {}
    for section, questions in questionnaire.items():
        print(f"\n--- {section} ---\n")
        responses[section] = {}
        
        for item in questions:
            question = item['question']
            field = item['field']
            
            # Progressive validation loop
            while True:
                answer = ask_chatgpt(question)
                
                # Field-specific validation
                if 'dob' in field:
                    if validate_date(answer):
                        break
                    else:
                        print("Invalid date format. Please use YYYY-MM-DD.")
                        continue
                elif 'not_us_citizen' in field or 'yes_no' in field:
                    if validate_yes_no(answer):
                        break
                    else:
                        print("Please answer 'Yes' or 'No'.")
                        continue
                else:
                    break
                    
            responses[section][field] = answer
            print(f"{question}\n{answer}\n")
            
    return responses

def main():
    """
    Main execution function that:
    1. Collects responses through the questionnaire
    2. Saves responses to a JSON file
    """
    responses = collect_responses(questionnaire)
    
    # Save responses to JSON file
    with open('client_responses.json', 'w') as f:
        json.dump(responses, f, indent=4)
    print("Thank you for providing your information.")

if __name__ == '__main__':
    # Questionnaire Structure
    # TODO: Move to separate configuration file
    questionnaire = {
        "Client/Co-Client Information": [
            {"question": "Please enter the client's name:", "field": "client_name"},
            {"question": "Please enter the client's date of birth (YYYY-MM-DD):", "field": "client_dob"},
            {"question": "Is the client not a U.S. citizen? (Yes/No):", "field": "client_not_us_citizen"},
            {"question": "Please enter the co-client's name:", "field": "co_client_name"},
            {"question": "Please enter the co-client's date of birth (YYYY-MM-DD):", "field": "co_client_dob"},
            {"question": "Is the co-client not a U.S. citizen? (Yes/No):", "field": "co_client_not_us_citizen"},
            {"question": "Please provide the home address:", "field": "home_address"},
            {"question": "Please select the tax filing status:", "field": "tax_filing_status"}
        ],
        # TODO: Add remaining sections from fact_finder_mass_markdown.md:
        # - Financial Goals
        # - Income & Employment
        # - Assets & Liabilities
        # - Insurance Coverage
        # - Estate Planning
    }
    main() 