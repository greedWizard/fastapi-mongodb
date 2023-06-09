DC = docker-compose
APP_FILE = docker_compose/app.yaml
STORAGE_FILE = docker_compose/storages.yaml

.PHONY: app
app-start:
	${DC} -f ${APP_FILE} up -d

.PHONY: drop-app
drop-app:
	${DC} -f ${APP_FILE} down

.PHONY: all
all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} up --build -d

.PHONY: drop-all
drop-all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} down

.PHONY: logs
logs:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} logs -f
