const sinon = require('sinon');
const chai = require('chai');
const { expect } = chai;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi to test', () => {
  let stubCalcNum = sinon.stub(Utils, 'calculateNumber').returns(10);
  let spyCalcNum = sinon.spy(console, 'log');
  it('should send payment request to API', () => {
    sendPaymentRequestToApi(100, 20);
    expect(stubCalcNum.calledWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyCalcNum).called('The total is: 10');
  });
  spyCalcNum.restore();
  stubCalcNum = restore();
});
