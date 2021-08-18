import "./style.scss";

interface AppState {
  imagePreviewUrl: string;
}

export function ImageUploaded({ imagePreviewUrl }: AppState) {
  return <img src={imagePreviewUrl} alt="img" />;
}
