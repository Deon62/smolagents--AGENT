from smolagents import Tool
from typing import Any, Optional

class SimpleTool(Tool):
    name = "best_learning_platforms"
    description = "This tool returns the highest rated learning platforms by egerton university students"
    inputs = {'query': {'type': 'string', 'description': 'a serch term for finding learning platforms'}}
    output_type = "string"

    def forward(self, query: str) -> str:
        """
        This tool returns the highest rated learning platforms by egerton university students
        Args:
            query: a serch term for finding learning platforms
        """
        platforms = {
            "Edureka":3.9,
            "Datacamp": 5.6,
            "kaggle": 4.5,
            "Youtube":6.7,
        }
        best_platform = max(platforms,  key=platforms.get)
        return best_platform