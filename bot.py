import os
import requests
import pytz
from datetime import time
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")

TZ = pytz.timezone("Africa/Maputo")


async def send_photo_post(context: ContextTypes.DEFAULT_TYPE, image_path: str, caption: str):
    with open(image_path, "rb") as photo:
        await context.bot.send_photo(
            chat_id=GROUP_ID,
            photo=photo,
            caption=caption
        )


async def morning_post(context):
    caption = """
🌅☀️ GOOD MORNING DIVERSITY VENTURES INVESTORS & TRADERS! ☀️🌅

A new day means new opportunities to grow, earn, and succeed in the market! 📈🔥

Stay focused. Stay disciplined. Remember — consistency builds profits. 💹

At Diversity Ventures, we provide a safe and reliable platform where you can:

✅ Invest securely
✅ Monitor & track your investments easily
✅ Receive free daily trading signals
✅ Access market insights and updates
✅ Get investment results within 24 hours with NO extra charges 💼⚡

💎 Want premium setups?
Join our VIP Futures Channel and receive 3–9 premium signals daily with 70–80% accuracy 🚀

🌐 Access the platform here:
Diversity Ventures Platform

📩 VIP Access & Inquiries:
Telegram Manager: @agent_rogermanuel

🔥 Let’s make today productive, profitable, and successful together!

#DiversityVentures #ForexTrading #CryptoTrading #InvestSmart #FinancialFreedom #MorningMotivation
"""
    await send_photo_post(context, "images/morning.jpg", caption)


async def market_update(context):
    data = requests.get(
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin,ethereum,solana,binancecoin,ripple"
        "&vs_currencies=usd"
        "&include_24hr_change=true"
    ).json()

    caption = f"""
📊 DIVERSITY VENTURES MARKET UPDATE

🟠 Bitcoin: ${data['bitcoin']['usd']} | 24h: {data['bitcoin']['usd_24h_change']:.2f}%
🔵 Ethereum: ${data['ethereum']['usd']} | 24h: {data['ethereum']['usd_24h_change']:.2f}%
🟣 Solana: ${data['solana']['usd']} | 24h: {data['solana']['usd_24h_change']:.2f}%
🟡 BNB: ${data['binancecoin']['usd']} | 24h: {data['binancecoin']['usd_24h_change']:.2f}%
⚫ XRP: ${data['ripple']['usd']} | 24h: {data['ripple']['usd_24h_change']:.2f}%

💼 Investor Reminder:
Protect your capital, manage your risk, and avoid emotional entries.

⚠️ Not financial advice.
"""
    await send_photo_post(context, "images/market.jpg", caption)


async def noon_post(context):
    caption = """
💎 MENTALIDADE DE INVESTIDOR ELITE

Todo trader de sucesso já foi um iniciante que se recusou a desistir. 📈🔥

O mercado não recompensa emoções — recompensa disciplina, paciência e execução inteligente.

✅ Mantenha o foco quando os outros entrarem em pânico
✅ Seja paciente quando os lucros demorarem
✅ Seja consistente mesmo nos dias mais lentos

Lembre-se:
Pequenos lucros fazem grandes contas crescerem.
Boas decisões constroem riqueza.
A disciplina cria campeões. 💹

Continue aprendendo. Continue negociando. Continue evoluindo. 🚀

🔥 Diversity Ventures
"""
    await send_photo_post(context, "images/noon.jpg", caption)


async def promo_post(context):
    caption = """
🚀 LEVEL UP YOUR TRADING GAME! 📈🔥

Looking for reliable trading signals and a serious trading community?

Join Diversity Ventures Platform today and start receiving FREE daily signals.

✅ What You Get:
• Free daily trading signals
• Market insights & updates
• Beginner-friendly trading environment
• Active trading community

💎 VIP Futures Channel:
🔥 3–9 premium signals DAILY
📊 70–80% accuracy rate
⚡ Faster entries & exclusive setups

📩 VIP Access:
Telegram: @agent_rogermanuel

🚨 Don’t miss profitable opportunities while others are cashing out.
"""
    await send_photo_post(context, "images/promo.jpg", caption)


async def evening_post(context):
    caption = """
🌙 EVENING INVESTOR REMINDER

Professional investors do not panic.

They study.
They plan.
They manage risk.
They stay consistent.

📊 Diversity Ventures
"""
    await send_photo_post(context, "images/evening.jpg", caption)


async def night_post(context):
    caption = """
🌃✨ GOOD NIGHT INVESTORS & TRADERS ✨🌃

Another trading day conquered. 📈
Another step closer to financial freedom and long-term success. 💼💰

Rest your mind.
Recharge your energy.
Tomorrow is another opportunity to learn, grow, and profit. 🚀🔥

Remember: disciplined investors build lasting wealth.

Sleep well and come back stronger tomorrow. 💎

🔥 Diversity Ventures
"""
    await send_photo_post(context, "images/night.jpg", caption)


app = ApplicationBuilder().token(BOT_TOKEN).build()

# DAILY AUTOMATIC POSTS — MOZAMBIQUE TIME
app.job_queue.run_daily(morning_post, time(6, 0, tzinfo=TZ))
app.job_queue.run_daily(market_update, time(10, 0, tzinfo=TZ))
app.job_queue.run_daily(noon_post, time(12, 0, tzinfo=TZ))
app.job_queue.run_daily(promo_post, time(15, 0, tzinfo=TZ))
app.job_queue.run_daily(evening_post, time(20, 0, tzinfo=TZ))
app.job_queue.run_daily(night_post, time(23, 55, tzinfo=TZ))


print("Diversity Ventures Telegram bot is running...")
app.run_polling()