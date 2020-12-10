import re
import os

dirContents = os.listdir(os.path.dirname(__file__))
pattern = '^(day\d+).py$'
matches = [re.search(pattern, m) for m in dirContents]
__all__ = [match.group(1) for match in matches if match is not None]
