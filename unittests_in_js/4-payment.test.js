const sinon = require('sinon');
const chai = require('chai');
const { expect } = chai;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi to test', () => {
  let stubCalcNum = sinon.stub(Utils, 'calculateNumber').returns(10);
  let spyCalcNum = sinon.spy(console, 'log');
  it('should call Utils.calculateNumber with type = SUM, a = 100, and b = 20', () => {
    const res = sendPaymentRequestToApi(100, 20);
    expect(stubCalcNum.calledWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyCalcNum).calledWithExactly('The total is: 10');
    expect(stubCalcNum.calledWithExactly('SUM', 100, 20)).to.equal(res);
  });
  spyCalcNum.restore();
  stubCalcNum = restore();
});
