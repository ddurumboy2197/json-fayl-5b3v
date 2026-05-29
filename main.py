import json

def oqish(fayl_ismi):
    try:
        with open(fayl_ismi, 'r') as f:
            ma'lumotlar = json.load(f)
            return ma'lumotlar
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return None
    except json.JSONDecodeError:
        print("Faylda ma'lumotlar yozilmagan.")
        return None

ma'lumotlar = oqish('ma'lumotlar.json')
print(ma'lumotlar)
```

```python
import json

def oqish(fayl_ismi):
    try:
        with open(fayl_ismi, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

ma'lumotlar = oqish('ma'lumotlar.json')
print(ma'lumotlar)
