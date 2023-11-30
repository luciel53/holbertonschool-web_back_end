const sinon = require('sinon');
const chai = require('chai');
const { expect } = chai;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi to test', () => {
  let spyCalcNum = sinon.spy(console, 'log');
  it('should call Utils.calculateNumber with type = SUM, a = 100, and b = 20', () => {
    let stubCalcNum = sinon.stub(Utils, 'calculateNumber').returns(10);
    sendPaymentRequestToApi(100, 20);
    expect(stubCalcNum.calledWithExactly('SUM', 100, 20)).to.equal(true);
    expect(spyCalcNum.calledWithExactly('The total is: 10')).to.be.true;
    spyCalcNum.restore();
    stubCalcNum = restore();
  });
});
