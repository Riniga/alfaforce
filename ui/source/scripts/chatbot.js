document.getElementById('chatForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from refreshing the page
    
    // Get the message input value
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value.trim();


    if (message) {
        const sentMessageContent = `
            <div class="p-2 bg-secondary text-white rounded">
                <small>Me:</small>
                <p class="mb-0">${message}</p>
            </div>
        `;
        const sentMessageBubble = document.createElement('div');
        sentMessageBubble.classList.add('d-flex', 'justify-content-end', 'mb-3');
        sentMessageBubble.innerHTML = sentMessageContent;
        const chatBox = document.getElementById('chatBox');
        chatBox.appendChild(sentMessageBubble);
        
        fetch(api_url +"/chatbot?query="+message)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json(); // Parse the JSON response
        })
        .then(data => {
            console.log(data.message)
            const responseMessageContent = `
                <div class="p-2 bg-primary text-white rounded">
                    <small>Hal 9000:</small>
                    <p class="mb-0">${data.message}</p>
                </div>
            `;

            const responseMessageBubble = document.createElement('div');
            responseMessageBubble.classList.add('d-flex', 'justify-content-start', 'mb-3');
            responseMessageBubble.innerHTML = responseMessageContent;

            const chatBox = document.getElementById('chatBox');
            chatBox.appendChild(sentMessageBubble);
            chatBox.appendChild(responseMessageBubble);


        })
        .catch(error => {
            console.error("Error:", error);
        });
        
        chatBox.scrollTop = chatBox.scrollHeight;
        messageInput.value = '';
    }
});