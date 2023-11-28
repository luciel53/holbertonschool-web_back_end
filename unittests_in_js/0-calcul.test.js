const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return a rounded sum', () => {
    assert.strictEqual(calculateNumber(1, 2), 3);
  });

  it('should return a rounded for first number float', () => {
    assert.strictEqual(calculateNumber(2.8, 2), 5);
  });

  it('should return a rounded for second number float', () => {
    assert.strictEqual(calculateNumber(3, 3.7), 7);
  });

  it('should return a rounded for both numbers float', () => {
    assert.strictEqual(calculateNumber(1.2, 2.6), 4);
  });
})
