const express = require("express");
const puppeteer = require("puppeteer");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

app.post("/extract", async (req, res) => {
  const { url } = req.body;
  if (!url) return res.status(400).json({ error: "No Instagram URL provided" });

  try {
    const browser = await puppeteer.launch({ headless: true, args: ["--no-sandbox"] });
    const page = await browser.newPage();

    // Spoof a real browser
    await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64)");

    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 0 });

    // Get video URL from meta tag
    const videoURL = await page.evaluate(() => {
      const meta = document.querySelector('meta[property="og:video"]');
      return meta?.content || null;
    });

    await browser.close();

    if (!videoURL) {
      return res.status(404).json({ error: "Video URL not found" });
    }

    return res.json({ video: videoURL });
  } catch (err) {
    console.error("Error:", err);
    return res.status(500).json({ error: "Failed to extract video" });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`🚀 Server running at http://localhost:${PORT}`));
