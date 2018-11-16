const rootRef = firebase.database().ref();

//Select user by UID
const user = rootRef.child('users').child('1');

//Find by email
const user = rootRef.child('users').orderByChild('email').equalTo('example@email.com');

//Limit to 10 user pages
const pages = rootRef.child('pages').orderByChild('UID').equalTo('1').limitToFirst(10);

//Users by first initial
const users = rootRef.child('users').orderByChild('name').startAt('D').endAt('D\uf8ff')

