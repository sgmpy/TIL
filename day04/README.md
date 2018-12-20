# Day 04

## Dictionary

- API를 활용하는데에 있어 가장 많이 사용되는 자료형. 웹을 하면서 계속 만나게 될 자료형.
- `Key`와 `Value`의 구조
- `Key`는 `string`, `integer`, `float`, `boolean` 가능하다. (`list`,`dictionary`는 안된다.)
- `Value`는 모든 자료형이 가능하다. `list`또는 `dictionary`도 가능하다.



1. 딕셔너리 만들기

```python
lunch = {
    '중식집':'02-123-123'
}
lunch = dict(중식집='02-123-123')
```

2. 딕셔너리 내용 추가하기

```python
lunch['분식집'] = '031'
```

3. 딕셔너리 내용 가져오기

```python
idol = {
    'bts': {
        '지민': 24,
        'RM': 26
    }
}
# 랩몬스터의 나이는?
idol['bts']['RM']
```

4. 딕셔너리 반복문 활용하기

```python
# 기본 활용
for key in lunch:
	print(key)
	print(lunch[key])
	
# .keys() - key 가져오기
for key in lunch.keys():
	print(key)
	
# .values() - value 가져오기
for value in lunch.values():
	print(value)

# .items() - items(key, value) 가져오기
for key, value in lunch.items():
	print(key, value)
```

