const sinon = require('sinon');
const chai = require('chai');
const { expect } = chai;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi to test', () => {
  let spy;
  beforeEach(() => {
    spy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spy.restore();
  });

  it('should send payment request with 100 and 20', () => {
    const result = sendPaymentRequestToApi(100, 20);
    expect(result).to.equal(120);
    expect(spy.calledOnceWithExactly('The total is: 120')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  });
  it('should send payment request with 10 and 10', () => {
    const result = sendPaymentRequestToApi(10, 10);
    expect(result).to.equal(20);
    expect(spy.calledOnceWithExactly('The total is: 20')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  });
});
