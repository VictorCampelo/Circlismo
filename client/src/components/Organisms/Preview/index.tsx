import { ProcessImageForm } from "../../Molecules/ProcessImageForm";
import { ImageUploaded } from "../../Atoms/ImageUploaded";
import { ImageDownloaded } from "../../Atoms/ImageDownloaded";

export function Preview() {
  return (
    <div className="previewComponent">
      <ProcessImageForm />
      <ImageUploaded />
      <ImageDownloaded />
    </div>
  );
}
