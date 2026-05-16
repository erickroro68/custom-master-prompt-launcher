# Prompt Launcher

A lightweight Python tool that lets you store your personal master prompts in local text files and load them instantly from a simple terminal menu. Choose a prompt → it copies directly to your clipboard → paste it into any AI model or workflow.

This project is designed for creators, developers, and prompt engineers who want fast access to their most-used prompts without digging through files or rewriting them.

---

## 🚀 Features

- Load prompts from clean `.txt` files  
- Copy any prompt to clipboard with one keypress  
- Add unlimited prompts by editing a single dictionary  
- No cloud dependency — everything stays local  
- Beginner‑friendly Python script  
- Works on Windows, macOS, and Linux  

---

## 📂 Folder Structure
Today
can you be my prompt enginner organizer or can i do it on my local machine easiest way since ive made two prompts that im  basically always going to use for specfic task and want it to be convineient
Absolutely, Ivan. You’ve got two “always‑use” prompts and you want a clean, convenient way to organize them so you can fire them off instantly. You’ve got two paths:

⭐ Fastest answer
Yes — I can be your prompt‑engineer organizer, and you can also set it up on your local machine if you want something physical and permanent.
Both options can work together.

🧩 Option 1: Let ME be your organizer
If you want, I can store your two core prompts in memory and treat them like “profiles” you can activate.

You’d say something like
“Use Prompt A”  
and I instantly load it into the conversation.
Or
“Switch to Prompt B”  
and I swap modes.

If you want this, just tell me:
“Remember these two prompts as my main prompt profiles.”

🧩 Option 2: Local machine organizer (super easy)
Here are the three easiest ways to keep your prompts locally so you can paste them instantly.

1. TextExpander‑style shortcuts (Windows built‑in)
You can create shortcuts like
/master → expands into your full Super Master Prompt
/agent → expands into your Agent Mode prompt

Windows has this built in:

Settings → Time & Language → Typing → Text Suggestions → Custom text shortcuts

This is the fastest method.

2. A local folder with .txt files
Make a folder like:

Code
C:\Prompts\
    master_prompt.txt
    agent_prompt.txt
Then pin it to Quick Access.
Double‑click → Ctrl+A → Ctrl+C → paste into any AI instantly.

Simple and reliable.

3. A tiny local “Prompt Launcher” script
If you want something cooler, you can have a small script that pops up a menu:

Code
1. Super Master Prompt
2. Agent Mode Prompt
3. OSINT Prompt
Press a number → it copies the prompt to your clipboard.

This works with PowerShell or Python.
If you want, I can generate the script for you.

🧩 Which one fits YOU best
Based on how you work — fast, practical, repeatable — the best combo is:

Text shortcuts + me as your organizer.  
You get speed on your machine and flexibility here.

🔥 If you want, I can set up your system right now
Just tell me:

“Here are my two prompts. Save them as Profile A and Profile B.”

Or if you want the local script:

“Make me the local prompt launcher script.”

Which direction do you want to go?

generate the scipt in python
Got you, Ivan.
Here’s a clean, simple Python Prompt Launcher that pops up a menu, lets you pick one of your saved prompts, and automatically copies it to your clipboard.

It works on any machine with Python installed and doesn’t require admin rights or extra packages.

✅ Python Prompt Launcher (copy‑paste ready)
python
import os
import sys
import pyperclip

# -----------------------------
#  YOUR SAVED PROMPTS GO HERE
# -----------------------------
PROMPTS = {
    "1": {
        "name": "Master Prompt",
        "text": """<PUT YOUR MASTER PROMPT HERE>"""
    },
    "2": {
        "name": "Agent Mode Prompt",
        "text": """<PUT YOUR AGENT MODE PROMPT HERE>"""
    },
    "3": {
        "name": "OSINT Prompt",
        "text": """<PUT YOUR OSINT PROMPT HERE>"""
    }
}

