# Interactive Learning System

Welcome to the Interactive Learning System! This README will walk you through what you'll experience when initializing and using the system, including some quirks and helpful tips from real usage.

---

## Initialization

When you start the system, you'll see something like:

```
Initializing Interactive Learning System...
Using default configuration
Enable autonomous learning in background? (y/n): Y
Enable web research capabilities? (y/n): Y
```

### Hugging Face Authentication

If you're running in Google Colab, you may see:

```
/usr/local/lib/python3.12/dist-packages/huggingface_hub/utils/_auth.py:94: UserWarning: 
The secret `HF_TOKEN` does not exist in your Colab secrets.
To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
You will be able to reuse this secret in all of your notebooks.
Please note that authentication is recommended but still optional to access public models or datasets.
  warnings.warn(
```

> **Tip:** If you need private models or higher usage limits, grab a token from Hugging Face!

---

## Model Downloads

The system will download whatever models or tokenizers it needs, printing progress like this:

```
tokenizer_config.json: 100%
config.json: 100%
vocab.json: 100%
merges.txt: 100%
tokenizer.json: 100%
model.safetensors: 100%
generation_config.json: 100%
Device set to use cpu
...
```

---

## Ready to Go!

Once everything is loaded, you'll see:

```
============================================================
Interactive Learning System Ready!
Type your questions or type 'exit' to quit
Type 'status' to see system status
Type 'config' to see current configuration
Type 'visualize' to generate a knowledge graph visualization
Autonomous learning is running in the background
Web research capabilities are enabled
============================================================
```

---

## Usage Example & Common Warnings

### File Analysis

If you ask to analyze files, you may get warnings like:

```
WARNING:AGISeed:Concept extraction failed:
Resource punkt_tab not found.
Please use the NLTK Downloader to obtain the resource:
>>> import nltk
>>> nltk.download('punkt_tab')
```

> **Tip:** If you see these NLTK errors, run the suggested code to install missing resources!

### System Status

Type `status` to see something like:

```
System Status:
Learning cycles: 20
Concepts learned: 61
Knowledge graph: 61 nodes, 159 edges
Semantic memory: 20 entries
Average concept confidence: 53.2%
Memory usage: 3874.6 MB
Current focus: web_research
Web research: Active
```

---

## FAQ & AI Logic

- **What does "analysing" do?**
  - Alters a file's contents. That's all. You don't need to do it unless you want to change something.
- **Why is analysis so common?**
  - Because it's a basic operation, not even worth putting in the FAQ!
- **What is the most important context for questions?**
  - The author's intention—what you (or the AI) are trying to achieve.

---

## Fun Interactions

You can play with meta-questions too!

**Q:** What question could I ask you that would make you smarter every time?
**A:** The one that asks "What question could I ask you that would make you smarter every time?" (recursive fun!)

---

## Troubleshooting

- If you see repeated warnings about missing resources (like `punkt_tab`), install the required NLTK data.
- If you see authentication warnings with Hugging Face, consider adding your token for seamless access.

---

## Credits

Most of the system's logic and quirkiness comes from a mix of autonomous learning, web research, and interactive feedback. If it says "It was me," it's just the AI having fun!

---

## Exit & Commands

- Type `exit` to quit.
- Type `status` for a system summary.
- Type `config` to review your settings.
- Type `visualize` to generate a knowledge graph.

---

Enjoy exploring, learning, and interacting with your AI learning buddy!
