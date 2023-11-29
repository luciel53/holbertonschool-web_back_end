const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

const { expect } = chai;

describe('calculateNumber for SUM', () => {
  it('check result for SUM', () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 2.8, 2)).to.equal(5);
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
    expect(calculateNumber('SUM', 1.5, 1.2)).to.equal(3);
  });
})

describe('calculateNumber for SUBTRACT', () => {
  it('should check the result of subtract', () => {
    expect(calculateNumber('SUBTRACT', 3, 1)).to.equal(2);
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    expect(calculateNumber('SUBTRACT', 4.5, 1.4)).to.equal(4);
  });
});

describe('calculateNumber for DIVIDE', () => {
  it('should check the result of divide', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
});
