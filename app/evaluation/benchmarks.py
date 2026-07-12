from app.evaluation.dataset import DatasetLoader
from app.evaluation.evaluator import Evaluator
from app.evaluation.report import ReportGenerator


class BenchmarkRunner:

    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.evaluator = Evaluator()

    async def run(self, dataset_path: str):
        samples = DatasetLoader.load(dataset_path)

        traces = []

        for sample in samples:

            trace = await self.pipeline.classify(sample.email)

            traces.append(trace)

        results = await self.evaluator.evaluate_many(samples, traces)

        report = ReportGenerator.generate(results)

        return report
