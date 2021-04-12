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

help: ## Display this help message
	@echo
	@echo $(GREEN)=$(BLUE)-------------------------------------------------$(GREEN)=$(NOCOLOR)
	@echo $(GREEN)="                       P y e x                   "=$(NOCOLOR)
	@echo $(GREEN)=$(BLUE)-------------------------------------------------$(GREEN)=$(NOCOLOR)
	@echo
	@echo $(LYELLOW)"Please use \`make <target>\` where <target> is one of\n"$(NOCOLOR)
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf $(GREEN)"%-25s"$(NOCOLOR)"%s\n", $$1, $$2}' | sed -e "s/\[32m##/[36m/"

.PHONY: help

##
## Dependencies
##

compile: ./requirements/requirements.in ./requirements/dev-requirements.in ## Compile deps
	cd ./requirements && pip-compile \
					  && pip-compile dev-requirements.in

install: requirements/requirements.in requirements/dev-requirements.in ## Install deps
