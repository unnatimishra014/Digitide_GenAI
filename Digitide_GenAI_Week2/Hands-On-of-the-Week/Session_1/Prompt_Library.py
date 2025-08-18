import streamlit as st
import random

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
# PROMPT LIBRARY (with multiple templates for each)
# ------------------------
PROMPT_LIBRARY = {
    "Marketing": [
        {"name": "Social Media Post Generator",
         "templates": [
             "Write a {tone} {platform} post promoting our {product} to {audience}, highlighting {key_benefits}.",
             "Create a {tone} post for {platform} that showcases {product} for {audience} with emphasis on {key_benefits}.",
             "Craft a {tone} {platform} update introducing {product} to {audience}, focusing on {key_benefits}.",
             "Generate a {tone} piece of content for {platform} promoting {product} to {audience} and stressing {key_benefits}."
         ],
         "variables": ["tone", "platform", "product", "audience", "key_benefits"]},
        {"name": "Email Campaign",
         "templates": [
             "Draft an engaging email to {audience} introducing {product} and offering {special_offer}.",
             "Compose a promotional email for {audience} to announce {product} with a {special_offer}.",
             "Create an email campaign aimed at {audience} to present {product} and highlight {special_offer}.",
             "Write a compelling email to {audience} featuring {product} and an exclusive {special_offer}."
         ],
         "variables": ["audience", "product", "special_offer"]},
        {"name": "SEO Blog Outline",
         "templates": [
             "Generate a blog post outline for the keyword {keyword} targeting {audience}.",
             "Create an SEO-optimized blog outline focused on {keyword} for {audience}.",
             "Draft a blog post plan targeting {audience} using the keyword {keyword}.",
             "Outline a blog structure optimized for {keyword} and aimed at {audience}."
         ],
         "variables": ["keyword", "audience"]}
    ],
    "Sales": [
        {"name": "Cold Outreach Script",
         "templates": [
             "Create a cold email pitch for {product} aimed at {industry} decision-makers, emphasizing {value_prop}.",
             "Draft a cold outreach email for {industry} leaders about {product}, highlighting {value_prop}.",
             "Write a sales pitch email for {product} targeting {industry} executives with a focus on {value_prop}.",
             "Generate a persuasive cold email about {product} for {industry} professionals, stressing {value_prop}."
         ],
         "variables": ["product", "industry", "value_prop"]},
        {"name": "Follow-Up Email",
         "templates": [
             "Write a polite follow-up email to {prospect} after our {event} discussing {product}.",
             "Draft a follow-up email to {prospect} post-{event} about {product}.",
             "Compose a courteous follow-up to {prospect} referencing {event} and {product}.",
             "Send a reminder email to {prospect} after {event} highlighting {product}."
         ],
         "variables": ["prospect", "event", "product"]}
    ],
    "Customer Support": [
        {"name": "Apology Email",
         "templates": [
             "Write a polite and empathetic apology email to a customer about {issue}, offering {resolution}.",
             "Draft an apologetic message to address {issue} and propose {resolution}.",
             "Compose a heartfelt apology email explaining {issue} and providing {resolution}.",
             "Create a customer care email about {issue} with a {resolution}."
         ],
         "variables": ["issue", "resolution"]},
        {"name": "FAQ Response",
         "templates": [
             "Answer this customer question in a helpful tone: {question}.",
             "Provide a clear and friendly answer to: {question}.",
             "Respond to the following customer inquiry: {question}.",
             "Craft a concise and informative answer to: {question}."
         ],
         "variables": ["question"]}
    ],
    "HR & Recruitment": [
        {"name": "Job Description",
         "templates": [
             "Draft a job description for the position of {role} requiring {skills} and offering {benefits}.",
             "Create a job listing for {role} highlighting {skills} and {benefits}.",
             "Write a recruitment post for {role} with {skills} requirements and {benefits}.",
             "Compose a job ad for {role} including {skills} and {benefits}."
         ],
         "variables": ["role", "skills", "benefits"]},
        {"name": "Interview Questions",
         "templates": [
             "Generate a list of {count} interview questions for a {role} position.",
             "Create {count} relevant interview questions for hiring a {role}.",
             "List {count} key questions to ask a {role} candidate.",
             "Prepare {count} interview prompts for {role} applicants."
         ],
         "variables": ["count", "role"]}
    ],
    "Data Analysis": [
        {"name": "Report Summary",
         "templates": [
             "Summarize the key insights from the following data: {data_summary}.",
             "Provide a concise summary of the dataset: {data_summary}.",
             "Analyze and summarize this data: {data_summary}.",
             "Give a brief overview of the main points from: {data_summary}."
         ],
         "variables": ["data_summary"]},
        {"name": "Chart Insights",
         "templates": [
             "Provide insights from this chart data: {chart_data}.",
             "Interpret the following chart: {chart_data}.",
             "Analyze and explain what this chart shows: {chart_data}.",
             "Summarize the findings from this chart: {chart_data}."
         ],
         "variables": ["chart_data"]}
    ],
    "Product & Strategy": [
        {"name": "Product Feature Ideas",
         "templates": [
             "Brainstorm {count} new feature ideas for {product} targeting {audience}.",
             "List {count} innovative features for {product} aimed at {audience}.",
             "Suggest {count} features to enhance {product} for {audience}.",
             "Come up with {count} possible improvements for {product} that suit {audience}."
         ],
         "variables": ["count", "product", "audience"]},
        {"name": "SWOT Analysis",
         "templates": [
             "Perform a SWOT analysis for {company} in the {industry} industry.",
             "Create a SWOT breakdown for {company} operating in {industry}.",
             "Analyze {company} in the {industry} sector using SWOT framework.",
             "Generate SWOT points for {company} in {industry}."
         ],
         "variables": ["company", "industry"]}
    ],
    "Legal & Compliance": [
        {"name": "Privacy Policy",
         "templates": [
             "Draft a privacy policy for a {business_type} business operating in {region}.",
             "Write a privacy agreement for a {business_type} company in {region}.",
             "Create a privacy statement for {business_type} services based in {region}.",
             "Prepare a privacy terms document for a {business_type} in {region}."
         ],
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
st.write("Your **all-in-one** hub for ready-to-use AI prompts across marketing, sales, HR, analytics, and more.")

filtered_prompts = [
    prompt for prompt in PROMPT_LIBRARY[category]
    if search_term.lower() in prompt["name"].lower()
]

# Track current prompt per prompt name
if "current_prompts" not in st.session_state:
    st.session_state.current_prompts = {}

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

        with col2:
            st.markdown("**Generated Prompt:**")

            if prompt['name'] not in st.session_state.current_prompts:
                st.session_state.current_prompts[prompt['name']] = random.choice(prompt["templates"])

            final_prompt = st.session_state.current_prompts[prompt['name']]
            for var, val in user_inputs.items():
                final_prompt = final_prompt.replace("{" + var + "}", val if val else f"{{{var}}}")

            col_prompt, col_refresh = st.columns([4, 1])
            with col_prompt:
                st.code(final_prompt, language="markdown")
            with col_refresh:
                if st.button("🔄", key=f"refresh_{prompt['name']}"):
                    st.session_state.current_prompts[prompt['name']] = random.choice(prompt["templates"])
                    st.rerun()  # fixed for new Streamlit

            if st.button("📋 Copy Prompt", key=f"copy_{prompt['name']}"):
                st.session_state["copied"] = final_prompt
                st.success("✅ Prompt copied to clipboard!")

st.markdown("---")
st.caption("💡 Works with ChatGPT, Gemini, Claude, or any other AI tool")
