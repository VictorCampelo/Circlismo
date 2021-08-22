import { createContext, ReactNode, useContext, useState } from "react";
import * as uuid from "uuid";
import { useUploaded } from "./useUploaded";

interface DownloadedProviderProps {
  children: ReactNode;
}

interface DownloadedContextData {
  download: string;
  numberator: string;
  Circlism: () => Promise<void>;
  Numberator: () => Promise<void>;
}

export const downloadContext = createContext<DownloadedContextData>(
  {} as DownloadedContextData
);

export function DownloadProvider({ children }: DownloadedProviderProps) {
  const { upload } = useUploaded();

  const [download, setDownload] = useState("");
  const [numberator, setNumberator] = useState("");
  const [filename, setFilename] = useState(uuid.v4());

  async function Circlism() {
    const data = new FormData();
    data.append("file", upload.file);
    data.append("id", filename);
    
    const res = await fetch("http://127.0.0.1:5000/upload/ciclism", {
      method: "POST",
      body: data,
    })
    .then((response) => response.json())
    .catch(console.log);
    setDownload(res.image);
  }

  async function Numberator() {
    const data = new FormData();
    data.append("file", upload.file);
    data.append("id", filename);

    const res = await fetch("http://127.0.0.1:5000/upload/number", {
      method: "POST",
      body: data,
    })
      .then((response) => response.json())
      .catch(console.log);
    setNumberator(res.image);
    setFilename(uuid.v4())
  }

  return (
    <downloadContext.Provider
      value={{ download, numberator, Circlism, Numberator }}
    >
      {children}
    </downloadContext.Provider>
  );
}

export function useDownloaded() {
  const context = useContext(downloadContext);

  return context;
}
