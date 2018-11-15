import React, {
  Component
} from 'react';
import logo from './boom.svg';
import './App.css';

class App extends Component {
  constructor() {
    super()
    this.state = {
      name: '',
      email: '',
      password: ''
    }
  }
  render() {
    return(
   <div className="App">
        <header className="App-header">
        <p> Comic </p> <img src = {logo} className= "App-logo" alt= "logo"/>

         <div id='form-style'>
         <form>
        <div>
        <label className='inputField'> Name </label> <input type = 'text' value = {this.state.name}/>
        </div>
        <div><label className='inputField'> Email </label >
        <input type= 'text' value = {this.state.email}/></div>
        <div><label className='inputField'> Password </label> <input type ='text' value = { this.state.password}/>
        </div>
        </form> </div>
        </header> </div >
        )
  }
}
  export default App;
