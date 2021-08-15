import "./style.scss";

interface AppState {
  text: string;
}
export function SubmitButton({ text }: AppState) {
  return (
    <button className="learn-more" type="submit">
      {text}
    </button>
  );
}
