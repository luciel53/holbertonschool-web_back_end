const request = require('request')
const chai = require('chai');
const { expect } = chai;

describe('index page', () => {
  const api = 'http://localhost:7865';
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

describe('GET /cart/:id', () => {
  const api = 'http://localhost:7865/cart/6';
  it('should have correct status if id a number', (done) => {
    request.get(api, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 6');
      done();
    });
  });

  const apiError = 'http://localhost:7865/cart/hello';
  it('should raise an error of id not a number', (done) => {
    request.get(apiError, (error, response, body) => {
      expect(body).to.equal(404);
      done();
    });
  });
});
