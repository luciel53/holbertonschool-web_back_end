const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return a rounded sum', () => {
    assert.strictEqual(calculateNumber(1, 2), 3);
  });
})
