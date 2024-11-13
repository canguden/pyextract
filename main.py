import json
import openai
import ollama


with open('input_data.json', 'r') as f:
    input_data = json.load(f)


output_format = {
    "metadata": {
        "source": "Original JSON file",
        "generated_by": "AI assistant"
    },
    "data": []
}


for item in input_data:
    transformed_item = {
        "id": item["id"],
        "name": item["name"],
        "description": item["description"],
        "tags": item["tags"],
        "sentiment_analysis": {
            "sentiment": ollama.analyze_sentiment(item["description"]),
            "keywords": openai.extract_keywords(item["description"])
        }
    }
    output_format["data"].append(transformed_item)


with open('output_data.json', 'w') as f:
    json.dump(output_format, f, indent=2)