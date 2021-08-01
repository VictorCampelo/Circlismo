import { Preview } from "../../components/Organisms/Preview";
import { Component } from "react";
import "./index.scss";

class ProcessImage extends Component {
  render() {
    return (
      <div className="main">
        <h1>File Upload</h1>
        <Preview />
      </div>
    );
  }
}

export default ProcessImage;
