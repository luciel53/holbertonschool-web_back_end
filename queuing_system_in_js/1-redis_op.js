import { createClient } from 'redis';
import redis from 'redis';

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

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, res) => {
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
