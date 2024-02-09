const _array = new WeakMap();

class Stack {
  constructor() {
    _array.set(this, []);
  }

  get count() {
    return _array.get(this).length;
  }

  push(value) {
    _array.get(this).push(value);
  }

  pop() {
    if (_array.get(this).length === 0) throw new Error("Stack is empty!");
    return _array.get(this).pop();
  }

  peek() {
    // shows the top element
    if (_array.get(this).length === 0) throw new Error("Stack is empty!");
    return _array.get(this)[_array.get(this).length - 1];
  }
}

try {}
catch (e) {
  console.log(e.message);
}
