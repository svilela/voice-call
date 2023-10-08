import os
import sys
from datetime import datetime
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING, log
from pathlib import Path

from behave import (  # type: ignore
    given,
    model,
    step,
    then,
    use_step_matcher,  # type: ignore
    when,
)
from behave.model import Feature, Scenario  # type: ignore

import voice_call
from voice_call.log_config import LogConfig
from voice_call.util import Util

# use_step_matcher("re")
use_step_matcher("parse")

LogConfig().initialize_logger(INFO)
logger = LogConfig().get_logger()
print('\n\n• The script "environment.py" was loaded ...\n')
print(f'\n• The python version used is "{sys.version_info}"\n')
# print(f"\n• voice-call package version is {voice_call.__version__}\n\n")


def list_files(prefix: str, path: Path):
    l: list = Util.list_all_files(path)
    for item in l:
        logger.info(prefix + item)


def before_all(context):
    # Inicializa o contexto do behave
    context.status = "initializing . . ."
    context.list_files = list_files
    logger.info("\n\nbefore_all() called . . .\n")
    logger.info("-------------------------------------------------")
    context.list_files("before_all: ", Path("/tmp/"))
    logger.info("-------------------------------------------------")


# HOOK
def before_feature(context, feature: Feature):
    # Inicializa o status no contexto
    context.status = context.status if hasattr(context, "status") else "not defined"
    # Execute um método uma única vez para todos os cenários de teste da Feature
    logger.info("-------------------------------------------------")
    logger.info(f"vars(feature): {vars(feature)}")
    logger.info("-------------------------------------------------")


# HOOK
def before_scenario(context, scenario: Scenario):
    logger.info("-------------------------------------------------")
    logger.info(f"vars(scenario): {vars(scenario)}")
    logger.info("-------------------------------------------------")
