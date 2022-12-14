# Individual task 2

## Общие требования

0. Строго после сдачи 1-й работы (я закрыл issue без вопросов) приступить к выполнению issues из своего проекта, следуя выбранному методу управления ветками.
1. Задачи необходимо линковать с issues. Если в процессе работы возникнет необходимость создать дополнительную issue под фичу или баг -- можно смело это сделать.
2. Предоставить возможность запуска своего сервиса в Docker-контейнере. При этом финальный образ должен быть чист от промежуточных артефактов сборки (используйте multistage build).
3. После завершения работы, подготовить релиз (в случае `git-flow`, это `release/` ветка и коммит в `master`). Протегать свой релиз (в случае GitHub, справа есть колонка, где можно указать тег решиза и написать `release notes`). В процессе подготовки релиза, обновить `README.md` файл, он должен содержать информацию о проекте, инструкцию по его сборке и запуску и пару примеров работы.
4. Отправить мне на проверку (так же создать issue в моём репо) -- <https://github.com/SemenMartynov/Software-Engineering-2022>
5. Пока не нужно беспокоиться о тестах, это будет в следующей работе.

Задание принято, если я закрыл issue.
Мягкий дедлайн по этой работе -- **03 декабря**. Тогда за 04 декабря я постараюсь всё проверить.

## На что я буду обращать внимание

0. Просто напоминаю, что это должна быть оригинальная работа автора.
1. Нарушение методов управления ветками (к примеру, прямые коммиты в `master` или `develop` ветки при работе по git-flow).
2. Нарушение хороших практик работы с git (если не настроен `.gitconfig` в системе, и коммиты идут от неизвестного пользователя).
3. Коммиты не слинкованы с issues, либо один коммит имеет решения для задачи выходящий за скоуп одной issue (коммит должен решать только ту задачу, которая поставлена в issue).
4. Наличие мусора в репозитории (бинарники, служебные файлы используемой IDE) -- всё это должно быть прикрыто `.gitignode`. Однако Gradle Wrapper в репо допускается.
5. Плохое (не полное, непонятное) описание сообщений к коммитам.