# -----------------------------
#  MENU UI
# -----------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        clear()
        print("=== Prompt Launcher ===")
        for key, item in PROMPTS.items():
            print(f"{key}. {item['name']}")
        print("0. Exit")

        choice = input("\nChoose a prompt number: ").strip()

        if choice == "0":
            sys.exit()

        if choice in PROMPTS:
            text = PROMPTS[choice]["text"]
            pyperclip.copy(text)
            clear()
            print(f"Copied '{PROMPTS[choice]['name']}' to clipboard.")
            input("\nPress Enter to return to menu...")
        else:
            print("Invalid choice.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
🧩 What this script does
• Shows a menu of your saved prompts
• You press 1, 2, or 3  
• It copies the full prompt to your clipboard instantly
• You paste it into any AI model
• No internet needed
• No external UI needed

🛠 Requirements (super light)
You only need one package:

Code
pip install pyperclip
That’s it.

🔥 Want me to customize it?
I can:

• Add unlimited prompt profiles
• Add folders for categories
• Add hotkeys
• Add a GUI window version
• Add auto‑sync with a local folder
• Add encryption if you want to store sensitive prompts

Just tell me what your two main prompts are and I’ll plug them in cleanly.

do i keep the <> or only have """ my prompt """ or  """<my prompt>"""
You do NOT keep the < > symbols.
Those were just placeholders to show “put your text here.”

Here’s the rule:

✅ Correct way
Use ONLY the triple quotes:

Code
"text": """YOUR FULL PROMPT HERE"""
❌ Wrong ways
These will break or look weird:

Code
"""<my prompt>"""      # wrong
""" <my prompt> """    # wrong
<my prompt>            # wrong
🧩 Why
Python treats """ ... """ as a multi‑line string.
Anything inside is copied exactly as-is.
The < > symbols were just visual placeholders, not syntax.

🔥 Example with your real usage
Code
PROMPTS = {
    "1": {
        "name": "Master Prompt",
        "text": """You are my master prompt. Do X, Y, Z..."""
    },
    "2": {
        "name": "Agent Mode",
        "text": """You are my agent mode prompt. Handle tasks like..."""
    }
}
Clean. Simple. Works perfectly.

If you want, paste your two prompts here and I’ll format them into the script cleanly so you can drop them in without worrying about spacing or escape issues.

can i just make some like path or PATH =  "Documents\Coding_TECHER_prompt_coding_atlas.txt"
Yes — you can absolutely load your prompts from a file path instead of pasting them directly into the Python script.
That’s actually cleaner, safer, and easier to maintain.

And you don’t keep the < > at all.
You just point to the file.

Let me show you the cleanest version.

✅ Python Prompt Launcher (FILE‑BASED VERSION)
This version loads each prompt from a .txt file in your Documents folder.

You just edit the text files whenever you want — no need to touch the Python script again.

python
import os
import sys
import pyperclip

# -----------------------------
#  PATHS TO YOUR PROMPT FILES
# -----------------------------
PROMPT_PATHS = {
    "1": {
        "name": "Coding Teacher Prompt",
        "path": r"C:\Users\Ivan\Documents\Coding_TEACHER_prompt_coding_atlas.txt"
    },
    "2": {
        "name": "Tech Agent Prompt",
        "path": r"C:\Users\Ivan\Documents\Tech_AGENT_prompt.txt"
    }
}

# -----------------------------
#  MENU UI
# -----------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    while True:
        clear()
        print("=== Prompt Launcher ===")
        for key, item in PROMPT_PATHS.items():
            print(f"{key}. {item['name']}")
        print("0. Exit")

        choice = input("\nChoose a prompt number: ").strip()

        if choice == "0":
            sys.exit()

        if choice in PROMPT_PATHS:
            file_path = PROMPT_PATHS[choice]["path"]

            if not os.path.exists(file_path):
                clear()
                print(f"Error: File not found:\n{file_path}")
                input("\nPress Enter to return to menu...")
                continue

            text = load_prompt(file_path)
            pyperclip.copy(text)

            clear()
            print(f"Copied '{PROMPT_PATHS[choice]['name']}' to clipboard.")
            input("\nPress Enter to return to menu...")
        else:
            print("Invalid choice.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
🧩 Why this version is better
• You don’t need to paste giant prompts into Python
• You can edit your .txt files anytime
• You can add more prompts by just adding more files
• No angle brackets, no escaping, no formatting issues

🔥 How to use it
Create your prompt files in Documents:

Code
C:\Users\Ivan\Documents\Coding_TEACHER_prompt_coding_atlas.txt
C:\Users\Ivan\Documents\Tech_AGENT_prompt.txt
Paste your full prompts inside each .txt file
(no quotes, no brackets — just the raw text)

Run the Python script

Choose 1 or 2

Your clipboard instantly gets the full prompt

🧩 Want me to generate the folder structure + file names for you?
If you want, tell me the names of your two main prompts and I’ll generate:

• the folder layout
• the file names
• the exact Python paths
• and I’ll format your prompts cleanly inside the files

Just drop the prompts here and I’ll wire everything up.

how to use git for this becuase im new
Alright Ivan, let’s slow this down and make it simple, clean, and beginner‑friendly so Git doesn’t feel like some monster hiding under your desk.

You want to know:

“How do I use Git for this prompt‑launcher project?”

I’ll walk you through it like a coding teacher sitting next to you.
No jargon. No stress. Just steps.

And don’t worry about the YouTube tab — your question isn’t about the page, so I won’t pull anything from it.

⭐ What you want to do with Git
You basically want:

A folder on your computer

Your Python script inside it

Your .txt prompt files inside it

A GitHub repo that stores all of this

The ability to update it easily

This is perfect for Git because it’s just files.

🧩 Step‑by‑step: Using Git for your prompt launcher
Here’s the cleanest workflow for a beginner.

01
Create a project folder
Make a folder like PromptLauncher on your computer and put your Python script and prompt text files inside it.
02
Open the folder in VS Code
Right-click the folder and choose Open with VS Code so you can use the built-in terminal and Git tools.
03
Initialize Git
Open the VS Code terminal and run git init to start tracking the folder with Git.
04
Add your files
Run git add . to stage all files so Git knows you want to include them in your first commit.
05
Commit your work
Run git commit -m "Initial commit" to save the first version of your project.
06
Create a GitHub repo
Go to GitHub, click New Repository, name it PromptLauncher, and leave it empty (no README).
07
Connect your folder to GitHub
Copy the repo URL from GitHub and run git remote add origin <URL> in your VS Code terminal.
08
Push your project online
Run git push -u origin main to upload your script and prompt files to GitHub.
🧠 What this gives you
Once this is set up:

• You can update your prompt files anytime
• Run git add . → git commit -m "update" → git push  
• Your prompt launcher stays backed up
• You can pull it on any computer
• You can version your prompts over time

This is exactly how pros manage their tools.

🔥 Want me to generate the full folder structure for you?
I can create:

Code
PromptLauncher/
    launcher.py
    prompts/
        coding_teacher.txt
        tech_agent.txt
And I can format your Python script to automatically load from this structure.

Just tell me:

“Yes, generate the folder structure.”

Or drop your two prompts and I’ll wire everything up cleanly.

mkae a good repo name for me changing this "Custom Master Prompt Picker:"
Alright Ivan, you’re on the GitHub “New Repository” page right now, so let’s give you a repo name that actually fits what you’re building — something clean, professional, and future‑proof.

You’re making a Python tool that loads your master prompts from files and copies them to your clipboard.
So the repo name should reflect:

• prompts
• launcher / picker
• local tool
• productivity
• clean dev vibe

Here are the best repo name options for your project — pick the one that hits your style.

⭐ Top 7 Repo Names (strong, clean, professional)
1. prompt-launcher
Simple. Direct. Perfect for a utility repo.

2. prompt-picker
Matches exactly what your script does.

3. master-prompt-launcher
If you want to emphasize your “master prompts.”

4. local-prompt-engine
Sounds like a personal productivity engine.

5. prompt-deck
Short and stylish. Like a deck of cards you pick from.

6. prompt-hub
If you plan to add more prompts later.

7. prompt-vault
If you want a secure, organized vibe.

🔥 My personal recommendation for YOU
Given your project and your style, the best fit is:

prompt-launcher
It’s clean
It’s professional
It’s exactly what your script does
It looks good on GitHub
It scales if you add more features later

🧩 If you want something more unique
Here are some creative options:

• atlas-prompt-launcher  
• prompt-orbit  
• prompt-switchboard  
• prompt-runner  
• prompt-console

🧠 If you want, I can also generate:
• a perfect README.md
• a folder structure
• a .gitignore
• commit message templates
• instructions for cloning and running

Just tell me which repo name you want and I’ll build the whole setup around it.

make a readme and decription
Absolutely, Ivan — here’s a clean, professional README you can drop straight into your new prompt-launcher repo. It explains exactly what your tool does, how to use it, and how the folder structure works. It’ll make your repo look polished and recruiter‑ready.

📘 README.md (ready to paste)
markdown
# Prompt Launcher

A lightweight Python tool that lets you store your personal master prompts in local text files and load them instantly from a simple terminal menu. Choose a prompt → it copies directly to your clipboard → paste it into any AI model or workflow.

This project is designed for creators, developers, and prompt engineers who want fast access to their most-used prompts without digging through files or rewriting them.

---

## 🚀 Features

- Load prompts from clean `.txt` files  
- Copy any prompt to clipboard with one keypress  
- Add unlimited prompts by editing a single dictionary  
- No cloud dependency — everything stays local  
- Beginner‑friendly Python script  
- Works on Windows, macOS, and Linux  

---

## 📂 Folder Structure

prompt-launcher/
│
├── launcher.py
│
└── prompts/
├── coding_teacher.txt
├── tech_agent.txt
└── (add more prompt files here)

=========================================


- `launcher.py` → The main Python script  
- `prompts/` → Store each prompt as its own `.txt` file  

---

## 🛠 Installation

1. Install Python (3.8+ recommended)
2. Install the clipboard library:

    pip install pyperclip


3. Clone this repository:

    Today
can you be my prompt enginner organizer or can i do it on my local machine easiest way since ive made two prompts that im  basically always going to use for specfic task and want it to be convineient
Absolutely, Ivan. You’ve got two “always‑use” prompts and you want a clean, convenient way to organize them so you can fire them off instantly. You’ve got two paths:

⭐ Fastest answer
Yes — I can be your prompt‑engineer organizer, and you can also set it up on your local machine if you want something physical and permanent.
Both options can work together.

🧩 Option 1: Let ME be your organizer
If you want, I can store your two core prompts in memory and treat them like “profiles” you can activate.

You’d say something like
“Use Prompt A”  
and I instantly load it into the conversation.
Or
“Switch to Prompt B”  
and I swap modes.

If you want this, just tell me:
“Remember these two prompts as my main prompt profiles.”

🧩 Option 2: Local machine organizer (super easy)
Here are the three easiest ways to keep your prompts locally so you can paste them instantly.

1. TextExpander‑style shortcuts (Windows built‑in)
You can create shortcuts like
/master → expands into your full Super Master Prompt
/agent → expands into your Agent Mode prompt

Windows has this built in:

Settings → Time & Language → Typing → Text Suggestions → Custom text shortcuts

This is the fastest method.

2. A local folder with .txt files
Make a folder like:

Code
C:\Prompts\
    master_prompt.txt
    agent_prompt.txt
Then pin it to Quick Access.
Double‑click → Ctrl+A → Ctrl+C → paste into any AI instantly.

Simple and reliable.

3. A tiny local “Prompt Launcher” script
If you want something cooler, you can have a small script that pops up a menu:

Code
1. Super Master Prompt
2. Agent Mode Prompt
3. OSINT Prompt
Press a number → it copies the prompt to your clipboard.

This works with PowerShell or Python.
If you want, I can generate the script for you.

🧩 Which one fits YOU best
Based on how you work — fast, practical, repeatable — the best combo is:

Text shortcuts + me as your organizer.  
You get speed on your machine and flexibility here.

🔥 If you want, I can set up your system right now
Just tell me:

“Here are my two prompts. Save them as Profile A and Profile B.”

Or if you want the local script:

“Make me the local prompt launcher script.”

Which direction do you want to go?

generate the scipt in python
Got you, Ivan.
Here’s a clean, simple Python Prompt Launcher that pops up a menu, lets you pick one of your saved prompts, and automatically copies it to your clipboard.

It works on any machine with Python installed and doesn’t require admin rights or extra packages.

✅ Python Prompt Launcher (copy‑paste ready)
python
import os
import sys
import pyperclip

# -----------------------------
#  YOUR SAVED PROMPTS GO HERE
# -----------------------------
PROMPTS = {
    "1": {
        "name": "Master Prompt",
        "text": """<PUT YOUR MASTER PROMPT HERE>"""
    },
    "2": {
        "name": "Agent Mode Prompt",
        "text": """<PUT YOUR AGENT MODE PROMPT HERE>"""
    },
    "3": {
        "name": "OSINT Prompt",
        "text": """<PUT YOUR OSINT PROMPT HERE>"""
    }
}

# -----------------------------
#  MENU UI
# -----------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        clear()
        print("=== Prompt Launcher ===")
        for key, item in PROMPTS.items():
            print(f"{key}. {item['name']}")
        print("0. Exit")

        choice = input("\nChoose a prompt number: ").strip()

        if choice == "0":
            sys.exit()

        if choice in PROMPTS:
            text = PROMPTS[choice]["text"]
            pyperclip.copy(text)
            clear()
            print(f"Copied '{PROMPTS[choice]['name']}' to clipboard.")
            input("\nPress Enter to return to menu...")
        else:
            print("Invalid choice.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
🧩 What this script does
• Shows a menu of your saved prompts
• You press 1, 2, or 3  
• It copies the full prompt to your clipboard instantly
• You paste it into any AI model
• No internet needed
• No external UI needed

🛠 Requirements (super light)
You only need one package:

Code
pip install pyperclip
That’s it.

🔥 Want me to customize it?
I can:

• Add unlimited prompt profiles
• Add folders for categories
• Add hotkeys
• Add a GUI window version
• Add auto‑sync with a local folder
• Add encryption if you want to store sensitive prompts

Just tell me what your two main prompts are and I’ll plug them in cleanly.

do i keep the <> or only have """ my prompt """ or  """<my prompt>"""
You do NOT keep the < > symbols.
Those were just placeholders to show “put your text here.”

Here’s the rule:

✅ Correct way
Use ONLY the triple quotes:

Code
"text": """YOUR FULL PROMPT HERE"""
❌ Wrong ways
These will break or look weird:

Code
"""<my prompt>"""      # wrong
""" <my prompt> """    # wrong
<my prompt>            # wrong
🧩 Why
Python treats """ ... """ as a multi‑line string.
Anything inside is copied exactly as-is.
The < > symbols were just visual placeholders, not syntax.

🔥 Example with your real usage
Code
PROMPTS = {
    "1": {
        "name": "Master Prompt",
        "text": """You are my master prompt. Do X, Y, Z..."""
    },
    "2": {
        "name": "Agent Mode",
        "text": """You are my agent mode prompt. Handle tasks like..."""
    }
}
Clean. Simple. Works perfectly.

If you want, paste your two prompts here and I’ll format them into the script cleanly so you can drop them in without worrying about spacing or escape issues.

can i just make some like path or PATH =  "Documents\Coding_TECHER_prompt_coding_atlas.txt"
Yes — you can absolutely load your prompts from a file path instead of pasting them directly into the Python script.
That’s actually cleaner, safer, and easier to maintain.

And you don’t keep the < > at all.
You just point to the file.

Let me show you the cleanest version.

✅ Python Prompt Launcher (FILE‑BASED VERSION)
This version loads each prompt from a .txt file in your Documents folder.

You just edit the text files whenever you want — no need to touch the Python script again.

python
import os
import sys
import pyperclip

# -----------------------------
#  PATHS TO YOUR PROMPT FILES
# -----------------------------
PROMPT_PATHS = {
    "1": {
        "name": "Coding Teacher Prompt",
        "path": r"C:\Users\Ivan\Documents\Coding_TEACHER_prompt_coding_atlas.txt"
    },
    "2": {
        "name": "Tech Agent Prompt",
        "path": r"C:\Users\Ivan\Documents\Tech_AGENT_prompt.txt"
    }
}

# -----------------------------
#  MENU UI
# -----------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    while True:
        clear()
        print("=== Prompt Launcher ===")
        for key, item in PROMPT_PATHS.items():
            print(f"{key}. {item['name']}")
        print("0. Exit")

        choice = input("\nChoose a prompt number: ").strip()

        if choice == "0":
            sys.exit()

        if choice in PROMPT_PATHS:
            file_path = PROMPT_PATHS[choice]["path"]

            if not os.path.exists(file_path):
                clear()
                print(f"Error: File not found:\n{file_path}")
                input("\nPress Enter to return to menu...")
                continue

            text = load_prompt(file_path)
            pyperclip.copy(text)

            clear()
            print(f"Copied '{PROMPT_PATHS[choice]['name']}' to clipboard.")
            input("\nPress Enter to return to menu...")
        else:
            print("Invalid choice.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
🧩 Why this version is better
• You don’t need to paste giant prompts into Python
• You can edit your .txt files anytime
• You can add more prompts by just adding more files
• No angle brackets, no escaping, no formatting issues

🔥 How to use it
Create your prompt files in Documents:

Code
C:\Users\Ivan\Documents\Coding_TEACHER_prompt_coding_atlas.txt
C:\Users\Ivan\Documents\Tech_AGENT_prompt.txt
Paste your full prompts inside each .txt file
(no quotes, no brackets — just the raw text)

Run the Python script

Choose 1 or 2

Your clipboard instantly gets the full prompt

🧩 Want me to generate the folder structure + file names for you?
If you want, tell me the names of your two main prompts and I’ll generate:

• the folder layout
• the file names
• the exact Python paths
• and I’ll format your prompts cleanly inside the files

Just drop the prompts here and I’ll wire everything up.

how to use git for this becuase im new
Alright Ivan, let’s slow this down and make it simple, clean, and beginner‑friendly so Git doesn’t feel like some monster hiding under your desk.

You want to know:

“How do I use Git for this prompt‑launcher project?”

I’ll walk you through it like a coding teacher sitting next to you.
No jargon. No stress. Just steps.

And don’t worry about the YouTube tab — your question isn’t about the page, so I won’t pull anything from it.

⭐ What you want to do with Git
You basically want:

A folder on your computer

Your Python script inside it

Your .txt prompt files inside it

A GitHub repo that stores all of this

The ability to update it easily

This is perfect for Git because it’s just files.

🧩 Step‑by‑step: Using Git for your prompt launcher
Here’s the cleanest workflow for a beginner.

01
Create a project folder
Make a folder like PromptLauncher on your computer and put your Python script and prompt text files inside it.
02
Open the folder in VS Code
Right-click the folder and choose Open with VS Code so you can use the built-in terminal and Git tools.
03
Initialize Git
Open the VS Code terminal and run git init to start tracking the folder with Git.
04
Add your files
Run git add . to stage all files so Git knows you want to include them in your first commit.
05
Commit your work
Run git commit -m "Initial commit" to save the first version of your project.
06
Create a GitHub repo
Go to GitHub, click New Repository, name it PromptLauncher, and leave it empty (no README).
07
Connect your folder to GitHub
Copy the repo URL from GitHub and run git remote add origin <URL> in your VS Code terminal.
08
Push your project online
Run git push -u origin main to upload your script and prompt files to GitHub.
🧠 What this gives you
Once this is set up:

• You can update your prompt files anytime
• Run git add . → git commit -m "update" → git push  
• Your prompt launcher stays backed up
• You can pull it on any computer
• You can version your prompts over time

This is exactly how pros manage their tools.

🔥 Want me to generate the full folder structure for you?
I can create:

Code
PromptLauncher/
    launcher.py
    prompts/
        coding_teacher.txt
        tech_agent.txt
And I can format your Python script to automatically load from this structure.

Just tell me:

“Yes, generate the folder structure.”

Or drop your two prompts and I’ll wire everything up cleanly.

mkae a good repo name for me changing this "Custom Master Prompt Picker:"
Alright Ivan, you’re on the GitHub “New Repository” page right now, so let’s give you a repo name that actually fits what you’re building — something clean, professional, and future‑proof.

You’re making a Python tool that loads your master prompts from files and copies them to your clipboard.
So the repo name should reflect:

• prompts
• launcher / picker
• local tool
• productivity
• clean dev vibe

Here are the best repo name options for your project — pick the one that hits your style.

⭐ Top 7 Repo Names (strong, clean, professional)
1. prompt-launcher
Simple. Direct. Perfect for a utility repo.

2. prompt-picker
Matches exactly what your script does.

3. master-prompt-launcher
If you want to emphasize your “master prompts.”

4. local-prompt-engine
Sounds like a personal productivity engine.

5. prompt-deck
Short and stylish. Like a deck of cards you pick from.

6. prompt-hub
If you plan to add more prompts later.

7. prompt-vault
If you want a secure, organized vibe.

🔥 My personal recommendation for YOU
Given your project and your style, the best fit is:

prompt-launcher
It’s clean
It’s professional
It’s exactly what your script does
It looks good on GitHub
It scales if you add more features later

🧩 If you want something more unique
Here are some creative options:

• atlas-prompt-launcher  
• prompt-orbit  
• prompt-switchboard  
• prompt-runner  
• prompt-console

🧠 If you want, I can also generate:
• a perfect README.md
• a folder structure
• a .gitignore
• commit message templates
• instructions for cloning and running

Just tell me which repo name you want and I’ll build the whole setup around it.

make a readme and decription
Absolutely, Ivan — here’s a clean, professional README you can drop straight into your new prompt-launcher repo. It explains exactly what your tool does, how to use it, and how the folder structure works. It’ll make your repo look polished and recruiter‑ready.

📘 README.md (ready to paste)
markdown
# Prompt Launcher

A lightweight Python tool that lets you store your personal master prompts in local text files and load them instantly from a simple terminal menu. Choose a prompt → it copies directly to your clipboard → paste it into any AI model or workflow.

This project is designed for creators, developers, and prompt engineers who want fast access to their most-used prompts without digging through files or rewriting them.

---

## 🚀 Features

- Load prompts from clean `.txt` files  
- Copy any prompt to clipboard with one keypress  
- Add unlimited prompts by editing a single dictionary  
- No cloud dependency — everything stays local  
- Beginner‑friendly Python script  
- Works on Windows, macOS, and Linux  

---

## 📂 Folder Structure

prompt-launcher/
│
├── launcher.py
│
└── prompts/
├── coding_teacher.txt
├── tech_agent.txt
└── (add more prompt files here)

Code

- `launcher.py` → The main Python script  
- `prompts/` → Store each prompt as its own `.txt` file  

---

## 🛠 Installation

1. Install Python (3.8+ recommended)
2. Install the clipboard library:

  pip install pyperclip

3. Clone this repository:
                  
  git clone https://github.com/<your-username>/prompt-launcher

4. Add your prompt files inside the `prompts/` folder.

---------------------------------

## ▶️ Usage

Run the launcher:

  python launcher.py


You’ll see a menu like:

=== Prompt Launcher ===

Coding Teacher Prompt

E-COmmernce Agent Prompt

Exit


Press a number → the script loads the corresponding `.txt` file → copies the full text to your clipboard.

Paste anywhere you want.

---

## 🧠 How It Works

Each prompt is stored as a plain `.txt` file.  
The Python script:

1. Reads the file path from a dictionary  
2. Opens the file  
3. Copies the entire contents to your clipboard  
4. Waits for your next selection  

This keeps your prompts clean, editable, and version-controlled.

---

## 🤝 Contributing

Feel free to fork the repo and customize it for your workflow.  
Add new prompt files, improve the menu, or build a GUI version.

---

## 📄 License

MIT License — free to use, modify, and share.


