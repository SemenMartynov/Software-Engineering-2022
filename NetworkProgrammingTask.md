# Задание

## Блокчейн

Блокчейн -- это распределённая база данных, где каждый участник может хранить, просматривать, проверять но не удалять данные. Все данные разбиваются на блоки, и каждый блок имеет односвязную связность с предыдущими блоками, позволяющую верифицировать эти блоки. Верификацией занимаются как раз узлы, которые и поддерживают работоспособность блокчейна.

Каждый блок состоит из следующих полей:
- index -- номер блока. Номера возрастают по порядку с первого.
- prev_hash -- хеш предыдущего блока.
- hash -- хеш текущего блока. Его нужно будет вычислить.
- data -- данные... В нашем случае пусть это будет строка длинной случайных 256 символов.
- nonce -- это дополнение, которое нужно будет сделать в блоке таким образом, чтобы выполнялось требование по хешированию.

Производство блока это простая операция.
Нужно сконкатенировать поля index, prev_hash, data и nonce, и результат записать в поле hash.
Но результат можно записывать только при условии, что hash заканчивается на 4 ноля. Если это не так, то нужно увеличить дополнение (nonce) и снова попробовать вычислить хеш (в качестве хеш-функции предлагаю использовать sha256, но окончательный выбор оставляю за вами).

Как только новый блок сгенерирован, то нужно отправить его остальным узлам (нодам) сети, и переходить к генерации следующего блока (т.е. index увеличивается, data нужно сгенерировать по новой, а в качестве prev_hash использовать хеш предыдущего блока). В то же время, пока мы подбираем хеш, кто-то из соседних узлов мог уже добиться успеха в этом, и присылает нам свой блок. Тогда нужно проверить, что хеш посчитан правильно, и переходить к генерации нового блока используя полученный в качестве предыдущего (если хеш не правильный, или блок произведён от уже устаревшего блока -- его нужно игнорировать). 

Так же нужно следить, чтобы нода не оказалась в minority. Такое возможно, если она пропустила какой-то блок, и пытается генерировать новые блоки от уже устаревшего блока. В это время остальные ноды и блокчейн ушли уже вперёд. Чтобы разрешить эту ситуацию, можно попросить блоки у своих соседней, проверить их цепочки и использовать "новый" последний блок для продолжения работы по генерации блоков.

## Демонстрация работы

Через Docker Compose запускаются три ноды. Одна из них (это можно сделать через передачу аргумента или переменную окружения) должна сгенерировать первый блок (genesis). Дальше либо эта нода оповестит соседей о выпуске блока, либо сами соседи опросят ноду на предмет наличия блока. А дальше начинается гонка между тремя нодами, кто первым рассчитает хеш заканчивающийся на 4 ноля для следующего блока, и отправит эту информацию в сеть. Каждый узел может использовать свой подход для расчёта nonce -- кто-то может каждый раз последовательно увеличивать на 1, кто-то увеличивает по Фибоначчи, кто-то вообще использует рандомное значение.

Если работу хочется делать командой, то задача усложнится -- нужно обеспечить обнаружение узлов (реализация gosip-протокола).

Работу можно выполнять на любом языке программирования, с использованием любых фреймворков. На практике довольно редко приходится писать что-то низкоуровневое, скорее придумывать какие-то протоколы взаимодействия. Ссылку на репозиторий с готовым проектом (естественно репозиторий нужно вести по всем правилам -- провести декомпозицию задачи, завести issues, оформить readme.md, каждую issue решать в своей ветке и т.д.) прислать в качестве PRа в репозиторий https://github.com/SemenMartynov/Software-Engineering-2022. Как всегда, жесткого дедлайна не указываю, он уже определён продолжительностью этого семестра. Давайте постараемся прислать всё на проверку до 15-го апреля.

## Тестирование

Я слышал, что у вас также есть задача продемонстрировать свои знания в области тестирования ПО.
В описанных выше требованиях не так много бизнес-логики для покрытия её всеми видами автотестов, но вы вольны расширить возможности этого блокчейна так, чтобы ничего вас не ограничивало.
