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
    setDownload({ processedImageUrl: "" });
    const data = new FormData();
    data.append("file", upload.file);

    await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: data,
    })
      .then(async (response: any) => setDownload({ processedImageUrl: response.json().image }))
      .catch(console.log);
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
