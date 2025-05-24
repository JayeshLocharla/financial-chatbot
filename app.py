from flask import Flask, request, render_template

app = Flask(__name__)

# Hardcoded chatbot responses
chatbot_responses = {
    'microsoft': {
        'total revenue': "Microsoft's total revenue in FY 2024 was $245,122 million.",
        'net income': "Microsoft's net income in FY 2024 was $88,136 million.",
        'total assets': "Microsoft's total assets in FY 2024 were $512,163 million.",
        'total liabilities': "Microsoft's total liabilities in FY 2024 were $243,686 million.",
        'cash flow': "Microsoft's cash flow from operating activities in FY 2024 was $118,548 million."
    },
    'tesla': {
        'total revenue': "Tesla's total revenue in FY 2024 was $97,690 million.",
        'net income': "Tesla's net income in FY 2024 was $7,153 million.",
        'total assets': "Tesla's total assets in FY 2024 were $122,070 million.",
        'total liabilities': "Tesla's total liabilities in FY 2024 were $48,390 million.",
        'cash flow': "Tesla's cash flow from operating activities in FY 2024 was $14,923 million."
    },
    'apple': {
        'total revenue': "Apple's total revenue in FY 2024 was $391,035 million.",
        'net income': "Apple's net income in FY 2024 was $93,736 million.",
        'total assets': "Apple's total assets in FY 2024 were $364,980 million.",
        'total liabilities': "Apple's total liabilities in FY 2024 were $308,030 million.",
        'cash flow': "Apple's cash flow from operating activities in FY 2024 was $118,254 million."
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        query = request.form.get("query", "").lower()
        found = False
        for company, topics in chatbot_responses.items():
            if company in query:
                for topic, answer in topics.items():
                    if topic in query:
                        response = answer
                        found = True
                        break
            if found:
                break
        if not found:
            response = "Sorry, I can only answer predefined queries about Microsoft, Tesla, or Apple."
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
