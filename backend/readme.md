бэкенд на фастапи

Запуск бэка в докере

```bash
docker build -t myimage .
```
```bash
docker run -d --name mycontainer -p 80:80 myimage
```

Сваггер запущенного бэка лежит на http://127.0.0.1/api/v1/docs
