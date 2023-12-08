import { createClient } from 'redis';
import redis from 'redis';

const client = createClient()

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
})
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const hashKey = 'HolbertonSchools';
const fields = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

/* create the hash in Redis */
fields.forEach((field, index) => {
  client.hset(hashKey, field, values[index], (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
});

/* print the hash */
client.hgetall(hashKey, (error, result) => {
  if (error) {
    console.error(error);
  } else {
    console.log(result);
  }
});
