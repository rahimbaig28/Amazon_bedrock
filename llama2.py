import boto3
import json

prompt_data = """
Act as Shakespeare and write a poem on machine learning.
"""

bedrock = boto3.client(service_name="bedrock-runtime")
payload = {
    "prompt": prompt_data,
    "max_gen_len": 512,
    "temperature": 0.5,
    "top_p": 0.9
}
body = json.dumps(payload)
model_id = "meta.llama3-70b-instruct-v1:0"

try:
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )

    # Print the full response for debugging
    print("Full response:", response)
    
    response_body = json.loads(response.get("body").read())
    
    # Print the response body for debugging
    print("Response body:", response_body)

    response_text = response_body.get('generation', 'No generation key found in response')
    print(response_text)
except Exception as e:
    print(f"An error occurred: {e}")
