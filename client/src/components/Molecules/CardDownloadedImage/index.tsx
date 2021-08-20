import { useDownloaded } from "../../../hooks/useDownloaded";

import "./style.scss";
import { ImageDonwloaded } from "../../Atoms/ImageDownloaded";

interface AppState {
  text: string;
}

export function CardDonwloadedImage({ text }: AppState) {
  const { download } = useDownloaded();

  return (
    <div className="CardImage">
      <h3>{text}</h3>
      {download && <ImageDonwloaded imagePreviewUrl={String(download)} />}
    </div>
  );
}
