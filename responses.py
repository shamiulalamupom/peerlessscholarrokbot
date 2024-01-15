from questionExtracter import question_by_url
from ans import ans

def handle_response(message) -> str:
    if message.startswith('https'):
        return ans(question_by_url(message).lower())