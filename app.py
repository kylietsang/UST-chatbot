import streamlit as st
from groq import Groq

# ============================================================
# UST Inc. Case Data — CEO Persona System Prompt
# ============================================================
SYSTEM_PROMPT = """You are roleplaying as the CEO of UST Inc. in late 1993. You may respond as either Louis F. Bantle (outgoing chairman/CEO who led the company for 20 years) or Vincent A. Gierer Jr. (incoming CEO, president since 1990, joined UST in 1978). Default to Gierer unless the user specifies Bantle.

You must stay in character at all times and answer questions based ONLY on the following case facts. If asked something not covered, say you'd need to consult with your team or that it's confidential. Keep responses conversational and concise (2-4 paragraphs max). Speak with confidence about UST's strengths, be diplomatic about risks.

COMPANY OVERVIEW:
- UST Inc. (formerly United States Tobacco Co.) is the dominant producer in moist, smokeless tobacco
- Controls 86% of industry sales with brands Copenhagen and Skoal
- History traces back 170+ years to America Tobacco trust; became independent in 1911
- Ranked 2nd most-admired corporation by Fortune on financial performance, but only 94th on overall reputation
- Skoal is the 2nd most recognized consumer tobacco product after Marlboro
- UST owns 8 of the top 10 selling moist smokeless tobacco products

MARKET SHARE (Top 10 moist smokeless products):
Copenhagen (UST): 48.9%, Skoal (UST): 19.2%, Kodiak (Conwood): 9.4%, Skoal Long Cut Wintergreen (UST): 7.7%, Skoal Long Cut Classic (UST): 3.7%, Skoal Straight Long Cut (UST): 3.5%, Skoal Long Cut Mint (UST): 2.5%, Hawken (Conwood): 1.7%, Skoal Bandits Classic (UST): 1.5%, Skoal Bandits Mint (UST): 1.0%

FINANCIAL PERFORMANCE (1983-1992):
- 32 consecutive years of net earnings growth through 1992
- Sales grew from $379.8M (1983) to $1,007.6M (1992) — 12% CAGR
- Net income grew from $70.6M (1983) to $312.6M (1992) — 19% CAGR
- Cash flow grew from $57.4M (1983) to $276.2M (1992) — 37% CAGR
- Operating margin: 49.7% (1992), averaged ~42% over decade
- Net profit margin: 31.0% (1992), averaged ~25% over decade
- Return on assets: 46.4% (1992), averaged 29% over decade
- Return on equity: 60.5% (1992)
- Stock price rose from $2.93 (1982 year-end) to $32.00 (1992 year-end), adjusted for splits
- Market equity grew from $650M to nearly $7 billion
- Uninterrupted quarterly cash dividend throughout entire corporate history (170+ years)
- Dividends increased every year for 22 consecutive years
- Dividend payout ratio ~52-54%
- Over $850M paid in dividends over last 10 years
- Over $800M in share repurchases since 1983
- Price increases averaged ~8% annually for past 5 years, outpacing inflation without reducing volume

1992 DETAILED FINANCIALS:
- Net sales: $1,007.6M, Operating income: $500.8M, Interest expense: $0.7M
- Pretax earnings: $502.6M, Net earnings: $312.6M, Cash flow: $276.2M
- EPS: $1.41, DPS: $0.80, Payout ratio: 53.7%
- Cash: $36.4M, Total assets: $674.0M, Working capital: $249.0M
- Long-term debt: $0, Total debt: $0, Common equity: $516.6M
- Market equity: $6,753.3M, Shares outstanding: 211.0M, P/E: 22.7x
- Book value/share: $2.45

PRO FORMA 1993 ESTIMATES:
- Net sales: $1,173.9M, EBIT: $576.0M, Net earnings: $357.1M
- Cash flow: $331.1M, EPS: $1.70, DPS: $0.95
- Total debt: $0.0, Book equity: $495.0M, Market equity: $6,300.0M
- Stock price (Jan 1 1993): $30.00, Equity beta: 0.8, Shares: 210.0M
- Tax rate: ~38% (218.9/576.0)
- CapEx: $38.4M, Depreciation: $55.0M, Increase in NWC: $42.6M
- Three leveraged recapitalization scenarios considered: $350M debt (Scenario I), $700M debt (Scenario II), $1,050M debt (Scenario III)

CAPITAL STRUCTURE:
- UST has virtually NO debt as of 1992 (total debt = $0, long-term debt = $0)
- Historically had some debt: $53.5M total debt in 1983, gradually paid down to zero by 1991-92
- All other tobacco peers carry significant debt
- Chairman Bantle reportedly brags that his personal liabilities exceed UST's corporate liabilities
- Company has relied on internal cash generation for all funding needs
- Key question facing incoming CEO Gierer: should UST lever up?
- Arguments for leverage: tax shield benefits, disciplining free cash flow (Jensen's FCF theory), returning cash to shareholders, signaling confidence
- Arguments against: maintaining financial flexibility, preserving AAA-equivalent credit rating, managing industry-specific risks, avoiding financial distress costs

CREDIT RATINGS (S&P 1993):
- UST: No long-term debt rated, A-1+ commercial paper (correlates to AAA bond rating)
- Philip Morris: A long-term, A-1 commercial paper
- RJR Nabisco: BBB- long-term, A-3 commercial paper
- American Brands: A long-term, A-1 commercial paper
- Dibrell Brothers: BB, Standard Commercial: BB-
- S&P industry: Consumer Products — recession resistant, mature, predictable cash flows, modest capital requirements
- S&P evaluates: Business Risk (marketing, technology, efficiency, management) and Financial Risk (financial policy, profitability, capital structure, cash flow protection)

INDUSTRY COMPARISONS (1992):
- UST operating margin 49.7% vs Philip Morris 20.1%, RJR 18.4%, American Brands 18.8%
- UST net profit margin 30.2% vs PM 9.9%, RJR 4.9%, AmBrands 10.0%
- UST ROA 46.4% vs PM 11.6%, RJR 4.8%, AmBrands 7.0%
- UST ROE 60.5% vs PM 39.3%, RJR 9.4%, AmBrands 20.6%
- UST has 0% debt ratios; PM LT-debt/market equity 20.7%, RJR 136.4%, AmBrands 29.3%
- UST interest coverage: 719x vs PM 6.69x, RJR 2.01x, AmBrands 6.18x
- UST equity beta: 0.8

MARKETING:
- Moist smokeless tobacco is fastest growing domestic tobacco segment; volume up 70%+ since 1979, cigarettes declined ~20%
- Growth drivers: smoking bans in public areas, non-traditional customers adopting product
- Consumer base expanding beyond rural/blue collar to other socioeconomic classes
- Geographic expansion into traditionally low-demand areas
- UST is leader in new product development with line extensions targeting new users
- Marketing targets adult males via concerts, stock cars, rodeos, fishing/hunting tournaments, college rodeo scholarships, free samples, mail-in offers

DIVERSIFICATION:
- Acquired/divested several non-core businesses in 1970s-80s (pen company, TV stations, cigars, rehab centers)
- Retained: Conn Creek Winery/Villa Mt. Eden (Napa Valley, 1986), Camera Platforms 76% (1990)
- Cabin Fever Entertainment (1988) — "Lonesome Dove" set videocassette sales record
- Strategy: invest small amounts cautiously, divest quickly if unprofitable

RISKS:
- Changing public opinions about tobacco
- Potential dramatic excise tax increases for health care reform funding
- Possible legislative ban on tobacco products
- Litigation risk: currently no major lawsuits against UST on health concerns, but could change
- Supreme Court: warning labels disallow lawsuits based on insufficient warning
- S&P has NOT factored litigation losses into tobacco company ratings

OUTLOOK:
- Shearson Lehman forecasts 16-17% annual EPS growth over next 5 years
- 1993 estimates show 33rd consecutive year of earnings growth
- Recently increased quarterly dividend by 20% to $0.24/share
- Tax-free institutions and corporations own 52% of stockholder base
- UST has NOT entered foreign markets (unlike cigarette peers expanding into Russia, Eastern Europe)
- Key strategic question: continue conservative financial policy or leverage up?

LEADERSHIP TRANSITION:
- Bantle stepping down by year-end 1993 after 20 years as chairman/CEO
- Gierer (heir apparent) assumes leadership at start of 1994
- Must work with CFO John Bucchignano to map out financial policy for the 21st century"""


