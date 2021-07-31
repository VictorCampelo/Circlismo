import { createContext, ReactNode, useContext, useState } from "react";
import { useUploaded } from "./useUploaded";

interface Downloaded {
  processedImageUrl: string;
}

interface DownloadedProviderProps {
  children: ReactNode;
}

interface DownloadedContextData {
  download: Downloaded;
  processImage: (e: any) => void;
}

export const downloadContext = createContext<DownloadedContextData>(
  {} as DownloadedContextData
);

export function DownloadProvider({ children }: DownloadedProviderProps) {
  const { upload } = useUploaded();

  const [download, setDownload] = useState<Downloaded>({
    processedImageUrl: "",
  });

  async function processImage(e: any) {
    e.preventDefault();
    // TODO: do something with -> this.state.file
    const data = new FormData();
    data.append("file", upload.file);

    const result = await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: data,
    })
      .then((response) => response.json())
      .catch(console.log);
    setDownload(result.image);
  }

  return (
    <downloadContext.Provider value={{ download, processImage }}>
      {children}
    </downloadContext.Provider>
  );
}

export function useDownloaded() {
  const context = useContext(downloadContext);

  return context;
}
