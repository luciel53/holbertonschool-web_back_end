const sinon = require('sinon');
const chai = require('chai');
const { expect } = chai;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi to test', () => {
  it('should send payment request to API', () => {
    const spyCalcNum = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    expect(spyCalcNum.calledOnce).to.be.true;
    expect(spyCalcNum.calledWith('SUM', 100, 20)).to.be.true;
    spyCalcNum.restore();
  });
});
