import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

app.post("/api/chat", async (req, res) => {
  try {
    const { prompt, mode, divergence } = req.body;

    const modes = {
      LOGIC: `Explain scientifically. Divergence: ${divergence}%`,
      NARRATIVE: `Describe cinematically. Divergence: ${divergence}%`,
      DRIVER: `User alters timelines. Describe consequences. Divergence: ${divergence}%`,
      HYBRID: `Blend science and narrative. Divergence: ${divergence}%`
    };

    const completion = await openai.chat.completions.create({
      model: "gpt-5",
      messages: [
        { role: "system", content: modes[mode] || modes.HYBRID },
        { role: "user", content: prompt }
      ],
      temperature: 0.8,
      max_tokens: 600
    });

    res.json({ reply: completion.choices[0].message.content });

  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("FINUX FROST CORE RUNNING ON PORT 3000");
});
