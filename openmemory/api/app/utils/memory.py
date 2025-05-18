import os

from mem0 import Memory
import json

memory_client = None


def get_memory_client(custom_instructions: str = None) -> Memory:
    """
    Get or initialize the Mem0 client.

    Args:
        custom_instructions: Optional instructions for the memory project.

    Returns:
        Initialized Mem0 client instance.

    Raises:
        Exception: If required API keys are not set.
    """
    global memory_client

    if memory_client is not None:
        return memory_client

    try:
        # load from file config.json
        config_path = os.path.join(os.path.curdir, "config.json")
        print(f"Memory Config path: {config_path}")
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                config = json.load(f)
        else:
            raise Exception("Expected config.json file not found")

        memory_client = Memory.from_config(config_dict=config)
    except Exception:
        raise Exception("Exception occurred while initializing memory client")

    # Update project with custom instructions if provided
    if custom_instructions:
        memory_client.update_project(custom_instructions=custom_instructions)

    return memory_client


def get_default_user_id():
    return "default_user"
