import "./styles.scss";

interface AppState {
  text: string;
}
export function TextPreview({ text }: AppState) {
  return <div>{text}</div>;
}
