import json
import boto3

# Create a boto3 client for the bedrock-runtime
client_bedrock_runtime = boto3.client('bedrock-runtime')

# Create the body of the request to Anthropic Claud v2
req_body = {
    "prompt": "Human: what is 2 + 2 Assistant:",
    "max_tokens_to_sample": 300 #,
    #"temperature": 0.1,
    #"top_k": 250,
    #"top_p": 0.999,
    #"stop_sequences": [],
    #"anthropic_version": "bedrock-2023-05-31"
}

req_body = json.dumps(req_body)

# Call the anthropic claud v2 model
output = client_bedrock_runtime.invoke_model(body = req_body, modelId="anthropic.claude-v2", accept="application/json", contentType="application/json")

# Format the model response
output = output['body'].read().decode()
answer = json.loads(output)['completion']
print(answer)
