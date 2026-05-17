import os
import sys
import pyperclip


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROMPTS_ROOT = os.path.join(BASE_DIR, "UsefulPrompts")
PUBLIC_PROMPTS_DIR = os.path.join(PROMPTS_ROOT, "public_prompts")
PRIVATE_PROMPTS_DIR = os.path.join(PROMPTS_ROOT, "private_prompts")


PROMPT_PATHS = {
    "1": {
        "visibility": "PRIVATE",
        "name_of_prompt": "Coding Architecture Teacher Helper Prompt",
        "prompt_file_path": os.path.join(
            PRIVATE_PROMPTS_DIR,
            "Coding_TECHER_prompt_coding_atlas.txt"
        )
    },
    "2": {
        "visibility": "PRIVATE",
        "name_of_prompt": "Selling Researcher Agent Prompt",
        "prompt_file_path": os.path.join(
            PRIVATE_PROMPTS_DIR,
            "E_COmmernce_AGENT_PROMPT.txt"
        )
    },
    "3": {
        "visibility": "PUBLIC",
        "name_of_prompt": "Example Prompt",
        "prompt_file_path": os.path.join(
            PUBLIC_PROMPTS_DIR,
            "Example_prompt.txt"
        )
    },
    "4": {
        "visibility": "PUBLIC",
        "name_of_prompt": "Project Builder Setup Prompt",
        "prompt_file_path": os.path.join(
            PUBLIC_PROMPTS_DIR,
            "Project_Builder_Setup_Prompt.txt"
        )
    },
}


def clear_screen():
    os.system("cls")


def open_menu():
    clear_screen()

    print("=" * 65)
    print(" " * 17 + "MASTER PROMPT LAUNCHER")
    print("=" * 65)
    print()

    for prompt_number, prompt_info in PROMPT_PATHS.items():
        visibility = prompt_info["visibility"]
        prompt_name = prompt_info["name_of_prompt"]

        print(f"{prompt_number}. [{visibility}] {prompt_name}")

    print()
    print("q. Quit")
    print()


def load_prompt_file(file_path):
    file_path = file_path.strip()

    if not os.path.exists(file_path):
        print()
        print("ERROR: Prompt file not found.")
        print()
        print("Python looked here:")
        print(file_path)
        print()
        print("Fix:")
        print("1. Make sure the file exists.")
        print("2. Make sure the filename spelling matches exactly.")
        print("3. Make sure it is inside the correct public_prompts or private_prompts folder.")
        print()
        input("Press Enter to return to the menu...")
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        prompt_text = file.read()

    return prompt_text


def display_and_copy_prompt(prompt_info):
    prompt_name = prompt_info["name_of_prompt"]
    visibility = prompt_info["visibility"]
    file_path = prompt_info["prompt_file_path"]

    prompt_text = load_prompt_file(file_path)

    if prompt_text is None:
        return

    clear_screen()

    print("=" * 65)
    print(f"{prompt_name}")
    print(f"Type: {visibility}")
    print("=" * 65)
    print()
    print(prompt_text)
    print()

    pyperclip.copy(prompt_text)

    print("=" * 65)
    print("Prompt copied to clipboard.")
    print("You can now paste it anywhere with Ctrl + V.")
    print("=" * 65)
    print()

    input("Press Enter to return to the menu...")


def handle_user_choice(user_choice):
    if user_choice.lower() == "q":
        print("Goodbye.")
        sys.exit()

    if user_choice in PROMPT_PATHS:
        selected_prompt = PROMPT_PATHS[user_choice]
        display_and_copy_prompt(selected_prompt)
    else:
        print()
        print("Invalid choice.")
        input("Press Enter to try again...")


def main():
    while True:
        open_menu()
        user_choice = input("Choose a prompt number: ").strip()
        handle_user_choice(user_choice)


if __name__ == "__main__":
    main()