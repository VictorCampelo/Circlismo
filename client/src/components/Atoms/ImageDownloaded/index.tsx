import "./style.scss";

interface AppState {
  imagePreviewUrl: string;
}

export function ImageDonwloaded({ imagePreviewUrl }: AppState) {
  return (
    <div className="imgPreview">
      <img src={imagePreviewUrl} alt="img" />
    </div>
  );
}
