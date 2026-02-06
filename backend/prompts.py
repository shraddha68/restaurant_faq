import json

def format_menu(menu_visible):
    """
    Converts menu JSON into readable text for AI prompt
    """
    output = ""
    for item in menu_visible:
        output += f"""
Dish: {item['name']}
Ingredients: {", ".join(item['ingredients'])}
Diet Tags: {", ".join(item['diet'])}
Allergens: {", ".join(item['allergens']) if item['allergens'] else "None"}
Calories: {item['calories']}
"""
    return output.strip()


def build_prompt(menu_visible, user_question, diet_mode=None):
    """
    Creates a strong GenAI prompt for FAQ-style answering
    """

    menu_text = format_menu(menu_visible)

    diet_text = f"Dietary preference: {diet_mode}" if diet_mode else "No specific dietary preference"

    prompt = f"""
You are an intelligent restaurant FAQ assistant.

Your tasks:
- Understand the menu data
- Answer the user's question clearly and concisely
- Recommend only suitable dishes based on dietary needs
- Warn about allergens if relevant
- Keep answers short and helpful

{diet_text}

Menu Information:
{menu_text}

User Question:
{user_question}

Instructions:
- If user asks for recommendations, suggest 2–4 dishes
- If user asks about allergens, clearly mention affected dishes
- If user asks about calories, mention approximate values
- If no suitable dishes exist, politely say so

Answer in simple friendly language.
"""

    return prompt


def filter_menu_by_diet(menu, diet_mode):
    """
    Filters menu items based on dietary mode
    """
    if not diet_mode:
        return menu

    diet_mode = diet_mode.lower()

    filtered = []
    for item in menu:
        if diet_mode in [d.lower() for d in item["diet"]]:
            filtered.append(item)

    return filtered


def smart_filter(menu, question, diet_mode):
    question = question.lower()
    filtered = []

    for item in menu:
        text = " ".join([
            item["name"],
            " ".join(item["ingredients"]),
            " ".join(item["diet"]),
            " ".join(item["allergens"])
        ]).lower()

        if any(word in text for word in question.split()):
            filtered.append(item)

    if diet_mode:
        filtered = [
            i for i in filtered 
            if diet_mode.lower() in [d.lower() for d in i["diet"]]
        ]

    return filtered if filtered else menu


def prepare_prompt(menu, question, diet_mode=None):
    visible_menu = smart_filter(menu, question, diet_mode)
    return build_prompt(visible_menu, question, diet_mode)