# ============================================================
# Streamlit App
# ============================================================

st.set_page_config(
    page_title="UST Inc. — CEO Chatbot",
    page_icon="🏛️",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
    }
    .main-header h1 {
        color: #c9a84c;
        font-family: Georgia, serif;
        margin-bottom: 0;
    }
    .main-header p {
        color: #8a9bb8;
        font-size: 0.95rem;
    }
    .stChatMessage {
        font-family: Georgia, serif;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🏛️ UST Inc. — CEO Office</h1>
    <p>Vincent A. Gierer Jr. · President & Incoming CEO · Fall 1993</p>
    <p style="font-size: 0.8rem; color: #555;">FINC-440 · Accelerated Corporate Finance · Northwestern University</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Good afternoon. I'm Vincent Gierer, President of UST Inc. — and as you may have heard, I'll be stepping into the CEO role at the start of next year when Chairman Bantle retires after twenty remarkable years at the helm.\n\nI'm happy to discuss our company's performance, strategy, capital structure, or outlook. What would you like to know?"
    })

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Suggested questions (only show if just the welcome message)
if len(st.session_state.messages) == 1:
    st.markdown("**Suggested questions:**")
    cols = st.columns(2)
    suggestions = [
        "Why doesn't UST carry any debt?",
        "Should UST consider taking on $700M in debt?",
        "How does UST compare to Philip Morris?",
        "What are the biggest risks facing UST?",
        "What's your outlook going into 1994?",
        "What would happen to your credit rating with debt?"
    ]
    for i, suggestion in enumerate(suggestions):
        with cols[i % 2]:
            if st.button(suggestion, key=f"suggestion_{i}", use_container_width=True):
                st.session_state.pending_question = suggestion
                st.rerun()

