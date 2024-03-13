
# Инструкция по развёртыванию проекта

## Установка Git
Если Git ещё не установлен на вашем сервере, выполните следующую команду:
```
sudo apt-get install git
```

## Клонирование репозитория
1. Перейдите в директорию, где должен быть развернут проект:
```
cd /путь/к/директории
```
2. Клонируйте репозиторий:
```
git clone https://github.com/Konstantin-Net/Picasso_app
```
3. Перейдите в директорию вашего проекта:
```
cd имя_вашего_проекта
```

## Установка Docker и Docker Compose
1. Установите Docker:
```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
2. Установите Docker Compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Сборка контейнеров
Выполните команду для сборки контейнеров:
```
docker-compose build
```

## Запуск контейнеров
Запустите контейнеры в фоновом режиме:
```
docker-compose up -d
```

## Выполнение миграций
Выполните миграции для контейнера Django:
```
docker-compose exec имя_контейнера_django python manage.py migrate
```

## Проверка
Убедитесь, что приложение запущено и доступно:
- Проверьте статус контейнеров:
```
docker-compose ps
```
- Посмотрите логи:
```
docker-compose logs
```
