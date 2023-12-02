const chai = require('chai');
const { expect } = chai;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('should test the result of getPaymentTokenFrom', (done) => {
    getPaymentTokenFromAPI(true)
    .then((result) => {
      expect(result).to.deep.equal({data: 'Successful response from the API' });
      done();
    }).catch(done);
  });
});
