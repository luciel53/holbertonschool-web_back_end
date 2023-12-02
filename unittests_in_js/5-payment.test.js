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
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledOnceWithExactly('The total is: 120')).to.be.true;
  });
  it('should send payment request with 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);
    expect(spy.calledOnceWithExactly('The total is: 20')).to.be.true;
  });
});
