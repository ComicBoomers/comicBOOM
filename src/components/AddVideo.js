import React, {
  Component
} from 'react';
import logo from './boom.svg';

class AddVideo extends Component {

  constructor() {
    super()
    this.state = {
      videoFile: ''
    }
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleSubmit() {
    //videofile to state? can a video file be on state?
    //call function to Boomify vid on state and initiate PageCreate with returned gifs
  }

  render() {
    <div>
      <form action="upload_file.php" method="post" enctype="multipart/form-data">
        <label>Boomify ur vid</label>
        <input type="file" name="video" id="vidfile"></input>
        <br />
        <input type="submit" name="submit" value="Submit" />
      </form>
    </div>
  }
}

export default AddVideo;
