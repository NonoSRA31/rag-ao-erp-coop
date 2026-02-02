def build_prompt(context: str, ao_section: dict, template: str) -> str:
    return f"""
CONTEXTE MÉTIER :
{context}

SECTION D'APPEL D'OFFRES :
{ao_section.get("cdc_text")}

EXIGENCES OBLIGATOIRES :
{ao_section.get("exigences", {}).get("EX_O", [])}

STRUCTURE DE RÉPONSE À RESPECTER :
{template}

INSTRUCTIONS STRICTES :
- Ne rien inventer
- Ne pas promettre de délais
- Ne pas promettre de coûts
- Utiliser uniquement les informations fournies
"""
