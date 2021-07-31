import { useDownloaded } from "../../../hooks/useDownloaded";

export function ImageDownloaded() {
  const { download } = useDownloaded();

  return download.processedImageUrl ? (
    <div className="imgPreview">
      <img src={download.processedImageUrl} alt="img" />
    </div>
  ) : (
    <div className="previewText">Please select an Image for Preview</div>
  );
}
