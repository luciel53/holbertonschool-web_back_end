import { uploadPhoto, createUser } from'./utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((response) => {
      const {body} = response[0];
      const {firstName} = response[1];
      const {lastName} = response[2];
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
};
