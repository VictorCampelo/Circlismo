import { ImageUploaded } from "../../Atoms/ImageUploaded";
import { ImageDownloaded } from "../../Atoms/ImageDownloaded";
import { useUploaded } from "../../../hooks/useUploaded";
import { useDownloaded } from "../../../hooks/useDownloaded";

export function Preview() {
  const { handleImageChange } = useUploaded();
  const { processImage } = useDownloaded();

  return (
    <div className="previewComponent">
      <form onSubmit={(e) => processImage(e)}>
        <input
          className="fileInput"
          type="file"
          onChange={(e) => handleImageChange(e)}
        />
        <button
          className="submitButton"
          type="submit"
          onClick={(e) => processImage(e)}
        >
          Upload Image
        </button>
      </form>
      <ImageUploaded />
      <ImageDownloaded />
    </div>
  );
}

export default Preview;
