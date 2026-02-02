



class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Tool] = {}  # Maps tool names to Tool instances

    def register_tool(self, name, tool):
        self.tools[tool.name] = tool

    def get_tool(self, name) -> Tool:
        if name not in self.tools.keys():
            raise ValueError(f"Tool '{name}' not found")
        return self.tools[name]

    def list_tools(self):
        return list(self.tools.keys())

