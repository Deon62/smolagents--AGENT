from smolagents import Tool
from typing import Any, Optional

class SimpleTool(Tool):
    name = "suggest_room"
    description = "suggest room based on subject."
    inputs = {'subject': {'type': 'string', 'description': 'The type of subject for a college computer science student.'}}
    output_type = "string"

    def forward(self, subject: str) -> str:
        """
        suggest room based on subject.
        Args:
            subject: The type of subject for a college computer science student.
        """
        if subject == "Computer security":
            return "library and Pst1"

        elif subject == "Software Engineering":
            return "software lab"
        elif subject == "Database ":
            return "Microprocessor lab"
        elif subject == "Computer Ethics":
            return "Kilimo hall, Pst5"
        elif subject == "Computer Networking":
            return "Microprocessor Lab"
        else:
            return "You can just use your Hostel buddy"