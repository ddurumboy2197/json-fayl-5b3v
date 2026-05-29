**Pytest uchun test kod**
```python
import pytest
import json

def oq_json(fayl):
    with open(fayl, 'r') as file:
        return json.load(file)

def test_oq_json():
    fayl = 'test.json'
    ma'lumotlar = oq_json(fayl)
    assert isinstance(ma'lumotlar, dict)
    assert ma'lumotlar['ismi'] == 'Test'
    assert ma'lumotlar['yoshi'] == 30

def test_oq_json_sahifasi():
    fayl = 'test.json'
    ma'lumotlar = oq_json(fayl)
    assert isinstance(ma'lumotlar, dict)
    assert 'ismi' in ma'lumotlar
    assert 'yoshi' in ma'lumotlar
```

**Jest uchun test kod**
```javascript
const fs = require('fs');
const json = require('json');

function oqJson(fayl) {
    return json.parse(fs.readFileSync(fayl, 'utf8'));
}

describe('oqJson', () => {
    it('ma\'lumotlarni o\'qish uchun muvaffaqiyatli', () => {
        const fayl = 'test.json';
        const ma\'lumotlar = oqJson(fayl);
        expect(ma\'lumotlar).toBeInstanceOf(Object);
        expect(ma\'lumotlar.ismi).toBe('Test');
        expect(ma\'lumotlar.yoshi).toBe(30);
    });

    it('sahifani o\'qish uchun muvaffaqiyatli', () => {
        const fayl = 'test.json';
        const ma\'lumotlar = oqJson(fayl);
        expect(ma\'lumotlar).toBeInstanceOf(Object);
        expect('ismi' in ma\'lumotlar).toBe(true);
        expect('yoshi' in ma\'lumotlar).toBe(true);
    });
});
```
