## Miscellaneous [기타]

### Input/Output [입출력]

- **Use 'sys.stdin.readline()' over 'input()'** when there are tons of data to read, since it is faster.

### Performance

- **Use 'timeit' over 'time' or 'time.clock'** since it repeats the tests many times to eliminate the influence of other tasks on the machine, disk flushing, OS scheduling, or gargabe collection.

### For Else

```python
for i in [...]:
    if ...:
        print("else doesn't get excuted if breaks")
        break
else:
    print("happens only after the full loop")
```

### Exception Handling

```python
def func(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError as e:
        print(f'Error : {e}')
    finally:
        print('this is always printed')
```
