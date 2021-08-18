import { ImageUploaded } from "../../Atoms/ImageUploaded";
import { SubmitButton } from "../../Atoms/SubmitButton";
import { useUploaded } from "../../../hooks/useUploaded";

import "./style.scss";
import { TextPreview } from "../../Atoms/TextPreview";

interface AppState {
  text: string;
}

export function CardUploadedImage({text}: AppState) {
  const { upload } = useUploaded();

  return (
    <div className="CardImage">
      <h3>{text}</h3>
      {upload.imagePreviewUrl ? (
        <>
          <ImageUploaded imagePreviewUrl={String(upload.imagePreviewUrl)} />
        </>
      ) : (
        <TextPreview text="Please select an Image for Preview" />
      )}
    </div>
  );
}
