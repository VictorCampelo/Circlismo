import { createContext, ReactNode, useContext, useState } from "react";

interface Uploaded {
  file: string;
  imagePreviewUrl: string | ArrayBuffer | null;
}

interface UploadedProviderProps {
  children: ReactNode;
}

interface UploadedContextData {
  upload: Uploaded;
  handleImageChange: (e: any) => void;
}

export const uploadContext = createContext<UploadedContextData>(
  {} as UploadedContextData
);

export function UploadProvider({ children }: UploadedProviderProps) {
  const [upload, setUpload] = useState<Uploaded>({
    file: "",
    imagePreviewUrl: "",
  });

  function handleImageChange(e: any): void {
    e.preventDefault();

    let reader = new FileReader();
    let file = e.target.files[0];

    reader.onloadend = () => {
      setUpload({
        file: file,
        imagePreviewUrl: reader.result,
      });
    };

    reader.readAsDataURL(file);
  }

  return (
    <uploadContext.Provider value={{ upload, handleImageChange }}>
      {children}
    </uploadContext.Provider>
  );
}

export function useUploaded() {
  const context = useContext(uploadContext);

  return context;
}
