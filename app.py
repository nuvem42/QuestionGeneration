from flask import Flask, request, jsonify
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

app = Flask(__name__)

# Use the same model name for consistency
pipe = pipeline("text2text-generation", model="valhalla/t5-small-e2e-qg")

def generate_questions(text_data, num_questions):
    # Load the pre-trained T5 model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained("valhalla/t5-small-e2e-qg", model_max_length=512, legacy=False)
    model = AutoModelForSeq2SeqLM.from_pretrained("valhalla/t5-small-e2e-qg")

    # Prepare the input for the model
    input_text = f"generate questions: {text_data}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate questions
    questions = []
    for _ in range(num_questions):
        # Generate a question
        gen_ids = model.generate(
            input_ids,
            max_length=512,  # Set max_length here if needed
            num_beams=5,
            early_stopping=True,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
            length_penalty=1.0,
            no_repeat_ngram_size=2,
            bad_words_ids=[[tokenizer.unk_token_id]],
            num_return_sequences=1,
        )

        # Decode the generated question
        gen_text = tokenizer.decode(gen_ids[0], skip_special_tokens=True)

        # Append the decoded question to the list
        questions.append(gen_text)

    return questions

@app.route('/generate_questions', methods=['POST'])
def generate_questions_route():
    data = request.get_json()
    input_text = data['input_text']
    num_questions = data['num_questions']
    questions = generate_questions(input_text, num_questions)
    return jsonify(questions=questions)

if __name__ == '__main__':
    app.run(debug=True)