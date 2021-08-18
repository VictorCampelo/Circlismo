import { Preview } from "../../components/Organisms/Preview";
import { Component } from "react";
import "./index.scss";
import Header from "../../components/Molecules/Header";

class ProcessImage extends Component {
  render() {
    return (
      <>
        <Header />
        <div className="main">
          <div className="title">
            <h1>File Upload</h1>
            <h2>
              Transform your photo to circlism mode and getting point to draw
            </h2>
          </div>
          <Preview />
        </div>
      </>
    );
  }
}

export default ProcessImage;
