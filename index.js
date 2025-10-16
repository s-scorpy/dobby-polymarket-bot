import dotenv from "dotenv";
dotenv.config();

import TelegramBot from "node-telegram-bot-api";
import fetch from "node-fetch";

const TG_TOKEN = process.env.TG_TOKEN;
const LLM_API_KEY = process.env.LLM_API_KEY;
const CRYPTO_TAG_ID = 21;

if (!TG_TOKEN) {
  console.error("Missing TG_TOKEN in environment. Add it to .env");
  process.exit(1);
}
if (!LLM_API_KEY) {
  console.error("Missing LLM_API_KEY in environment. Add it to .env");
  process.exit(1);
}

const bot = new TelegramBot(TG_TOKEN, { polling: true });
console.log("🤖 Dobby Polymarket Bot started!");

// Example: /start
bot.onText(/\/start/, (msg) => {
  bot.sendMessage(
    msg.chat.id,
    `👋 Hey ${msg.from.first_name || "friend"}!

I'm Dobby — your Polymarket Advisor 🤖

I track crypto markets and give short, witty insights (~30 words).
Always remember to DYOR. DON'T TAKE FINANCIAL ADVICE FROM THIS BOT

Commands you can use:
/start - Show this message
/market <keyword> - Search crypto markets (e.g., /market bitcoin)
/top - List top crypto markets (10 at a time — up to 150)`,
    { parse_mode: "Markdown" }
  );
});

// Add your full bot logic here (truncated for brevity)
