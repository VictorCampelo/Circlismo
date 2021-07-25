import React from "react";

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = { file: "", imagePreviewUrl: "", response: "" };
  }

  async _handleSubmit(e) {
    e.preventDefault();
    // TODO: do something with -> this.state.file
    const data = new FormData();
    data.append("file", this.state.file);

    const result = await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: data,
    })
      .then((response) => response.json())
      .catch(console.log);
    this.setState({ response: result.image });
    console.log("handle uploading-", this.state.file);
  }

  _handleImageChange(e) {
    e.preventDefault();

    let reader = new FileReader();
    let file = e.target.files[0];

    reader.onloadend = () => {
      this.setState({
        file: file,
        imagePreviewUrl: reader.result,
      });
    };

    reader.readAsDataURL(file);
  }

  checkIfImageWasUploaded() {
    let { imagePreviewUrl } = this.state;
    let $imagePreview = null;
    if (imagePreviewUrl) {
      $imagePreview = <img src={imagePreviewUrl} alt="img" />;
    } else {
      $imagePreview = (
        <div className="previewText">Please select an Image for Preview</div>
      );
    }
    return $imagePreview;
  }
  checkIfImageWasDownload() {
    let { response } = this.state;
    let $imagePreview = null;
    if (response) {
      $imagePreview = <img src={response} alt="img" />;
    } else {
      $imagePreview = (
        <div className="previewText">Please select an Image for Preview</div>
      );
    }
    return $imagePreview;
  }

  render() {
    return (
      <div className="previewComponent">
        <form onSubmit={(e) => this._handleSubmit(e)}>
          <input
            className="fileInput"
            type="file"
            onChange={(e) => this._handleImageChange(e)}
          />
          <button
            className="submitButton"
            type="submit"
            onClick={(e) => this._handleSubmit(e)}
          >
            Upload Image
          </button>
        </form>
        <div className="imgPreview">{this.checkIfImageWasUploaded()}</div>
        <div className="imgPreview">{this.checkIfImageWasDownload()}</div>
      </div>
    );
  }
}

export default Main;
