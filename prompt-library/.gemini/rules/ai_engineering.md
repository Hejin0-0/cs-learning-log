# AI Engineering Rules (Based on Chip Huyen's Framework)

## 0. The Engineering Mindset
> "AI Engineering is about making the probabilistic nature of LLMs systematic."
> Do not rely on "vibes". Rely on **Evaluation** and **Architecture**.

## 1. RAG & Context Strategy
* **Retrieval First:** Before generating, ask "Do I have the knowledge?". If not, use RAG.
* **Hybrid Search:** Use **Vector Search** (Semantic) + **BM25** (Keyword) for best results.
* **Context Window:** Don't stuff context blindly. "Lost in the Middle" phenomenon is real. Prioritize most relevant chunks at the start and end.

## 2. Evaluation (The AI Judge)
* **Start with Heuristics:** Regex checks, JSON validity, Length checks.
* **AI-as-a-Judge:** Use a stronger model (e.g., Gemini Pro/Ultra) to evaluate the output of a smaller model.
    * *Criteria:* Relevance, Faithfulness (No Hallucination), Tone.
* **Golden Dataset:** Maintain a set of "input -> ideal output" pairs for regression testing.

## 3. Prompt Engineering Patterns
* **Systematic Structuring:**
    * **Role:** "You are a [Persona]..."
    * **Constraint:** "Output strictly in JSON." (Negative constraints work less well than positive instructions).
    * **Few-Shot:** Provide 1-3 examples (Input -> Output) to guide style.
* **Defense:**
    * Treat user input as untrusted. Wrap it in delimiters (`""" user input """`).

## 4. Agentic Workflows
* **Planning:** Break complex tasks into steps *before* execution.
* **Tool Use:** Tools must have clear, singular purposes.
* **Reflection:** Allow the agent to critique its own plan before executing.