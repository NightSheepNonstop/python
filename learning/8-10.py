_messages = ['hello', 'world', 'python']
_sent_messages = []


def show_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        sent_messages.append(message)


def send_messages(sent_messages):
    for sent_message in sent_messages:
        print(sent_message)


show_messages(_messages, _sent_messages)
send_messages(_sent_messages)
print(_messages, _sent_messages)
