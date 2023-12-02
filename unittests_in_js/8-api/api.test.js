const request = require('request')
const chai = require('chai');
const { expect } = chai;
const api = 'http://localhost:7865';

describe('index page', () => {
  it('should had the correct status code', (done) => {
    request.get(api, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });

  });

  it('should have the correct result', (done) => {
    request.get(api, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
