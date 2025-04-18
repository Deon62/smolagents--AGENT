import yaml
import os
from smolagents import GradioUI, CodeAgent, HfApiModel
from langfuse_setup import *

# Step 2: Setup OpenTelemetry + SmolAgents tracing
from tracing_setup import *
# Get current directory path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

from tools.web_search import DuckDuckGoSearchTool as WebSearch
from tools.visit_webpage import VisitWebpageTool as VisitWebpage
from tools.suggest_room import SimpleTool as SuggestRoom
from tools.best_learning_platforms import SimpleTool as BestLearningPlatforms
from tools.final_answer import FinalAnswerTool as FinalAnswer



model = HfApiModel(
model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
)

web_search = WebSearch()
visit_webpage = VisitWebpage()
suggest_room = SuggestRoom()
best_learning_platforms = BestLearningPlatforms()
final_answer = FinalAnswer()


with open(os.path.join(CURRENT_DIR, "prompts.yaml"), 'r') as stream:
    prompt_templates = yaml.safe_load(stream)

# agent = CodeAgent(
#     model=model,
#     tools=[web_search, visit_webpage, suggest_room, best_learning_platforms],
#     managed_agents=[],
#     agent_name='CodeAgent',
#     max_steps=10,
#     verbosity_level=2,
#     grammar=None,
#     planning_interval=None,
#     name=None,
#     description=None,
#     executor_type='local',
#     executor_kwargs={},
#     max_print_outputs_length=None,
#     prompt_templates=prompt_templates
# )
agent = CodeAgent(
    model=model,
    tools=[web_search, visit_webpage, suggest_room, best_learning_platforms],
    managed_agents=[],
    max_steps=10,
    verbosity_level=2,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    executor_type='local',
    executor_kwargs={},
    max_print_outputs_length=None,
    prompt_templates=prompt_templates
)

if __name__ == "__main__":
    GradioUI(agent).launch()
