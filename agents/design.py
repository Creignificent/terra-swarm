"""Consortium Design Agent: creates microbial mix and BOM."""
from .base import BaseAgent
from typing import Dict, Any

class ConsortiumDesignAgent(BaseAgent):
    def __init__(self):
        super().__init__("ConsortiumDesign")

    def plan(self, context: Dict[str, Any]) -> Dict[str, Any]:
        profile = context.get("profile", {})
        # Placeholder design logic
        design = {
            "strains": ["Pseudomonas putida", "Bacillus subtilis"],
            "ratios": [0.6, 0.4],
            "carrier": "biochar",
            "predicted_efficacy": 0.78,
            "bom": [{"item": "culture_A", "qty": 1}, {"item": "packaging", "qty": 1}]
        }
        context["design"] = design
        return context

    def evaluate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        design = plan.get("design", {})
        approved = design.get("predicted_efficacy", 0) > 0.6
        return {"approved": approved, **plan}
