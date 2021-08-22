import { SubmitButton } from "../../Atoms/SubmitButton";
import { FileInput } from "../../Atoms/FileInput";
import "./style.scss";

export function ProcessImageForm() {

  return (
    <div className="processImageForm">
      <FileInput />
      <SubmitButton text="Processar imagem" />
    </div>
  );
}
