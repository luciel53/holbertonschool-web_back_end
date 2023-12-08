import { createClient } from 'redis';
import redis from 'redis';
import { promisify } from 'util';

const client = createClient()

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
})
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, res) => {
    redis.print('Reply:' + res);
  });
}

/* convert client.get to a function based on the promises */
const promGet = promisify(client.get).bind(client);

/* async function */
const displaySchoolValue = async (schoolName) => {
  const val = await promGet(schoolName);
    console.log(val);
  }


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
