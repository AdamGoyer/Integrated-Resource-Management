# This file contains the blueprint for creating a standardized folder structure
# The structure is represented as a dictionary (like a folder tree)
# Main folders are the keys (like "Financial Planning")
# Subfolders are listed in the square brackets [] after each main folder
# Empty brackets [] mean no subfolders will be created

FOLDER_STRUCTURE = {
    # General administrative documents and correspondence
    "Administrative Correspondence": [],
    
    # Information and documents related to professional advisors
    "Advisors": [],
    
    # Business planning and strategy documents
    "Business Planning": [],
    
    # Property and real estate documentation
    "Deeds": [],
    
    # Financial planning documents with several categorized subfolders
    "Financial Planning": [
        "Notes",
        "CRIA Annual Client Contact - Global",
        "Investment Correspondence",
        "Retirement Income/Planning",
        "Statements",
        "Tax Returns",
        "To Do",
    ],
    
    # Archive of historical documents
    "Historical Documents": [],
    
    # Insurance policies and risk management documentation
    "Insurance & Risk Management": [
        "Life Insurance",
        "Disability Insurance",
        "Long Term Care",
        "Auto Insurance",
        "Home Insurance",
        "Umbrella Insurance",
        "Medicare",
        "Other Policies",
    ],
    
    # Investment-related documents and records
    "Investments": [
        "Accounts",
        "Confirmations",
        "Reports",
        "Performance Statements",
    ],
    
    # Legal documents and estate planning
    "Legal": [
        "Estate Planning/Wills",
        "Estate Planning/Trusts/Crummey Notices",
        "Estate Planning/Power of Attorney",
        "Healthcare Proxies",
    ],
    
    # Medical and health-related records
    "Medical Records": [],
    
    # Miscellaneous documents
    "Other": [],
    
    # Passport and travel documents
    "Passports": [],
    
    # Access and permission-related documents
    "Permissions": [],
    
    # Image files and photographs
    "Pictures": [],
    
    # PSG-specific documentation
    "PSG Documents": [],
    
    # Documents shared with other parties
    "Shared Documents": [],
} 