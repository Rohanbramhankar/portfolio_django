(function () {
    var launcher = document.getElementById("assistantLauncher");
    var panel = document.getElementById("assistantPanel");
    var closeButton = document.getElementById("assistantClose");
    var form = document.getElementById("assistantForm");
    var input = document.getElementById("assistantInput");
    var messagesElement = document.getElementById("assistantMessages");
    var sendButton = form.querySelector("button[type='submit']");
    var conversation = [];

    function addMessage(content, sender) {
        var message = document.createElement("p");
        message.className = "assistant-message assistant-message--" + sender;
        message.textContent = content;
        messagesElement.appendChild(message);
        messagesElement.scrollTop = messagesElement.scrollHeight;
        return message;
    }

    function setOpen(open) {
        panel.hidden = !open;
        launcher.setAttribute("aria-expanded", String(open));
        if (open) {
            input.focus();
        }
    }

    launcher.addEventListener("click", function () {
        setOpen(panel.hidden);
    });
    closeButton.addEventListener("click", function () {
        setOpen(false);
        launcher.focus();
    });

    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        var text = input.value.trim();
        if (!text) {
            return;
        }

        conversation.push({ role: "user", content: text });
        conversation = conversation.slice(-10);
        addMessage(text, "user");
        input.value = "";
        input.disabled = true;
        sendButton.disabled = true;
        var pending = addMessage("Thinking...", "bot");

        try {
            var response = await fetch(form.action, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": form.querySelector("[name='csrfmiddlewaretoken']").value
                },
                body: JSON.stringify({ messages: conversation })
            });
            var data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || "The assistant could not respond. Please try again.");
            }
            conversation.push({ role: "assistant", content: data.reply });
            conversation = conversation.slice(-10);
            pending.textContent = data.reply;
        } catch (error) {
            conversation.pop();
            pending.textContent = error.message || "The assistant could not respond. Please try again.";
        } finally {
            input.disabled = false;
            sendButton.disabled = false;
            input.focus();
            messagesElement.scrollTop = messagesElement.scrollHeight;
        }
    });
})();
