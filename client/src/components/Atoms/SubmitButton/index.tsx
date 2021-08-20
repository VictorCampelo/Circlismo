import { useState } from "react";
import { useDownloaded } from "../../../hooks/useDownloaded";
import "./style.scss";
interface AppState {
  text: string;
}

export function SubmitButton({ text }: AppState) {
  const { Process } = useDownloaded();

  const [animation, setAnimation] = useState(false)

  async function handleAnimation() {
    setAnimation(true);
    await Process();
    setAnimation(false);
  }

  return (
    <button
      type="button"
      onClick={() => {
        Process();
        handleAnimation();
      }}
      className={
        animation ? "button col-1 animate" : "button col-1"
      }
    >
      {text}
    </button>
  );
}
