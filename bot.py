from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from policy import MrServicePolicy

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.featurizers import (
    MaxHistoryTrackerFeaturizer,
    BinarySingleStateFeaturizer)
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)


def train_online(input_channel=ConsoleInputChannel(),
                     interpreter= RasaNLUInterpreter("models/nlu/default/current"),
                     domain_file="mrservice_domain.yml",
                     training_data_file='data/dialogue/stories.md'):
                       
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), MrServicePolicy()],
                  interpreter=interpreter)

    training_data = agent.load_data(training_data_file)
    agent.train_online(training_data,
                       input_channel=input_channel,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent


def train_dialogue(domain_file="mrservice_domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/dialogue/stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=3),
                            MrServicePolicy()])

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            epochs=100,
            batch_size=64,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('data/nlu/')
    trainer = Trainer(config.load("nlu_model_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      project_name='default',  
                                      fixed_model_name="current")

    return model_directory


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


def visualize(output_file='stories.png'):
    agent = Agent("mrservice_domain.yml",
                  policies=[MemoizationPolicy(), MrServicePolicy()])

    agent.visualize("data/dialogue/stories.md",
                    output_file, max_history=2)


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "train-online", "run", "visualize"],
            help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "train-online":
        train_online()
    elif task == "run":
        run()
    elif task == "visualize":
        visualize()
