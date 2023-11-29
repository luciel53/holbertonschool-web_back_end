const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber for SUM', () => {
  it('check result for SUM', () => {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 2.8, 2), 5);
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
    assert.strictEqual(calculateNumber('SUM', 1.5, 1.2), 3);
  });
})

describe('calculateNumber for SUBTRACT', () => {
  it('should check the result of subtract', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 3, 1), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.strictEqual(calculateNumber('SUBTRACT', 4.5, 1.4), 4);
  });
});

describe('calculateNumber for DIVIDE', () => {
  it('should check the result of divide', () => {
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
