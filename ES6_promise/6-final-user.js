/*eslint-disable*/

import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default function handleProfileSignup(firstName, lastName, fileName) {
  const premtimet = [];
  premtimet.push(signUpUser(firstName, lastName));
  premtimet.push(uploadPhoto(fileName));

  return Promise.allSettled(premtimet)
    .then(results => {
      return results.map(result => ({
        status: result.status,
        value: (() => {
          if (result.value === 'fulfilled') {
            return result.value;
          } else {
            return result.reason;
          }
        })()
      }));
    });
}

