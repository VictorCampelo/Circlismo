import { useUploaded } from "../../../hooks/useUploaded";
import "./style.scss";

export function ImageUploaded() {
  const { upload } = useUploaded();

  return upload.imagePreviewUrl ? (
    <div className="imgPreview">
      <img src={String(upload.imagePreviewUrl)} alt="img" />
    </div>
  ) : (
    <div className="previewText">Please select an Image for Preview</div>
  );
}
