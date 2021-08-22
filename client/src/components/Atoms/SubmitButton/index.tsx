import { useState } from "react";
import { useDownloaded } from "../../../hooks/useDownloaded";
import "./style.scss";
interface AppState {
  text: string;
}

export function SubmitButton({ text }: AppState) {
  const { Circlism, Numberator } = useDownloaded();

  const [animation, setAnimation] = useState(false)

  async function handleAnimation() {
    setAnimation(true);
    await Circlism();
    await Numberator();
    setAnimation(false);
  }

  return (
    <button
      type="button"
      onClick={() => {
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
