help:
	@echo:"	   python -m rasa_nlu.train -c nlu_model_config.yml \
	--fixed_model_name current --data ./data/nlu/ --path ./models/nlu"
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    train-online"
	@echo "        Train a dialogue model online using Rasa core."	
	@echo "    run"
	@echo "        Runs the bot on the command line."

run:
	python bot.py run

train-nlu:
	python bot.py train-nlu

train-core:
	python bot.py train-dialogue

train-online:
	python bot.py train-online