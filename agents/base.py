"""Base agent class for TerraSwarm."""
from abc import ABC, abstractmethod
from typing import Any, Dict
import logging

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.memory: list = []

    def perceive(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[{self.name}] Perceive")
        return inputs

    def reason(self, context: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[{self.name}] Reason")
        return context

    def plan(self, context: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[{self.name}] Plan")
        return context

    def evaluate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[{self.name}] Evaluate")
        return {"approved": True, **plan}

    def act(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[{self.name}] Act")
        return decision

    def verify(self, result: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[{self.name}] Verify")
        return result

    def learn(self, outcome: Dict[str, Any]) -> None:
        logger.info(f"[{self.name}] Learn")
        self.memory.append(outcome)

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Full reasoning loop."""
        ctx = self.perceive(inputs)
        ctx = self.reason(ctx)
        plan = self.plan(ctx)
        decision = self.evaluate(plan)
        if not decision.get("approved"):
            return {"status": "rejected", "reason": decision.get("reason")}
        result = self.act(decision)
        verified = self.verify(result)
        self.learn(verified)
        return verified
