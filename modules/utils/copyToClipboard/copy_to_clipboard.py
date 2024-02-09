import pyperclip

def copy_text_to_clipboard(text):
    pyperclip.copy(text)
    print("copied to clipboard.")
