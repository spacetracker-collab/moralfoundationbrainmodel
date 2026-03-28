# Moral Foundations AI

Neural network inspired by Jonathan Haidt's Moral Foundations Theory.

## Run
pip install -r requirements.txt
python train.py
python inference.py


What you’re seeing is a **mid-range, non-dominant moral profile**, which is exactly why the system outputs *REVIEW REQUIRED*. Let’s interpret it cleanly.

---

### 🧠 1. Overall Pattern: No strong moral signal

All scores are clustered around **0.4–0.54**, which means:

* No foundation is strongly activated (>0.7)
* No foundation is strongly rejected (<0.3)

This indicates a **morally ambiguous or balanced scenario**, where the system cannot confidently justify approval or rejection.

---

### ⚖️ 2. Care & Fairness (~0.50–0.54)

* **Care (0.54)** and **Fairness (0.50)** are moderate
* This means:

  * Some concern for harm exists, but not urgent
  * Some fairness is present, but not clearly just or unjust

👉 Interpretation:
The action is *not clearly harmful*, but also *not strongly ethical*.

---

### 🏛️ 3. Authority (~0.53)

* Moderate respect for rules/institutions
* Not strongly aligned with governance or compliance

👉 Interpretation:
The system sees **partial legitimacy**, but nothing strongly validating it.

---

### 🤝 4. Loyalty (~0.42)

* Slightly lower score
* Weak group alignment or collective benefit

👉 Interpretation:
The action may not strongly support a community, nation, or shared identity.

---

### 🧼 5. Purity (~0.41)

* Low-moderate purity signal
* No strong moral disgust or ethical violation

👉 Interpretation:
There’s **no clear red flag**, but also nothing “morally clean” enough to strongly approve.

---

### ⚠️ 6. Why “REVIEW REQUIRED”

Your decision logic requires:

* High care + fairness → APPROVE
* High authority + loyalty → APPROVE
* High purity → REJECT

But here:

* Nothing crosses thresholds
* No moral axis dominates

👉 So the system is essentially saying:

> “This situation falls into a gray zone where automated moral judgment is insufficient.”

---

### 🔍 7. Deeper Interpretation (Important)

This is actually a **very realistic output**.

Most real-world ethical decisions:

* Are not extreme
* Involve trade-offs
* Sit in the middle of moral dimensions

So your model is behaving correctly—it is:

* Avoiding overconfidence
* Flagging ambiguity
* Deferring to human judgment

---

### 🧭 8. What this means in AI governance terms

If this were applied to AI alignment or policy:

* The system would **escalate for human review**
* Possibly request:

  * More context
  * Risk assessment
  * Stakeholder analysis

---

### 💡 Final Insight

This output represents a **“moral equilibrium state”**:

* No strong justification to act
* No strong reason to block
* Requires deliberation

In Haidt’s terms (from The Righteous Mind), the “elephant” (intuition) is **not leaning strongly in any direction**, so the “rider” (reasoning) cannot confidently decide.

---

If you want, I can:

* Adjust thresholds to make it stricter or more permissive
* Add uncertainty estimation (confidence scores)
* Turn this into a **multi-scenario ethical simulator**

