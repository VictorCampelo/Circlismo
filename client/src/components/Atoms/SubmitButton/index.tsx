import "./style.scss";

interface AppState {
  text: string;
}
export function SubmitButton({ text }: AppState) {
  return (
    <button className="submitButton" type="submit">
      {text}
    </button>
  );
}
