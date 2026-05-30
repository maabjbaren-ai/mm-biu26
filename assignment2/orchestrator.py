import os
from openai import OpenAI
from vector_comparer import calculate_cosine_similarity

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def load_skill_prompt(skill_path: str) -> str:
    """טעינת קובץ ה-Skill.md המגדיר את אופי הסוכן"""
    with open(skill_path, 'r', encoding='utf-8') as file:
        return file.read()

def run_agent_step(input_text: str, skill_file_path: str) -> str:
    """הפעלת סוכן עם התחפושת (Skill) המתאימה"""
    system_prompt = load_skill_prompt(skill_file_path)
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_text}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def run_broken_phone_pipeline(original_sentence: str):
    print(f"=== Starting Level 4 Orchestration Session ===")
    print(f"[INPUT] Original English: '{original_sentence}'\n")
    
    # הגדרת נתיבי ה-Skills (יושבים בתיקייה .claude/skills)
    skills_dir = os.path.join(os.path.dirname(__file__), "..", ".claude", "skills")
    
    # שלב 1: אנגלית לצרפתית
    print("-> Activating Agent 1 (Skill: EN_TO_FR)...")
    french_out = run_agent_step(original_sentence, os.path.join(skills_dir, "en_to_fr", "Skill.md"))
    print(f"[RESULT] French: {french_out}\n")
    
    # שלב 2: צרפתית לעברית
    print("-> Activating Agent 2 (Skill: FR_TO_HE)...")
    hebrew_out = run_agent_step(french_out, os.path.join(skills_dir, "fr_to_he", "Skill.md"))
    print(f"[RESULT] Hebrew: {hebrew_out}\n")
    
    # שלב 3: עברית חזרה לאנגלית
    print("-> Activating Agent 3 (Skill: HE_TO_EN)...")
    final_english = run_agent_step(hebrew_out, os.path.join(skills_dir, "he_to_en", "Skill.md"))
    print(f"[RESULT] Final English: {final_english}\n")
    
    # שלב 4: הפעלת ה-Tool הווקטורי להערכת הביצועים
    print("-> Invoking Vector Comparison Tool...")
    similarity_score = calculate_cosine_similarity(original_sentence, final_english)
    drift_score = 1 - similarity_score
    
    print(f"==========================================")
    print(f"Execution Analytics Matrix:")
    print(f" - Semantic Cosine Similarity: {similarity_score:.4f}")
    print(f" - Semantic Vector Drift Rate: {drift_score:.4f}")
    print(f"==========================================")

if __name__ == "__main__":
    test_phrase = "One for all and all for one"
    run_broken_phone_pipeline(test_phrase)
