from app.classifiers.result import ClassificationResult


def build_prompt(
    email,
    rule: ClassificationResult,
    hf: ClassificationResult,
):

    return f"""
You are an expert email classifier.

Your job is to classify the email into EXACTLY ONE category.

Categories:

- Job Opening
- Software
- Technical Blogs
- Bank Statements
- Marketing
- Personal
- Fitness and Gym

----------------------

Email

Sender:
{email.sender_name}

Domain:
{email.sender_domain}

Subject:
{email.subject}

Snippet:
{email.snippet}

----------------------

Rule Engine Prediction

Category:
{rule.category.value}

Confidence:
{rule.confidence:.2f}

----------------------

HuggingFace Prediction

Category:
{hf.category.value}

Confidence:
{hf.confidence:.2f}

----------------------

Return ONLY JSON.

Example

{{
    "category":"Software",
    "confidence":0.93,
    "reason":"Email discusses cloud deployment and APIs."
}}
"""
