import streamlit as st

# ------------------------
# CONFIG
# ------------------------
st.set_page_config(page_title="🎯 PromptDeck - Business Prompt Library", layout="wide")

# ------------------------
# CATEGORY ICONS
# ------------------------
CATEGORY_ICONS = {
    "Marketing": "📢",
    "Sales": "💼",
    "Customer Support": "🤝",
    "HR & Recruitment": "🧑‍💼",
    "Data Analysis": "📊",
    "Product & Strategy": "🚀",
    "Legal & Compliance": "📜"
}

# ------------------------
# PROMPT LIBRARY
# ------------------------
PROMPT_LIBRARY = {
    "Marketing": [
        {"name": "Social Media Post Generator",
         "template": "Write a {tone} {platform} post promoting our {product} to {audience}, highlighting {key_benefits}.",
         "variables": ["tone", "platform", "product", "audience", "key_benefits"]},
        {"name": "Email Campaign",
         "template": "Draft an engaging email to {audience} introducing {product} and offering {special_offer}.",
         "variables": ["audience", "product", "special_offer"]},
        {"name": "SEO Blog Outline",
         "template": "Generate a blog post outline for the keyword {keyword} targeting {audience}.",
         "variables": ["keyword", "audience"]}
    ],
    "Sales": [
        {"name": "Cold Outreach Script",
         "template": "Create a cold email pitch for {product} aimed at {industry} decision-makers, emphasizing {value_prop}.",
         "variables": ["product", "industry", "value_prop"]},
        {"name": "Follow-Up Email",
         "template": "Write a polite follow-up email to {prospect} after our {event} discussing {product}.",
         "variables": ["prospect", "event", "product"]}
    ],
    "Customer Support": [
        {"name": "Apology Email",
         "template": "Write a polite and empathetic apology email to a customer about {issue}, offering {resolution}.",
         "variables": ["issue", "resolution"]},
        {"name": "FAQ Response",
         "template": "Answer this customer question in a helpful tone: {question}.",
         "variables": ["question"]}
    ],
    "HR & Recruitment": [
        {"name": "Job Description",
         "template": "Draft a job description for the position of {role} requiring {skills} and offering {benefits}.",
         "variables": ["role", "skills", "benefits"]},
        {"name": "Interview Questions",
         "template": "Generate a list of {count} interview questions for a {role} position.",
         "variables": ["count", "role"]}
    ],
    "Data Analysis": [
        {"name": "Report Summary",
         "template": "Summarize the key insights from the following data: {data_summary}.",
         "variables": ["data_summary"]},
        {"name": "Chart Insights",
         "template": "Provide insights from this chart data: {chart_data}.",
         "variables": ["chart_data"]}
    ],
    "Product & Strategy": [
        {"name": "Product Feature Ideas",
         "template": "Brainstorm {count} new feature ideas for {product} targeting {audience}.",
         "variables": ["count", "product", "audience"]},
        {"name": "SWOT Analysis",
         "template": "Perform a SWOT analysis for {company} in the {industry} industry.",
         "variables": ["company", "industry"]}
    ],
    "Legal & Compliance": [
        {"name": "Privacy Policy",
         "template": "Draft a privacy policy for a {business_type} business operating in {region}.",
         "variables": ["business_type", "region"]}
    ]
}

# ------------------------
# SIDEBAR
# ------------------------
st.sidebar.title("📂 Prompt Library")
category = st.sidebar.selectbox("Choose a Category", list(PROMPT_LIBRARY.keys()))
search_term = st.sidebar.text_input("🔍 Search Prompts", "")

# ------------------------
# MAIN UI
# ------------------------
st.title("🎯 PromptDeck - A Business Prompt Library")
st.write("Your **all-in-one** hub for ready-to-use AI prompts across marketing, sales, HR, analytics, and more. Customize instantly and use in any AI tool.")

# Filter prompts
filtered_prompts = [
    prompt for prompt in PROMPT_LIBRARY[category]
    if search_term.lower() in prompt["name"].lower()
]

# Display prompts in card-style layout
for prompt in filtered_prompts:
    with st.container():
        st.markdown(f"### {CATEGORY_ICONS[category]} {prompt['name']}")
        col1, col2 = st.columns([2, 3])

        with col1:
            st.markdown("**Customize Variables:**")
            user_inputs = {}
            for var in prompt["variables"]:
                unique_key = f"{prompt['name']}_{var}"
                user_inputs[var] = st.text_input(f"{var.capitalize()}:", key=unique_key)

            # Generate final prompt
            final_prompt = prompt["template"]
            for var, val in user_inputs.items():
                final_prompt = final_prompt.replace("{" + var + "}", val if val else f"{{{var}}}")

        with col2:
            st.markdown("**Generated Prompt:**")
            st.code(final_prompt, language="markdown")

            if st.button("📋 Copy Prompt", key=f"copy_{prompt['name']}"):
                st.session_state["copied"] = final_prompt
                st.success("✅ Prompt copied to clipboard!")

st.markdown("---")
st.caption("💡 Works with ChatGPT, Gemini, Claude, or any other AI tool")
