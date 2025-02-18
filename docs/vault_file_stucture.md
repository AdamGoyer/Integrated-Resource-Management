# File Structure Creator

This Python script automates the creation of a well-organized file structure designed for managing client-related documents.

## Features
- **Predefined Folder Structure**: Includes folders for administrative correspondence, legal documents, financial planning, insurance, investments, and more.
- **Nested Folders**: Automatically creates subfolders within parent folders to ensure logical organization.
- **Customizable**: Easily modify the predefined structure to suit your specific requirements.

## File Structure
The script generates the following directory structure:

```
Client Name/
├── Administrative Correspondence
├── Advisors
├── Business Planning
├── Deeds
├── Financial Planning/
│   ├── Notes
│   ├── CRIA Annual Client Contact - Global
│   ├── Investment Correspondence
│   ├── Retirement Income/Planning
│   ├── Statements
│   ├── Tax Returns
│   └── To Do
├── Historical Documents
├── Insurance & Risk Management/
│   ├── Life Insurance
│   ├── Disability Insurance
│   ├── Long Term Care
│   ├── Auto Insurance
│   ├── Home Insurance
│   ├── Umbrella Insurance
│   ├── Medicare
│   └── Other Policies
├── Investments/
│   ├── Accounts
│   ├── Confirmations
│   ├── Reports
│   └── Performance Statements
├── Legal/
│   ├── Estate Planning/
│   │   ├── Wills
│   │   ├── Trusts/
│   │   │   ├── Crummey Notices
│   │   └── Power of Attorney
│   └── Healthcare Proxies
├── Medical Records
├── Other
├── Passports
├── Permissions
├── Pictures
├── PSG Documents
└── Shared Documents
```

## How to Use
1. Clone or download this repository to your local machine.
2. Open the script file `create_file_structure.py` in your preferred code editor.
3. Update the `base_dir` variable in the script with the path to the directory where you want the structure to be created.
4. Run the script by executing:
   ```bash
   python create_file_structure.py
   ```
5. The file structure will be created in the specified directory.

## Requirements
- **Python 3.x**
- No additional libraries are required.

## Customization
- Modify the `structure` dictionary in the script to add, remove, or rename folders and subfolders as needed.
- For example, to add a new folder under "Financial Planning," simply include it in the corresponding list in the dictionary.

## License
This script is open-source and free to use for personal or professional purposes.

---

For any questions, feedback, or assistance, please feel free to reach out!

