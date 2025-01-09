from terminal import run_ollama
from email_integration import list_emails
from whatsapp_integration import send_whatsapp_message

def dispatch_query(query):
    from classifier import classify_query
    query_type = classify_query(query)
    if query_type == 'friendly':
        return run_ollama('samantha-mistral', query)
    elif query_type == 'normal':
        return run_ollama('mistral', query)
    elif query_type == 'long':
        return run_ollama('llama2', query)
    elif "check email" in query or "can you please check my emails" in query or "check email" in query or "check my email" in query:
        list_emails()
        return "Checking your emails."
    elif "send WhatsApp message" in query:
        send_whatsapp_message("123456789", "Hello from your AI assistant!")
        return "Sending WhatsApp message."
    # Add more commands here
