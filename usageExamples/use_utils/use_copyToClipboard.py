import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(__file__))), '..', '..'))
from modules.utils.copyToClipboard.copy_to_clipboard import copy_text_to_clipboard


copy_text_to_clipboard("Some random text")
