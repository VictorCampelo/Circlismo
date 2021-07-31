import Main from "./Pages/Main/index";
import { UploadProvider } from "./hooks/useUploaded";
import { DownloadProvider } from "./hooks/useDownloaded";
import { BrowserRouter, Route, Switch } from "react-router-dom";

const App = () => {
  return (
    <BrowserRouter>
      <UploadProvider>
        <DownloadProvider>
          <Switch>
            <Route path="/" exact component={Main} />
          </Switch>
        </DownloadProvider>
      </UploadProvider>
    </BrowserRouter>
  );
};

export default App;
