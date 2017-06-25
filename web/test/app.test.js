const assert = require('assert');
const rp = require('request-promise');
const app = require('../src/app');
const port = process.env.WEBSERVICE_SERVICE_PORT;

describe('intouch front-end webservice tests', () => {
  before(function(done) {
    this.server = app.listen(port);
    this.server.once('listening', () => done());
  });

  after(function(done) {
    this.server.close(done);
  });

  it('starts and shows the index page', () => {
    return rp(`http://${app.get('host')}:${port}`).then(body =>
      assert.ok(body.indexOf('<html') !== -1)
    );
  });

  describe('404', function() {
    it('shows a 404 HTML page', () => {
      return rp({
        url: `http://${app.get('host')}:${port}/path/to/nowhere`,
        headers: {
          'Accept': 'text/html'
        }
      }).catch(res => {
        assert.equal(res.statusCode, 404);
        assert.ok(res.error.indexOf('<html>') !== -1);
      });
    });

    it('shows a 404 JSON error without stack trace', () => {
      return rp({
        url: `http://${app.get('host')}:${port}/path/to/nowhere`,
        json: true
      }).catch(res => {
        assert.equal(res.statusCode, 404);
        assert.equal(res.error.code, 404);
        assert.equal(res.error.message, 'Page not found');
        assert.equal(res.error.name, 'NotFound');
      });
    });
  });
});
