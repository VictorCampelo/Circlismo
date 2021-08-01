import ProcessImage from "./Pages/ProcessImage/index";
import { UploadProvider } from "./hooks/useUploaded";
import { DownloadProvider } from "./hooks/useDownloaded";
import { BrowserRouter, Route, Switch } from "react-router-dom";

const App = () => {
  return (
    <BrowserRouter>
      <UploadProvider>
        <DownloadProvider>
          <Switch>
            <Route path="/" exact component={ProcessImage} />
          </Switch>
        </DownloadProvider>
      </UploadProvider>
    </BrowserRouter>
  );
};

export default App;