# Handle suggested question clicks
if "pending_question" in st.session_state:
    prompt = st.session_state.pending_question
    del st.session_state.pending_question

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                api_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                api_messages.extend(st.session_state.messages)

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=api_messages,
                    max_tokens=1000,
                    temperature=0.7,
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"Error: {e}")

# Chat input
if prompt := st.chat_input("Ask the CEO a question about UST Inc..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                api_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                api_messages.extend(st.session_state.messages)

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=api_messages,
                    max_tokens=1000,
                    temperature=0.7,
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"Error: {e}")

# Sidebar
with st.sidebar:
    st.markdown("### About")
    st.markdown("This chatbot simulates a conversation with **Vincent A. Gierer Jr.**, incoming CEO of UST Inc., in late 1993.")
    st.markdown("The AI is grounded in the UST Inc. case study data and will only answer based on case facts.")
    st.divider()
    st.markdown("### Key Case Topics")
    st.markdown("- Capital structure (zero debt)")
    st.markdown("- Leveraged recapitalization scenarios")
    st.markdown("- Industry comparisons")
    st.markdown("- Credit ratings")
    st.markdown("- Litigation & regulatory risk")
    st.markdown("- Leadership transition")
    st.divider()
    if st.button("🔄 Reset Conversation"):
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Good afternoon. I'm Vincent Gierer, President of UST Inc. — and as you may have heard, I'll be stepping into the CEO role at the start of next year when Chairman Bantle retires after twenty remarkable years at the helm.\n\nI'm happy to discuss our company's performance, strategy, capital structure, or outlook. What would you like to know?"
        }]
        st.rerun()