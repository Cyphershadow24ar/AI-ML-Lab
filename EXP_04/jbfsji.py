import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow

fig, ax = plt.subplots(figsize=(12,7))
ax.axis('off')

# Title
plt.text(0.5, 1.05, "Feasibility & Viability – Public Health Chatbot", fontsize=18, weight='bold', ha='center')

# Left box - Feasibility
feasibility_text = """📱 Operational → Mobile/web use, multilingual chatbot, OTP/ID access
🌐 Technical → Databases, Blockchain, AI/NLP, Cloud (Hybrid model)
💰 Economic → Moderate setup cost, Govt/NGO/CSR support, hospital savings
📜 Legal → Health data privacy (HIPAA/GDPR-like laws)
⏳ Schedule → MVP core features, advanced AI/Blockchain later"""

plt.text(0.05, 0.8, "Feasibility", fontsize=14, weight='bold', color='blue')
plt.text(0.05, 0.35, feasibility_text, fontsize=11, va='top')

# Right box - Viability
viability_text = """👥 Social → Impact on migrant workers, better treatment quality
🏥 Business → Hospitals, NGOs, govt partnerships, reduced costs
🌱 Sustainability → Govt digital health mission alignment (Ayushman Bharat)
📖 Adoption → Awareness campaigns, user-friendly design"""

plt.text(0.65, 0.8, "Viability", fontsize=14, weight='bold', color='green')
plt.text(0.65, 0.45, viability_text, fontsize=11, va='top')

# Center Problem → Solution with lightbulb
plt.text(0.5, 0.55, "Problem → Solution", fontsize=14, weight='bold', ha='center')
plt.text(0.5, 0.5, "💡", fontsize=40, ha='center')

# Bottom box - Drawbacks & Strategies
bottom_text = """🗣️ Dialect issues → 📘 Local glossaries + Human validation
🤔 Low trust → 🩺 Doctor referral + NGO endorsement
🔒 Data risk → 🔐 Encryption + Opt-out
📶 Connectivity → 💾 Offline cache + Queue queries
⚠️ Wrong advice → ✅ Govt guidelines + Expert audits
💻 Server spikes → ☁️ Auto-scaling + Cached answers"""

plt.text(0.5, 0.25, "Drawbacks & Strategies", fontsize=14, weight='bold', ha='center', color='darkred')
plt.text(0.5, 0.05, bottom_text, fontsize=11, ha='center', va='bottom')

plt.show()
