import { useDownloaded } from "../../../hooks/useDownloaded";
import { SubmitButton } from "../../Atoms/SubmitButton";
import { FileInput } from "../../Atoms/FileInput";

export function ProcessImageForm() {
  const { processImage } = useDownloaded();

  return (
    <form onSubmit={(e) => processImage(e)}>
      <FileInput />
      <SubmitButton text="Upload Image" />
    </form>
  );
}
