import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"
headers = {'Content-Type': 'application/json'}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "codeguru",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = json.loads(response.text)
        actual_response = response_data['response']
        return actual_response
    else:
        print("error:", response.text)

with gr.Blocks() as demo:
    prompt_input = gr.Textbox(lines=4, placeholder="Enter your Prompt")
    output_text = gr.Textbox()

    submit_button = gr.Button("Generate")

    submit_button.click(generate_response, inputs=prompt_input, outputs=output_text)

demo.launch()
