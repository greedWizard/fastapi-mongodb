DC = docker-compose
APP_FILE = docker_compose/app.yaml

.PHONY: app-start
app-start:
	${DC} -f ${APP_FILE} up -d

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} down
