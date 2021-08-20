import {
  createContext,
  ReactNode,
  useContext,
  useState,
} from "react";
import { useUploaded } from "./useUploaded";

interface DownloadedProviderProps {
  children: ReactNode;
}

interface DownloadedContextData {
  download: string;
  Process: () => Promise<void>;
}

export const downloadContext = createContext<DownloadedContextData>(
  {} as DownloadedContextData
);

export function DownloadProvider({ children }: DownloadedProviderProps) {
  const { upload } = useUploaded();

  const [download, setDownload] = useState("");

  async function Process() {
    const data = new FormData();
    data.append("file", upload.file);

    const res = await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: data,
    })
      .then((response) => response.json())
      .catch(console.log);
      console.log(res.image)
    setDownload(res.image);
  }

  return (
    <downloadContext.Provider value={{ download, Process }}>
      {children}
    </downloadContext.Provider>
  );
}

export function useDownloaded() {
  const context = useContext(downloadContext);

  return context;
}
