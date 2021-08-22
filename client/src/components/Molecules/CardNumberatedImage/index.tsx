import { useDownloaded } from "../../../hooks/useDownloaded";

import "./style.scss";
import { ImageDonwloaded } from "../../Atoms/ImageDownloaded";

interface AppState {
  text: string;
}

export function CardNumberatedImage({ text }: AppState) {
  const { numberator } = useDownloaded();

  return (
    <div className="CardImage">
      <h3>{text}</h3>
      {numberator && <ImageDonwloaded imagePreviewUrl={String(numberator)} />}
    </div>
  );
}
