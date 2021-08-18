import { useDownloaded } from "../../../hooks/useDownloaded";

import "./style.scss";
import { TextPreview } from "../../Atoms/TextPreview";
import { ImageDonwloaded } from "../../Atoms/ImageDownloaded";

interface AppState {
  text: string;
}

export function CardDonwloadedImage({text}: AppState) {
  const { download } = useDownloaded();

  return (
    <div className="CardImage">
      <h3>{text}</h3>
      {download.processedImageUrl && (
        <ImageDonwloaded imagePreviewUrl={String(download.processedImageUrl)} />
      )}
    </div>
  );
}
