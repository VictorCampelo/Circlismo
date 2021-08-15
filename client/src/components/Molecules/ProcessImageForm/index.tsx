import { useDownloaded } from "../../../hooks/useDownloaded";
import { SubmitButton } from "../../Atoms/SubmitButton";
import { FileInput } from "../../Atoms/FileInput";
import "./style.scss";

export function ProcessImageForm() {
  const { processImage } = useDownloaded();

  return (
    <form className="processImageForm" onSubmit={(e) => processImage(e)}>
      <FileInput />
      <SubmitButton text="Processar imagem" />
    </form>
  );
}
