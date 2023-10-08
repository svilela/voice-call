"""Constants for use with tests. Don't move this file elsewhere"""
from __future__ import annotations

import pathlib

CONSTANTS_DIR = pathlib.Path(__file__).parent
if not (
    str(CONSTANTS_DIR).endswith("voice-call/src/voice_call")
    or str(CONSTANTS_DIR).endswith("voice-call\\src\\voice_call")
):
    msg = "This file must be in a directory named 'src/voice_call'"
    raise ValueError(msg)
# caminho absoluto para o diretório do projeto
PROJECT_ROOT = CONSTANTS_DIR.parent.parent
# caminho absoluto para o diretório data
TEST_DATA = PROJECT_ROOT / "data"
TEST_ROOT = PROJECT_ROOT / "tests"
