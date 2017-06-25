/* eslint-disable no-console */
const logger = require('winston');
const app = require('./app');
const port = process.env.WEBSERVICE_SERVICE_PORT;
const server = app.listen(port);

process.on('unhandledRejection', (reason, p) =>
  logger.error('Unhandled Rejection at: Promise ', p, reason)
);

server.on('listening', () =>
  logger.info(`${app.get('service_id')} started on ${app.get('host')}:${port}`)
);
