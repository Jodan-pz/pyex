.DEFAULT_GOAL := help

ROOT:=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))

# Args

# Colors
RED="\033[1;31m"
GREEN="\033[32m"
YELLOW="\033[1;33m"
LYELLOW="\033[33m"
BLUE="\033[1;34m"
LBLUE="\033[34m"
PINK="\033[35m"
CYAN="\033[1;36m"
NOCOLOR="\033[0m\033[K"

.PHONY: help

help: ## Display this help message
	@echo
	@echo $(GREEN)=$(BLUE)-------------------------------------------------$(GREEN)=$(NOCOLOR)
	@echo $(GREEN)="                    P y e x                      "=$(NOCOLOR)
	@echo $(GREEN)=$(BLUE)-------------------------------------------------$(GREEN)=$(NOCOLOR)
	@echo
	@echo $(LYELLOW)"Please use \`make <target>\` where <target> is one of\n"$(NOCOLOR)
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf $(GREEN)"%-25s"$(NOCOLOR)"%s\n", $$1, $$2}' | sed -e "s/\[32m##/[36m/"


.PHONY: upgrade-pip-tools compile upgrade install uninstall

##
## Dependencies
##

upgrade-pip-tools: ## Upgrade pip, setup & pip tools
	@source ./env/bin/activate; \
	python -m pip install --upgrade pip pip-tools setuptools 

compile: ./requirements/requirements.in ./requirements/dev-requirements.in ## Compile deps
	@source ./env/bin/activate; \
    cd ./requirements && pip-compile && pip-compile dev-requirements.in;
	
upgrade: ./requirements/requirements.in ./requirements/dev-requirements.in ## Upgrade deps
	@source ./env/bin/activate; \
    cd ./requirements && pip-compile -U && pip-compile -U dev-requirements.in;
	

install: requirements/requirements.txt requirements/dev-requirements.txt ## Install deps
	@source ./env/bin/activate; \
    cd ./requirements && pip-sync requirements.txt dev-requirements.txt;

uninstall: requirements/requirements.txt requirements/dev-requirements.txt ## Uninstall deps
	@source ./env/bin/activate; \
    cd ./requirements && pip uninstall -y -r requirements.txt && pip uninstall -y -r  dev-requirements.txt;
