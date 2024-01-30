document.getElementById('generate-btn').addEventListener('click', () => {
    const inputText = document.getElementById('input-text').value;
    const numQuestions = document.getElementById('num-questions').value;

    // Make an AJAX request to the Flask server
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/generate_questions');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = () => {
        if (xhr.status === 200) {
            const questions = JSON.parse(xhr.responseText);
            const generatedQuestionsDiv = document.getElementById('generated-questions');
            generatedQuestionsDiv.innerHTML = '';

            questions.forEach((question, index) => {
                const questionP = document.createElement('p');
                questionP.textContent = `Question ${index + 1}: ${question}`;
                generatedQuestionsDiv.appendChild(questionP);
            });
        } else {
            console.error(xhr.responseText);
            alert('An error occurred while generating questions.');
        }
    };
    xhr.send(JSON.stringify({ input_text: inputText, num_questions: numQuestions }));
});
