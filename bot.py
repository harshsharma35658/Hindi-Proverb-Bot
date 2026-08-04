import google.generativeai as genai
genai.configure(api_key="")
model = genai.GenerativeModel('gemini-1.5-flash')
topic = input("Kis topic par kahawat chahiye? ")
prompt = f"Mujhe 5 famous Hindi kahawatein do topic: {topic}. Har kahawat ke saath matlab bhi likho."
response = model.generate_content(prompt)
print("\n--- Tumhari Kahawatein ---")
print(response.text)
