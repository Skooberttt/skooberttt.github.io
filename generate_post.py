import datetime
import os
from transformers import pipeline, set_seed

# ── Your Amazon Associates ID here ──
TAG = "skooberttt-20"

def main():
    # Create a text-generation pipeline using DistilGPT-2
    generator = pipeline(
        "text-generation",
        model="distilgpt2",
        device=-1  # CPU
    )
    set_seed(42)  # for reproducible outputs (optional)

    # Build prompt
    niche = "home office gadgets under $50"
    today = datetime.date.today().isoformat()
    filename = f"{today}-top-10.md"
    prompt = (
        f"Write a blog post titled \"Top 10 {niche} in 2025\" with:\n"
        "1. A quick intro\n"
        f"2. Ten items: name, 2-sentence description, and link [Product](https://amzn.to/{TAG})\n"
        "3. A short conclusion inviting readers to more deals.\n\n"
    )

    # Generate post (max_length caps total tokens; adjust as needed)
    result = generator(prompt, max_length=500, do_sample=True, temperature=0.7, num_return_sequences=1)
    post = result[0]["generated_text"]

    # Ensure output dir exists
    os.makedirs("posts", exist_ok=True)
    outpath = os.path.join("posts", filename)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(post)

    print(f"✅ Generated: {outpath}")

if __name__ == "__main__":
    main()
