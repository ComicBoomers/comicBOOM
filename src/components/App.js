import React, {
  Component
} from 'react';
import logo from './boom.svg';
import './App.css';

class App extends Component {
  constructor() {
    super()
    this.state = {
      // name: '',
      email: '',
      password: '',
      UID: ''
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange() {
    //changes to state
  }

  handleSubmit() {
    //login user with cridentials on state via firebase authentication
    //get back UID and initiate User Main with said ID
  }

  render() {
    return(

      this.state.UID ?
      <UserMain UID={this.state.UID}></UserMain>
      :
   <div className="App">
        <header className="App-header">
        <p> Comic </p> <img src = {logo} className= "App-logo" alt= "logo"/>

         <div id='form-style'>
          <form onChange={this.handleChange}>
            {/* <div>
              <label className='inputField'> Name </label>
              <input type = 'text' value = {this.state.name}/>
            </div> */}
            <div>
              <label className='inputField'> Email </label >
              <input type= 'text' value = {this.state.email}/>
            </div>
            <div>
              <label className='inputField'> Password </label>
              <input type ='text' value = {this.state.password}/>
            </div>
            <button type='submit' onClick={this.handleSubmit}></button>
          </form>
        </div>
        </header> </div >
        )
  }
}
  export default App;
