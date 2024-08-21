def process_command(command):
    if "weather" in command:
        return "Fetching weather..."
    elif "news" in command:
        return "Getting latest news..."
    elif "email" in command:
        return "Sending an email..."
    else:
        return "Command not recognized"
