const loginForm = document.getElementById('loginform');
const baseEndponint = 'http://127.0.0.1:8000/api/' ;

if(loginForm) {
  loginForm.addEventListener('submit' , handleLogin)
}

function handleLogin(event) {
  console.log(event);
  event.preventDefault() ;
  let loginFormData = new FormData(loginForm);
  let loginOjectData = Object.fromEntries(loginFormData)
  let loginEndponit = `${baseEndponint}token/`
  console.log(loginOjectData)

  const options = {
    method: 'POST' ,
    headers : {
      'Content-Type': 'application/json',
    },
    body : JSON.stringify(loginOjectData)
  }

  fetch(loginEndponit , options)
  .then(res => {
    console.log(res)
    return res.json()
  }).then( x => {
    console.log(x);
  }).catch(err => {
    console.log('err' , err );
  })
}