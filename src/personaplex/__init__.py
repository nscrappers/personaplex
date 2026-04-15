"""PersonaPlex: A multi-persona conversational AI framework.

Fork of NVIDIA/personaplex with extended persona management,
audio processing, and flexible LLM backend support.

Personal fork notes:
- Using this for experimenting with custom persona configs
- See examples/ directory for my test scripts
"""

__version__ = "0.1.0"
__author__ = "PersonaPlex Contributors"
__license__ = "MIT"

from personaplex.persona import Persona
from personaplex.engine import PersonaEngine

__all__ = [
    "Persona",
    "PersonaEngine",
    "__version__",
]
