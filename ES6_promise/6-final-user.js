import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignUp(firstName, lastName, fileName) {
  const user = signUpUser(firstName, lastName);
  const file = uploadPhoto(fileName);

  return Promise.all([user, file]).then((res) => {
    return res.map((res) => ({
      status: res.status,
      value: res.status === 'ok' ? res.value : `Error: ${res.status}`,
    }));
  });
}
