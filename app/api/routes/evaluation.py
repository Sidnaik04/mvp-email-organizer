from fastapi import APIRouter

from app.classifiers.decision_engine import DecisionEngine
from app.evaluation.benchmarks import BenchmarkRunner

router = APIRouter(prefix="/evaluation", tags=["Evaluation"])


@router.get("/run")
async def run_benchmark():
    runner = BenchmarkRunner(DecisionEngine())

    return await runner.run("evaluation/gold_dataset.json")
