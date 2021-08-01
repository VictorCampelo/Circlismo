import { useUploaded } from "../../../hooks/useUploaded";

export function FileInput() {
  const { handleImageChange } = useUploaded();

  return (
    <input
      className="fileInput"
      type="file"
      onChange={(e) => handleImageChange(e)}
    />
  );
}
