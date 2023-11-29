const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return the sum of 2 integers', () => {
    assert.equal(calculateNumber(1, 3), 4);
  });

  it('should return the rounded sum when first number is a float', () => {
    assert.strictEqual(calculateNumber(2.8, 2), 5);
  });

  it('should return the rounded sum when second number is a float', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return the rounded for both numbers float', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(1.5, 1.2), 3);
  });

})
