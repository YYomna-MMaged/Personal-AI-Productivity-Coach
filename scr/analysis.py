from scr.llm_prompts import daily_analysis_prompt, task_organization_prompt
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch


from huggingface_hub import login
login()

model_name = "mistralai/Mistral-Nemo-Instruct-2407"
tok = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",     
    torch_dtype=torch.float16
)

def analyze_day_report(user_text, kb_context, tasks_text=""):
    prompt = daily_analysis_prompt(user_text, kb_context)  

    inputs = tok(prompt, return_tensors="pt", max_length=3000)
    outputs = model.generate(
        **inputs, 
        max_new_tokens=1200,
        temperature=0.7,
        top_p=0.95,
        do_sample=True,
        pad_token_id=tok.eos_token_id
    )
    llm_output_text = tok.decode(outputs[0], skip_special_tokens=True)

    return llm_output_text

def analyze_tasks(tasks_text: str):
    prompt = task_organization_prompt(tasks_text)

    inputs = tok(prompt, return_tensors="pt", max_length=3000)
    outputs = model.generate(
        **inputs,
        max_new_tokens=1000,
        temperature=0.7,
        top_p=0.95,
        do_sample=True,
        pad_token_id=tok.eos_token_id
    )
    llm_output_text = tok.decode(outputs[0], skip_special_tokens=True)

    return llm_output_text

