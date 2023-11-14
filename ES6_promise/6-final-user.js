import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignUp(firstName, lastName, fileName) {
  const user = signUpUser(firstName, lastName);
  const file = uploadPhoto(fileName);

  return Promise.allSettled([user, file]).then((res) =>
    res.map((res) =>
    ({
      status: res.status,
      value: res.status === 'fulfilled' ? res.value : `Error: ${res.reason.message}`,
    })));
}
