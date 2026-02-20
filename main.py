import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate # التعديل اللي عملناه للمسار

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0
)
reasoning_template = """
You are a sentiment analyst. Provide reasoning steps to enhance transparency.
Identify emotional triggers and context before deciding.

Text: {user_input}

Return ONLY a JSON object:
{{
    "approach": "Reasoning",
    "steps": ["step 1", "step 2"],
    "final_sentiment": "Positive/Negative"
}}
"""

reliability_template = """
Classify the sentiment of the text as Positive or Negative.
To maintain reliability and reduce errors, provide the final answer only.

Text: {user_input}

Return ONLY a JSON object:
{{
    "approach": "Reliability",
    "final_sentiment": "Positive/Negative"
}}
"""

def run_sentiment_analysis(text):
    results = {}
    try:
        # 1. Reasoning
        reasoning_prompt = PromptTemplate.from_template(reasoning_template)
        chain_1 = reasoning_prompt | llm
        results["reasoning_output"] = json.loads(chain_1.invoke({"user_input": text}).content.strip('`json\n '))

        # 2. Reliability
        reliability_prompt = PromptTemplate.from_template(reliability_template)
        chain_2 = reliability_prompt | llm
        results["reliability_output"] = json.loads(chain_2.invoke({"user_input": text}).content.strip('`json\n '))

        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        
        print("\n✅ تم التحليل بنجاح! النتائج في ملف output.json")
        print(json.dumps(results, indent=4, ensure_ascii=False))

    except Exception as e:
        print(f"❌ حدث خطأ أثناء التحليل: {e}")

if __name__ == "__main__":
    user_in = input("Enter text to analyze: ")
    run_sentiment_analysis(user_in)
