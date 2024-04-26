[System.Runtime]                                                                
    % Time in GC since last GC (%)                                         0    
    Allocation Rate (B / 1 sec)                                        8,200    
    CPU Usage (%)                                                          0.205
    Exception Count (Count / 1 sec)                                        0    
    GC Committed Bytes (MB)                                               12.55 
    GC Fragmentation (%)                                                  44.848
    GC Heap Size (MB)                                                      2.885
    Gen 0 GC Budget (MB)                                                  60    
    Gen 0 GC Count (Count / 1 sec)                                         0    
    Gen 0 Size (B)                                                 1,435,568    
    Gen 1 GC Count (Count / 1 sec)                                         0    
    Gen 1 Size (B)                                                 1,706,680    
    Gen 2 GC Count (Count / 1 sec)                                         0    
    Gen 2 Size (B)                                                         0    
    IL Bytes Jitted (B)                                              656,579    
    LOH Size (B)                                                           0    
    Monitor Lock Contention Count (Count / 1 sec)                          0    
    Number of Active Timers                                               44    
    Number of Assemblies Loaded                                           92    
    Number of Methods Jitted                                           6,133    
    POH (Pinned Object Heap) Size (B)                                 81,856    
    ThreadPool Completed Work Item Count (Count / 1 sec)                  11    
    ThreadPool Queue Length                                                0    
    ThreadPool Thread Count                                                5    
    Time paused by GC (ms / 1 sec)                                         0    
    Time spent in JIT (ms / 1 sec)                                         0    
    Working Set (MB)                                                     115.671

Эти счетчики предоставляют информацию о различных аспектах работы приложения на платформе .NET Core:

1. **% Time in GC since last GC (%)**: Процент времени, затраченного на выполнение сборки мусора (GC), с момента последней сборки мусора.

2. **Allocation Rate (B / 1 sec)**: Скорость выделения памяти в байтах за одну секунду.

3. **CPU Usage (%)**: Использование процессора в процентах.

4. **Exception Count (Count / 1 sec)**: Количество исключений, возникших за одну секунду.

5. **GC Committed Bytes (MB)**: Количество памяти, выделенной для GC в мегабайтах.

6. **GC Fragmentation (%)**: Уровень фрагментации памяти, используемой для GC, в процентах.

7. **GC Heap Size (MB)**: Размер кучи GC в мегабайтах.

8. **Gen 0 GC Budget (MB)**: Бюджет сборки мусора поколения 0 в мегабайтах.

9. **Gen 0 GC Count (Count / 1 sec)**: Количество сборок мусора поколения 0 за одну секунду.

10. **Gen 0 Size (B)**: Размер поколения 0 в байтах.

11. **Gen 1 GC Count (Count / 1 sec)**: Количество сборок мусора поколения 1 за одну секунду.

12. **Gen 1 Size (B)**: Размер поколения 1 в байтах.

13. **Gen 2 GC Count (Count / 1 sec)**: Количество сборок мусора поколения 2 за одну секунду.

14. **Gen 2 Size (B)**: Размер поколения 2 в байтах.

15. **IL Bytes Jitted (B)**: Объем байт, скомпилированных в исполняемый код (JIT) из Intermediate Language (IL).

16. **LOH Size (B)**: Размер большого объектного кучи в байтах.

17. **Monitor Lock Contention Count (Count / 1 sec)**: Количество конфликтов по монитору за одну секунду.

18. **Number of Active Timers**: Количество активных таймеров.

19. **Number of Assemblies Loaded**: Количество загруженных сборок.

20. **Number of Methods Jitted**: Количество методов, которые были скомпилированы в исполняемый код (JIT).

21. **POH (Pinned Object Heap) Size (B)**: Размер кучи закрепленных объектов в байтах.

22. **ThreadPool Completed Work Item Count (Count / 1 sec)**: Количество завершенных рабочих элементов в пуле потоков за одну секунду.

23. **ThreadPool Queue Length**: Длина очереди пула потоков.

24. **ThreadPool Thread Count**: Количество потоков в пуле потоков.

25. **Time paused by GC (ms / 1 sec)**: Время, на которое был приостановлен процессор в миллисекундах из-за выполнения сборки мусора, за одну секунду.

26. **Time spent in JIT (ms / 1 sec)**: Время, затраченное на компиляцию кода в исполняемый код (JIT), в миллисекундах за одну секунду.

27. **Working Set (MB)**: Рабочий набор памяти в мегабайтах.