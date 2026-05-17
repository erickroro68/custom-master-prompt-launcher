import os
import sys
import pyperclip

PROMPT_PATHS = {
    "1": {
        "name_of_prompt": " Coding Archetecture Teacher Helper  Prompt ",
        "prompt_file_path": r"X:\UsefulPrompts\Coding_TEACHER_prompt_coding_atlas.txt"
    },
    "2": {
        "name_of_prompt": " Selling Researcher Agent Prompt",
        "prompt_file_path": r"X:\UsefulPrompts\E_COmmernce_AGENT_PROMPT "
    },

}  


def clearScreen():
    os.system("cls")

def openMenu():
    clearScreen()

    print("*" * 40)
    print(" " * 5 ,"MASTER PROMPT LIST")
    print("*" * 40)


def main():

    openMenu()

main()