# diagnostic

## cases
### simple-load
Запуск:  
`docker-compose -f simple-load.yml up --build --force-recreate`  
Нагрузка 1rps, инициализирующая обращение к стороннему сервису


## tools

### dotnet-counter

Внутри контейнера в папке tools:

Найти на каком процессе приложение
```
./dotnet-counters ps
```

Мониторинг существующих счетчиков (<pid_of_your_dotnet_application> = PID приложения)
```
./dotnet-counters monitor --process-id <pid_of_your_dotnet_application>
```

Сбор счетчиков
```
./dotnet-counters collect --process-id <pid_of_your_dotnet_application> --format csv
```

Доступные счетчики с их поставщиками
```
./dotnet-counters list
```
