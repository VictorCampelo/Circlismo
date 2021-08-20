import { useDownloaded } from "../../../hooks/useDownloaded";
import { SubmitButton } from "../../Atoms/SubmitButton";
import { FileInput } from "../../Atoms/FileInput";
import "./style.scss";

export function ProcessImageForm() {
  const { Process } = useDownloaded();

  return (
    <form className="processImageForm">
      <FileInput />
      <SubmitButton text="Processar imagem" />
      {/* <button type="button" onClick={(e) => Process()}>test</button> */}
    </form>
  );
}
