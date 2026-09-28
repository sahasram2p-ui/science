const input = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatBox = document.getElementById("chat-box");

function addMessage(text, className) {
    const message = document.createElement("div");
    message.className = `message ${className}`;
    message.textContent = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function useSuggestion(text) {
    input.value = text;
    input.focus();
}

async function sendMessage() {
    const message = input.value.trim();
    if (!message) return;

    const welcome = document.querySelector(".welcome");
    if (welcome) welcome.remove();

    addMessage(message, "user-message");
    input.value = "";
    sendButton.disabled = true;

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({message})
        });

        const data = await response.json();

        if (data.success) {
            addMessage(data.reply, "bot-message");
        } else {
            addMessage("Error: " + data.error, "bot-message");
        }
    } catch (error) {
        addMessage("Unable to connect to the server.", "bot-message");
    } finally {
        sendButton.disabled = false;
        input.focus();
    }
}

sendButton.addEventListener("click", sendMessage);

input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
});
