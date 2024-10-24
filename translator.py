import sys
import click
import os
from googletrans import Translator, LANGUAGES
from rich.console import Console
from rich.prompt import Prompt

console = Console()
translator = Translator()

LANGUAGE_NAMES_TO_CODES = {name.lower(): code for code, name in LANGUAGES.items()}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def translate_text(text, src_lang, dest_lang):
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

@click.command()
@click.option('--text', prompt='Enter text to translate', help='Text to translate')
@click.option('--src-lang', prompt='Enter the source language name', help='Source language name (e.g., English)')
@click.option('--dest-lang', prompt='Enter the destination language name', help='Destination language name (e.g., French)')
def main(text, src_lang, dest_lang):
    console.print("Welcome to the Interactive Translator!", style="bold green")

    if text.lower() == 'exit':
        console.print("Exiting the translator. Goodbye!", style="bold red")
        return

    src_lang_name_lower = src_lang.lower()
    if src_lang_name_lower not in LANGUAGE_NAMES_TO_CODES:
        console.print("Invalid source language name. Please try again.", style="bold red")
        return
    src_lang_code = LANGUAGE_NAMES_TO_CODES[src_lang_name_lower]

    dest_lang_name_lower = dest_lang.lower()
    if dest_lang_name_lower not in LANGUAGE_NAMES_TO_CODES:
        console.print("Invalid destination language name. Please try again.", style="bold red")
        return
    dest_lang_code = LANGUAGE_NAMES_TO_CODES[dest_lang_name_lower]

    translated_text = translate_text(text, src_lang_code, dest_lang_code)
    console.print(f"Translated text in {dest_lang}: {translated_text}", style="bold blue")

    # Check for Ctrl + L to clear the screen
    while True:
        if click.getchar() == '\x12':  # Ctrl + L
            clear_screen()
            break

if __name__ == "__main__":
    console.print("Welcome to the Interactive Translator!", style="bold green")
    main()
