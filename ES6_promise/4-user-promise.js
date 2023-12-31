export default function signUpUser(firstName, lastName) {
  const promise = new Promise((resolve, reject) => {
    if (firstName && lastName) {
      resolve({
        firstName,
        lastName,
      });
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
  return promise;
}
