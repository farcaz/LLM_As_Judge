from chatbot import get_chatbot_response
from judge import judge_response

def main():
    conversation = []
    print("Type 'exit' or 'quit' to end the conversation and get the evaluation report.\n")
    while True:
        user_prompt = input("You: ")
        if user_prompt.strip().lower() in ("exit", "quit"):
            break
        # Build context messages for the chatbot
        messages = []
        for turn in conversation:
            messages.append({"role": "user", "content": turn["user"]})
            messages.append({"role": "assistant", "content": turn["chatbot"]})
        messages.append({"role": "user", "content": user_prompt})
        chatbot_reply = get_chatbot_response(messages)
        print(f"Chatbot: {chatbot_reply}")
        conversation.append({"user": user_prompt, "chatbot": chatbot_reply})

    if conversation:
        # Build a conversation transcript for the judge
        transcript = ""
        for idx, turn in enumerate(conversation, 1):
            transcript += f"Turn {idx}:\nUser: {turn['user']}\nChatbot: {turn['chatbot']}\n"
        evaluation = judge_response(
            "The following is a conversation between a user and a chatbot:\n" + transcript,
            "Please evaluate the chatbot's overall performance in this conversation."
        )
        print("\n--- Evaluation Report ---")
        print(evaluation)
    else:
        print("No conversation to evaluate.")

if __name__ == "__main__":
    main()