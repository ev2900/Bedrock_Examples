# pip install -
# python -m streamlit run app.py

import json
import boto3
import streamlit as st

# Create a boto3 client for the bedrock-runtime
client_bedrock_runtime = boto3.client('bedrock-runtime')

def main():

    # Side bar  
    with st.sidebar:
        
        # Select LLM drop down         
        models = ['anthropic.claude-v2']
        llm_model_name = st.selectbox('Select LLM', options = models)
        
        # Output length slider
        max_len = st.slider('Output Length', min_value = 100, max_value = 5000, value = 300, step = 100)
        
        # Tempature slider
        temp = st.slider('Temperature', min_value = 0., max_value = 1., value = 0.1, step =.01)
        
        # Prompt input
        user_input = st.text_area("Prompt goes here", "")
        
        if user_input:
            st.session_state['prompt'] = user_input
        
        # Button
        st.session_state['button'] = st.button('Generate', type='primary', key='structured')
    
    if st.session_state['button']: 
        
        # Create the body of the request to Anthropic Claud v2
        req_body = {
            "prompt": "Human:" + st.session_state['prompt'] + "Assistant:",
            "max_tokens_to_sample": max_len,
            "temperature": temp #,
            #"top_k": 250,
            #"top_p": 0.999,
            #"stop_sequences": [],
            #"anthropic_version": "bedrock-2023-05-31"
        }
        
        req_body = json.dumps(req_body)
        
        output = client_bedrock_runtime.invoke_model(body = req_body, modelId="anthropic.claude-v2", accept="application/json", contentType="application/json")
        
        # Format the model response
        output = output['body'].read().decode()
        answer = json.loads(output)['completion']
        
        st.markdown(answer)
        
        print(answer)
        
if __name__ == "__main__":
    main()