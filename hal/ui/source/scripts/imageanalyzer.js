

const fileInput = document.getElementById('fileUpload');


function SendChatMessage(message)
{
    const messageBubble = document.createElement('div');
    messageBubble.classList.add('d-flex', 'justify-content-end', 'mb-3');
    messageBubble.innerHTML = message;
    const chatBox = document.getElementById('chatBox');
    chatBox.appendChild(messageBubble);
    chatBox.scrollTop = chatBox.scrollHeight;
}


async function uploadFile() {
    const fileInput = document.getElementById('fileUpload');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const result = await response.json();
            SendChatMessage(result.message)
        } else {
            SendChatMessage('File upload failed.');
        }
    } catch (error) {
        console.error('Error uploading file:', error);
        SendChatMessage('An error occurred during upload.');
    }
}




fileInput.addEventListener('change', (event) => uploadFile());
{
    const file = event.target.files[0]; 
    if (file) 
    {
        const reader = new FileReader();
        reader.onload = (e) => SendChatMessage(e.target.result);
        reader.onerror = (e) => SendChatMessage("File could not be read!", e);
        reader.readAsText(file);
    } else SendChatMessage("No file selected")
}