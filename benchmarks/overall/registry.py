from benchmarks.overall.methods.gt import GTMethod
from benchmarks.overall.methods.marker import MarkerMethod
from benchmarks.overall.methods.mathpix import MathpixMethod
from benchmarks.overall.scorers.heuristic import HeuristicScorer
from benchmarks.overall.scorers.llm import LLMScorer

SCORE_REGISTRY = {
    "heuristic": HeuristicScorer,
    "llm": LLMScorer
}

METHOD_REGISTRY = {
    "marker": MarkerMethod,
    "gt": GTMethod,
    "mathpix": MathpixMethod
}