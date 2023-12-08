const kue = require('kue');
const queue = kue.createQueue();

const obj = {
  phoneNumber: '0765992245',
  message: 'Hello, How are you?',
};

/* Create a queue named push_notification_code, and create a job with the object created before*/
const job = queue.create('push_notification_code', obj);

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed')
});

/* save the job to the queue */
job.save();
